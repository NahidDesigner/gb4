# Reference: getbierlaw.com — the agency's own injury site

Live review, 2026-08-05, desktop 1440px and mobile 390px, DOM + stylesheet
inspection. This is one of the "other injury sites we did" the client told us to
study. It is the house pattern. DESIGN.md §1b and §8 rest on these findings.

## Stack

**WordPress + Elementor 4.2.1**, jQuery, Swiper. Not hand-built. (Contrast with
`hotelroyaloak.com`, which the same reviewer hand-coded with zero libraries —
he is comfortable both ways, so our static build is not a liability.)

## Palette — and the rule hiding inside it

- Ground: navy `#0A192F`
- Accent: orange `#EB5600`
- Success/live badges: green `#27AE60`
- Radii: 3, 12, 14, 15, 16px, 50%

**Orange is Get Bier's own logo colour.** The hotel site is likewise dark ground
+ its own orange logo colour. So the house method is not "navy and orange" — it
is **dark ground + that client's logo accent**. Applied to GB, whose logo samples
to navy `#00183C` and gold `#C09030`, it yields **navy + gold**. This is the
single most important finding in this document and it resolves the palette
question without compromise.

## Type

Roboto (H1 700/45px), Inter, **Bebas Neue** (condensed caps display),
Playfair Display (serif accent), plus a script face for signatures. DESIGN.md
deliberately declines Bebas Neue: condensed caps is the loud register, and GB's
positioning is the quiet one.

**Two-tone headline** — "JEFF **BIER**" white/orange. Identical device to the
hotel's "A 1954 motor inn, **REBUILT**". Imported into DESIGN.md §4, re-voiced
as one word switching to gold or oxblood.

## Density — the actual bar

- **126 images** on the homepage; cut-out attorney photography throughout
- **13,600–14,500px** page heights
- **Three** separate tickers: credentials, settlement alerts, nav-adjacent
- Sticky call bar, floating "Investigate my accident" chip, and a video-concierge
  widget (same vendor as the hotel site)
- Ghosted watermark type behind headings; topographic line texture
- Trust-badge strip: Super Lawyers, Google Guaranteed, National Trial Lawyers
- `$10M+ Recovered` badges over city photography

## Proof mechanism — and the blocker it creates for GB

The template's spine is **settlement figures**: a live "SETTLEMENT ALERT — JUST
WON $305,000" ticker, and a carousel of $4.55M / $3.2M / $2.15M repeated on the
homepage *and* every practice-area page.

**GB's figures are invented placeholders and a launch blocker (HANDOFF §5.1.)**
So GB cannot ship the house template's loudest module until the firm supplies
verified results. DESIGN.md §8.3 therefore specifies The Record of Recovery to be
built against clearly-marked placeholders and to **remain a finished section if
the numbers never clear**. Same applies to the trust-badge strip (§8.9, Avvo and
NYSBA unverified per §5.2) and cut-out photography (§8.11, GB has two headshots).

## Information architecture — already matched

Get Bier: Home · Practice Areas · Legal Team (attorney children) · Testimonials ·
Case Results · Resources (Blog, Videos, Disclosure) · Contact Us.

GB's nav is effectively this list. **The IA was never the problem** — the gap was
density and finish, which is what DESIGN.md §8 addresses.

## What transfers, and what does not

**Transfers:** dark ground + logo accent; the two-tone headline; ticker devices;
sticky conversion furniture at all times; photography as load-bearing; live proof
modules; long pages that never thin out.

**Does not:** orange (GB's accent is gold, from its own logo); Bebas Neue; pills
and rounded cards; Elementor. Cloning Get Bier would make GB read as a lesser
copy of a sibling site and would contradict the client's own "old money means
classy, not basic."
