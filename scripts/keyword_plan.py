#!/usr/bin/env python3
"""Assign every keyword in keywords/Houston-Roofing-Keywords.xlsx (ALL tab, 937 rows) to a page as
its target or a supporting keyword, or to the deliberately-unused list with a one-line reason.
Writes docs/keyword-plan.md.

CLAUDE.md rule: every Houston-area keyword with a volume of 10 or more must be assigned or listed as
unused with a reason. Rows under 10 are classified by the same rules for reference ("below 10").
"Near me" rows carry national volume: they are supporting keywords only, never targets.

Usage: python3 scripts/keyword_plan.py   (exit code 1 if any row with volume 10+ is unclassified)
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/",
    "repair": "/roof-repair/", "replacement": "/roof-replacement/", "leak": "/roof-leak-repair/",
    "storm": "/storm-damage-roof-repair/", "hail": "/hail-damage-roof-repair/",
    "inspection": "/roof-inspection/", "emergency": "/roof-repair-emergency.html",
    "commercial": "/commercial-roofing/", "flat": "/flat-roof-repair/", "metal": "/metal-roofing/",
    "wind": "/wind-damage-roof.html", "flashing": "/roof-flashing-repair.html",
    "g-cost": "/roof-replacement-cost.html", "g-insurance": "/hail-damage-roof-insurance.html",
    "g-license": "/do-roofers-need-a-license-in-texas/", "g-lifespan": "/how-long-does-a-roof-last-in-houston/",
    "g-storm": "/what-to-do-after-roof-storm-damage/",
    # towns (existing URLs kept; new towns use /roofing-<town>-tx/)
    "town:katy": "/roofing-companies-katy-tx/", "town:sugar-land": "/roofing-companies-sugar-land-tx/",
    "town:cypress": "/roofing-companies-cypress-tx/", "town:the-woodlands": "/roofing-companies-the-woodlands-tx/",
    "town:spring": "/roofing-companies-spring-tx/", "town:pearland": "/roofing-pearland-tx/",
    "town:league-city": "/league-city-roofing-company/", "town:pasadena": "/pasadena-roofing-contractors/",
    "town:conroe": "/conroe-roofer/", "town:humble": "/humble-roofing/", "town:kingwood": "/roofing-kingwood-tx/",
    "town:tomball": "/roofing-company-tomball-tx/", "town:missouri-city": "/roofing-company-missouri-city/",
    "town:richmond": "/roofing-companies-richmond-tx/", "town:friendswood": "/friendswood-roofing/",
    "town:baytown": "/baytown-roofing/", "town:atascocita": "/roofing-atascocita-tx/",
    "town:galveston": "/roofing-galveston-tx/", "town:magnolia": "/roofing-magnolia-tx/",
    "town:rosenberg": "/roofing-rosenberg-tx/", "town:webster": "/roofing-webster-tx/",
    "town:alvin": "/roofing-alvin-tx/", "town:la-porte": "/roofing-la-porte-tx/",
    "town:seabrook": "/roofing-seabrook-tx/", "town:deer-park": "/roofing-deer-park-tx/",
    "town:stafford": "/roofing-stafford-tx/", "town:channelview": "/roofing-channelview-tx/",
    "town:texas-city": "/roofing-texas-city-tx/",
}

# One target keyword per page (exact row in the spreadsheet).
TARGETS = {
    "roofing houston": "home", "roofing services houston": "services", "roofing near houston": "areas",
    "roof repair in houston": "repair", "roof replacement in houston": "replacement",
    "roof leak repair houston tx": "leak", "storm damage roof repairs": "storm",
    "hail damage repair houston": "hail", "roof inspection houston": "inspection",
    "houston emergency roof repair": "emergency", "commercial roofing houston": "commercial",
    "flat roof repair companies": "flat", "metal roofing houston": "metal",
    "where does flashing go on a roof": "flashing",
    "roof replacement cost houston tx": "g-cost", "how much does insurance pay for roof replacement": "g-insurance",
    "do roofers need a license in texas": "g-license", "how long does a roof last in houston": "g-lifespan",
    "what is considered storm damage to roof": "g-storm",
    "katy tx roofing companies": "town:katy", "roofing company sugar land tx": "town:sugar-land",
    "roofing cypress tx": "town:cypress", "roofing company the woodlands tx": "town:the-woodlands",
    "roofing spring tx": "town:spring", "roofing pearland tx": "town:pearland",
    "league city roofing": "town:league-city", "pasadena roofing contractors": "town:pasadena",
    "roofing conroe tx": "town:conroe", "roofing humble tx": "town:humble", "roofing kingwood tx": "town:kingwood",
    "roofing company tomball tx": "town:tomball", "roofing companies missouri city tx": "town:missouri-city",
    "roofing richmond tx": "town:richmond", "roofing friendswood tx": "town:friendswood",
    "baytown roofing companies": "town:baytown", "atascocita roof repair": "town:atascocita",
    "roofing galveston tx": "town:galveston", "roofing magnolia tx": "town:magnolia",
    "roofing rosenberg tx": "town:rosenberg", "roofing webster tx": "town:webster",
    "roofing alvin tx": "town:alvin", "la porte roofing": "town:la-porte", "roofing seabrook tx": "town:seabrook",
    "roof repair deer park tx": "town:deer-park", "roofing stafford tx": "town:stafford",
    "roofing channelview tx": "town:channelview", "roofing texas city tx": "town:texas-city",
}
# The wind damage page has no row in the Oct 12 pull; it is kept because the URL is live and indexed.
NO_ROW_TARGETS = {"wind": "wind damage roof (no row in the Oct 12 2026 pull; live URL kept)"}

# Supporting keywords for 10+ rows (and a few useful sub-10 rows).
SUPPORT = {
    "home": ["roofing in houston", "houston roofing companies", "roofing in houston texas", "roofers in houston tx",
             "roofing company houston", "roofing company in houston tx", "roofing company in houston",
             "quality roofing houston", "roofing companies in houston area", "roofers near houston tx",
             "houston roofers near me", "roofing companies near houston tx", "roofing service in houston"],
    "services": ["roofing contractors houston", "roofing contractor houston", "roofing services houston tx",
                 "roofing services in houston", "roofing contractor in houston texas", "roof repair services houston",
                 "roofing repair houston", "roofing services in houston tx", "roof repair services houston texas"],
    "areas": ["roofing katy", "galveston county roofing", "roofing companies in texas"],
    "repair": ["roof repair houston", "roof repair in houston tx", "roofing repair in houston", "roofing repair houston tx",
               "houston roof repairs", "roof repair solutions houston", "tile roof repair houston", "roof repair description",
               "houston roof repair company", "roof repair companies in houston", "roof repair houston cost",
               "how often roof repair", "can roof leaks be repaired"],
    "replacement": ["roof replacement houston", "construction permits houston", "when is roofing season",
                    "do roofers work on weekends", "what time do roofers start work", "roofing shingles houston",
                    "roofing shingles houston texas", "city of houston roof replacement permit", "houston roofing permit",
                    "roof replacement in houston texas", "when to replace roof in texas"],
    "leak": ["roofing leak repair near me", "roof leak repair houston", "who fixes leaking roof", "roof leak houston",
             "who fixes roof leaks near me", "roof leaking houston", "houston roof leaking", "who repairs a leaking roof",
             "how much roof leak repair cost"],
    "storm": ["storm damage roof repair near me", "houston roof damage", "roof damage houston",
              "storm damage roof repair cost", "storm damage roof repair houston"],
    "hail": ["average hail damage repair cost", "how much hail damage to replace roof", "hail damage roof repair cost",
             "how long does hail damage repair take", "hail damage houston tx", "hail damage roof repair houston",
             "how serious is hail damage to a roof", "how much to repair hail damage on roof"],
    "inspection": ["roof inspection report example", "what do roof inspectors look for", "does a home inspector check the roof",
                   "what do home inspectors look for during an inspection", "how much does it cost to have a roof inspection",
                   "when to get a roof inspection", "how often roof inspection", "how often roof maintenance",
                   "roof inspectors in houston", "do home inspections check the roof"],
    "emergency": ["emergency roof repair near me", "emergency roof leak repair near me", "emergency roof repair houston",
                  "emergency roof repair cost", "is a leaking roof an emergency", "who to call for emergency roof leak",
                  "when is a roof leak an emergency"],
    "commercial": ["commercial roofing in houston", "commercial roofing companies in houston", "commercial roofing houston tx",
                   "commercial roofing companies houston tx", "commercial roof repair houston", "commercial roofing services houston tx",
                   "commercial roofing in houston texas", "commercial roofers in houston",
                   "how often should commercial roofs be inspected", "how often should a commercial roof be replaced"],
    "flat": ["flat roof repair near me", "how do you repair a flat roof", "flat roof repair houston",
             "flat roof repair companies near me", "when to replace a flat roof", "carlisle tpo roofing details",
             "why flat roofs leak", "how often to replace a flat roof", "houston flat roof"],
    "metal": ["metal roof examples", "metal roofing companies houston", "how much do metal roofing panels cost",
              "will insurance cover a metal roof", "are metal roofs hotter", "metal roofing conroe tx",
              "are metal roofs good in texas", "green metal roofing near me", "how often do metal roofs need maintenance"],
    "flashing": ["how much is flashing for roof"],
    "g-cost": ["how much does a roof replacement cost", "roof replacement cost houston", "houston roof replacement cost",
               "how much should a roof replacement cost", "average roof replacement cost houston",
               "how much is a roof replacement in texas", "how much does a roof replacement cost in texas",
               "average cost of a roof replacement in texas", "how much does a new roof cost in texas",
               "how much does a roof cost in texas", "why is replacing a roof so expensive",
               "how much does a complete roof replacement cost", "roofing quotes examples",
               "how much do roofers charge to replace plywood", "roofing companies in houston that finance",
               "cost of roof replacement houston per square foot", "how much does a roof replacement cost in houston"],
    "g-insurance": ["how does roof insurance claim work", "does insurance cover storm damage to roof",
                    "does home insurance cover storm damage to roof", "how much hail damage for insurance to replace roof",
                    "can i get my roof replaced for free", "roof insurance claim texas",
                    "how does a roof insurance claim work in texas", "how do i file a claim for roof damage"],
    "g-license": ["best roofing company houston tx", "best roof repair houston", "best roofing houston", "houston roofers reviews",
                  "which roofing company is the best", "can you negotiate with roofing contractors", "when to pay roofing contractor",
                  "can a general contractor replace a roof", "general contractor license houston", "how many roofing companies in texas",
                  "how many roofing companies are in texas", "best roofing contractors in houston"],
    "g-lifespan": ["how often replace roof texas", "how often are roofs replaced in texas", "how often to replace roof on a house"],
    "g-storm": ["how much hail damage to replace roof in texas"],
    "town:katy": ["katy roofing companies", "roofers in katy tx", "roofing katy tx", "katy roofing repair", "katy roof replacement",
                  "roofing in katy tx", "hail damage repair katy tx", "roof inspection katy tx", "roof leak repair katy tx",
                  "roofing company katy texas", "roofing contractor in katy tx", "emergency roof repair katy tx", "roof inspection katy"],
    "town:sugar-land": ["roofing sugar land tx", "sugar land roof", "sugar land roofers", "sugar land roof repair"],
    "town:cypress": ["roofing companies in cypress tx", "roofers cypress tx", "roofing company cypress", "roofing contractor cypress tx",
                     "cypress roofers", "roofing company cypress texas", "cypress tx roofing company"],
    "town:the-woodlands": ["roofing company the woodlands", "roofing the woodlands tx", "roof replacement the woodlands tx",
                           "roofers the woodlands tx", "roofing woodlands", "roofing the woodlands", "roof repair the woodlands tx",
                           "woodlands roofing", "woodlands roofing company"],
    "town:spring": ["roofing contractor spring tx", "roof repair spring tx", "roofers in spring tx"],
    "town:pearland": ["roofing company pearland tx", "pearland roofing company", "pearland roofing companies"],
    "town:league-city": ["roofing company league city tx", "league city roofers", "roofer league city tx", "roofing league city",
                         "roofing league city tx", "league city roof repair", "roofing companies in league city texas"],
    "town:pasadena": ["pasadena roofing companies", "roofing company pasadena tx", "roofing pasadena tx"],
    "town:conroe": ["roofing conroe texas", "conroe roofing companies", "roof repair conroe tx", "roofing companies conroe tx",
                    "roofers in conroe tx", "roofing in conroe tx", "roofing company conroe texas", "roofing contractors in conroe"],
    "town:humble": ["roofing companies humble tx", "roofing humble texas", "roofing humble", "roofers in humble tx",
                    "roofing companies humble texas", "humble tx roofer", "humble tx roofing"],
    "town:kingwood": ["roofing kingwood", "roofing companies kingwood tx", "kingwood roof", "roofing contractor kingwood tx"],
    "town:tomball": ["tomball roofing companies", "roofing tomball tx", "roofing contractor tomball tx"],
    "town:missouri-city": ["roofing missouri city tx", "roofing missouri city", "roof repair missouri city tx"],
    "town:richmond": [],
    "town:friendswood": ["friendswood roofing", "friendswood roofing companies", "friendswood roofers",
                         "roofing companies friendswood tx", "roofing companies in friendswood texas",
                         "roofing companies in friendswood tx", "roofers in friendswood texas"],
    "town:baytown": ["roofing baytown tx", "roofing baytown texas", "baytown roofers", "roofing companies in baytown texas"],
    "town:atascocita": ["roofing atascocita tx", "roofer atascocita tx", "atascocita roofing", "roofers atascocita"],
    "town:galveston": ["galveston roofing companies", "galveston county roofing", "roofing companies in galveston texas",
                       "roofers galveston texas", "roofing companies in galveston tx", "roofing companies galveston tx",
                       "emergency roof repairs galveston county", "galveston roof"],
    "town:magnolia": ["magnolia roofers", "roofing companies in magnolia tx"],
    "town:rosenberg": ["roofing companies in rosenberg tx", "roofing in rosenberg"],
    "town:webster": [],
    "town:alvin": ["roofing companies alvin tx", "roofing companies in alvin tx", "roofing alvin texas", "roofing companies alvin texas",
                   "alvin roofer", "alvin tx roofing", "roofing alvin", "metal roofing alvin tx"],
    "town:la-porte": ["roofing la porte tx", "roof repair la porte tx", "roofing companies in la porte tx"],
    "town:seabrook": ["roofing repair seabrook"],
    "town:deer-park": ["roofing deer park tx", "deer park roofing texas", "roofing companies deer park tx",
                       "roofing companies in deer park tx", "roofing companies in deer park texas"],
    "town:stafford": ["roofing stafford texas", "emergency roof repair stafford tx", "emergency roof repair in stafford tx"],
    "town:channelview": [],
    "town:texas-city": [],
}
# Ambiguous rows that we can still use because the seed tab is Texas and the row has no other state:
# "roofing seabrook" (Seabrook NH exists) and "roofing magnolia" are kept as supporting only.
SUPPORT["town:seabrook"].append("roofing seabrook")
SUPPORT["town:magnolia"].append("roofing magnolia")

KW_TO_PAGE = {}
for k, p in TARGETS.items():
    KW_TO_PAGE[k] = (p, "target")
for p, kws in SUPPORT.items():
    for k in kws:
        KW_TO_PAGE.setdefault(k, (p, "supporting"))

# Unused groups: (reason, regex). Order matters; first match wins.
U = [
    ("ambiguous place with no state: another state's town is far larger (Pasadena CA, Richmond VA); only Texas rows count",
     r"^(roofing pasadena|richmond roofing contractor)$"),
    ("names a specific roofing, supply or construction company (CLAUDE.md rule 3: never name a roofing company)",
     r"\b(telge|remedy|callen|colony|boral|rios|durdin|coastal roofing|holden|alliance roofing|ameristar|allegiance|domingo|"
     r"shamrock|anderson roofing|fitz roofing|palacios|mars roofing|luxe|discount roofing|dixie|fsr|chavez|morgan roofing|"
     r"spartan|perry brothers|braun|punum|hargrove|moss roofing|ruff roofing|ideal roofing|apollo|battalion|dlv|"
     r"priority roofing|empire roofing|chamberlin|kidd|activ|walton|mighty dog|amstill|competition roofing|diversified|"
     r"newhaus|ready roofing|martin family|quick roofing|united roofing|rise roofing|roofing 911|roof repair squad|"
     r"houston strong|houston northside|roofing contractors houston elite|prime texas metal|roofing supply inc|"
     r"houston roofing (?:and|&) (?:construction|gutters)|houston commercial roofing (?:and|&)|la porte roofing and remodeling|"
     r"bellaire roofing|red roof|performance roofing|abc roofing|now roofing|eldridge|beacon|compass|adams roofing|"
     r"royal roofing|deer roofing|brentwood|smart choice|partners commercial|eagle eye|jc roofing|integrity roofing|onit|jolly|"
     r"advanced roofing|mission roofing|modern day|premier choice|surface roofing|sentry|r&s|westlake|delta roofing|"
     r"houston construction pro|houston construction pueblo|construction ltd|asap roof|speedy roof|roof repair hub|why town|"
     r"wilson roofing|anchor roofing|bueno roofing|roof co ventures|simple growth|rescue roofing|matias|upstanding|kainos|ksm|kgm|"
     r"noble roofing|newfield|nonstop|nexgen|paramount|integris|cedar roofing|meis|monarch|associates roofing|universal roofing|"
     r"uptown roofing|waggoner|dynasty|houston roofing experts|bumble|brazos roofing|corey roofing|dr roofing|d7 roofing|davidson|"
     r"dalco|five star roofing|global roofing|roofing solutions group|graziano|heart roofing|houston roofing & improvements|"
     r"roofing linares|skyline|houston roofing llc|houston roofing solutions|houston roofing group|roofing depot|ramirez|"
     r"urena|aztec|edwards roofing|absi|tx roofing & services|houston roofing pro)\b"),
    ("a metro, state or country outside greater Houston (CLAUDE.md rule 4)",
     r"\b(kansas city|missouri\b(?! city)|virginia|stafford va|pasadena (?:ca|md)|webster (?:ny|ma)|seabrook nh|dallas|dfw|"
     r"austin|queens|uk\b|flower mound|weatherford|springtown|big spring|kerrville|florida|bellville|glasgow|leeds|strabane|"
     r"sion mills|calgary|hyde park|lone cypress)"),
    ("jobs, wages, careers or contractor-business questions (not a homeowner looking for roofing help)",
     r"\b(jobs?|salary|make a week|make in texas|make an hour|makes|internships?|apprenticeship|hiring|careers?|job description|"
     r"job fair|how to get commercial roofing leads|open a roofing company|roofing sales|go out of business|school|degree|"
     r"how many roofers|charge per hour|union|roofing business)\b"),
    ("roofing or building-material supply-store intent (the line sells no materials)",
     r"\b(supply|suppliers|materials|cut to size|panel suppliers|where to buy|tar for roof|plant)\b"),
    ("legal, financing or real-estate services outside the line (attorneys, loans, tax rates, home inspection pricing)",
     r"\b(attorney|lawyer|law\b|loans?|tax rate|property tax|home inspection in texas|mediators|stafford loan)\b"),
    ("general construction news, events, traffic or projects, not roofing help",
     r"\bconstruction\b|\bcontractor (?:association|convention|salary|school)\b|general contractor in houston|"
     r"commercial construction companies"),
    ("town trivia, weather, directions, safety or ZIP lookups with no roofing intent",
     r"\b(weather|directions|events|why is|is .* safe|good place to live|time\b|where is the woodlands|cities near|"
     r"77530|77015|77471|7744|zip|county is|chip and joanna|how large|happy hour|county fair|fence company|plumb|"
     r"channelview tx$|channelview companies|channelview tx website|channelview tx to|is channelview|fulshear (?:tx )?(?:plumber|address|359)|when galveston|"
     r"insurance companies in deer park)"),
    ("off-topic or meaningless fragment (no roofing-service intent)",
     r"^(roofing channel|with roofing|how roofing|how roofing works|roofing views|roof v channel|who's roofing|will roofers|the roofing channel|"
     r"w roofing consultants|best roofing c|which roofing|what is an emergency repair|emergency hot water repair near me|"
     r"rv roof repair houston|emergency roof and ceiling repair|roofing 77024|roofing 77346|houston roofing association|"
     r"how many roofing companies in the us|how much roofing company makes|how many roofing companies (?:are )?in houston.*|"
     r"how often (?:roofing|to check roof|to change roofing|are roofs repaired|are roof replaced|roofed)|when roofing.*|"
     r"roofing near.*|how much hail damage to replace roof car|deer park roofing (?:financing|sold|jobs|owner|phone number|bbb)|"
     r"friendswood roof collapses|metal roof houston reddit|.*reddit.*|.*reviews|.*photos|.*by owner|.*owner)$"),
    ("Fulshear: no roofing search volume in the data, so no town page (CLAUDE.md)", r"fulshear"),
]


def unused_reason(kw):
    for reason, pat in U:
        if re.search(pat, kw):
            return reason
    return None


def page_rule(kw):
    """Rule-based page for sub-10 rows that were not mapped explicitly."""
    towns = {"katy": "town:katy", "sugar land": "town:sugar-land", "cypress": "town:cypress", "woodlands": "town:the-woodlands",
             "spring": "town:spring", "pearland": "town:pearland", "league city": "town:league-city", "pasadena": "town:pasadena",
             "conroe": "town:conroe", "humble": "town:humble", "kingwood": "town:kingwood", "tomball": "town:tomball",
             "missouri city": "town:missouri-city", "richmond": "town:richmond", "friendswood": "town:friendswood",
             "baytown": "town:baytown", "atascocita": "town:atascocita", "galveston": "town:galveston", "magnolia": "town:magnolia",
             "rosenberg": "town:rosenberg", "webster": "town:webster", "alvin": "town:alvin", "la porte": "town:la-porte",
             "seabrook": "town:seabrook", "deer park": "town:deer-park", "stafford": "town:stafford",
             "channelview": "town:channelview", "texas city": "town:texas-city"}
    for t, p in towns.items():
        if t in kw:
            return p
    rules = [("flat roof", "flat"), ("metal roof", "metal"), ("commercial", "commercial"), ("hail", "hail"),
             ("emergency", "emergency"), ("inspect", "inspection"), ("leak", "leak"), ("storm", "storm"),
             ("insurance claim", "g-insurance"), ("claim", "g-insurance"), ("replacement cost", "g-cost"),
             ("cost", "g-cost"), ("how much", "g-cost"), ("how often", "g-lifespan"), ("replace", "replacement"),
             ("permit", "replacement"), ("repair", "repair"), ("roofing", "home"), ("roofer", "home")]
    for needle, p in rules:
        if needle in kw:
            return p
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Houston-Roofing-Keywords.xlsx", read_only=True)
    rows = list(wb["ALL"].iter_rows(values_only=True))[1:]
    by_page = defaultdict(list)
    unused = defaultdict(list)
    unclassified = []
    for seed, kw, typ, vol, sd, cpc, pd in rows:
        kw = str(kw).strip().lower()
        vol = vol or 0
        rec = (kw, typ, vol, sd)
        if kw in KW_TO_PAGE:
            p, role = KW_TO_PAGE[kw]
            by_page[p].append((role, rec))
            continue
        r = unused_reason(kw)
        if r:
            unused[r].append(rec)
            continue
        if vol < 10:
            p = page_rule(kw)
            if p:
                by_page[p].append(("below 10", rec))
            else:
                unused["below the 10-search threshold and no page fits"].append(rec)
            continue
        unclassified.append(rec)

    total10 = sum(1 for r in rows if (r[3] or 0) >= 10)
    assigned10 = sum(1 for p in by_page.values() for role, rec in p if rec[2] >= 10)
    unused10 = sum(1 for g in unused.values() for rec in g if rec[2] >= 10)
    out = [
        "# Keyword plan (houstonexpertroofers.com, Playbook 2.0, Oct 12 2026)",
        "",
        "Generated by `python3 scripts/keyword_plan.py` from keywords/Houston-Roofing-Keywords.xlsx (Ubersuggest,",
        "United States, pulled Oct 12 2026, ALL tab). Volume is monthly searches; SD is Ubersuggest SEO difficulty.",
        "",
        "Rules applied (CLAUDE.md): every keyword with a volume of 10 or more is a page's target, a supporting",
        "keyword, or listed below as deliberately unused with a reason. \"Near me\" rows are national volume and",
        "are only ever supporting keywords. Rows naming a roofing company, rows about other states or metros and",
        "off-topic rows are unused. Rows under 10 are classified by the same rules for reference.",
        "",
        f"Totals: {len(rows)} keywords. {total10} have a volume of 10 or more: {assigned10} assigned to a page,",
        f"{unused10} deliberately unused, {len(unclassified)} unclassified.",
        "",
        "## Town page decisions",
        "",
        "Maurice's rule: a greater-Houston town with 10 or more searches a month on a roofing term gets a page.",
        "Only Texas rows count and rows naming a roofing company do not count.",
        "",
        "- 28 towns qualify (listed under Pages below with their target keyword and volume).",
        "- **Bellaire: no page.** Its only row with 10+ searches is \"bellaire roofing\" (50), which is the name of",
        "  a Houston roofing company (Bellaire Roofing Company, Inc.), and \"roofing bellaire tx\" shows 0.",
        "- **Fulshear: no page.** \"roofing fulshear tx\" shows 0 and no other Fulshear row is about roofing.",
        "",
        "## Pages",
        "",
    ]
    for key, url in PAGES.items():
        items = by_page.get(key, [])
        tgt = [rec for role, rec in items if role == "target"]
        sup = sorted([rec for role, rec in items if role == "supporting"], key=lambda r: -r[2])
        low = sorted([rec for role, rec in items if role == "below 10"], key=lambda r: -r[2])
        out.append(f"### {url}")
        out.append("")
        if tgt:
            t = tgt[0]
            out.append(f"- Target: **{t[0]}** ({t[2]}/mo, SD {t[3]}, {t[1]})")
        elif key in NO_ROW_TARGETS:
            out.append(f"- Target: **{NO_ROW_TARGETS[key]}**")
        else:
            out.append("- Target: none in the data (support page)")
        if sup:
            out.append("- Supporting: " + "; ".join(f"{r[0]} ({r[2]}{', Q' if r[1] == 'Question' else ''}"
                                                       f"{', national near-me' if 'near me' in r[0] else ''})" for r in sup))
        if low:
            out.append("- Under 10 (reference): " + "; ".join(f"{r[0]} ({r[2]})" for r in low))
        out.append("")
    out += ["## Deliberately unused", ""]
    for reason, recs in sorted(unused.items(), key=lambda kv: -sum(r[2] for r in kv[1])):
        recs.sort(key=lambda r: -r[2])
        big = [r for r in recs if r[2] >= 10]
        out.append(f"### {reason}")
        out.append("")
        out.append(f"{len(recs)} rows ({len(big)} with 10+ searches).")
        if big:
            out.append("")
            out.append("10+: " + "; ".join(f"{r[0]} ({r[2]})" for r in big))
        small = [r[0] for r in recs if r[2] < 10]
        if small:
            out.append("")
            out.append(f"Under 10 ({len(small)}): " + "; ".join(small))
        out.append("")
    if unclassified:
        out += ["## UNCLASSIFIED (fix scripts/keyword_plan.py)", ""] + [f"- {r[0]} ({r[2]})" for r in unclassified]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    print(f"{len(rows)} rows; {total10} with 10+: {assigned10} assigned, {unused10} unused, {len(unclassified)} unclassified")
    for r in unclassified:
        print("UNCLASSIFIED", r)
    missing = [k for k in TARGETS if k not in {rec[0] for v in by_page.values() for role, rec in v if role == 'target'}]
    for k in missing:
        print("TARGET NOT FOUND IN DATA", k)
    return 1 if unclassified or missing else 0


if __name__ == "__main__":
    sys.exit(main())
