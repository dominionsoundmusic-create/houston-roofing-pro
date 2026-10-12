#!/usr/bin/env python3
"""Old-URL check for houstonexpertroofers.com.

Every URL the live site has today must still return a page or a 301 to the closest new page. This
script lists every old URL (the CLAUDE.md list, every page file in docs/old-site/, the old PDF, and
every rule source in the old _redirects), then proves each one either is served from dist/ or is
caught by a rule in dist/_redirects whose target is served from dist/. Redirect chains are followed
(at most 3 hops) and reported. It also checks that every page in src/data/site.json is built.

Netlify serves an existing file before it applies a non-forced rule, so a URL that resolves in dist/
is reported as 200 even if a wildcard rule would also match it.

Usage: python3 scripts/check_old_urls.py [--dist dist] [--report docs/qa-urls.md]
Exit code 1 if any old URL neither resolves nor redirects.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CLAUDE_LIST = """/ /about/ /contact/ /contact/thanks/ /faq/ /services/ /free-roof-inspection/
/hail-claim-checklist/ /hail-claim-checklist/thanks/ /hail-damage-roof-insurance.html
/hail-damage-roof-repair/ /roof-flashing-repair.html /roof-leak-repair/ /roof-repair-emergency.html
/roof-repair/ /roof-replacement-cost.html /roof-replacement/ /storm-damage-roof-repair/ /wind-damage-roof.html
/privacy-policy.html /terms.html /baytown-roofing/ /conroe-roofer/ /friendswood-roofing/ /humble-roofing/
/league-city-roofing-company/ /pasadena-roofing-contractors/ /roofing-companies-cypress-tx/
/roofing-companies-katy-tx/ /roofing-companies-richmond-tx/ /roofing-companies-spring-tx/
/roofing-companies-sugar-land-tx/ /roofing-companies-the-woodlands-tx/ /roofing-company-missouri-city/
/roofing-company-tomball-tx/ /roofing-kingwood-tx/ /roofing-pearland-tx/
/files/houston-hail-storm-claim-checklist.pdf""".split()


def served(url, dist):
    """True if Netlify would serve a file for this URL path from dist/."""
    url = url.split("#")[0].split("?")[0]
    p = dist / url.lstrip("/")
    if url.endswith("/"):
        return (p / "index.html").exists()
    if p.is_file():
        return True
    # Netlify pretty URLs: /page serves page.html, and /dir serves dir/index.html
    return (dist / (url.lstrip("/") + ".html")).exists() or (p / "index.html").exists()


def load_rules(path):
    rules = []
    for line in path.read_text().splitlines():
        parts = line.split()
        if not parts or parts[0].startswith("#"):
            continue
        rules.append((parts[0], parts[1], parts[2] if len(parts) > 2 else "301"))
    return rules


def match(rule_src, url):
    if rule_src.endswith("/*"):
        base = rule_src[:-1]  # "/x/" ; Netlify's splat also matches the bare "/x/" and "/x"
        return url.startswith(base) or url == base.rstrip("/")
    return url == rule_src or url.rstrip("/") == rule_src.rstrip("/")


def resolve(url, dist, rules, hops=0):
    """Return (status_text, ok)."""
    if served(url, dist):
        return ("200", True)
    if hops >= 3:
        return ("too many redirect hops", False)
    for src, dst, code in rules:
        if match(src, url):
            if served(dst, dist):
                return (f"{code} -> {dst}", True)
            nxt, ok = resolve(dst, dist, rules, hops + 1)
            return (f"{code} -> {dst} ({nxt})", ok)
    return ("NOT FOUND", False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    dist = Path(args.dist)
    rules = load_rules(dist / "_redirects")
    old = set(CLAUDE_LIST)
    old_root = ROOT / "docs" / "old-site"
    for f in old_root.rglob("*.html"):
        rel = f.relative_to(old_root).as_posix()
        old.add("/" if rel == "index.html" else "/" + rel[:-len("index.html")] if rel.endswith("/index.html") else "/" + rel)
    old_rule_srcs = [src for src, dst, code in load_rules(old_root / "_redirects")]
    for src in old_rule_srcs:
        old.add(src.replace("*", "some-old-page"))
    # .html files were also reachable without the extension on Netlify (pretty URLs), and folder pages
    # were linked as /x/index.html in the old canonicals
    extra = set()
    for u in old:
        if u.endswith(".html") and "/" not in u[1:]:
            extra.add(u[:-5])
        if u.endswith("/") and u != "/":
            extra.add(u + "index.html")
    old |= extra
    rows, bad = [], 0
    for u in sorted(old):
        status, ok = resolve(u, dist, rules)
        bad += not ok
        rows.append((u, status if ok else "PROBLEM: " + status))
    # every old _redirects rule must still be present (CLAUDE.md: keep them)
    new_srcs = {src for src, dst, code in rules}
    for src in old_rule_srcs:
        if src not in new_srcs:
            bad += 1
            rows.append((src, "PROBLEM: old _redirects rule missing from the new _redirects"))
    # every planned page is built
    site = json.loads((ROOT / "src" / "data" / "site.json").read_text())
    for key in ("services", "guides", "areas"):
        for i in site[key]:
            if not served(i["url"], dist):
                bad += 1
                rows.append((i["url"], "PROBLEM: planned page not built"))
    for u, r in rows:
        print(f"{r:60s} {u}")
    print(f"\n{len(rows)} old URLs and rules checked, {bad} problems")
    if args.report:
        Path(args.report).write_text("\n".join(["| Old URL | Result on the new build |", "|---|---|"] +
                                               [f"| {u} | {r} |" for u, r in rows]) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
