#!/usr/bin/env python3
"""Audit the SEO/GEO layer. Checks the things Lighthouse does not: description
length, canonical/og/twitter presence, JSON-LD validity, @id references that
point at nothing, heading levels that skip, and the claims that must never
appear in structured data.

Exits non-zero if anything fails, so it drops into a pre-commit hook or CI.

    python3 tools/seo_audit.py
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://gblawfirm.com"

# HANDOFF §5.1 / §5.11a / §5.2 — these must not reach structured data until the
# client verifies them. A future pass "completing" the schema is exactly how
# they would get in, so the audit fails rather than trusting anyone to remember.
FORBIDDEN_IN_LD = [
    ("aggregateRating", "reviews are Gurevich Law's, not GB Law Firm's — HANDOFF 5.11a"),
    ("ratingValue",     "same as above"),
    ('"@type": "Review"', "same as above"),
    ("NYSBA",           "membership unverified with the firm — HANDOFF 5.2"),
    ("New York State Bar Association", "membership unverified — HANDOFF 5.2"),
]
MONEY = re.compile(r"\$\s?[\d,]{4,}")   # settlement figures — HANDOFF 5.1

failures, checked = [], 0


def fail(page, msg):
    failures.append(f"{page}: {msg}")


for p in sorted(ROOT.rglob("index.html")):
    rel = p.relative_to(ROOT)
    if "original-untouched" in str(rel):
        continue
    checked += 1
    raw = p.read_text(encoding="utf-8")
    nocomment = re.sub(r"<!--.*?-->", "", raw, flags=re.S)

    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    if not t:
        fail(rel, "no <title>")
    elif len(t.group(1)) > 60:
        fail(rel, f"title {len(t.group(1))} chars (>60, truncated in results)")

    d = re.search(r'name="description" content="(.*?)"', raw, re.S)
    if not d:
        fail(rel, "no meta description")
    elif len(d.group(1)) > 160:
        fail(rel, f"description {len(d.group(1))} chars (>160, truncated)")

    for needle, what in (('rel="canonical"', "canonical"),
                         ('property="og:title"', "og:title"),
                         ('property="og:image"', "og:image"),
                         ('name="twitter:card"', "twitter:card")):
        if needle not in raw:
            fail(rel, f"missing {what}")

    # heading levels, comments stripped first: a literal tag inside a comment is
    # not an outline entry, and matching one is a false positive we already hit.
    hs = [int(m.group(1)) for m in re.finditer(r"<h([1-6])\b", nocomment)]
    if hs.count(1) != 1:
        fail(rel, f"{hs.count(1)} h1 elements (want exactly 1)")
    for a, b in zip(hs, hs[1:]):
        if b - a > 1:
            fail(rel, f"heading level skips h{a} -> h{b}")

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', raw, re.S)
    if not blocks:
        fail(rel, "no JSON-LD")
    for b in blocks:
        try:
            data = json.loads(b)
        except json.JSONDecodeError as e:
            fail(rel, f"JSON-LD does not parse: {e}")
            continue
        graph = data.get("@graph", [])
        if not graph:
            fail(rel, "JSON-LD has no @graph")
        blob = json.dumps(graph)

        defined = {n["@id"] for n in graph if "@id" in n}
        refs = set(re.findall(r'"@id":\s*"([^"]+)"', blob))
        dangling = {r for r in refs - defined
                    if not r.startswith(f"{SITE}/our-team/")}
        if dangling:
            fail(rel, f"JSON-LD @id references nothing: {sorted(dangling)}")

        for needle, why in FORBIDDEN_IN_LD:
            if needle in blob:
                fail(rel, f"structured data contains '{needle}' — {why}")
        if MONEY.search(blob):
            fail(rel, "structured data contains a money figure — settlement "
                      "figures are placeholders, HANDOFF 5.1")

# files the GEO layer depends on
for f in ("robots.txt", "llms.txt", "sitemap.xml", "favicon.ico",
          "assets/GBlogo.png"):
    if not (ROOT / f).exists():
        fail("site", f"missing {f}")

# every URL in sitemap.xml must actually exist on disk
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for loc in re.findall(r"<loc>(.*?)</loc>", sm):
    path = loc.replace(SITE, "").strip("/")
    target = ROOT / (path + "/index.html" if path else "index.html")
    if not target.exists():
        fail("sitemap.xml", f"lists {loc} but {target.relative_to(ROOT)} does not exist")

print(f"checked {checked} pages")
if failures:
    print(f"\n{len(failures)} FAILURE(S):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("all checks passed")
