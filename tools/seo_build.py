#!/usr/bin/env python3
"""Add the SEO/GEO layer to every page: Open Graph, Twitter cards, and a JSON-LD
@graph. Written as one script rather than ten hand-edits for the reason PAGES.md
§1 already gives about the shared shell — hand-copying across ten files is how
they drift apart.

WHAT IS DELIBERATELY NOT MARKED UP, and why (see HANDOFF §5):
  * Settlement figures / case results — HANDOFF §5.1 records them as INVENTED
    placeholders pending verified results, and a launch blocker under NY RPC 7.1.
    Putting them in schema would hand a known-fabricated claim to Google and to
    every AI answer engine as machine-readable fact. That is strictly worse than
    leaving them as page text.
  * AggregateRating / Review — the 106 reviews are GUREVICH LAW's, not GB Law
    Firm's (HANDOFF §5.11a). Marking them as this organisation's rating would
    assert something the source does not support, and rating snippets are
    exactly what gets amplified.
  * NYSBA membership — unverified with the firm (HANDOFF §5.2).
Each becomes valid the moment the client verifies it; the hooks are commented
in place so it is an uncomment, not a rebuild."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://gblawfirm.com"
ORG  = f"{SITE}/#organization"
WEB  = f"{SITE}/#website"

# ---- entities shared by every page ---------------------------------------
ORGANIZATION = {
    "@type": ["LegalService", "Attorney"],
    "@id": ORG,
    "name": "GB Law Firm",
    "url": SITE + "/",
    "telephone": "+1-516-444-1000",
    "description": "Personal injury and car accident law firm serving Long Island "
                   "and New York City.",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "580 Oak St",
        "addressLocality": "Copiague",
        "addressRegion": "NY",
        "postalCode": "11726",
        "addressCountry": "US",
    },
    "areaServed": [
        {"@type": "AdministrativeArea", "name": "Suffolk County, New York"},
        {"@type": "AdministrativeArea", "name": "Nassau County, New York"},
        {"@type": "Place", "name": "Long Island, New York"},
        {"@type": "City", "name": "New York City"},
    ],
    "knowsAbout": [
        "Car accident claims", "Personal injury law", "New York no-fault insurance",
        "Premises liability", "Slip and fall claims", "Wrongful death claims",
        "Uninsured motorist claims", "Truck accident claims",
    ],
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/GBlogo.png"},
    "image": f"{SITE}/assets/og-cover.jpg",
    # NOT SET, deliberately: aggregateRating (reviews are Gurevich Law's,
    # HANDOFF 5.11a), openingHours / email / geo / priceRange (no verified
    # source), sameAs (footer profiles are still href="#", HANDOFF 5.4).
}

WEBSITE = {
    "@type": "WebSite", "@id": WEB, "url": SITE + "/",
    "name": "GB Law Firm", "publisher": {"@id": ORG}, "inLanguage": "en-US",
}


def faq_from(rel, sec_id):
    """FAQPage built from the FAQ already on the page — client copy under the
    §9 lock, quoted exactly. Schema that does not match visible text is a
    guideline violation, so this reads the markup instead of restating it."""
    s = (ROOT / rel).read_text(encoding="utf-8")
    sec = s[s.index(f'id="{sec_id}"'):]
    sec = sec[:sec.index("</section>")]
    out = []
    for m in re.finditer(
            r"<summary><span>(.*?)</span>.*?<div class=\"acc-body\"><p>(.*?)</p>",
            sec, re.S):
        q = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", m.group(1))).strip()
        a = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", m.group(2))).strip()
        # Only the entries actually phrased as questions. The accordion also
        # holds five statement-titled panels ("Strict Legal Deadlines for Filing
        # a Claim"), which are good page content but are not `Question`s — and
        # FAQPage is defined as questions with answers. On a legal site, which
        # search engines hold to a higher bar than most, markup that overstates
        # what it is describing is a worse trade than five fewer entries. They
        # stay on the page and remain readable to anything that reads the page.
        if q.endswith("?"):
            out.append({"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}})
    return out


def faq_from_homepage():
    return faq_from("index.html", "questions")


def crumbs(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n,
         **({"item": u} if u else {})}
        for i, (n, u) in enumerate(trail, 1)]}


ATTORNEYS = {
 "philip-gurevich": {
   "name": "Philip Gurevich", "jobTitle": "Founding Partner",
   "image": f"{SITE}/assets/team-gurevich.webp",
   "alumniOf": "Florida A&M University College of Law",
   "knowsAbout": ["Personal injury litigation", "Car accident claims",
                  "Accident litigation"],
   # Bar admissions as stated in the client's own published bio.
   "hasCredential": [
     {"@type": "EducationalOccupationalCredential",
      "credentialCategory": "Bar admission",
      "name": "New York State Bar, admitted 2014"},
     {"@type": "EducationalOccupationalCredential",
      "credentialCategory": "Bar admission",
      "name": "The Florida Bar, admitted 2014 (currently inactive)"},
   ],
 },
 "albert-buznik": {
   "name": "Albert Buznik", "jobTitle": "Founding Partner",
   "image": f"{SITE}/assets/team-buznik.jpg",
   "alumniOf": "Nova Southeastern University, Shepard Broad Law Center",
   "knowsAbout": ["Personal injury litigation", "Medical malpractice",
                  "Commercial litigation", "Trial advocacy"],
   "hasCredential": [
     {"@type": "EducationalOccupationalCredential",
      "credentialCategory": "Bar admission",
      "name": "New York and Florida state courts"},
     {"@type": "EducationalOccupationalCredential",
      "credentialCategory": "Bar admission",
      "name": "U.S. District Courts, Eastern and Southern Districts of New York"},
   ],
 },
}


def person(slug):
    a = ATTORNEYS[slug]
    return {"@type": ["Person", "Attorney"], "@id": f"{SITE}/our-team/{slug}/#person",
            "name": a["name"], "jobTitle": a["jobTitle"], "image": a["image"],
            "url": f"{SITE}/our-team/{slug}/", "worksFor": {"@id": ORG},
            "alumniOf": {"@type": "EducationalOrganization", "name": a["alumniOf"]},
            "knowsAbout": a["knowsAbout"], "hasCredential": a["hasCredential"]}


# ---- per-page definitions -------------------------------------------------
PAGES = {
 "index.html": dict(
    url=SITE + "/", type="WebPage", title="GB Law Firm — Long Island Car Accident Lawyers",
    desc="Long Island car accident and personal injury lawyers. Free case review, "
         "no fee unless we win. Call (516) 444-1000.",
    extra=lambda: [{"@type": "FAQPage", "@id": f"{SITE}/#faq",
                    "mainEntity": faq_from_homepage()}],
    trail=[("Home", None)]),
 "our-team/index.html": dict(
    url=f"{SITE}/our-team/", type="WebPage", title="Our Legal Team | GB Law Firm",
    desc="The attorneys of GB Law Firm — Philip Gurevich and Albert Buznik, both "
         "admitted in New York state and federal courts.",
    extra=lambda: [{"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i,
         "url": f"{SITE}/our-team/{s}/", "name": ATTORNEYS[s]["name"]}
        for i, s in enumerate(ATTORNEYS, 1)]}],
    trail=[("Home", SITE + "/"), ("Legal Team", None)]),
 "our-team/philip-gurevich/index.html": dict(
    url=f"{SITE}/our-team/philip-gurevich/", type="ProfilePage",
    title="Philip Gurevich, Founding Partner | GB Law Firm",
    desc="Philip Gurevich has focused exclusively on personal-injury and accident "
         "litigation since 2013, serving New York City, Nassau and Suffolk County.",
    extra=lambda: [person("philip-gurevich")],
    mainEntity=f"{SITE}/our-team/philip-gurevich/#person",
    trail=[("Home", SITE + "/"), ("Legal Team", f"{SITE}/our-team/"),
           ("Philip Gurevich", None)]),
 "our-team/albert-buznik/index.html": dict(
    url=f"{SITE}/our-team/albert-buznik/", type="ProfilePage",
    title="Albert Buznik, Founding Partner | GB Law Firm",
    desc="Albert Buznik is a trial attorney handling personal injury, medical "
         "malpractice and commercial litigation in New York and Florida.",
    extra=lambda: [person("albert-buznik")],
    mainEntity=f"{SITE}/our-team/albert-buznik/#person",
    trail=[("Home", SITE + "/"), ("Legal Team", f"{SITE}/our-team/"),
           ("Albert Buznik", None)]),
 "contact/index.html": dict(
    url=f"{SITE}/contact/", type="ContactPage", title="Contact Us | GB Law Firm",
    desc="Contact GB Law Firm for a free, confidential consultation with a Long "
         "Island personal injury attorney. Call (516) 444-1000.",
    trail=[("Home", SITE + "/"), ("Contact Us", None)]),
 "case-results/index.html": dict(
    url=f"{SITE}/case-results/", type="WebPage", title="Case Results | GB Law Firm",
    desc="Amounts recovered by GB Law Firm for injured clients. Prior results do "
         "not guarantee a similar outcome.",
    # NO ItemList of the figures — HANDOFF 5.1 records them as invented.
    trail=[("Home", SITE + "/"), ("Case Results", None)]),
 "testimonials/index.html": dict(
    url=f"{SITE}/testimonials/", type="WebPage", title="Testimonials | GB Law Firm",
    desc="What clients said about the firm, in their own words — Google reviews "
         "reproduced without edits.",
    # NO Review/AggregateRating — the reviews are Gurevich Law's, HANDOFF 5.11a.
    trail=[("Home", SITE + "/"), ("Testimonials", None)]),
 "blog/index.html": dict(
    url=f"{SITE}/blog/", type="CollectionPage", title="Blog | GB Law Firm",
    desc="Notes from GB Law Firm on injury claims, deadlines and the process in "
         "New York.",
    trail=[("Home", SITE + "/"), ("Blog", None)]),
 "blog/hello-world/index.html": dict(
    url=f"{SITE}/blog/hello-world/", type="WebPage", title="Hello World | GB Law Firm",
    desc="The first entry on the GB Law Firm journal, and a note on what this "
         "section will be used for.",
    extra=lambda: [{"@type": "BlogPosting", "@id": f"{SITE}/blog/hello-world/#post",
                    "headline": "Hello World", "datePublished": "2026-08-05",
                    "author": {"@id": ORG}, "publisher": {"@id": ORG},
                    "mainEntityOfPage": f"{SITE}/blog/hello-world/"}],
    trail=[("Home", SITE + "/"), ("Blog", f"{SITE}/blog/"), ("Hello World", None)]),
 "sitemap/index.html": dict(
    url=f"{SITE}/sitemap/", type="WebPage", title="Sitemap | GB Law Firm",
    desc="Every page and homepage section on the GB Law Firm site, in one index.",
    trail=[("Home", SITE + "/"), ("Sitemap", None)]),
}

# ---- practice areas -------------------------------------------------------
# One page per tile in the homepage's Practice Areas section. Generated in a
# loop rather than written out four times, for the reason at the top of this
# file: four hand-copied entries is four things to forget to update.
#
# Each page's FAQ is marked up from that page's OWN visible text, by the same
# reader the homepage uses, so the schema and the page cannot drift apart.
#
# NOTHING here asserts an outcome, a figure or a credential. This copy is
# unverified draft pending client sign-off — HANDOFF §5, item 17.
PRACTICE_AREAS = {
    "rear-end-collisions": (
        "Rear-End Collisions", "Rear-End Collision Lawyers | GB Law Firm",
        "Rear-end collision lawyers serving Long Island. Fault, the serious "
        "injury threshold and no-fault deadlines explained. Call (516) 444-1000."),
    "head-on-collisions": (
        "Head-On Collisions", "Head-On Collision Lawyers | GB Law Firm",
        "Head-on collision lawyers serving Long Island. Finding every available "
        "policy, proving lifetime loss, wrongful death claims. Call (516) 444-1000."),
    "intersection-t-bone-crashes": (
        "Intersection and T-Bone Crashes",
        "Intersection and T-Bone Crash Lawyers | GB Law Firm",
        "Intersection and T-bone crash lawyers on Long Island. Right of way, "
        "signal timing, witnesses and camera footage. Call (516) 444-1000."),
    "distracted-driving-crashes": (
        "Distracted Driving Crashes",
        "Distracted Driving Accident Lawyers | GB Law Firm",
        "Distracted driving accident lawyers on Long Island. Phone records, "
        "telematics and preservation notices before the data is gone. Call (516) 444-1000."),
}

for _slug, (_name, _title, _desc) in PRACTICE_AREAS.items():
    _rel = f"practice-areas/{_slug}/index.html"
    PAGES[_rel] = dict(
        url=f"{SITE}/practice-areas/{_slug}/", type="WebPage",
        title=_title, desc=_desc,
        # default arg binds the slug at definition time; a bare closure over the
        # loop variable would give all four the last slug's FAQ.
        extra=(lambda rel=_rel, slug=_slug: [
            {"@type": "FAQPage", "@id": f"{SITE}/practice-areas/{slug}/#faq",
             "mainEntity": faq_from(rel, "faq")}]),
        trail=[("Home", SITE + "/"), ("Practice Areas", f"{SITE}/#practice"),
               (_name, None)])

# ---- service areas --------------------------------------------------------
# /service-areas/ plus one page per county and one per town beneath it. Same
# loop reasoning as the practice areas above: this set is four counties today
# and is built to hold many more, so it is generated rather than written out.
#
# The county and town pages carry no FAQPage of their own unless they have a
# visible FAQ — the town pages do not, and inventing schema for questions that
# are not on the page is exactly the mismatch this file exists to avoid.
SERVICE_AREAS = {
    "suffolk-county": ("Suffolk County", "Suffolk County Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Suffolk County — the LIE, Sunrise Highway "
        "and the parkways. Free case review. Call (516) 444-1000.",
        "huntington", "Huntington", "Huntington Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Huntington, Suffolk County — Route 110, "
        "Jericho Turnpike and the Melville corridor. Call (516) 444-1000."),
    "nassau-county": ("Nassau County", "Nassau County Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Nassau County — Hempstead Turnpike, the "
        "parkways and the Meadowbrook. Free case review. Call (516) 444-1000.",
        "hempstead", "Hempstead", "Hempstead Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Hempstead, Nassau County — Hempstead "
        "Turnpike and the Southern State. Call (516) 444-1000."),
    "queens-county": ("Queens County", "Queens Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Queens — the Van Wyck, Queens Boulevard "
        "and Grand Central Parkway. Free case review. Call (516) 444-1000.",
        "flushing", "Flushing", "Flushing Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Flushing, Queens — Main Street, Northern "
        "Boulevard and the Van Wyck. Call (516) 444-1000."),
    "kings-county": ("Kings County", "Brooklyn Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Brooklyn and Kings County — the BQE, the "
        "Belt Parkway and Atlantic Avenue. Call (516) 444-1000.",
        "bay-ridge", "Bay Ridge", "Bay Ridge Car Accident Lawyers | GB Law Firm",
        "Car accident lawyers serving Bay Ridge, Brooklyn — the Belt Parkway, "
        "the Verrazzano approach and Fifth Avenue. Call (516) 444-1000."),
}

PAGES["service-areas/index.html"] = dict(
    url=f"{SITE}/service-areas/", type="CollectionPage",
    title="Service Areas | GB Law Firm",
    desc="Where GB Law Firm works — Suffolk, Nassau, Queens and Kings counties, "
         "county by county and town by town. Call (516) 444-1000.",
    extra=lambda: [{"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i,
         "url": f"{SITE}/service-areas/{s}/", "name": v[0]}
        for i, (s, v) in enumerate(SERVICE_AREAS.items(), 1)]}],
    trail=[("Home", SITE + "/"), ("Service Areas", None)])

for _slug, (_cname, _ctitle, _cdesc, _tslug, _tname, _ttitle, _tdesc) in SERVICE_AREAS.items():
    _crel = f"service-areas/{_slug}/index.html"
    PAGES[_crel] = dict(
        url=f"{SITE}/service-areas/{_slug}/", type="WebPage",
        title=_ctitle, desc=_cdesc,
        # default args bind at definition time; a bare closure over the loop
        # variable would give every county the last one's FAQ.
        extra=(lambda rel=_crel, slug=_slug: [
            {"@type": "FAQPage", "@id": f"{SITE}/service-areas/{slug}/#faq",
             "mainEntity": faq_from(rel, "faq")}]),
        trail=[("Home", SITE + "/"), ("Service Areas", f"{SITE}/service-areas/"),
               (_cname, None)])
    PAGES[f"service-areas/{_slug}/{_tslug}/index.html"] = dict(
        url=f"{SITE}/service-areas/{_slug}/{_tslug}/", type="WebPage",
        title=_ttitle, desc=_tdesc,
        trail=[("Home", SITE + "/"), ("Service Areas", f"{SITE}/service-areas/"),
               (_cname, f"{SITE}/service-areas/{_slug}/"), (_tname, None)])

BLOCK_START = "<!-- ===== SEO / GEO: generated by seo_build.py — edit there, not here ===== -->"
BLOCK_END   = "<!-- ===== end SEO / GEO ===== -->"

for rel, cfg in PAGES.items():
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    depth = "../" * rel.count("/")

    graph = [ORGANIZATION, WEBSITE]
    page = {"@type": cfg["type"], "@id": cfg["url"] + "#webpage", "url": cfg["url"],
            "name": cfg["title"], "description": cfg["desc"],
            "isPartOf": {"@id": WEB}, "about": {"@id": ORG}, "inLanguage": "en-US",
            "breadcrumb": crumbs(cfg["trail"])}
    if cfg.get("mainEntity"):
        page["mainEntity"] = {"@id": cfg["mainEntity"]}
    graph.append(page)
    if cfg.get("extra"):
        graph.extend(cfg["extra"]())

    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    indent=2, ensure_ascii=False)

    og = f"""{BLOCK_START}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="GB Law Firm" />
<meta property="og:locale" content="en_US" />
<meta property="og:url" content="{cfg['url']}" />
<meta property="og:title" content="{cfg['title']}" />
<meta property="og:description" content="{cfg['desc']}" />
<meta property="og:image" content="{SITE}/assets/og-cover.jpg" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="GB Law Firm — Long Island personal injury attorneys" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{cfg['title']}" />
<meta name="twitter:description" content="{cfg['desc']}" />
<meta name="twitter:image" content="{SITE}/assets/og-cover.jpg" />
<script type="application/ld+json">
{ld}
</script>
{BLOCK_END}"""

    # replace an existing generated block, else insert before </head>
    if BLOCK_START in s:
        s = re.sub(re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END), og, s, flags=re.S)
    else:
        s = s.replace("</head>", og + "\n</head>", 1)

    # the homepage was the one page with no canonical
    if 'rel="canonical"' not in s:
        s = s.replace('<meta name="theme-color" content="#0A1628" />',
                      '<meta name="theme-color" content="#0A1628" />\n'
                      f'<link rel="canonical" href="{cfg["url"]}" />', 1)

    # descriptions over 160 chars get truncated in results; use the same text
    # already written for og/twitter so all three agree.
    s = re.sub(r'<meta name="description" content="[^"]*" />',
               f'<meta name="description" content="{cfg["desc"]}" />', s, count=1)

    p.write_text(s, encoding="utf-8")
    print(f"{rel:38s} ld-nodes={len(graph)} desc={len(cfg['desc'])}")
