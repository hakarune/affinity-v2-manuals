#!/usr/bin/env python3
"""Convert a mirrored Affinity 2 help site into a manuals/<app>/ Markdown tree.

Reads   .work/mirror/<app>/           (produced by scripts/mirror_manual.py)
Writes  manuals/<app>/index.md               curated TOC (books bold, pages linked)
        manuals/<app>/content/NN-book/NN-page.md   one file per help page
        manuals/<app>/assets/shared/**       shared image pool (only what's used)
        manuals/<app>/assets/images/**       page-specific images (only what's used)
        manuals/<app>/README.md
        manuals/<app>/MISSING_IMAGES.md
        sources/<app>/                        lean raw mirror (no shared/, no resources/)

Conversion mirrors the hand-checked Affinity Designer 2 import: `##`/`###`
headings, `> **Note:**` / `> **Tip:**` / `> **Warning:**` call-outs, a
`#### SEE ALSO:` list, relative Markdown links between pages, relative image
links.  Rough edges of the original Designer pass are fixed here: no `###`
headings buried inside block-quotes, clean `# Title` lines (heading icons
dropped).

Usage:  scripts/import_manual.py <app>            # app = photo | publisher | designer
        scripts/import_manual.py <app> --dry-run  # report the plan, write nothing
"""
from __future__ import annotations

import re
import shutil
import sys
import unicodedata
from html import unescape
from pathlib import Path
from urllib.parse import urldefrag, urljoin

from bs4 import BeautifulSoup, Comment, NavigableString, Tag

ROOT = Path(__file__).resolve().parent.parent

# lxml parses the help site's slightly-malformed tables / nested <details>
# correctly; html.parser dumps the rest of such a block as literal text.
try:
    import lxml  # noqa: F401
    _PARSER = "lxml"
except ImportError:
    _PARSER = "html.parser"


def parse_html(markup) -> BeautifulSoup:
    return BeautifulSoup(markup, _PARSER)


_PLAT_MAC = {"osx", "mac", "macos"}
_PLAT_WIN = {"win32", "win", "windows"}


def _plat(el) -> str | None:
    if not isinstance(el, Tag):
        return None
    cls = set(el.get("class", []))
    if cls & _PLAT_MAC:
        return "**macOS:**"
    if cls & _PLAT_WIN:
        return "**Windows:**"
    return None

# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
_slug_keep = re.compile(r"[^a-z0-9]+")


def slug(text: str, maxlen: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = text.lower().replace("&", " and ").replace("/", " ")
    text = _slug_keep.sub("-", text).strip("-")
    if len(text) > maxlen:
        text = text[:maxlen].rsplit("-", 1)[0] or text[:maxlen]
    return text or "page"


def nn(i: int) -> str:
    return f"{i:02d}"


def _title_from_source(path: Path, default: str) -> str:
    """Best page title for an orphan: <h1> text, else <title>, else the stem."""
    if not path.is_file():
        return default
    s = parse_html(path.read_bytes())
    for pick in (s.find("h1"), s.title):
        if pick:
            for img in pick.find_all("img"):
                img.decompose()
            t = re.sub(r"\s+", " ", pick.get_text(" ", strip=True)).strip()
            if t:
                return t
    return default


BLOCK_TAGS = ("p", "ul", "ol", "table", "div", "figure", "aside", "details",
              "blockquote", "pre", "section", "h1", "h2", "h3", "h4", "h5", "h6",
              "x-osx", "x-win32")

CALLOUT = {
    "note": "Note",
    "tip": "Tip",
    "warning": "Warning",
    "prefs": "Preferences",
    "caution": "Caution",
    "important": "Important",
}
KEY_TAGS = {
    "CMD-TAG": "Cmd", "CTRL-TAG": "Ctrl", "ALT-TAG": "Alt", "OPT-TAG": "Option",
    "SHIFT-TAG": "Shift", "WIN-TAG": "Win", "CMD": "Cmd", "CTRL": "Ctrl",
    "ALT": "Alt", "SHIFT": "Shift", "OPTION-TAG": "Option",
    "RETURN-TAG": "Return", "ENTER-TAG": "Enter", "ESC-TAG": "Esc",
    "TAB-TAG": "Tab", "SPACE-TAG": "Space", "SPACEBAR-TAG": "Spacebar",
    "DEL-TAG": "Delete", "DELETE-TAG": "Delete", "BACKSPACE-TAG": "Backspace",
    "BACKSP-TAG": "Backspace", "HOME-TAG": "Home", "END-TAG": "End",
}


# --------------------------------------------------------------------------
# TOC parsing  ->  numbered page tree
# --------------------------------------------------------------------------
class Page:
    __slots__ = ("title", "href", "md_rel", "chapter", "subpages")

    def __init__(self, title: str, href: str):
        self.title = title
        self.href = href            # normalised "pages/Book/name.html"
        self.md_rel: str | None = None   # e.g. "content/03-get-started/02-save.md"
        self.chapter: str = ""
        self.subpages: list = []    # orphan Pages nested under this one in the TOC


class Book:
    __slots__ = ("title", "children")

    def __init__(self, title: str):
        self.title = title
        self.children: list = []     # list[Book | Page | ("dup", Page, title)]


def norm_href(href: str, *, base="index.html") -> str:
    """Resolve an href to a canonical 'pages/Book/name.html'.

    `base` is the location of the *referring* document relative to en-US.lproj/ :
    "index.html" for TOC entries, "pages/Book/cur.html" for in-body links.
    Query string and fragment are dropped.
    """
    href, _frag = urldefrag(href)
    href = href.split("?", 1)[0]
    joined = urljoin("http://x/en-US.lproj/" + base, href)
    path = joined.split("://x/", 1)[-1]
    path = path.split("en-US.lproj/", 1)[-1]
    return path


def parse_toc(index_html: bytes) -> Book:
    soup = parse_html(index_html)
    menu = soup.find("div", id="menu")
    root = Book("__root__")
    seen: dict[str, Page] = {}

    def walk(ul: Tag, into: Book):
        for li in ul.find_all("li", recursive=False):
            a = li.find("a", recursive=False)
            sub = li.find("ul", recursive=False)
            if a is None:
                if sub:
                    walk(sub, into)
                continue
            cls = a.get("class", [])
            title = a.get_text(" ", strip=True)
            if "mlink" in cls or (a.get("href", "#") not in ("#", "")):
                href = norm_href(a["href"])
                if href in seen:
                    into.children.append(("dup", seen[href], title))
                else:
                    pg = Page(title, href)
                    seen[href] = pg
                    into.children.append(pg)
                # a page may itself carry a child <ul> (rare) - treat as siblings
                if sub:
                    walk(sub, into)
            else:  # book
                bk = Book(title)
                into.children.append(bk)
                if sub:
                    walk(sub, bk)

    top = menu.find("ul", recursive=False)
    walk(top, root)
    return root


def number_tree(root: Book) -> list[Page]:
    """Assign md_rel to every Page. Returns the unique pages in document order."""
    pages: list[Page] = []

    def bare_page_chapter(pg: Page, ci: int):
        d = f"content/{nn(ci)}-{slug(pg.title)}"
        pg.md_rel = f"{d}/01-{slug(pg.title)}.md"
        pg.chapter = pg.title
        pages.append(pg)

    def do_book(bk: Book, prefix: str, ci: int):
        pi = 0
        for ch in bk.children:
            if isinstance(ch, Book):
                pi += 1
                sub_prefix = f"{prefix}/{nn(pi)}-{slug(ch.title)}"
                do_book(ch, sub_prefix, ci)
            elif isinstance(ch, Page):
                pi += 1
                ch.md_rel = f"{prefix}/{nn(pi)}-{slug(ch.title)}.md"
                ch.chapter = bk.title
                pages.append(ch)
            # ("dup", ...) handled at index.md render time

    ci = 0
    for ch in root.children:
        if isinstance(ch, Book):
            ci += 1
            do_book(ch, f"content/{nn(ci)}-{slug(ch.title)}", ci)
        elif isinstance(ch, Page):
            ci += 1
            bare_page_chapter(ch, ci)
    return pages


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------
class Ctx:
    def __init__(self, md_rel: str):
        # depth of the .md file below manuals/<app>/  -> "../" count to reach it
        self.depth = md_rel.count("/")
        self.md_dir = "/".join(md_rel.split("/")[:-1])   # e.g. content/03-x
        self.orphans: set[str] = set()

    def asset(self, kind: str, name: str) -> str:
        return "../" * self.depth + f"assets/{kind}/{name}"


ASSET_PREFIXES = ("shared/", "images/")


def resolve_asset(src: str) -> tuple[str, str] | None:
    """('shared'|'images', 'sub/path.png') or None if not a local asset."""
    src, _ = urldefrag(src)
    src = (src or "").strip()
    if not src or src.startswith(("http://", "https://", "data:")):
        return None
    joined = urljoin("http://x/photo2/en-US.lproj/pages/B/p.html", src)
    path = joined.split("://x/photo2/", 1)[-1]
    path = path.split("en-US.lproj/", 1)[-1]
    if not path or path.endswith("/"):
        return None
    for p in ASSET_PREFIXES:
        if path.startswith(p):
            return p.rstrip("/"), path[len(p):]
    if path.startswith(("resources/", "pages/")):
        return None
    return "shared", path   # bare or shared-relative filename


def render_page(html: bytes, ctx: Ctx, used_assets: set[tuple[str, str]]) -> str:
    soup = parse_html(html)
    # drop commented-out source (legacy blocks, editorial notes, image briefs)
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    body = soup.body or soup

    parts: list[str] = []
    title_done = False

    # H1 / page title
    h1 = body.find("h1")
    if h1:
        t = _text_only(h1)
        parts.append(f"# {t}".rstrip())
        title_done = True

    # everything after <header>'s h1, in document order
    for el in _top_blocks(body):
        if el is h1:
            continue
        md = block(el, ctx, used_assets)
        if md and md.strip():
            parts.append(md.strip("\n"))

    if not title_done:
        parts.insert(0, "# " + (soup.title.get_text(strip=True) if soup.title else "Untitled"))

    text = "\n\n".join(p for p in parts if p is not None)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return _code_wrap_paths(text)


# Bare Windows/UNC paths in prose (e.g. C:\plugins\nik) otherwise reach the
# LaTeX PDF build as undefined control sequences (\plugins). Wrap them in a
# code span, which every output format escapes correctly. Skips text that is
# already inside backticks.
_PATH_RE = re.compile(
    r"(?<![`\w])((?:[A-Za-z]:\\|\\\\)[^\s`\]]*[A-Za-z0-9_\\/-])")


def _code_wrap_paths(text: str) -> str:
    out = []
    for i, seg in enumerate(text.split("`")):
        out.append(seg if i % 2 else _PATH_RE.sub(r"`\1`", seg))
    return "`".join(out)


def _text_only(el: Tag) -> str:
    # heading text with icons/images stripped
    for img in el.find_all("img"):
        img.decompose()
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()


def _top_blocks(body: Tag):
    """Yield the block-level elements to walk, unwrapping <header>/<section>."""
    out = []

    def collect(container: Tag):
        for c in container.children:
            if isinstance(c, NavigableString):
                if c.strip():
                    out.append(c)
                continue
            if c.name in ("script", "style", "nav", "link", "meta"):
                continue
            if c.name in ("header", "section", "article", "main"):
                collect(c)
            else:
                out.append(c)

    collect(body)
    return out


# ---- block-level ---------------------------------------------------------
def block(el, ctx: Ctx, used: set) -> str:
    if isinstance(el, Comment):
        return ""
    if isinstance(el, NavigableString):
        return re.sub(r"\s+", " ", str(el)).strip()
    name = el.name or ""

    if name in ("script", "style", "select", "option", "form", "nav",
                "link", "meta", "input", "button"):
        return ""

    # platform variant carried as a class (e.g. <p class="osx">) rather than
    # an <x-osx> wrapper: label it, then fall through on a class-less clone
    plat = _plat(el)
    if plat and name not in ("x-osx", "x-win32", "x-win"):
        el.attrs.pop("class", None)
        inner = block(el, ctx, used).strip()
        if not inner:
            return ""
        return f"{plat} {inner}" if "\n" not in inner else f"{plat}\n\n{inner}"

    if name in ("x-osx", "x-win32", "x-win"):
        label = "**macOS:**" if name == "x-osx" else "**Windows:**"
        inner = "\n\n".join(
            b for b in (block(c, ctx, used) for c in el.children) if b and b.strip()
        )
        if not inner.strip():
            return ""
        # inline-only content -> keep on one line after the label
        if not el.find(BLOCK_TAGS):
            return f"{label} {inline(el, ctx, used).strip()}"
        return f"{label}\n\n{inner}"

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        lvl = int(name[1])
        lvl = max(2, lvl)  # page H1 already emitted; demote stray h1
        return f"{'#' * lvl} {_text_only(el)}".rstrip()

    if name == "p":
        return inline(el, ctx, used).strip()

    if name in ("ul", "ol"):
        return list_block(el, ctx, used, ordered=(name == "ol"))

    if name == "figure":
        return figure_block(el, ctx, used)

    if name == "aside":
        return aside_block(el, ctx, used)

    if name == "details":
        return details_block(el, ctx, used)

    if name == "table":
        return table_block(el, ctx, used)

    if name == "blockquote":
        inner = "\n".join(
            b for b in (block(c, ctx, used) for c in el.children) if b and b.strip()
        )
        return "\n".join("> " + ln if ln else ">" for ln in inner.splitlines())

    if name in ("pre",):
        return "```\n" + el.get_text() + "\n```"

    if name == "figcaption":
        t = inline(el, ctx, used).strip()
        return f"*{t}*" if t else ""

    if name in ("div", "span", "x-tag") or name.startswith("x-"):
        # transparent wrapper: is it a SEE ALSO block? handled by section id, but
        # some pages put id="also" on a section already unwrapped -> detect here
        if el.get("id") == "also":
            return seealso_block(el, ctx, used)
        # if the wrapper only held inline content, join as a paragraph
        if not el.find(BLOCK_TAGS):
            return inline(el, ctx, used).strip()
        blocks = [block(c, ctx, used) for c in el.children]
        return "\n\n".join(b for b in blocks if b and b.strip())

    if name == "img":
        return img_md(el, ctx, used)

    if name == "hr":
        return "---"

    if name == "a" and el.get("id") and not el.get_text(strip=True):
        return ""

    # fallback: recurse
    inner = inline(el, ctx, used).strip()
    return inner


def _is_seealso(el: Tag) -> bool:
    return el.name == "section" and el.get("id") == "also"


def seealso_block(el: Tag, ctx: Ctx, used: set) -> str:
    ul = el.find(["ul", "ol"])
    items = []
    if ul:
        for li in ul.find_all("li", recursive=False):
            items.append("- " + inline(li, ctx, used).strip())
    return "#### SEE ALSO:\n\n" + "\n".join(items) if items else ""


_LI_BLOCK = ("ul", "ol", "aside", "details", "figure", "table", "blockquote")


def list_block(el: Tag, ctx: Ctx, used: set, ordered: bool, indent: int = 0) -> str:
    lines: list[str] = []
    pad = "  " * indent
    cpad = "  " * (indent + 1)
    i = 0
    for li in el.find_all("li", recursive=False):
        i += 1
        marker = f"{i}." if ordered else "-"
        # pull block-level children out; the rest is the item's inline text
        sub = [c for c in li.find_all(_LI_BLOCK, recursive=False)]
        for s in sub:
            s.extract()
        text = inline(li, ctx, used).strip()
        lp = _plat(li)
        if lp and text:
            text = f"{lp} {text}"
        lines.append(f"{pad}{marker} {text}" if text else f"{pad}{marker}")
        for s in sub:
            if s.name in ("ul", "ol"):
                lines.append(list_block(s, ctx, used, ordered=(s.name == "ol"),
                                        indent=indent + 1))
            else:
                rendered = block(s, ctx, used).strip()
                if rendered:
                    lines.append("")
                    lines.append("\n".join(cpad + ln if ln else ""
                                           for ln in rendered.splitlines()))
    return "\n".join(lines)


def figure_block(el: Tag, ctx: Ctx, used: set) -> str:
    out = []
    for img in el.find_all("img"):
        out.append(img_md(img, ctx, used))
    cap = el.find("figcaption")
    if cap:
        t = inline(cap, ctx, used).strip()
        if t:
            out.append(f"*{t}*")
    return "\n".join(x for x in out if x)


def aside_block(el: Tag, ctx: Ctx, used: set) -> str:
    classes = set(el.get("class", []))
    kind = next((CALLOUT[c] for c in classes if c in CALLOUT), "Note")
    # inner heading -> use as bold lead instead of a buried "###"
    head = el.find(["h2", "h3", "h4", "h5", "h6"])
    lead_title = None
    if head:
        lead_title = _text_only(head)
        head.extract()
    body_blocks = [block(c, ctx, used) for c in el.children]
    body_blocks = [b for b in body_blocks if b and b.strip()]
    inner = "\n\n".join(body_blocks).strip()
    if lead_title:
        merged = f"**{kind} — {lead_title}:** {inner}".rstrip()
    else:
        # fold the label into the first paragraph
        if inner.lower().startswith(("**", "- ")):
            merged = f"**{kind}:**\n\n{inner}"
        else:
            merged = f"**{kind}:** {inner}"
    return "\n".join("> " + ln if ln else ">" for ln in merged.splitlines())


def details_block(el: Tag, ctx: Ctx, used: set) -> str:
    summ = el.find("summary")
    label = _text_only(summ) if summ else ""
    if summ:
        summ.extract()
    body_blocks = [block(c, ctx, used) for c in el.children]
    body_blocks = [b for b in body_blocks if b and b.strip()]
    inner = "\n\n".join(body_blocks).strip()
    if label and inner:
        return f"**{label}**\n\n{inner}"
    return f"**{label}**" if label else inner


def table_block(el: Tag, ctx: Ctx, used: set) -> str:
    rows = el.find_all("tr")
    if not rows:
        return ""
    def cells(tr, tagnames):
        return [inline(td, ctx, used).strip().replace("\n", " ").replace("|", "\\|")
                for td in tr.find_all(tagnames, recursive=False)]
    header = cells(rows[0], ["th", "td"])
    ncol = len(header) or max((len(r.find_all(["th", "td"])) for r in rows), default=0)
    if not any(header):
        header = [""] * ncol
    out = ["| " + " | ".join(header) + " |",
           "| " + " | ".join(["---"] * ncol) + " |"]
    for tr in rows[1:]:
        c = cells(tr, ["td", "th"])
        c += [""] * (ncol - len(c))
        out.append("| " + " | ".join(c[:ncol]) + " |")
    return "\n".join(out)


def img_md(el: Tag, ctx: Ctx, used: set) -> str:
    src = el.get("src", "")
    alt = (el.get("alt") or "").strip()
    res = resolve_asset(src)
    if res is None:
        return f"![{alt}]({src})" if src else ""
    kind, name = res
    used.add((kind, name))
    return f"![{alt}]({ctx.asset(kind, name)})"


# ---- inline ------------------------------------------------------------
def inline(el, ctx: Ctx, used: set) -> str:
    if isinstance(el, NavigableString):
        return re.sub(r"[ \t\r\n]+", " ", unescape(str(el)))
    name = el.name or ""

    if name in ("script", "style", "select", "option", "input", "button"):
        return ""

    if name == "br":
        return "  \n"

    if name == "img":
        return img_md(el, ctx, used)

    if name in ("b", "strong"):
        return f"**{_inline_children(el, ctx, used).strip()}**"

    if name in ("i", "em"):
        return f"*{_inline_children(el, ctx, used).strip()}*"

    if name in ("code", "kbd", "samp", "tt"):
        return f"`{el.get_text().strip()}`"

    if name in ("sup", "sub"):
        return f"<{name}>{_inline_children(el, ctx, used)}</{name}>"

    if name == "span":
        classes = set(el.get("class", []))
        if "key" in classes:
            txt = el.get_text().strip()
            if not txt:  # e.g. <span class="key CMD-TAG"></span>
                for c in classes:
                    if c in KEY_TAGS:
                        txt = KEY_TAGS[c]
                        break
                else:
                    tagish = next((c for c in classes if c.endswith("-TAG")), "")
                    txt = KEY_TAGS.get(tagish, tagish.replace("-TAG", "").title() or "")
            return f"`{txt}`" if txt else ""
        if "ui" in classes or "menu" in classes or "filepath" in classes:
            return f"**{_inline_children(el, ctx, used).strip()}**"
        plat = _plat(el)
        if plat:
            inner = _inline_children(el, ctx, used).strip()
            return f"{plat} {inner}" if inner else ""
        # term / plain
        return _inline_children(el, ctx, used)

    if name in ("x-osx", "x-win32", "x-win"):
        lbl = "**macOS:**" if name == "x-osx" else "**Windows:**"
        inner = _inline_children(el, ctx, used).strip()
        return f"{lbl} {inner}" if inner else ""

    if name == "a":
        return link_md(el, ctx, used)

    if name in ("ul", "ol", "li", "p", "div", "figure", "figcaption",
                "aside", "details", "section", "table", "tr", "td", "th"):
        # inline() called on a container: flatten its text
        return _inline_children(el, ctx, used)

    return _inline_children(el, ctx, used)


def _is_key_span(c) -> bool:
    return isinstance(c, Tag) and c.name == "span" and "key" in c.get("class", [])


def _inline_children(el: Tag, ctx: Ctx, used: set) -> str:
    out: list[str] = []
    prev_key = False
    for c in el.children:
        # join adjacent keyboard-key spans as "`A` + `B`"
        if _is_key_span(c):
            if prev_key:
                # drop a trailing lone "+" / whitespace we just emitted, add joiner
                while out and out[-1].strip() in ("", "+"):
                    out.pop()
                out.append(" + ")
            out.append(inline(c, ctx, used))
            prev_key = True
            continue
        if isinstance(c, NavigableString) and not str(c).strip():
            out.append(inline(c, ctx, used))
            continue  # keep prev_key across pure whitespace
        prev_key = False
        out.append(inline(c, ctx, used))
    return "".join(out)


PAGE_LINK_RE = re.compile(r"\.html?($|[#?])", re.I)


def link_md(el: Tag, ctx: Ctx, used: set) -> str:
    text = _inline_children(el, ctx, used).strip()
    href = (el.get("href") or "").strip()
    if not href or href.startswith("#"):
        return text
    if href.startswith(("http://", "https://", "mailto:")):
        # normalise same-site help links to internal placeholders
        m = re.search(r"affinity\.help/\w+2?/en-US\.lproj/(pages/[^\s\"'?#]+\.html)",
                      href)
        if m:
            frag = urldefrag(href)[1]
            tgt = norm_href(m.group(1))
            ctx.orphans.add(tgt)
            return f"[{text}](AFF:{tgt}{('#' + frag) if frag else ''})"
        return f"[{text}]({href})"
    if PAGE_LINK_RE.search(href):
        _base, frag = urldefrag(href)
        tgt = norm_href(href, base=getattr(ctx, "cur_href", "index.html"))
        ctx.orphans.add(tgt)
        return f"[{text}](AFF:{tgt}{('#' + frag) if frag else ''})"
    return f"[{text}]({href})"


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------
def build_index_md(app: str, root: Book, title: str) -> str:
    lines = [f"# Affinity {title} 2 — Manual (Table of Contents)", "",
             "Converted from the official Affinity " + title + " 2 HTML help pages. "
             "Some screenshots are missing from the source export and show as broken "
             "images until you add them — see `MISSING_IMAGES.md` in this folder.", ""]

    def emit(node, depth):
        pad = "  " * depth
        if isinstance(node, Book):
            if node.title != "__root__":
                lines.append(f"{pad}- **{node.title}**")
            for ch in node.children:
                emit(ch, depth + (0 if node.title == "__root__" else 1))
        elif isinstance(node, Page):
            lines.append(f"{pad}- [{node.title}]({node.md_rel})")
            for sp in node.subpages:
                lines.append(f"{pad}  - [{sp.title}]({sp.md_rel})")
        elif isinstance(node, tuple) and node[0] == "dup":
            _, pg, dtitle = node
            lines.append(f"{pad}- [{dtitle}]({pg.md_rel}) _(see above)_")

    emit(root, 0)
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    app = argv[0]
    dry = "--dry-run" in argv[1:]
    titles = {"photo": "Photo", "designer": "Designer", "publisher": "Publisher"}
    title = titles.get(app, app.title())

    mirror = ROOT / ".work" / "mirror" / app
    if not (mirror / "index.html").is_file():
        print(f"no mirror at {mirror}/index.html — run scripts/mirror_manual.py {app}",
              file=sys.stderr)
        return 1

    man = ROOT / "manuals" / app
    src_out = ROOT / "sources" / app

    root = parse_toc((mirror / "index.html").read_bytes())
    pages = number_tree(root)
    print(f"{app}: {len(pages)} pages from TOC")

    if dry:
        for pg in pages[:12]:
            print(f"  {pg.href:45s} -> {pg.md_rel}")
        print("  ...")
        return 0

    # fresh manuals/<app>
    for sub in ("content", "assets"):
        shutil.rmtree(man / sub, ignore_errors=True)
    (man / "content").mkdir(parents=True, exist_ok=True)
    (man / "assets" / "shared").mkdir(parents=True, exist_ok=True)
    (man / "assets" / "images").mkdir(parents=True, exist_ok=True)

    href_to_md = {pg.href: pg.md_rel for pg in pages}
    toc_order = {pg.href: i for i, pg in enumerate(pages)}
    page_by_href = {pg.href: pg for pg in pages}
    used_assets: set[tuple[str, str]] = set()
    orphan_refs: dict[str, set[str]] = {}   # orphan href -> referring TOC hrefs
    written = 0

    def convert(pg: Page):
        nonlocal written
        src = mirror / pg.href
        if not src.is_file():
            (man / pg.md_rel).parent.mkdir(parents=True, exist_ok=True)
            (man / pg.md_rel).write_text(
                f"# {pg.title}\n\n_(source page not available)_\n",
                encoding="utf-8", newline="\n")
            return
        ctx = Ctx(pg.md_rel)
        ctx.cur_href = pg.href
        md = render_page(src.read_bytes(), ctx, used_assets)
        (man / pg.md_rel).parent.mkdir(parents=True, exist_ok=True)
        (man / pg.md_rel).write_text(md, encoding="utf-8", newline="\n")
        written += 1
        return ctx

    for pg in pages:
        if not (mirror / pg.href).is_file():
            print(f"  MISSING SOURCE {pg.href}")
            convert(pg)
            continue
        ctx = convert(pg)
        for o in ctx.orphans:
            if o not in href_to_md:
                orphan_refs.setdefault(o, set()).add(pg.href)

    # ---- orphan pages: nest each under its most-specific TOC referrer ---
    # only pages that were actually mirrored; a link to a non-existent page
    # just loses its hyperlink (label kept) in fix_links below.
    orphans = [o for o in sorted(orphan_refs) if (mirror / o).is_file()]
    orphan_pages: list[Page] = []
    fallback = Book("Additional pages")
    if orphans:
        # a referrer is "more specific" the fewer orphans it introduces
        ref_load: dict[str, int] = {}
        for refs in orphan_refs.values():
            for r in refs:
                ref_load[r] = ref_load.get(r, 0) + 1
        seq: dict[str, int] = {}

        def book_of(href: str) -> str:
            parts = href.split("/")
            return parts[1].lower() if len(parts) > 2 else ""

        def pick_parent(orphan_href: str, refs: list[str]) -> str:
            """Most-specific referrer, preferring one in the same content family."""
            fam = re.split(r"[_-]", Path(orphan_href).stem, maxsplit=1)[0].lower()
            family = [r for r in refs if fam and book_of(r).startswith(fam[:5])]
            pool = family or refs
            # fewest orphans introduced == most specific; break ties by TOC order
            return min(pool, key=lambda r: (ref_load[r], toc_order[r]))

        for href in orphans:
            name = Path(href).stem
            otitle = _title_from_source(mirror / href, name)
            refs = [r for r in orphan_refs[href] if r in page_by_href]
            child = Page(otitle, href)
            if refs:
                parent = page_by_href[pick_parent(href, refs)]
                pdir = parent.md_rel[:-3]             # ".../03-blur-filters.md" -> dir
                seq[pdir] = seq.get(pdir, 0) + 1
                child.md_rel = f"{pdir}/{nn(seq[pdir])}-{slug(name)}.md"
                parent.subpages.append(child)
            else:
                seq["_fb"] = seq.get("_fb", 0) + 1
                child.md_rel = (f"content/{nn(99)}-additional-pages/"
                                f"{nn(seq['_fb'])}-{slug(name)}.md")
                fallback.children.append(child)
            href_to_md[href] = child.md_rel
            orphan_pages.append(child)

        for child in orphan_pages:
            convert(child)
        if fallback.children:
            root.children.append(fallback)

    # ---- resolve AFF: link placeholders -------------------------------
    def fix_links(md_text: str, md_rel: str) -> str:
        here = (man / md_rel).parent

        def repl(m):
            tgt, frag = m.group("tgt"), m.group("frag") or ""
            dest = href_to_md.get(tgt)
            if not dest:
                return m.group("text")  # drop dead link, keep label
            relpath = _relpath(here, man / Path(dest))
            return f"[{m.group('text')}]({relpath}{frag})"

        return re.sub(
            r"\[(?P<text>[^\]]+)\]\(AFF:(?P<tgt>[^)#\s]+)(?P<frag>#[^)\s]*)?\)",
            repl, md_text)

    for md_file in (man / "content").rglob("*.md"):
        rel = md_file.relative_to(man).as_posix()
        txt = md_file.read_text(encoding="utf-8")
        if "AFF:" in txt:
            md_file.write_text(fix_links(txt, rel), encoding="utf-8", newline="\n")

    # ---- copy used images -------------------------------------------
    missing_imgs: list[str] = []
    copied = 0
    for kind, name in sorted(used_assets):
        srcf = mirror / (kind + "/" + name)
        dstf = man / "assets" / kind / name
        if srcf.is_file():
            dstf.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(srcf, dstf)
            copied += 1
        else:
            missing_imgs.append(f"{kind}/{name}")

    # ---- index.md, README.md, MISSING_IMAGES.md --------------------
    (man / "index.md").write_text(build_index_md(app, root, title),
                                  encoding="utf-8", newline="\n")

    n_shared = sum(1 for k, _ in used_assets if k == "shared")
    n_imgs = sum(1 for k, _ in used_assets if k == "images")
    (man / "README.md").write_text(
        f"# Affinity {title} 2 — Manual (Markdown source)\n\n"
        f"Converted from the official Affinity {title} 2 HTML help pages by "
        f"`scripts/import_manual.py`. This folder is the **canonical source**; the "
        f"EPUB, PDF, Obsidian vault, and HTML site in each release are all "
        f"generated from it.\n\n"
        f"- `index.md` — full table of contents, in the same order as the "
        f"original manual's sidebar. `scripts/gen_summary.py` turns this into "
        f"`SUMMARY.md`.\n"
        f"- `content/` — one Markdown file per help page, in chapter folders.\n"
        f"- `assets/images/` — {n_imgs} screenshots bundled in the page export.\n"
        f"- `assets/shared/` — {n_shared} shared UI/diagram images from the "
        f"site's `shared/` folder.\n\n"
        f"Links between pages and images are relative Markdown (work on GitHub, "
        f"in mdBook, and in Obsidian).\n\n"
        + (f"**Known gaps:** {len(missing_imgs)} referenced screenshots could not "
           f"be downloaded — see `MISSING_IMAGES.md`.\n" if missing_imgs else ""),
        encoding="utf-8", newline="\n")

    mi = ["# Missing images", ""]
    if missing_imgs:
        mi.append(f"{len(missing_imgs)} image(s) referenced by the manual could not "
                  f"be retrieved from the source site (blocked/failed downloads). "
                  f"Drop the files in at the paths below and they resolve with no "
                  f"Markdown edits:")
        mi.append("")
        for m in missing_imgs:
            mi.append(f"    assets/{m}")
    else:
        mi.append("None — every referenced image was retrieved.")
    (man / "MISSING_IMAGES.md").write_text("\n".join(mi) + "\n",
                                           encoding="utf-8", newline="\n")

    # ---- lean sources/<app> --------------------------------------
    shutil.rmtree(src_out, ignore_errors=True)
    src_out.mkdir(parents=True, exist_ok=True)
    for item in ("index.html", "search.js", "landing.html", "landing.js",
                 "InfoPlist.strings", "help.idx", "Results.html"):
        p = mirror / item
        if p.is_file():
            shutil.copy2(p, src_out / item)
    if (mirror / "pages").is_dir():
        shutil.copytree(mirror / "pages", src_out / "pages")
    if (mirror / "images").is_dir():
        shutil.copytree(mirror / "images", src_out / "images")
    if (mirror / "stylesheets").is_dir():
        shutil.copytree(mirror / "stylesheets", src_out / "stylesheets")

    print(f"  wrote {written} markdown files")
    print(f"  copied {copied} images ({n_shared} shared, {n_imgs} page)")
    if orphans:
        n_fb = len(fallback.children)
        print(f"  {len(orphans)} non-TOC page(s): {len(orphans) - n_fb} nested "
              f"under their referring page" +
              (f", {n_fb} -> 99-additional-pages/" if n_fb else ""))
    if missing_imgs:
        print(f"  !! {len(missing_imgs)} referenced images missing (MISSING_IMAGES.md)")
    print(f"  lean mirror -> sources/{app}/")
    print(f"\n  next: python3 scripts/gen_summary.py {app}")
    return 0


def _relpath(frm: Path, to: Path) -> str:
    import os
    return Path(os.path.relpath(to, frm)).as_posix()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
