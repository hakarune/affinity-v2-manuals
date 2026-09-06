# Known issues

## Affinity Designer 2

- **2 missing screenshots.** `assets/shared/shapes_dragnode.png` and
  `assets/shared/shapes_dragshape.png` returned blocked/failed downloads from
  the source site. They are referenced from the curve/node editing pages and
  currently render as broken images. If you obtain them, drop the files at those
  exact paths — no Markdown edits needed. (See `manuals/designer/MISSING_IMAGES.md`.)
- **Cross-page links in the single-file EPUB/PDF/HTML.** Those builds concatenate
  every page into one document; links that point to *other pages* become inert
  there. The multi-page HTML site and the Markdown/Obsidian builds keep working
  links.

## Affinity Photo 2 / Publisher 2

- Not imported yet. See `docs/ADDING-A-MANUAL.md`.
