# Affinity Photo 2 — Manual (Markdown source)

Converted from the official Affinity Photo 2 HTML help pages by `scripts/import_manual.py`. This folder is the **canonical source**; the EPUB, PDF, Obsidian vault, and HTML site in each release are all generated from it.

- `index.md` — full table of contents, in the same order as the original manual's sidebar. `scripts/gen_summary.py` turns this into `SUMMARY.md`.
- `content/` — one Markdown file per help page, in chapter folders.
- `assets/images/` — 92 screenshots bundled in the page export.
- `assets/shared/` — 966 shared UI/diagram images from the site's `shared/` folder.

Links between pages and images are relative Markdown (work on GitHub, in mdBook, and in Obsidian).

**Known gaps:** 3 referenced screenshots could not be downloaded — see `MISSING_IMAGES.md`.
