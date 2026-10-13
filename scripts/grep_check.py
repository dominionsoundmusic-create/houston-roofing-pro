#!/usr/bin/env python3
"""CLAUDE.md final grep (Houston Expert Roofers): banned strings in the built site's visible text, titles, meta and alt text.

Usage: python3 scripts/grep_check.py [--dist dist]. Exit code 1 on any hit.
"""
import argparse
import html
import re
import sys
from pathlib import Path

# The final grep list from CLAUDE.md ("Before you finish"), plus a few close variants.
PATS = ["—", "–", "we repair", "we replace", "we inspect", "our roofers", "our crew", "our team", "licensed and insured",
        "free estimate", "free inspection", "same-day", "same day", "guarantee", "GAF certified", "GAF-certified",
        "Houston Roofing Pro", "Dallas", "Fort Worth", "Austin", "(903)", "(214)", "(469)"]
# The Duplantis credit uses the one allowed dash; it is drawn by CSS (::before), so it never appears in the HTML text.


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(Path(__file__).resolve().parent.parent / "dist"))
    dist = Path(ap.parse_args().dist)
    total = 0
    for p in PATS:
        files = []
        for f in sorted(dist.rglob("*.html")):
            raw = f.read_text()
            vis = re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", raw)
            vis = re.sub(r"(?s)<!--.*?-->", " ", vis)
            vis = html.unescape(re.sub(r"<[^>]+>", " ", vis)) + " " + " ".join(re.findall(r'(?:content|alt|title)="([^"]*)"', raw))
            pat = re.escape(p.lower())
            if p[0].isalnum():
                pat = r"(?<![a-z])" + pat
            if p[-1].isalnum():
                pat += r"(?![a-z])"
            if re.search(pat, vis.lower()):
                files.append("/" + f.relative_to(dist).as_posix())
        total += len(files)
        print(f"{p!r}: {len(files)} hits {files[:5]}")
    print(f"\n{total} hits in total")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
