# Adding a manual (Photo / Publisher)

The build treats any `manuals/<app>/` that contains an `index.md` as a manual and
generates every format for it. To add Photo or Publisher, reproduce the shape of
`manuals/designer/`.

## 1. Mirror the source

The official help lives at `https://affinity.help/<app>2/en-US.lproj/` with a
shared image pool at `https://affinity.help/<app>2/shared/`. If the live site is
gone, use the Internet Archive (`https://web.archive.org/web/2id_/<url>`).

```sh
app=photo   # or publisher
wget --mirror --page-requisites --convert-links --adjust-extension \
     --no-parent --directory-prefix="sources/$app" \
     "https://affinity.help/${app}2/en-US.lproj/index.html"
wget --mirror --no-parent --directory-prefix="sources/$app-shared" \
     "https://affinity.help/${app}2/shared/"
```

Keep the raw mirror under `sources/<app>/` — it is shipped as
`affinity-<app>-2-source-html.zip` and lets the conversion be redone later.
Put any bulk image-download scratch in `sources/<app>/Missing images/`
(git-ignored).

## 2. Convert pages to Markdown

One Markdown file per help page, mirroring the original chapter structure:

```
manuals/<app>/
├── index.md                       curated TOC (see below)
├── content/NN-chapter/NN-page.md  pandoc -f html -t gfm, one per page
└── assets/
    ├── images/    per-page screenshots from the export
    └── shared/    the shared/ image pool
```

Rules that keep every downstream format working:

- **Links between pages:** relative Markdown, e.g. `[Personas](03-personas.md)`
  or `../04-artboards/01-about-artboards.md`.
- **Images:** relative Markdown, e.g. `![](../../assets/shared/foo.png)`.
- **First line of every page:** a single `# Page Title` H1.
- Filenames: `NN-kebab-case.md`; chapter dirs: `NN-kebab-case/`. The `NN-`
  prefixes set the reading order.

## 3. Write `index.md`

A nested bullet list, chapters in `**bold**`, pages as links — same as
`manuals/designer/index.md`:

```markdown
- **Introduction**
  - [Affinity Photo](content/01-introduction/01-affinity-photo.md)
  - [Personas](content/01-introduction/02-personas.md)
- **Get started**
  - [Create new documents](content/02-get-started/01-create-new-documents.md)
```

`scripts/gen_summary.py <app>` converts this to `SUMMARY.md` for mdBook and
provides the page order for the EPUB/PDF.

## 4. Check and build

```sh
python3 scripts/gen_summary.py <app>
scripts/build.sh <app>          # needs mdbook, pandoc, xelatex or weasyprint, zip
```

Fix any `warning: ... points at missing file` from `gen_summary.py`, and confirm
images resolve (a quick link-checker like the one used for Designer helps).

## 5. Ship it

Commit `manuals/<app>/` and `sources/<app>/`, push to `main` (the Pages site
rebuilds), then tag a release (`git tag vX.Y.Z && git push --tags`) to publish
the new EPUB/PDF/zips.
