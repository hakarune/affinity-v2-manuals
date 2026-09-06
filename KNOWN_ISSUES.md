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

## Affinity Photo 2

- **3 missing screenshots.** `assets/images/smooth_low_high.jpg`,
  `assets/images/feather_low_high.jpg` and
  `assets/images/feature_focusmerge_sources.png` return blocked/failed downloads
  from the source site (the same CDN behaviour that costs Designer 2 images).
  They render as broken images on the selection-refinement and focus-merge pages.
  Drop the files in at those exact paths — no Markdown edits needed. See
  `manuals/photo/MISSING_IMAGES.md`.
- **Non-sidebar pages are nested by heuristic.** Photo's official sidebar groups
  ~100 per-filter / per-adjustment / per-tool pages behind overview pages. The
  import attaches each to the sidebar page that links it (e.g.
  `content/11-filters-and-effects/02-blur-filters/07-gaussian-blur.md`). A page
  linked from several places lands under the most specific one; a few of these
  choices are debatable but every page is reachable and every link resolves.
- **Two upstream content glitches, preserved as-is.** The regular-expressions
  page carries a leftover image brief, and one row of the Settings/Preferences
  table contains an unfilled `<# name #>` template. Both are in Serif's published
  HTML.
- **Cross-page links in the single-file EPUB/PDF/HTML** go inert, as with
  Designer — the multi-page HTML, Markdown and Obsidian builds keep them.

## Affinity Publisher 2

- Not imported yet. See `docs/ADDING-A-MANUAL.md`.
