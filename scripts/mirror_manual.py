#!/usr/bin/env python3
"""TOC-driven mirror of an Affinity 2 help site into .work/mirror/<app>/.

Usage:  mirror_manual.py <app>          # app = photo | publisher | designer

Why TOC-driven and not `wget -r`: the origin serves a 403 "error" page for any
URL that does not exist, so blind recursion chases stale in-body links into dead
ends. The sidebar TOC in index.html is the authoritative list of real pages.

This writes the FULL raw mirror (pages + shared pool + resources) into the
git-ignored .work/ scratch area. `scripts/import_manual.py` then derives the
lean, committed sources/<app>/ and the manuals/<app>/ Markdown tree from it.

Writes:
  .work/mirror/<app>/index.html
  .work/mirror/<app>/pages/<Book>/<page>.html   (one per TOC entry, query dropped)
  .work/mirror/<app>/shared/...                  (shared image pool, as referenced)
  .work/mirror/<app>/resources/...               (css/js referenced by pages)
  .work/mirror/<app>/images/...                  (page-specific images)
  .work/mirror/<app>/_mirror_report.txt
"""
from __future__ import annotations

import sys
import time
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
ASSET_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".tif", ".tiff",
             ".css", ".js", ".mp4", ".webm")
WORKERS = 6
PAUSE = 0.15


def fetch(url: str, tries: int = 5) -> bytes:
    """GET with exponential backoff. Raises on final failure."""
    last = None
    for i in range(tries):
        try:
            req = Request(url, headers={"User-Agent": UA,
                                        "Accept": "*/*",
                                        "Referer": url})
            with urlopen(req, timeout=30) as r:
                return r.read()
        except (HTTPError, URLError, TimeoutError) as e:
            last = e
            # 403/404 here are almost always "page really gone" - bail fast.
            if isinstance(e, HTTPError) and e.code in (403, 404):
                raise
            time.sleep(1.5 * (2 ** i))
    raise last  # type: ignore[misc]


def strip_query(url: str) -> str:
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path, "", ""))


def toc_pages(index_html: bytes, page_base: str) -> list[str]:
    """Ordered, de-duplicated list of absolute page URLs from the sidebar TOC."""
    soup = BeautifulSoup(index_html, "html.parser")
    menu = soup.find("div", id="menu")
    out, seen = [], set()
    for a in menu.find_all("a", class_="mlink"):
        href = a.get("href", "")
        if not href or href.startswith("#"):
            continue
        absu = strip_query(urljoin(page_base, href))
        if absu not in seen:
            seen.add(absu)
            out.append(absu)
    return out


def rel_from_site_root(url: str, site_root: str) -> str | None:
    if not url.startswith(site_root):
        return None
    return url[len(site_root):].lstrip("/")


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    app = argv[0]
    site_root = f"https://affinity.help/{app}2/"
    page_base = f"{site_root}en-US.lproj/"
    dest = ROOT / ".work" / "mirror" / app

    print(f"== mirroring {app} ==")
    print(f"   site root : {site_root}")
    dest.mkdir(parents=True, exist_ok=True)

    # --- index.html -------------------------------------------------------
    index_html = fetch(page_base + "index.html")
    (dest / "index.html").write_bytes(index_html)
    pages = toc_pages(index_html, page_base)
    print(f"   TOC pages : {len(pages)}")

    # --- helper .lproj files (best effort) -------------------------------
    for extra in ("search.js", "help.idx", "Results.html", "InfoPlist.strings",
                  "landing.html"):
        try:
            (dest / extra).write_bytes(fetch(page_base + extra, tries=2))
        except Exception:
            pass

    # --- pages ----------------------------------------------------------
    page_fail: dict[str, str] = {}
    page_html: dict[str, bytes] = {}

    def get_page(url: str):
        time.sleep(PAUSE)
        rel = rel_from_site_root(url, site_root)  # e.g. en-US.lproj/pages/X/y.html
        try:
            data = fetch(url)
        except Exception as e:
            return url, rel, None, str(e)
        return url, rel, data, None

    def discover(html: bytes, from_url: str) -> set[str]:
        """In-body links to other help pages (pages/**/*.html), absolute, deduped."""
        found = set()
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all("a", href=True):
            h = a["href"]
            if h.startswith(("http", "#", "mailto:")) or ".html" not in h.lower():
                continue
            absu = strip_query(urljoin(from_url, h))
            if absu.startswith(page_base + "pages/") and absu.endswith(".html"):
                found.add(absu)
        return found

    # BFS: TOC pages, then in-body links they reach, capped a few hops deep.
    frontier = list(dict.fromkeys(pages))
    done: set[str] = set()
    hop = 0
    while frontier and hop < 4:
        hop += 1
        new_links: set[str] = set()
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            for fut in as_completed(ex.submit(get_page, u) for u in frontier):
                url, rel, data, err = fut.result()
                done.add(url)
                if err:
                    page_fail[url] = err
                    if hop == 1:
                        print(f"   PAGE FAIL {url}  ({err})")
                    continue
                page_fail.pop(url, None)
                page_html[url] = data
                sub = rel.split("en-US.lproj/", 1)[-1]
                p = dest / sub
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
                new_links |= discover(data, url)
        frontier = [u for u in new_links if u not in done]
        if frontier:
            print(f"   hop {hop}: +{len(frontier)} linked pages to fetch")

    # pages that only ever 403'd are dead links in the source, not our failure
    page_fail = {u: e for u, e in page_fail.items() if u not in page_html}
    print(f"   pages ok  : {len(page_html)} (of {len(pages)} TOC + "
          f"{len(page_html) - len([u for u in pages if u in page_html])} discovered)")

    # --- assets referenced by the pages + index ------------------------
    want: set[str] = set()
    for src_url, html in list(page_html.items()) + [(page_base + "index.html", index_html)]:
        soup = BeautifulSoup(html, "html.parser")
        for tag, attr in (("img", "src"), ("link", "href"),
                          ("script", "src"), ("source", "src")):
            for el in soup.find_all(tag):
                v = el.get(attr)
                if not v or v.startswith(("data:", "#", "mailto:")):
                    continue
                absu = strip_query(urljoin(src_url, v))
                if absu.lower().endswith(ASSET_EXT) and absu.startswith(site_root):
                    want.add(absu)

    print(f"   assets    : {len(want)} referenced under {site_root}")

    asset_fail: dict[str, str] = {}
    asset_ok = 0

    def get_asset(url: str):
        time.sleep(PAUSE)
        rel = rel_from_site_root(url, site_root)
        try:
            return url, rel, fetch(url), None
        except Exception as e:
            return url, rel, None, str(e)

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for fut in as_completed(ex.submit(get_asset, u) for u in sorted(want)):
            url, rel, data, err = fut.result()
            if err:
                asset_fail[url] = err
                continue
            p = dest / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
            asset_ok += 1

    print(f"   assets ok : {asset_ok} / {len(want)}")

    # --- tidy layout: en-US.lproj/{images,pages,...} -> top level ------
    lproj = dest / "en-US.lproj"
    if lproj.is_dir():
        for child in lproj.iterdir():
            target = dest / child.name
            if target.exists():
                for sub in child.rglob("*"):
                    if sub.is_file():
                        rel = sub.relative_to(child)
                        (target / rel).parent.mkdir(parents=True, exist_ok=True)
                        sub.replace(target / rel)
            else:
                child.replace(target)
        import shutil as _sh
        _sh.rmtree(lproj, ignore_errors=True)

    # --- report -------------------------------------------------------
    report = {
        "app": app,
        "toc_pages": len(pages),
        "pages_ok": len(page_html),
        "pages_failed": page_fail,
        "assets_referenced": len(want),
        "assets_ok": asset_ok,
        "assets_failed": asset_fail,
    }
    (dest / "_mirror_report.txt").write_text(
        json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(f"\n   report    : {(dest / '_mirror_report.txt').relative_to(ROOT)}")
    if page_fail:
        print(f"   !! {len(page_fail)} pages failed (see report)")
    if asset_fail:
        print(f"   !! {len(asset_fail)} assets failed (see report)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
