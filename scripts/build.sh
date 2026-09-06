#!/usr/bin/env bash
# Build every distributable format for each manual under manuals/<app>/.
#
#   scripts/build.sh [app ...]      default: all apps that have an index.md
#
# Outputs (per app) into dist/:
#   affinity-<app>-2-manual-markdown.zip        canonical Markdown tree
#   affinity-<app>-2-manual-obsidian-vault.zip  same + .obsidian/ + wikilinks
#   affinity-<app>-2-manual-html.zip            self-contained mdBook site
#   affinity-<app>-2-manual.epub
#   affinity-<app>-2-manual.pdf                 (needs xelatex/weasyprint)
#   affinity-<app>-2-manual.html                single self-contained file
#   affinity-<app>-2-source-html.zip            raw mirrored HTML (if sources/<app>/)
#
# Also assembles .work/site/<app>/ + a landing page for GitHub Pages.
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
DIST="$ROOT/dist"
WORK="$ROOT/.work"
rm -rf "$WORK"
mkdir -p "$DIST" "$WORK"

REPO="${GITHUB_REPOSITORY:-USER/affinity-v2-manuals}"

have() { command -v "$1" >/dev/null 2>&1; }

PLACEHOLDER="$ROOT/config/pandoc/placeholder.png"

# Any image a manual references but doesn't ship (see MISSING_IMAGES.md) would
# make pandoc --embed-resources abort. Drop a placeholder in the staged copy so
# every format builds; the committed tree still shows the gap.
fill_missing_assets() {
  local dir="$1" tail
  grep -rhoE 'assets/(shared|images)/[^)"'"'"' ]+\.(png|jpe?g|gif|svg|webp|tiff?)' \
    "$dir" 2>/dev/null | sort -u | while IFS= read -r tail; do
    if [ ! -f "$dir/$tail" ]; then
      mkdir -p "$dir/$(dirname "$tail")"
      cp "$PLACEHOLDER" "$dir/$tail"
      echo "   placeholder: $tail"
    fi
  done
}

MDBOOK_OK=1; have mdbook || { MDBOOK_OK=0; echo "note: mdbook not found - skipping HTML site"; }
PANDOC_OK=1; have pandoc || { PANDOC_OK=0; echo "note: pandoc not found - skipping epub/pdf/single-html"; }
ZIP_OK=1;    have zip    || { ZIP_OK=0;    echo "note: zip not found - skipping all .zip artefacts"; }

PDF_ENGINE="${PDF_ENGINE:-}"
if [ -z "$PDF_ENGINE" ]; then
  if   have weasyprint; then PDF_ENGINE=weasyprint
  elif have xelatex;    then PDF_ENGINE=xelatex
  elif have pdflatex;   then PDF_ENGINE=pdflatex
  fi
fi

# Which apps?
if [ "$#" -gt 0 ]; then
  APPS=("$@")
else
  APPS=()
  for d in manuals/*/; do
    a=$(basename "$d")
    [ -f "manuals/$a/index.md" ] && APPS+=("$a")
  done
fi
[ "${#APPS[@]}" -gt 0 ] || { echo "no manuals with an index.md under manuals/"; exit 0; }

BUILT_SITES=()

for app in "${APPS[@]}"; do
  man="manuals/$app"
  [ -f "$man/index.md" ] || { echo ">> $app: no $man/index.md, skipping"; continue; }
  echo
  echo "=================  $app  ================="

  # --- table of contents ---------------------------------------------------
  python3 scripts/gen_summary.py "$app"
  mapfile -t ORDER < <(python3 scripts/gen_summary.py "$app" --list)

  # --- Markdown zip ------------------------------------------------------------
  if [ "$ZIP_OK" = 1 ]; then
    md_stage="$WORK/md/$app"
    mkdir -p "$md_stage"
    cp -r "$man/." "$md_stage/"
    rm -f "$md_stage/SUMMARY.md"          # mdBook-only artefact
    (cd "$WORK/md" && zip -qr "$DIST/affinity-$app-2-manual-markdown.zip" "$app")
    echo ">> markdown zip"
  fi

  # --- Obsidian vault zip ----------------------------------------------------
  if [ "$ZIP_OK" = 1 ]; then
    python3 scripts/make_obsidian.py "$app" "$WORK/obsidian/$app"
    (cd "$WORK/obsidian" && zip -qr "$DIST/affinity-$app-2-manual-obsidian-vault.zip" "$app")
    echo ">> obsidian vault zip"
  fi

  # --- mdBook HTML site ----------------------------------------------------
  if [ "$MDBOOK_OK" = 1 ]; then
    bk="$WORK/mdbook/$app"
    mkdir -p "$bk/src"
    cp -r "$man/." "$bk/src/"
    fill_missing_assets "$bk/src"
    title="Affinity ${app^} 2 Manual (Community Archive)"
    sed -e "s|@APP@|$app|g" -e "s|@TITLE@|$title|g" -e "s|@REPO@|$REPO|g" \
      config/mdbook/book.toml.tmpl > "$bk/book.toml"
    (cd "$bk" && mdbook build >/dev/null)
    if [ "$ZIP_OK" = 1 ]; then
      site_stage="$WORK/htmlzip/affinity-$app-2-manual-html"
      mkdir -p "$(dirname "$site_stage")"
      cp -r "$bk/book" "$site_stage"
      (cd "$(dirname "$site_stage")" && zip -qr "$DIST/affinity-$app-2-manual-html.zip" "$(basename "$site_stage")")
    fi
    mkdir -p "$WORK/site"
    cp -r "$bk/book" "$WORK/site/$app"
    BUILT_SITES+=("$app")
    echo ">> html site (mdbook)"
  fi

  # --- pandoc: epub / pdf / single-file html ------------------------------
  if [ "$PANDOC_OK" = 1 ] && [ "${#ORDER[@]}" -gt 0 ]; then
    # Stage a copy with every image path made absolute. pandoc --file-scope
    # resolves resources relative to the run directory, not each source file,
    # so the tree's relative `../../assets/...` links would otherwise miss.
    pd="$WORK/pandoc/$app"
    rm -rf "$pd"; mkdir -p "$pd"
    cp -r "$man/." "$pd/"
    rm -f "$pd/SUMMARY.md"
    fill_missing_assets "$pd"
    pd_abs=$(cd "$pd" && pwd)
    find "$pd" -name '*.md' -print0 \
      | xargs -0 sed -i -E "s#\]\((\.\./)+assets/#](${pd_abs}/assets/#g"

    inputs=()
    for rel in "${ORDER[@]}"; do
      [ -f "$pd/$rel" ] && inputs+=("$pd/$rel")
    done
    common=(
      --file-scope
      --metadata-file="config/pandoc/$app.yaml"
      --resource-path="$pd_abs"
      --toc --toc-depth=2
    )

    echo ">> epub"
    pandoc "${common[@]}" --css config/pandoc/epub.css \
      "${inputs[@]}" -o "$DIST/affinity-$app-2-manual.epub" \
      || echo "   epub FAILED (non-fatal)"

    echo ">> single-file html"
    pandoc "${common[@]}" --standalone --embed-resources --number-sections \
      "${inputs[@]}" -o "$DIST/affinity-$app-2-manual.html" \
      || echo "   single-file html FAILED (non-fatal)"

    if [ -n "$PDF_ENGINE" ]; then
      echo ">> pdf ($PDF_ENGINE)"
      pdf_opts=()
      if [ "$PDF_ENGINE" = xelatex ] || [ "$PDF_ENGINE" = lualatex ]; then
        # DejaVu covers the bullets / Greek / arrows Latin Modern lacks
        pdf_opts=(-V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono")
      fi
      pandoc "${common[@]}" --pdf-engine="$PDF_ENGINE" "${pdf_opts[@]}" \
        "${inputs[@]}" -o "$DIST/affinity-$app-2-manual.pdf" \
        || echo "   pdf FAILED (non-fatal) - check the $PDF_ENGINE toolchain"
    else
      echo ">> pdf skipped (no weasyprint / xelatex / pdflatex)"
    fi
  fi

  # --- raw source HTML zip ------------------------------------------------
  if [ "$ZIP_OK" = 1 ] && [ -d "sources/$app" ]; then
    (cd sources && zip -qr "$DIST/affinity-$app-2-source-html.zip" "$app" \
        -x "$app/Missing images/*" -x "$app/missing images/*")
    echo ">> source html zip"
  fi
done

# --- Pages landing page ---------------------------------------------------
if [ "${#BUILT_SITES[@]}" -gt 0 ]; then
  python3 scripts/gen_landing.py "$WORK/site" "${BUILT_SITES[@]}"
fi

echo
echo "Done."
echo "  release artefacts : $DIST"
echo "  pages site tree   : $WORK/site"
ls -la "$DIST" || true
