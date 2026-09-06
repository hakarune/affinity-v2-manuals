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
    inputs=()
    for rel in "${ORDER[@]}"; do
      [ -f "$man/$rel" ] && inputs+=("$man/$rel")
    done
    common=(
      --file-scope
      --metadata-file="config/pandoc/$app.yaml"
      --resource-path="$man"
      --toc --toc-depth=2
    )

    echo ">> epub"
    pandoc "${common[@]}" --css config/pandoc/epub.css \
      "${inputs[@]}" -o "$DIST/affinity-$app-2-manual.epub"

    echo ">> single-file html"
    pandoc "${common[@]}" --standalone --embed-resources --number-sections \
      "${inputs[@]}" -o "$DIST/affinity-$app-2-manual.html"

    if [ -n "$PDF_ENGINE" ]; then
      echo ">> pdf ($PDF_ENGINE)"
      pandoc "${common[@]}" --pdf-engine="$PDF_ENGINE" \
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
