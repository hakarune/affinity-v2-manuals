#!/usr/bin/env python3
"""Produce an Obsidian-vault copy of a manual.

Takes manuals/<app>/ (the canonical Markdown, with relative links) and writes a
vault to <outdir>/ where:

  * internal  [text](rel/path.md)  links become  [[content/full/path|text]]
    wikilinks (resolved relative to each file, expressed vault-root-relative);
  * image links are left as-is (Obsidian renders standard Markdown images);
  * the vault config from config/obsidian/.obsidian/ is copied in;
  * SUMMARY.md is dropped (mdBook-only artefact).

Usage:
    scripts/make_obsidian.py <app> <outdir>
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# [text](target.md)  or  [text](target.md#anchor)   -- not preceded by '!'
LINK = re.compile(r"(?<!\!)\[([^\]]+)\]\((?!https?://)([^)]+?\.md)(#[^)]*)?\)")


def to_wikilinks(text: str, md_file: Path, vault_root: Path) -> str:
    def repl(m: re.Match) -> str:
        label, href, anchor = m.group(1), m.group(2), m.group(3) or ""
        target = (md_file.parent / href).resolve()
        try:
            rel = target.relative_to(vault_root.resolve()).with_suffix("")
        except ValueError:
            return m.group(0)  # points outside the vault; leave untouched
        link = rel.as_posix() + anchor
        return f"[[{link}|{label}]]"

    return LINK.sub(repl, text)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    app, outdir = argv[0], Path(argv[1])
    src = ROOT / "manuals" / app
    if not src.is_dir():
        print(f"no manuals/{app}/", file=sys.stderr)
        return 1

    if outdir.exists():
        shutil.rmtree(outdir)
    shutil.copytree(src, outdir)

    summary = outdir / "SUMMARY.md"
    if summary.exists():
        summary.unlink()

    obsidian_cfg = ROOT / "config" / "obsidian" / ".obsidian"
    if obsidian_cfg.is_dir():
        shutil.copytree(obsidian_cfg, outdir / ".obsidian", dirs_exist_ok=True)

    converted = 0
    for md in outdir.rglob("*.md"):
        original = md.read_text(encoding="utf-8")
        new = to_wikilinks(original, md, outdir)
        if new != original:
            md.write_text(new, encoding="utf-8")
            converted += 1
    print(f"{app}: vault at {outdir} ({converted} files rewritten to wikilinks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
