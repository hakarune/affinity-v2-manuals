# affinity-v2-manuals

Offline archive of the official help documentation for **Affinity Photo 2**,
**Affinity Designer 2**, and **Affinity Publisher 2** (Serif).

The official Affinity help site needs an internet connection and may disappear.
This repo keeps a portable copy: Markdown as the single source of truth, with
EPUB, PDF, an Obsidian vault, a self-hostable HTML site, and a single-file HTML
build all **generated** from it and attached to each [Release](../../releases).

| Manual | Status |
| --- | --- |
| Affinity Designer 2 | imported — 316 pages, 737 images (2 screenshots missing, see `KNOWN_ISSUES.md`) |
| Affinity Photo 2 | not yet imported |
| Affinity Publisher 2 | not yet imported |

## Downloads

Each release (per manual) contains:

| File | What it is |
| --- | --- |
| `affinity-<app>-2-manual-markdown.zip` | the `manuals/<app>/` Markdown tree, as-is |
| `affinity-<app>-2-manual-obsidian-vault.zip` | same content + `.obsidian/` config + `[[wikilinks]]` — unzip and "Open folder as vault" |
| `affinity-<app>-2-manual-html.zip` | self-contained static site — unzip, open `index.html`, works offline (search included), or drop on a NAS/web server |
| `affinity-<app>-2-manual.epub` | for e-readers |
| `affinity-<app>-2-manual.pdf` | for printing / fixed layout |
| `affinity-<app>-2-manual.html` | one self-contained HTML file (no folder) |
| `affinity-<app>-2-source-html.zip` | the raw mirrored help pages, for preservation / re-conversion |

Live HTML editions are also published to GitHub Pages, one per manual:
`https://<owner>.github.io/affinity-v2-manuals/designer/` (and `/photo/`, `/publisher/`).

## Repository layout

```
manuals/<app>/        Markdown source of truth (index.md + content/ + assets/)
sources/<app>/         raw mirrored HTML help pages
config/
  pandoc/*.yaml        per-manual EPUB/PDF/HTML metadata
  mdbook/book.toml.tmpl
  obsidian/.obsidian/  vault config copied into the Obsidian build
scripts/
  gen_summary.py       manuals/<app>/index.md  ->  SUMMARY.md + build order
  make_obsidian.py     Markdown tree  ->  Obsidian vault (wikilinks + config)
  gen_landing.py       GitHub Pages landing page
  build.sh             builds every format into dist/
.github/workflows/
  pages.yml            build + deploy the HTML sites to GitHub Pages (on push to main)
  release.yml          build every format + attach to the Release (on tag v*)
```

## Building locally

Needs: [`mdbook`](https://rust-lang.github.io/mdBook/), [`pandoc`](https://pandoc.org/),
a PDF engine (`weasyprint` or `xelatex`), `zip`, `python3`.

```sh
scripts/build.sh            # all imported manuals
scripts/build.sh designer   # just one
```

Output lands in `dist/` (release artefacts) and `.work/site/` (the Pages tree).
Missing a tool just skips the formats that need it.

## Cutting a release

```sh
git tag v0.1.0
git push --tags        # release.yml builds everything and creates the Release
```

Pushes to `main` that touch `manuals/**` rebuild the GitHub Pages sites automatically.

## Adding Photo / Publisher

See [`docs/ADDING-A-MANUAL.md`](docs/ADDING-A-MANUAL.md). Any `manuals/<app>/`
with an `index.md` is picked up automatically.

## Copyright

The manual text and images are © Serif (Europe) Ltd. This is an unofficial
archive for offline reference and is **not affiliated with or endorsed by
Serif**. Only the tooling in `scripts/`, `config/`, and `.github/` is covered by
[LICENSE](LICENSE); see [NOTICE](NOTICE). Rights holders: open an issue to
request removal.
