# QA record (Oct 13 2026, final run on the `build` branch)

All commands run from the repo root against the production build in dist/ (`.imgcache/` cleared first).

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 58 pages built; 139 planned photos listed in docs/image-list.md (44 heroes, 95 in-body), each served as a navy brand-color block under its final file name until generated, never a broken image |
| Rules and SEO | `python3 scripts/check.py` | 58 pages checked, **0 errors, 0 warnings**. Covers banned phrases and INTAKE.md words to avoid, contractor voice, dashes, places outside greater Houston, DIY roof wording, the two Netlify forms (exact names, actions, fields and select options; no other form anywhere), eyebrow labels, the exact quote bar, footer copyright and credit, referral disclosure, handwritten marker in the first 4KB, one H1, unique titles and descriptions, canonical, OG tags, one valid JSON-LD block, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus 2 in-body images with lazy loading, alt/width/height, internal links, sitemap, _redirects targets, and no phone number typed into any page source |
| CLAUDE.md grep | `python3 scripts/grep_check.py` | **0 hits** for em/en dashes, "we repair", "we replace", "we inspect", "our roofers", "our crew", "our team", "licensed and insured", "free estimate", "free inspection", "same-day", "same day", "guarantee", "GAF certified", "Houston Roofing Pro", "Dallas", "Fort Worth", "Austin", "(903)", "(214)", "(469)" in visible text, titles, meta and alt text. (The Duplantis credit dash is drawn by CSS, the one allowed dash.) |
| Old URLs | `python3 scripts/check_old_urls.py --report docs/qa-urls.md` | **102 old URLs and rules checked, 0 problems**: every CLAUDE.md URL, every old page file (and its /index.html and extensionless forms), the old PDF, and every old _redirects rule resolves to a page (200) or a 301 to a built page; every old rule is still present |
| Keywords | `python3 scripts/keyword_plan.py` | 937 rows; 431 with 10+ searches: 245 assigned to a page, 186 deliberately unused with a reason, **0 unclassified** |
| Duplication | `python3 scripts/similarity.py --other ../water-damage-pro-houston/dist --other ../dominionsoundmusic-create/houston-powerwashing-pro/dist` | Town pairs max **2.9%**, service pairs max **2.3%**, guide pairs max **1.1%** (limit 15%). **0 pages** share an 8-word run with either sister site (max Jaccard 1.1% and 2.2%, legal pages). Full table: docs/qa-similarity.md |
| Browser | `node scripts/responsive_check.js` (dist served locally, Chromium) | **238 page loads, 0 problems**: every page at 1440, 1024, 768 and 390 px plus samples at 1920 and 2560 (no horizontal overflow, no script errors, no failed same-origin requests, hero edge to edge, hero at most 700px tall with the call button above the fold, headline on the left rail). Third-party requests (Google Analytics, Translate) are blocked in this sandbox and excluded |
| Visual review | screenshots of / and /roofing-companies-katy-tx/ at 1440, 1920, 2560, scrolled to load every image | Navy header with red call button and EN/ES toggle; hero content on the left rail at every width; white sections with one navy and one gold band (gold always with navy text); FAQ band gold, call band navy; short card rows centered (5 guides = 3 + 2 centered); no white on white; planned photos show as navy blocks with a gold roofline |
| Forms | built HTML | `houston-roofing-contact` on /contact/ (name, phone, city, need, message, bot-field honeypot, action /contact/thanks/) and `houston-hail-checklist` on /hail-claim-checklist/ (name, email, zip, phone, action /hail-claim-checklist/thanks/, which links /files/houston-hail-storm-claim-checklist.pdf). Both thanks pages are noindex and left out of the sitemap |
| Sitemap and robots | dist/sitemap.xml, dist/robots.txt | 55 URLs (58 pages minus the 404 and two noindex thanks pages); robots allows all and points to the sitemap |
| Analytics | built HTML | GA4 G-KBRNTW0VQP with the `phone_call_click` event on every page |
| Fact-check | 10 independent sub-agents | 374 claims confirmed, 70 corrected, 42 softened, 19 removed, 17 sourced facts added (docs/fact-check.md) |

Not verified here (needs the live site): Netlify's form registration and submissions, the 404 status and
redirect behavior in production, the Google Translate ES toggle on the real domain, and the phone line's
routing.

## Duplication (Jaccard on 5-word shingles, page copy and FAQ answers; shared template parts excluded)

| Group | Pairs | Max | Mean | Min |
|---|---:|---:|---:|---:|
| area (towns) | 378 | 2.9% | 0.8% | 0.1% |
| guide | 10 | 1.1% | 0.5% | 0.2% |
| legal | 1 | 0.9% | 0.9% | 0.9% |
| mixed | 1020 | 2.9% | 0.3% | 0.0% |
| page | 10 | 1.1% | 0.2% | 0.0% |
| service | 66 | 2.3% | 0.6% | 0.1% |

Top pairs: /roof-repair/ vs /roofing-deer-park-tx/ 2.9%; /roofing-channelview-tx/ vs /roofing-deer-park-tx/
2.9%; /roofing-company-missouri-city/ vs /roofing-pearland-tx/ 2.6%; /roofing-seabrook-tx/ vs
/roofing-webster-tx/ 2.5%; /conroe-roofer/ vs /roofing-magnolia-tx/ 2.5%. Full list: docs/qa-similarity.md.
