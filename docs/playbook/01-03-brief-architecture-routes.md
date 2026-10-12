# Prompts 1 to 3: fact brief, architecture, baseline and route plan (Oct 12 2026)

PLAYBOOK.md was written for GoHighLevel AI Studio (TanStack Start SSR). This site is a static Jinja build
on Netlify, which already meets the playbook's SSR goal: every title, description, canonical, Open Graph
tag, JSON-LD block, H1, body copy and form is in the HTML file Netlify serves, with no client rendering.

## Prompt 1: client fact brief (from INTAKE.md)

| Item | Value | Status |
|---|---|---|
| Official name | Houston Expert Roofers, a d/b/a of Dominion Digital Group | Confirmed |
| What it is | A free phone line and website, not a roofing contractor. Automated assistant answers, transfers the caller to an independent, locally owned roofing company, or passes name, number, city, need and urgency for a call back | Confirmed |
| Category | Roofing referral line for greater Houston | Confirmed |
| Services | From the keyword data: repair, replacement, leak repair, storm, hail, inspection, emergency and tarping, commercial, flat roof, metal, wind, flashing | Confirmed (CLAUDE.md rules) |
| Not offered | Gutters alone, solar, siding, remodeling, insurance advice, public adjusting, claim handling | Confirmed |
| Area | Houston and suburbs in Harris, Fort Bend, Montgomery, Brazoria, Galveston and Chambers counties | Confirmed |
| Address | Do not display | Confirmed (omitted) |
| Phone | (832) 662-4107, tel:+18326624107, shared line, set once in src/data/site.json | Confirmed |
| Email | Unknown, not displayed | Missing, deferrable |
| Hours | Line answered 24/7 by an automated assistant | Confirmed |
| Year, owner, team, licenses, reviews, guarantees | None; do not display | Confirmed (omitted) |
| CTAs | Call the number (header and hero of every page); secondary: how the line works or a page anchor | Confirmed |
| Forms | houston-roofing-contact on /contact/, houston-hail-checklist on /hail-claim-checklist/ | Confirmed |
| Brand | Logo images/logo.svg, favicons, navy #1a1a2e, gold #c9a84c, red #c1121f (Call Now only), white sections | Confirmed |
| Top bar | "John 3:16" left; quote and Jesse Duplantis credit exactly as INTAKE.md | Confirmed |
| Footer | © 2026 Dominion Digital Group. All rights reserved. Designed by Dominion Web Design Pro (followed link) | Confirmed |
| Language | EN / ES Google Translate toggle in the header | Confirmed |
| Analytics | GA4 G-KBRNTW0VQP with the phone_call_click event | Confirmed |
| Social, Google Business Profile | None yet; slots hidden | Missing, deferrable |
| Photos | 12 roof photos (roof-01 to roof-06, hero 1920x800 and card 1200x675); every other image is planned in docs/image-list.md | Confirmed; new images deferrable |
| Domain | https://houstonexpertroofers.com, live from `main` on Netlify | Confirmed |

Contradictions: none found. Launch blockers: none in the facts; Maurice must decide when to merge `build`
into `main`, and may want the planned photos generated first (they show as navy blocks until then).

## Prompt 2: architecture

- Build: `python3 build.py` (Python 3, Jinja2, PyYAML, Pillow) renders src/pages/*.html (YAML front
  matter + Jinja body) through src/templates/layouts/base.html into dist/, writes sitemap.xml and
  robots.txt, makes WebP sizes of every photo, serves navy placeholders for planned photos and writes
  docs/image-list.md.
- Data: src/data/site.json (business, phone, CTA, analytics, forms, nav, services, guides, areas).
- Shared components: partials (header, hero, faq, cta, footer, social icons) and macros.html.
- Structured data: one JSON-LD @graph per page (Organization, WebSite on the home page, WebPage or
  ContactPage/AboutPage, BreadcrumbList, Service, Article for guides, FAQPage).
- Hosting: netlify.toml `publish = "dist"`, no build command; dist/_redirects; dist/404.html.
- Checks: scripts/check.py, check_old_urls.py, similarity.py, grep_check.py, keyword_plan.py,
  responsive_check.js (Playwright + the preinstalled Chromium).

## Prompt 3: baseline and route matrix

Baseline: the old site was 37 hand-built HTML files with inline styles, a css/fullwidth.css override, and
no build step. They are in docs/old-site/ for reference. The route matrix (every page, URL, target keyword,
existing or new) is SERVICES.md; old URLs and their new status are checked by scripts/check_old_urls.py
(results in docs/qa.md). All routes are static. Navigation: Services, Service Areas and Guides menus from
site.json, plus How It Works, About, FAQ and Contact. Sitemap: every indexable page; the 404 and the two
thanks pages are noindex and left out.

Plan: Prompts 4 to 6 (site.json, brand tokens, header, footer, routes) in the copied build system;
Prompts 7, 8, 10, 12 and 13 core pages written by the coordinator; Prompt 9 (12 services) and Prompt 11
(28 towns) and the 5 guides written by separate writer agents, one page at a time, each researched on the
web; Prompts 14 to 20 run as scripted checks plus a browser pass and an independent fact-check by agents
that wrote none of the pages.
