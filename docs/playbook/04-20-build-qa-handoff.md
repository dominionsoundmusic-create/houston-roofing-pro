# Prompts 4 to 20: build, QA and handoff (Oct 13 2026)

## Prompts 4 to 6: configuration, brand, navigation
- Business data lives once in src/data/site.json (name, d/b/a, origin, phone, hours, disclosure, quote bar,
  footer, GA4 ID, form names, social slots, nav, services, guides, 28 areas). build.py derives the phone's
  display and tel forms; check.py fails if the number is typed into a page.
- Brand tokens in src/static/css/site.css: navy #1a1a2e, gold #c9a84c (navy text on gold), red #c1121f for
  the header Call button only, white sections, self-hosted Inter woff2. Logo and favicons unchanged.
- Header: logo, Services / Service Areas / Guides menus from site.json, How It Works, About, FAQ, Contact,
  EN/ES toggle, red tap-to-call. Footer: disclosure, phone, services, guides, company links, all 28 towns,
  copyright and the followed Dominion Web Design Pro credit. Old-site leftovers: none (grep check).

## Prompts 7 to 13: pages
58 pages: 13 core and utility pages (home, services, service areas, how it works, about, FAQ, contact,
contact thanks, storm claim checklist, checklist thanks, privacy, terms, 404), 12 service pages, 5 guides,
28 town pages. Route list with target keywords: SERVICES.md. Each page has its own H1, title, description,
3 to 6 FAQs (visible and FAQPage JSON-LD), a hero, at least two in-body images, the referral disclosure and
a sources list (except legal pages). Service pages were written one at a time (Prompt 9) and town pages one
at a time (Prompt 11) by writer agents following docs/WRITING-GUIDE.md, each researched for its own keyword
or town.

## Prompt 14: reviews, social, profiles
None exist (INTAKE.md). Social icon slots stay hidden until URLs are added to site.json. No review widget,
no ratings, no badges.

## Prompt 15: media
12 existing photos used first (roof-01 to roof-06, hero and card). 139 planned photos (44 heroes 1920x1080,
95 in-body 1200x800) are listed with Artistly prompts in docs/image-list.md, heroes first; until each file is
saved in src/static/images/, the build serves a navy block of the same name and size. Every photo gets WebP
copies at 480/800/1200/1600/1920 with srcset; heroes are eager with fetchpriority high and a preload;
in-body images are lazy with width and height.

## Prompt 16: SEO
Route-by-route table: docs/playbook/16-seo-routes.md (titles 64 characters or fewer, descriptions 145 to 169,
one H1, canonical on https://houstonexpertroofers.com for every indexable page, noindex on the 404 and both
thanks pages). JSON-LD: Organization, WebSite (home), WebPage/ContactPage/AboutPage, BreadcrumbList,
Service, Article (guides), FAQPage. Sitemap 55 URLs; robots.txt points to it.

## Prompt 17: remnant and placeholder sweep
grep_check.py and check.py: no old brand name, no other Dominion phone numbers, no other metros, no
placeholder text, no empty hrefs, no duplicate IDs, no duplicate metadata, no broken internal links or
images. Intentional placeholders: the 139 planned photos (navy blocks) only.

## Prompts 18 and 19: responsive, accessibility, functional QA
responsive_check.js: 238 page loads, 0 problems (see docs/qa.md). Keyboard: skip link, focusable menus and
submenus (Escape closes), visible focus outline, FAQ accordions are native details/summary, reduced-motion
respected. Forms render in the static HTML with labels; submissions were not sent (production forms are not
to be submitted). Not verifiable here: Netlify form delivery, Google Translate on the live domain, the
phone routing.

## Prompt 20: final readiness
| Item | Status |
|---|---|
| Build, rules, grep, old URLs, keywords, duplication, browser | Passed (docs/qa.md) |
| Independent fact-check | Run on all 58 pages (docs/fact-check.md) |
| Forms | Present with exact names and fields; delivery not verified until live |
| Photos | 139 planned photos still to generate (navy placeholders meanwhile) |
| Launch blockers | None in the code. Going live is Maurice's decision: merge `build` into `main` |

Readiness: ready for Maurice's review on the `build` branch. Not deployed, not merged.
