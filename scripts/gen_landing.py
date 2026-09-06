#!/usr/bin/env python3
"""Write a small landing page linking to each built manual site.

Usage:
    scripts/gen_landing.py <outdir> <app> [<app> ...]

Creates <outdir>/index.html with one card per app, each linking to ./<app>/.
"""
from __future__ import annotations

import html
import sys
from pathlib import Path

TITLES = {
    "photo": "Affinity Photo 2",
    "designer": "Affinity Designer 2",
    "publisher": "Affinity Publisher 2",
}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Affinity V2 Manuals - Community Archive</title>
<style>
  :root {{
    --bg: #faf9f7; --fg: #1b1b1b; --muted: #666;
    --card: #ffffff; --border: #e2ddd5; --accent: #a3320b;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #1a1a1a; --fg: #e8e6e3; --muted: #9a948c;
      --card: #242424; --border: #383838; --accent: #ff7043;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--fg);
    font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    display: flex; flex-direction: column; align-items: center;
    padding: 4rem 1.5rem;
  }}
  main {{ width: 100%; max-width: 640px; }}
  h1 {{ font-size: 1.6rem; margin: 0 0 .4rem; }}
  p.lead {{ color: var(--muted); margin: 0 0 2.5rem; }}
  a.card {{
    display: block; text-decoration: none; color: inherit;
    background: var(--card); border: 1px solid var(--border); border-radius: 12px;
    padding: 1.1rem 1.3rem; margin-bottom: 1rem; transition: border-color .15s, transform .15s;
  }}
  a.card:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  a.card .name {{ font-weight: 600; font-size: 1.1rem; }}
  a.card .go {{ color: var(--accent); }}
  footer {{ margin-top: 2.5rem; color: var(--muted); font-size: .85rem; }}
  footer a {{ color: inherit; }}
</style>
</head>
<body>
<main>
  <h1>Affinity V2 Manuals</h1>
  <p class="lead">Offline archive of the Affinity Photo, Designer, and Publisher
  version&nbsp;2 help documentation. Content &copy; Serif (Europe)&nbsp;Ltd.</p>
{cards}
  <footer>
    <a href="https://github.com/{repo}">Source &amp; downloadable EPUB / PDF / Markdown / Obsidian builds on GitHub</a>
  </footer>
</main>
</body>
</html>
"""

CARD = '  <a class="card" href="./{app}/"><span class="name">{title}</span> &nbsp;<span class="go">Read &rarr;</span></a>'


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    outdir = Path(argv[0])
    apps = argv[1:]
    repo = "USER/affinity-v2-manuals"
    env_repo = __import__("os").environ.get("GITHUB_REPOSITORY")
    if env_repo:
        repo = env_repo
    cards = "\n".join(
        CARD.format(app=html.escape(a), title=html.escape(TITLES.get(a, a.title())))
        for a in apps
    )
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "index.html").write_text(
        PAGE.format(cards=cards, repo=html.escape(repo)), encoding="utf-8"
    )
    print(f"wrote {outdir/'index.html'} ({len(apps)} manual(s): {', '.join(apps)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
