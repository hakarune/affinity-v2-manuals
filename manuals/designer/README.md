# Affinity Designer 2 — Manual (Markdown source)

Converted from the official Affinity Designer 2 HTML help pages (retrieved via the
Internet Archive). This folder is the **canonical source**; the EPUB, PDF,
Obsidian vault, and HTML site in each release are all generated from it.

- `index.md` — full table of contents, in the same order as the original
  manual's sidebar. `scripts/gen_summary.py` turns this into `SUMMARY.md`.
- `content/` — one Markdown file per help page, in chapter folders
  (`01-introduction/`, `02-user-interface/`, …).
- `assets/images/` — 50 screenshots bundled in the original page export.
- `assets/shared/` — 687 shared UI/diagram images pulled from the site's
  `shared/` folder.

Links between pages are relative Markdown links (work on GitHub, in mdBook, and
in Obsidian). Image links are relative too.

**Known gaps:** 2 of 689 referenced screenshots could not be downloaded — see
`MISSING_IMAGES.md`. Drop the files in at the named paths and they resolve with
no edits.
