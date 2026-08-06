#!/usr/bin/env python3
"""The firm's identity facts — phone, address, domain, name — in one place,
with every serialisation each one uses and every file it appears in.

WHY THIS EXISTS. The phone number is written four different ways across this
site: `tel:+15164441000` in every call link, `(516) 444-1000` in visible text,
`+1-516-444-1000` in the JSON-LD, and the same display form in the meta
descriptions. Search-and-replace on the one a human sees updates 53 places and
misses the 76 `tel:` links, so every button on the site still dials the old
number while every page shows the new one. Nothing looks broken. That is the
failure this file is here to prevent.

    python3 tools/identity.py                 # report: where every fact appears
    python3 tools/identity.py --check         # exit 1 on drift or stray values
    python3 tools/identity.py --set phone='(516) 555-0199'
    python3 tools/identity.py --set domain=https://newdomain.com
    python3 tools/identity.py --set phone='...' --dry-run

--set rewrites EVERY serialisation of that fact everywhere, then re-runs the
check. Always run it on a clean tree so `git diff` shows you exactly what moved.
"""
import argparse, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Files that are the live site. Excluded: original-untouched/ and *-v2.* are
# superseded drafts (they keep their old values on purpose, as a record);
# .impeccable/ is editor/tooling scratch; both of those are gitignored and so
# never reach a git-based deploy. .git / tools are not content.
#
# Scanning a gitignored directory would mean --set edits a file git cannot
# restore, which is exactly the sort of surprise this tool exists to avoid.
SKIP_DIRS = {".git", ".impeccable", "original-untouched", "tools", "node_modules"}
SKIP_NAMES = {"index-v2.html", "styles-v2.css"}
EXTS = {".html", ".css", ".js", ".md", ".txt", ".xml", ".json", ".webmanifest"}


def files():
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir() or p.suffix not in EXTS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.name in SKIP_NAMES:
            continue
        yield p


# --- the facts -------------------------------------------------------------
# `variants` renders the canonical value into every form the site actually uses.
# Add a form here the moment you introduce one anywhere, or --set will miss it.

def phone_variants(v):
    d = re.sub(r"\D", "", v)[-10:]                      # 5164441000
    return {
        "tel: link (href)":      f"tel:+1{d}",
        "display":               f"({d[:3]}) {d[3:6]}-{d[6:]}",
        "schema.org telephone":  f"+1-{d[:3]}-{d[3:6]}-{d[6:]}",
    }


def address_variants(v):
    street, city, region_zip = [s.strip() for s in v.split(",")]
    region, postal = region_zip.split()
    return {
        "display":               f"{street}, {city}, {region} {postal}",
        "maps query (+ sep)":    f"{street}+{city}+{region}+{postal}".replace(" ", "+"),
        "maps embed (+ commas)": f"{street},+{city},+{region}+{postal}".replace(" ", "+"),
    }


def domain_variants(v):
    return {"absolute URL": v.rstrip("/")}


def name_variants(v):
    return {"firm name": v}


def email_variants(v):
    return {"mailto: link": f"mailto:{v}", "display": v}


FACTS = {
    "phone":   dict(value="(516) 444-1000", variants=phone_variants,
                    note="Four written forms. The tel: links are the ones that get missed."),
    "address": dict(value="580 Oak St, Copiague, NY 11726", variants=address_variants,
                    note="Two of the three forms are URL-encoded inside Google Maps links."),
    "domain":  dict(value="https://gblawfirm.com", variants=domain_variants,
                    note="Canonicals, og:url, JSON-LD @id, sitemap.xml, robots.txt, llms.txt."),
    "name":    dict(value="GB Law Firm", variants=name_variants,
                    note="Also the og:site_name and the JSON-LD organisation name."),
    "email":   dict(value=None, variants=email_variants,
                    note="THE SITE HAS NO EMAIL ADDRESS. Adding one is an insertion, not a "
                         "replacement — --set cannot do it. See IDENTITY.md."),
}

# Values that must never appear: the old/other numbers and domains that would
# mean a partial update happened. Extend this when a fact changes.
STRAY = [
    (re.compile(r"\btel:\+?1?\d{10}\b"), "tel: link", "phone"),
    (re.compile(r"\(\d{3}\)\s?\d{3}-\d{4}"), "display phone", "phone"),
]


def occurrences(text_cache, needle):
    hits = []
    for p, text in text_cache:
        n = text.count(needle)
        if n:
            hits.append((p.relative_to(ROOT), n))
    return hits


def load():
    return [(p, p.read_text(encoding="utf-8", errors="replace")) for p in files()]


def report(cache, check=False):
    problems = []
    print(f"scanned {len(cache)} files\n")
    for key, f in FACTS.items():
        print(f"── {key.upper()}")
        if f["value"] is None:
            print(f"   (not set) {f['note']}\n")
            continue
        print(f"   canonical: {f['value']}")
        total = 0
        for label, form in f["variants"](f["value"]).items():
            hits = occurrences(cache, form)
            n = sum(c for _, c in hits)
            total += n
            print(f"     {label:24s} {form:38s} {n:4d} in {len(hits)} files")
            for rel, c in hits:
                print(f"        {c:3d}  {rel}")
        if total == 0:
            problems.append(f"{key}: canonical value appears nowhere — has it been changed?")
        print()

    # stray values: any phone-shaped string that is not the canonical one
    canon = set(FACTS["phone"]["variants"](FACTS["phone"]["value"]).values())
    for p, text in cache:
        if p.name in {"IDENTITY.md", "identity.py"}:
            continue
        for rx, what, _ in STRAY:
            for m in set(rx.findall(text)):
                if m.strip() not in canon:
                    problems.append(f"{p.relative_to(ROOT)}: stray {what} {m!r} "
                                    f"(canonical is {FACTS['phone']['value']})")
    return problems


def apply_set(cache, key, new):
    f = FACTS.get(key)
    if f is None:
        sys.exit(f"unknown fact {key!r}; known: {', '.join(FACTS)}")
    if f["value"] is None:
        sys.exit(f"{key} is not set anywhere yet — adding it is an insertion, "
                 f"not a replacement. See IDENTITY.md.")
    old_forms = f["variants"](f["value"])
    new_forms = f["variants"](new)
    changes = []
    for label in old_forms:
        o, n = old_forms[label], new_forms[label]
        if o == n:
            continue
        for p, text in cache:
            if o in text:
                changes.append((p, o, n, text.count(o)))
    return changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--set", dest="sets", action="append", default=[],
                    metavar="key=value")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cache = load()

    if a.sets:
        edits = {}
        for pair in a.sets:
            k, _, v = pair.partition("=")
            for p, o, n, count in apply_set(cache, k.strip(), v.strip()):
                edits.setdefault(p, []).append((o, n, count))
        if not edits:
            print("nothing to change")
            return
        for p, subs in sorted(edits.items()):
            print(f"{p.relative_to(ROOT)}")
            for o, n, c in subs:
                print(f"   {c:3d}x  {o}  ->  {n}")
        if a.dry_run:
            print("\n--dry-run: nothing written")
            return
        for p, subs in edits.items():
            t = p.read_text(encoding="utf-8")
            for o, n, _ in subs:
                t = t.replace(o, n)
            p.write_text(t, encoding="utf-8")
        print("\nWritten. Update FACTS in tools/identity.py to the new canonical "
              "value, then re-run: python3 tools/identity.py --check")
        return

    problems = report(cache, a.check)
    if problems:
        print(f"{len(problems)} PROBLEM(S):")
        for x in problems:
            print("  -", x)
        sys.exit(1 if a.check else 0)
    print("no drift, no stray values")


if __name__ == "__main__":
    main()
