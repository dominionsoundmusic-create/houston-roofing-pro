# Fact-check brief (Houston Expert Roofers, Oct 13 2026)

You are an independent fact-checker. You did NOT write the pages you check. Your job: find every
non-obvious factual claim on your assigned pages, verify it, and correct, soften or remove it in place.

Read first: CLAUDE.md (hard rules), INTAKE.md (the business facts), docs/WRITING-GUIDE.md (banned phrases,
safety rules), docs/research/followups.md (claims already flagged), and the writer's research notes in
docs/research/ for your pages (they list sources and what was left out).

## What counts as a claim
Laws and their section numbers, TDI/TWIA rules and form numbers, permit rules, fees, office names, phone
numbers and addresses, licensing and registration rules, insurance mechanics, dates, storm facts (dates,
wind speeds, ratings, outage counts, rainfall), statistics, prices and cost ranges, product standards
(UL 2218, code sections), lifespans, neighborhood names and which town or county they are in, utility
service areas, populations, history. Also check every source URL label matches what the source is.

## How to verify
- WebSearch works; WebFetch and curl cannot reach outside sites here. Verify against search results,
  preferably restricted to the official domain (allowed_domains). Respect your search budget exactly;
  the cap is shared by every agent in this turn.
- A claim is CONFIRMED only if a search result from a credible source supports it. Otherwise CORRECT it
  (when the right fact is found), SOFTEN it (when only part is supported, e.g. drop a precise number) or
  REMOVE it. Never add a new unsourced fact. If you add a source, add it to the page's sources list.
- Keep within the rules: no em or en dashes, no banned phrases, no DIY roof work, never imply the line
  does roofing work, never name a roofing company, only greater-Houston places.
- Keep the page's meaning, structure and FAQs (3 to 6). Do not edit shared files (site.json, macros,
  templates, scripts); report needed shared changes instead.

## After editing
`python3 build.py --out /tmp/hxr-<your-name>`; `python3 scripts/check.py --dist /tmp/hxr-<your-name>`
(0 errors); `python3 scripts/similarity.py --dist /tmp/hxr-<your-name> --other /home/user/water-damage-pro-houston/dist --other /home/user/dominionsoundmusic-create/houston-powerwashing-pro/dist`
(no FAIL lines); `python3 scripts/grep_check.py --dist /tmp/hxr-<your-name>` (0 hits). Do not commit.

## Log
Write docs/fact-check/<your-name>.md: a table per page with | Claim | Verdict (confirmed / corrected /
softened / removed / kept without a search) | Source or reason |, then totals per verdict. Be honest:
mark anything you did not search as "kept without a search" with a reason (for example, a general
statement that needs no source).
