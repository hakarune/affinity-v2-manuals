# Adding a manual (Photo / Publisher)

The build treats any `manuals/<app>/` that contains an `index.md` as a manual and
generates every format for it. Designer and Photo were imported with the two
scripts below; Publisher is the same three commands.

```sh
python  scripts/mirror_manual.py  publisher   # 1. mirror affinity.help -> .work/mirror/publisher/
python  scripts/import_manual.py  publisher   # 2. convert -> manuals/publisher/ + sources/publisher/
python3 scripts/gen_summary.py    publisher   # 3. index.md -> SUMMARY.md (checks every link)
```

`mirror_manual.py` and `import_manual.py` need **beautifulsoup4** and, strongly
recommended, **lxml** (`pip install beautifulsoup4 lxml`). Without lxml the
converter falls back to the stdlib parser, which mangles the help site's
slightly-malformed tables. `gen_summary.py` is standard-library only.

Then review the diff, commit `manuals/<app>/` + `sources/<app>/`, push to `main`
(the Pages site rebuilds), and tag a release (`git tag vX.Y.Z && git push
--tags`) to publish the EPUB/PDF/zips.

---

## What the scripts do

### 1. `mirror_manual.py <app>`

Fetches `https://affinity.help/<app>2/en-US.lproj/index.html`, parses the sidebar
**table of contents** for the authoritative page list, downloads every page, then
follows in-body links a few hops out to catch pages the sidebar omits (Photo, for
instance, hides ~100 per-filter / per-adjustment pages behind overview pages).
Images and CSS referenced by the pages are pulled too.

It is TOC-driven rather than `wget -r` because the origin answers **403 for any
URL that does not exist**, so blind recursion chases dead links forever.

Output goes to the git-ignored `.work/mirror/<app>/` (full raw mirror, ~70 MB for
Photo) plus a `_mirror_report.txt` listing any pages/images the origin refused
(a handful of genuinely-dead links and, historically, 2-3 screenshots the CDN
blocks — the same ones missing from Designer).

If `affinity.help` is unreachable, the Internet Archive form is
`https://web.archive.org/web/2id_/<url>`.

### 2. `import_manual.py <app>`

Converts the mirror to the canonical Markdown tree:

```
manuals/<app>/
├── index.md                       curated TOC (chapters **bold**, pages linked,
│                                   non-sidebar pages nested under their referrer)
├── content/NN-chapter/NN-page.md   one Markdown file per help page
├── assets/shared/                  shared image pool (only images actually used)
├── assets/images/                  page-specific screenshots (only those used)
├── README.md   MISSING_IMAGES.md
sources/<app>/                      lean raw mirror committed for preservation:
                                    index.html + pages/ + images/ (no shared/ pool,
                                    no resources/ — same shape as sources/designer/)
```

Conversion rules (matching the hand-checked Designer import):

- `<h1>` → `# Title` (heading icons dropped).
- `<section>` wrappers unwrapped, their `<h2>`/`<h3>` kept as `##`/`###`.
- `<aside class="box note|tip|warning|prefs">` → `> **Note:**` / `> **Tip:**` /
  `> **Warning:**` / `> **Preferences:**` block-quotes (an inner heading becomes
  the bold lead, not a `###` buried in the quote).
- `<figure>` → `![alt](rel)` images followed by `*figcaption*`.
- `<details><summary>X</summary>…` → **X** then the contents.
- `<section id="also">` → a `#### SEE ALSO:` list.
- `<span class="ui">` → `**bold**`; `<span class="key">` → `` `Key` `` (adjacent
  keys joined as `` `A` + `B` ``); `<x-osx>` / `<x-win32>` / `class="osx"` /
  `class="win32"` → **macOS:** / **Windows:** labels.
- HTML comments (Serif leaves legacy blocks and editorial notes commented out)
  are dropped.
- Links between pages become relative Markdown; a link to a page that does not
  exist keeps its text but loses the hyperlink.
- Image `src` rewritten to `../…/assets/shared/…` or `…/assets/images/…`.

Pages reachable only through in-body links are nested under whichever sidebar
page links them, in that page's chapter (`…/03-color-filters/07-filter-halftone.md`).

### 3. `gen_summary.py <app>`

Turns `index.md` into mdBook's `SUMMARY.md` and prints a warning for any TOC
entry whose target file is missing. Zero warnings = every link resolves.

## 4. Ship it

```sh
scripts/build.sh <app>          # needs mdbook, pandoc, xelatex or weasyprint, zip
```

Fix anything `build.sh` reports, then commit and tag as above.
