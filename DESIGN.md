---
version: 6
name: GB-Law-Firm-design-system
description: >
  A Long Island personal injury firm formed by the merger of two practices, presenting as an
  institution rather than two attorneys. The register is old money — Skadden's institutional
  confidence rather than a startup's polish, restraint executed with craft rather than the
  absence of design. The base is bluestone (#E3E6E4 pale ground, #0A1628 deep field), cut with
  cast bronze (#C9A227) as the single voltage, pinned to the client's logo. Type runs Cinzel for
  display — a Roman inscriptional serif, never below 20px, never for body — against Source Sans 3
  for reading and Archivo Narrow for data and labels. Display weight is heavy and the scale is
  large: this system trusts typographic muscle and real evidence (settlement figures, client
  names, Long Island place names) where a consumer brand would trust photography. Shape language
  is hard — 0 to 2px radius everywhere, hairline incised rules instead of shadows, no lifted
  cards. Depth comes from the dark field and from cut rules, never from elevation. The governing
  law of the system is compositional variety: seven layout archetypes, none permitted to appear
  in consecutive sections.

supersedes: all previous DESIGN.md, creative direction, and constitution documents (deleted)
status: binding — implement exactly, no improvisation
---

# GB LAW FIRM — DESIGN SYSTEM & BUILD SPEC

## 0. MANDATE

This is a **clean-sheet redesign.** Do not open the existing homepage implementation for design
inspiration. Do not preserve, refine, or evolve any current section treatment.

**Only three things survive:**
1. The hero — locked by the Creative Director
2. The color tokens (§2) — pinned to the client's logo, mandated by brief
3. The section inventory and body copy (§7) — client-approved, contractual

Everything else is a blank page.

---

## 1. WHY THE PREVIOUS BUILD WAS REJECTED

Not craft. Not code. One measurable defect:

> **Eight of fourteen sections used the identical composition** — a bronze rule, a stacked serif
> heading in the left column, body text or rows in the right column. Alternating pale and navy
> grounds did not break it; it was one layout wearing two colors.

The page read as a formatted document. The reviewer's words: "basic," "outdated," "like a high
schooler designed it."

**§4 exists to prevent this.** Craft was never the deficit — do not spend effort re-polishing it
at the expense of composition.

---

## 2. TOKENS

### Colors

```yaml
colors:
  # Bluestone — the ground the page is cut from
  stone-pale:    "#E3E6E4"   # primary reading ground
  stone-light:   "#EDEFEE"   # raised plates, finer cut
  stone-mid:     "#D3D8D6"   # the settlements slab
  stone-deep:    "#0A1628"   # dark field — logo-pinned
  stone-raised:  "#132540"   # raised surface on dark
  stone-black:   "#06101F"   # footer, deepest cut

  # Cast bronze — the single polished signal
  bronze:        "#C9A227"   # logo-pinned. 7.6:1 on stone-deep
  bronze-lit:    "#E7CE84"   # struck highlight — dark grounds only
  bronze-ink:    "#7A5D14"   # bronze as text on pale — 4.9:1
  bronze-deep:   "#5E4A0E"   # bronze as text on mid slab — 5.8:1
  bronze-rake:   "#DCBB4E"   # gradient stop — polished top rake
  bronze-body:   "#B08F1E"   # gradient stop — body
  bronze-edge:   "#8A6A12"   # gradient stop — shaded edge

  # Verdigris — the patina third, used sparingly
  verdigris:     "#3C625C"   # 5.4:1 on pale
  verdigris-lit: "#7FA8A0"   # 6.9:1 on deep

  ink:           "#10151A"   # 14.4:1 on pale
  ink-soft:      "#47525A"   # 6.3:1 on pale
  on-dark:       "#E8EDF2"
  on-dark-soft:  "rgba(232,237,242,.66)"
  rule-cut:      "#BEC5C2"   # incised hairline on light
  rule-cut-dark: "rgba(198,214,226,.19)"
  error:         "#8C2F1E"   # the only red — failed fields only
```

**Bronze law.** Bronze is a signal, not a highlighter. **Maximum two bronze elements visible per
viewport.** If a third appears, remove one. Bronze never fills large areas — it is a rule, a
figure, a button, an underline.

> **Amended 2026-08-06.** The per-viewport cap applies to **section content only**. Persistent
> chrome is exempt: `{component.button-call}` in `{component.site-header}` and
> `{component.sticky-call-bar}` do not count against a section's two. Without the exemption the
> fixed header CTA spent one of every section's two slots page-wide, which made the cap
> unsatisfiable rather than disciplined. The settlements landmark figure **stays bronze**.

**Ground rhythm.** Never more than **two consecutive pale sections.** The dark field marks the
page's landmarks; it is structure, not variety-relief.

### Typography

```yaml
fonts:
  display: "'Cinzel', 'Trajan Pro', Georgia, serif"       # headings only, never below 20px
  body:    "'Source Sans 3', -apple-system, sans-serif"
  utility: "'Archivo Narrow', 'Archivo', sans-serif"      # labels, data, buttons, eyebrows

typography:
  display-xl:                                  # landmarks and settlement figures
    fontFamily: "{fonts.display}"
    fontSize: "clamp(52px, 7vw, 104px)"
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "-0.01em"
  display-l:                                   # section headings
    fontFamily: "{fonts.display}"
    fontSize: "clamp(34px, 4vw, 56px)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "0.005em"
  display-m:                                   # card and sub headings
    fontFamily: "{fonts.display}"
    fontSize: "clamp(24px, 2.4vw, 32px)"
    fontWeight: 600
    lineHeight: 1.2
  display-s:                                   # smallest permitted display use
    fontFamily: "{fonts.display}"
    fontSize: "20px"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "{fonts.body}"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  body-lead:                                   # section intro paragraphs
    fontFamily: "{fonts.body}"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.6
  body-s:
    fontFamily: "{fonts.body}"
    fontSize: "15px"
    lineHeight: 1.6
  label:                                       # eyebrows, captions, data labels
    fontFamily: "{fonts.utility}"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.14em"
    textTransform: "uppercase"
  button:
    fontFamily: "{fonts.utility}"
    fontSize: "13px"
    fontWeight: 700
    letterSpacing: "0.12em"
    textTransform: "uppercase"
  figure:                                      # settlement amounts
    fontFamily: "{fonts.display}"
    # Amended 2026-08-06 (second revision). Was clamp(40px, 6.3vw, 87px) when the
    # landmark carried five stacked rows. The landmark now carries a two-column
    # grid of 12-16 cells: impact comes from QUANTITY, not point size, so the
    # figure steps down to sit inside a dense grid without crowding.
    fontSize: "clamp(28px, 3.2vw, 44px)"
    fontWeight: 600
    lineHeight: 1
    fontVariantNumeric: "lining-nums tabular-nums"
```

**Type law.** Cinzel is inscriptional — it is set with *space*, never crammed. No Cinzel below
20px. No Cinzel for body copy, ever. Headings run 2–4 lines maximum; if a heading needs five
lines, the copy is wrong, not the type.

### Shape, spacing, elevation

```yaml
rounded:
  none: "0px"     # default for everything
  xs:   "2px"     # inputs and buttons — the only permitted rounding

spacing:
  xxs: "4px"
  xs:  "8px"
  sm:  "12px"
  md:  "20px"
  lg:  "32px"
  xl:  "48px"
  xxl: "80px"
  section: "clamp(88px, 11vh, 168px)"   # top and bottom padding, every section

layout:
  container: "1200px"
  container-narrow: "760px"    # centered statement archetype
  gutter-mobile: "24px"
  grid-gap: "32px"
  grid-gap-mobile: "20px"

elevation:
  flat: "none"                 # 100% of surfaces
  # There is no shadow in this system. Depth comes from the dark field
  # and from incised hairline rules. Never add a box-shadow.
```

**Shape law.** This is a hard-cornered system. 0px is the default; 2px is the maximum, and only
on inputs and buttons. **No shadows anywhere.** A lifted card with a drop shadow is a 2015 tell
and reads as exactly the failure this redesign is correcting.

---

## 3. COMPONENTS

Every interactive and repeating element is defined here. **Do not invent a variant.** If a
section needs something not listed, stop and report.

### Rules and marks

**`rule-cut`** — The system's hairline. 1px, `{colors.rule-cut}` on pale grounds,
`{colors.rule-cut-dark}` on the dark field. Divides rows and closes sections. Never used
decoratively above a heading — that was the rejected build's signature tic.

**`rule-bronze`** — A 2px bronze rule, maximum 64px long. **Permitted at most twice per page.**
Draws left-to-right on entry (§5).

**`eyebrow`** — `{typography.label}` in `{colors.bronze-ink}` on pale, `{colors.bronze}` on dark.
Sits above a heading with `{spacing.sm}` beneath. No rule, no icon.

### Buttons

**`button-primary`** — Bronze fill (`{colors.bronze}`), `{colors.stone-deep}` text,
`{typography.button}`, `{rounded.xs}`, padding 18×36px, height 56px. The page's primary CTA.
Hover: fill deepens to `{colors.bronze-body}` over `{motion.t-fast}`. **Never scales, never
lifts, never gains a shadow.**

**`button-secondary`** — Transparent fill, 1px `{colors.ink}` border on pale / `{colors.bronze}`
border on dark, matching text color. Same metrics as primary. Hover: border and text shift to
bronze on pale, bronze-lit on dark.

**`button-text`** — `{typography.label}` with a 1px underline growing 0 → 100% width on hover over
`{motion.t-fast}`. Used for "View all case results" style links.

**`button-call`** — Bronze fill carrying a phone number in `{typography.button}`, numerals tabular.
Appears in the header, the bands, and the sticky mobile bar.

### Header and navigation

**`site-header`** — **Amended 2026-08-06.** Absent over the hero; slides down solid on
`{motion.t-base}` `{motion.ease-out}` once the hero exits. The locked hero carries its own brand
lockup and its own menu/search controls, so a header over it put two brand marks and two nav
controls on screen at once — the header must never be visible at the same time as the hero.

Height 72px desktop / 64px mobile, `{colors.stone-deep}`, 1px bottom `{colors.rule-cut-dark}`.
**The logo is sized by height, not width — 52px mark in the 72px bar, 44px in the 64px bar on
mobile**, centred, with utilities (menu trigger, search, call) flanking it. Sizing by width was
not buildable: every logo asset is 560×406 (1.379:1), so the previous 180px-wide rule computed to
131px tall and overflowed the bar onto the content beneath it. Brand prominence is carried by the
hero (§12), not by this bar.

**`nav-trigger`** — `{typography.label}` text label plus a 3-line glyph, `{colors.on-dark}`. Opens
`{component.nav-overlay}`. No hamburger-only icon — the word is part of the register.

**`nav-overlay`** — Full-viewport `{colors.stone-deep}` panel. Links in `{typography.display-m}`,
stacked, left-aligned in the container, staggered reveal at 60ms. Closes on Escape.

**`sticky-call-bar`** — Mobile only. Appears after the hero exits, slides up over
`{motion.t-base}`. Full-width `{colors.bronze}` strip, 64px tall, carrying
`{component.button-call}`. Persistent thereafter. Respects safe-area inset.

### Proof components

**`figure-cell`** — The settlements landmark unit and the system's signature. Amount in
`{typography.figure}`, `{colors.bronze-lit}` on the dark field. Beneath it the case type in
`{typography.label}` `{colors.on-dark}`, and a one-line detail in `{typography.body-s}`
`{colors.on-dark-soft}`. Separated from neighbors by `{component.rule-cut}` only — no card, no
border box, no fill. Counts up on entry (§5.5).

> **Amended 2026-08-06.** Cells are laid out as a **two-column grid of 12–16**, not a stacked
> list. Five stacked rows undersold the $100M+ claim: the section's job is proof *density*, and
> density is a count, not a type size — hence the `{typography.figure}` step down in §2. The
> no-card rule is unchanged and load-bearing at this quantity: 14 bordered boxes would read as a
> pricing table. Separation stays `{component.rule-cut}` alone — **no cards, no shadows, no
> gradients.** Collapses to one column below 1025px.
>
> Counter stagger is **60ms** across the grid with the whole sequence under **1.6s**, which
> supersedes §5.5's 1400ms per-figure duration for this component — at 14 cells the last figure
> would otherwise start at 780ms and finish at 2.18s. Per-figure duration is 680ms so the
> sequence closes at ~1.46s.

**`stat-band`** — A row of `{component.figure-cell}` at reduced scale, where a section needs
supporting numbers rather than a landmark.

**`review-card`** — `{colors.stone-light}` surface, `{rounded.none}`, 1px `{colors.rule-cut}`
border, 28px padding. Five bronze stars at 12px, the excerpt in `{typography.body-s}`
`{colors.ink}` clamped to 6 lines, the reviewer name in `{typography.label}`, the source in
`{typography.body-s}` `{colors.ink-soft}`. Fixed height within a row so the grid stays true.

**`review-summary`** — The Google mark, score at `{typography.display-m}`, five stars, review count
in `{typography.label}`. Sits above the review grid, left-aligned in container.

**`badge-marquee`** — Continuous horizontal strip on `{colors.stone-deep}`, 88px tall, carrying
authority marks at 32px height in `{colors.on-dark}` separated by a 6px bronze dot. 40s linear
loop, pauses on hover, duplicated track for seamless wrap.

### Content components

**`practice-louver`** — **Added 2026-08-06.** An expanding louver. Supersedes
`{component.practice-index}` for section #9.

Four vertical panels spanning the container, `gap: 2px`, `{rounded.none}`, section height
`clamp(560px, 72vh, 760px)`. **Exactly one panel is expanded at any time** (58%), holding its
photograph at full size with its name and description; the other three collapse to slivers (14%
each) carrying an index numeral and the practice-area name set vertically. Hover or keyboard focus
redistributes the widths.

*Mechanic* is reused from the agency's house Bier practice-areas widget — flex-grow redistribution,
`writing-mode: vertical-rl` labels, a dimmed copy of each panel's own image behind the collapsed
state — because it is proven at these proportions. **None of its surface treatment is reused:** no
shadow, no radius, no gradient accent bar, no hover translateY, no accordion, no bottom bar, none
of its palette. §2 tokens only.

**Expanded panel.** Photograph `object-fit: cover`, graded `saturate(0.55) contrast(1.06)`. A
`{colors.stone-deep}` scrim rises from the base, 78% → transparent at 52% height. In the bottom
40px padding: a 40px `{component.rule-bronze}`, the name at `{typography.display-m}`
`{colors.on-dark}`, the description at `{typography.body-s}` `{colors.on-dark-soft}`, max 42ch.

**Collapsed panels.** The same photograph behind at `opacity: .18` over `{colors.stone-deep}`.
Index numeral top-left in `{typography.label}`; the name in `writing-mode: vertical-rl` at
`{typography.display-s}` `{colors.on-dark-soft}`, reading bottom-to-top, vertically centred. No
description.

**Each panel's image is pinned to the EXPANDED width** (via container-query units) with
`overflow: hidden` on the panel, so collapsing **crops** the photograph rather than squashing it.
First panel expanded by default.

**Bronze budget:** the drawn rule plus the **active** numeral — two, exactly at §2's cap.
**Inactive numerals are `{colors.on-dark-soft}`, never bronze**; three bronze slivers would put
four bronze elements on screen.

**Motion.** Panel redistribution `flex-grow` 620ms `{motion.ease-inout}` is the section's one
animated element. Image settle `scale(1.05) → scale(1)` over `{motion.t-slow}`. Type crossfade:
vertical name out over `{motion.t-fast}`, horizontal name and description in on an 80ms delay,
opacity only. Bronze rule draws `scaleX(0) → 1` over `{motion.t-base}` on a 120ms delay.
`prefers-reduced-motion`: transitions instant, image at `scale(1)`, rule at full width.

**Below 1025px** the same louver rotates to horizontal: collapsed rows 76px with the image behind
at `opacity: .14` and the name set horizontally, expanded row 380px. Driven by tap, no hover
dependency.

*Implementation note.* Pure CSS via `:has()`, carrying no JavaScript. Panels are `<button>`s rather
than links — a tap must expand the panel, and an anchor would navigate away instead — so keyboard
focus drives exactly the same state as the pointer through `:focus-within`, and the section is
identical with JS disabled.

**`practice-index`** — *Superseded by `{component.practice-louver}` on 2026-08-06; not
instantiated.* A typographic index driving a single image plate.

*Why.* The card grid failed **structurally, not cosmetically**: four mismatched stock photographs
on screen simultaneously read as a stock library whatever grade was applied to them. Duotoning made
it worse by mapping bronze — a signal colour — across a full luminance range, so the photographs
read brighter than the header's bronze CTA and inverted the page's hierarchy. **A signal colour
cannot also be a surface.** Only one image is on screen at a time here.

Two columns. Left ≈55%: the practice-area names stacked at `{typography.display-l}` on
`{colors.stone-deep}`, divided by `{component.rule-cut}`, each with a one-line description beneath
at `{typography.body-s}`. Right ≈45%: a single image plate, full section height, `{rounded.none}`.

The active name is `{colors.on-dark}` with a 2px `{colors.bronze}` rule at its left edge; inactive
names are `{colors.on-dark-soft}` with no rule. Hover or focus makes a name active and crossfades
the plate to its photograph over `{motion.t-base}` — **opacity only, no transform**. First item
active by default. Exactly one name is ever active, so exactly one bronze rule is ever on screen.

**Grade:** one consistent desaturation and contrast across every image. **No duotone, no scrim, no
text over image.**

Below 1025px it collapses to a single column — image plate above its own name and description,
stacked in sequence, with no hover dependency and every image simply visible.

*Implementation note.* The crossfade is pure CSS (`:has`), carrying no JavaScript at all. The
section is therefore legible and usable with JS disabled by construction rather than through a
fallback path, keyboard focus drives exactly the same state as the pointer via `:focus-within`, and
it adds nothing to the §5.6 motion budget.

**`practice-card`** — *Superseded for #9 by `{component.practice-index}` on 2026-08-06. Retained as
a defined component; not currently instantiated anywhere.* Photograph with a `{colors.stone-deep}` scrim from 55% opacity at the base to
transparent at 45% height. `{rounded.none}`. Title in `{typography.display-m}` `{colors.on-dark}`
with a 24px `{component.rule-bronze}` above it, one-line description in `{typography.body-s}`
`{colors.on-dark-soft}`. Hover: image scales 1.0 → 1.03 over `{motion.t-base}`; bronze rule extends
to 48px. No shadow, no lift.

**`sequence-step`** — The numbered progression unit. **Amended 2026-08-06 (second revision).**

Was: a 48px numeral sitting left, with the connector on the left edge and text to its right. That
was rejected under §4 RULE 3 — it is the rejected build's own composition (a narrow left-aligned
numbered column) with a rail added, and adding a rail is polish, not structural change.

Now a **centred alternating timeline**. The connector runs down the **centre of the container**,
not the left edge. Steps alternate across it — 01 left, 02 right, 03 left — each with its numeral
**adjacent to the rail** and its text running **outward**, away from the rail. The numeral is
`clamp(64px, 7vw, 120px)` in `{colors.bronze-ink}`: at that scale it is the section's structural
device, not a marker beside a paragraph. Title in `{typography.display-s}`, body in
`{typography.body}`. Heading and lede sit **above** the timeline, never beside it — a heading
column with content alongside is archetype A, which §4 Rule 2 bans outright.

The rail **draws progressively on entry**, segment by segment as each step arrives — that
animation is the point of the archetype (§5.4).

Below 1025px it collapses to a **single left-rail column** with every step on one side.

**`index-column`** — Compact multi-column link list for directory content. Items in
`{typography.body-s}`, 12px row rhythm, separated by `{component.rule-cut}`. 3 columns desktop,
2 tablet, 1 mobile. Hover: text shifts to `{colors.bronze-ink}`.

**`accordion-row`** — Question in `{typography.display-s}` `{colors.ink}`, a +/− mark at the right
edge that **rotates 45°** rather than swapping glyphs. Body reveals with a height transition over
`{motion.t-base}`. Rows divided by `{component.rule-cut}`. One open at a time.

**`inline-callout`** — Short emphasis block: 3px left `{colors.bronze}` border, 20px left padding,
text in `{typography.body}` weight 600. Used for phone-number prompts inside body copy.

**`resource-row`** — Document icon, title in `{typography.body}` weight 600, description in
`{typography.body-s}` `{colors.ink-soft}`, right-aligned arrow. Top and bottom
`{component.rule-cut}`. Arrow translates 4px right on hover.

### Forms

**`text-input`** — `{colors.stone-light}` fill, 1px `{colors.rule-cut}` border, `{rounded.xs}`,
height 56px, padding 14×16px. Label above in `{typography.label}` `{colors.ink-soft}`. On focus the
border becomes 2px `{colors.bronze}` — **no glow, no ring, no shadow.** Error: border
`{colors.error}`, message beneath in `{typography.body-s}`.

**`textarea`** — As `{component.text-input}`, min-height 140px.

**`form-panel`** — `{colors.stone-light}` surface, 1px `{colors.rule-cut}` border,
`{rounded.none}`, 48px padding desktop / 24px mobile. Heading in `{typography.display-m}` centered,
fields stacked full-width, `{component.button-primary}` full-width at the base.

### Structural

**`cta-band`** — Full-width `{colors.stone-deep}` strip, 120px tall. Heading in
`{typography.display-m}` `{colors.bronze}` left, `{component.button-call}` right. No entrance
animation — it is punctuation. Top and bottom 1px `{colors.bronze}` hairline.

**`preloader`** — `{colors.stone-deep}` full-bleed field carrying the centered logo mark.
Choreography in §5.2. Homepage only, session-flagged.

**`footer`** — `{colors.stone-black}` surface, 96px top padding. Centered brand logo above a
`{component.rule-cut}`, then four link columns in `{typography.body-s}` `{colors.on-dark-soft}`
with `{typography.label}` `{colors.bronze}` column heads. Legal band beneath in
`{typography.body-s}`, `{colors.on-dark-soft}` at 60%.

---

## 4. THE ARCHETYPE SYSTEM ★ GOVERNING LAW

Each section is assigned one archetype, derived from **what its content is** — never from what it
currently looks like.

| Code | Archetype | Composition |
|---|---|---|
| ~~**A**~~ | ~~Split-editorial~~ | **BANNED — zero uses.** Left heading + rule, right body/rows. This is the composition the CD rejected; see Rule 2. |
| **B** | Full-bleed grid | Edge-to-edge cards or figures, heading above, no side column |
| **C** | Centered statement | `{layout.container-narrow}`, centered, generous air, nothing else |
| **D** | Image-dominant | Photograph carries it; text overlaid or beneath |
| **E** | Numbered sequence | A designed progression — connected, not a list |
| **F** | Dense wall | Many small units at once: reviews, badges, index |
| **G** | Band | `{component.cta-band}` |

### THE THREE RULES

> **RULE 1 — No archetype appears in two consecutive sections.**
>
> **RULE 2 — Archetype A is BANNED. Zero uses on this page.**
>
> **Amended 2026-08-06.** Was "at most twice." A *is* the composition the Creative Director
> rejected — the bronze rule, the stacked serif heading left, the body column right, eight times
> over (§1). His test for "redesigned" is **structural change, not polish**, and a page that still
> opens two of its sections with the rejected composition has not passed that test regardless of
> how well those two are executed. Rationing a rejected layout is still shipping it. There is no
> budget and no exception: if a section seems to need A, it has been assigned the wrong archetype.
>
> **RULE 3 — No section may reuse the composition it had in the rejected build.**
> If the new treatment resembles the old one, it is wrong by definition.

These are acceptance criteria. A build violating any of them is rejected before review.

---

## 5. MOTION

The Creative Director's benchmark site was praised because **scrolling through it feels
satisfying.** Motion is half of what "premium" means to this reviewer. But scattered effects are
the fastest way to look AI-generated. The law: **one orchestrated moment, then quiet, disciplined
consistency.**

### 5.1 Physics

```yaml
motion:
  ease-out:   "cubic-bezier(0.22, 1, 0.36, 1)"    # reveals, entrances
  ease-inout: "cubic-bezier(0.65, 0, 0.35, 1)"    # transforms
  t-fast:  "180ms"    # hover, focus, small state
  t-base:  "420ms"    # reveals
  t-slow:  "900ms"    # landmark moments
```

**Banned:** bounce/elastic easing, default `ease-in-out`, durations over 1000ms, anything that
delays reading. Motion should feel engineered, not playful.

### 5.2 The orchestrated moment — preloader (brief-mandated)

```
0ms      stone-deep field, full bleed
200ms    logo fades in centered — t-slow, ease-out
900ms    logo settles; bronze hairline draws outward from center
1300ms   field lifts, revealing the hero already in place
```
Total ≤ 1.8s. Homepage only. Session-flagged. Hero image preloads behind the field so LCP is never
blocked.

### 5.3 Scroll reveal — one rule for the entire page

- Transform and opacity only. **Never** animate layout properties.
- `translateY(24px) → 0`, `opacity 0 → 1`, `{motion.t-base}`, `{motion.ease-out}`
- IntersectionObserver at 15% entry. **Fires once** — never re-animates on scroll-up.
- Stagger children 60ms, capped at 6. Grids reveal by row, not by cell.
- Headings lead; body follows 120ms. Nothing reveals later than 500ms.

### 5.4 Motion per archetype

| Archetype | Motion |
|---|---|
| ~~**A**~~ | *Inapplicable — A is banned (§4 Rule 2). Row kept only so the table stays a complete key to the archetype letters.* |
| **B** | Row-staggered reveal. Settlements: count-up (§5.5) |
| **C** | Reveal only. Silence is the treatment. |
| **D** | Image scales 1.06 → 1.0 over `{motion.t-slow}` on entry. No parallax. |
| **E** | The connector line **draws** as the section enters — that is the archetype |
| **F** | Marquee continuous; review grid reveals as a block, not per-card |
| **G** | None. Punctuation. |

### 5.5 Signature motion — the settlements counter

- Figures count 0 → value over 1400ms, `{motion.ease-out}`, once, at 30% entry
- Real format (`$2,400,000`), tabular numerals so width never jitters
- Staggered 120ms so they land in sequence, not together
- `prefers-reduced-motion`: final values render immediately
- **Nothing else on the page counts, pulses, or draws attention this hard**

### 5.6 Hard limits

- **Maximum one animated element per viewport** at any scroll position
- No parallax on more than one section. No scroll-jacking, cursor followers, or text scrambles.
- Content legible and usable if JS fails
- `prefers-reduced-motion: reduce` → reveals instant, counters final, marquee stopped. Ship it,
  don't retrofit it.
- Motion JS ≤ 8KB. IntersectionObserver + CSS transitions. No animation library.

---

## 6. HARD CONSTRAINTS

| Constraint | Source |
|---|---|
| **Hero is LOCKED** — layout, copy, image, type untouched | Creative Director |
| Preloader **homepage only** | Client brief + CD |
| Logo **centered and prominent** — firm brand, not a small header mark | Client brief |
| **No attorney portraits on the front page** | Client brief |
| Palette and fonts from §2 only | Client brief |
| Body copy locked — no rewriting | Project rule |
| Mobile-first | Client brief |
| Fully custom-coded, no page builder | Client brief |
| Section inventory client-approved — may be cut or merged, never added to | Client brief |

---

## 7. SECTION MAP — CLEAN SHEET

Content is fixed. **Every treatment is new.** Build grouped by archetype.

| # | What the section must say | Archetype | Direction |
|---|---|---|---|
| 1 | Preloader | — | `{component.preloader}` |
| 2 | **Hero** | **LOCKED** | Untouched. Extract its scale and confidence as DNA for what follows. |
| 3 | **Header** | — | `{component.site-header}` — design from zero. First thing the CD rejected. |
| 4 | Credentials | F | `{component.badge-marquee}` |
| 5 | Who the firm is + where | **C** | **The page's typographic statement.** Reassigned A → D → C; C assigned 2026-08-06. Type-dominant with **no photograph at all**, and the deliberate counterweight to #9: #9 is image-dominant with type as caption, so scrolling between them changes register. One `{colors.stone-deep}` ground, `{typography.display-xl}` heading, body in two `column-count` columns, and `{component.rule-cut}` hairlines as the only structural device. As D it was the third image-dominant section on the page, which rebuilt the monotony §1 exists to remove; the assigned photograph was also wrong on content — generic corporate glass towers against copy that is entirely Long Island. **No photography debt** — the section no longer wants an image. |
| 6 | No fee unless we win | G | `{component.cta-band}` |
| 7 | **$100M+ in settlements** | **B** | **Page landmark.** `{component.figure-cell}` grid on the dark field. The signature. |
| 8 | Why clients choose GB | C | Four commitments as centered statements — NOT a two-column row list |
| 9 | Practice areas | D | `{component.practice-louver}` — expanding louver, exactly one panel open. Third structure here: the card grid read as a stock library, the index-and-plate layout was rejected. Panel order puts the muted head-on shot first and the blue car last, whose saturation fights the navy ground. |
| 10 | Types of case handled | F | `{component.index-column}` — this is a directory, not a section |
| 11 | Google reviews | B | `{component.review-summary}` + `{component.review-card}` grid, dense |
| 12 | No fee unless we win | G | `{component.cta-band}` |
| 13 | Case evaluation form | C | `{component.form-panel}` |
| 14 | **What to do after a crash** | **E** | **Second landmark.** `{component.sequence-step}` with the drawn connector |
| 15 | Trip-and-fall / premises | **F** ⚠ | **The page's pivot.** Reassigned D → F 2026-08-06. Everything above this section is roads; this is where the site widens to property, and the old build gave no signal that the subject had changed. `{colors.stone-pale}` ground marks the change of chapter. Heading `{typography.display-l}`, a 68ch lede, then the premises-liability paragraph at `{typography.body-lead}` filling the container — that upsize is the point, it is the densest legal reasoning on the page and at `{typography.body}` in a narrow column nobody read it — closed by the CTA over a `{component.rule-cut}`. **No photography debt:** `winter.jpg` carried a Boston MBTA bus and illustrated nothing in the copy, so the image was removed rather than replaced. ⚠ Two open notes beneath the sequence check: the ground-rhythm breach, and the archetype letter. |
| 16 | Where we work — Long Island | B | Local knowledge is the differentiator. Render the geography, don't describe it. |
| 17 | ~~Third CTA band~~ | **CUT** | Third identical band |
| 18 | ~~Experienced advocates~~ | **MERGE into #5** | Duplicate content |
| 19 | FAQ | **F** | Two-column dense accordion wall of `{component.accordion-row}` — six on the homepage, not twelve. Reassigned from A 2026-08-06. §3's "one open at a time" governs the **whole wall**, not each column. |
| 20 | Talk to our attorneys | C | `{component.form-panel}` on the dark field |
| 21 | Footer | — | `{component.footer}` |

**Archetype A: 0 uses — banned (§4 Rule 2).**

**Sequence check** (sections 4→20 in render order; 17 is cut and 18 merges into 5, so 16 is
adjacent to 19):

```
 #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15 #16 #19 #20
  F   C   G   B   C   D   F   B   G   C   E   F   B   F   C
```

**F C G B C D F B G C E F B F C** — 14 transitions, no adjacent repeats ✔
Distribution: C×4, F×4, B×3, G×2, D×1, E×1, **A×0**.

Amended 2026-08-06, twice. **#5 D → C:** Rule 1 holds at both joins — #4 is F, #6 is G.
**#15 D → F:** Rule 1 holds at both joins — #14 is E, #16 is B. Rule 2 is untouched in
both cases; A stays at zero. C and F at four uses each break no rule — only A is capped —
and both are spread with at least two sections between consecutive uses (C: #5, #8, #13,
#20; F: #4, #10, #15, #19).

**D falling from three uses to one is the whole point of both changes, not a side effect.**
D ran #5, #9, #15 — three image-dominant sections, which is the compositional monotony §1
exists to eliminate. Neither #5 nor #15 was given a different photograph; both had the
photograph removed, because in both cases the image was the problem. #9's louver is the
page's single remaining D and the only section where a photograph does real work.

> ⚠ **GROUND-RHYTHM BREACH INTRODUCED BY #15, NOT YET RESOLVED.** §2 permits at most two
> consecutive pale sections. With #15 on `{colors.stone-pale}` the rendered page runs
> **four**: #13 (form) → #14 (sequence) → #15 (pivot) → the legacy "What to Expect"
> section. Measured against this table alone — which does not contain that legacy section —
> it is still **three**: #13 → #14 → #15. Either way it exceeds the limit. #15's pale
> ground is load-bearing for the pivot and is not the part to change.
>
> ⚠ **#15'S ARCHETYPE LETTER NO LONGER DESCRIBES ITS COMPOSITION.** F was assigned because the
> section carried a five-item ruled hazard band — many small units at once, which is what F is.
> **That band was cut on 2026-08-06**, one pass after it was built: repeating the paragraph's own
> opening five hazards directly above the sentence containing them read as a table, not as
> structure. What remains is heading, lede, one long paragraph, rule, CTA — no small units at all,
> so nothing about it is a dense wall.
>
> **Proposed, not applied — reassign #15 to C.** By the same reading applied to #5, it is a
> type-only statement with generous air and nothing else. Rule 1 still holds: #14 is E, #16 is B,
> and the nearest other C (#13) is separated by #14. It would put C at five uses and F back to
> three, which breaks no rule since only A is capped. Left for the CD: the letter is governing law
> and reassigning it twice in two passes is a decision, not a cleanup. The row above is marked ⚠
> and its description has been corrected to what is actually built.
>
> **Proposed fix, not applied — give #13 the dark field.** §7 already assigns #20 the same
> `{component.form-panel}` "on the dark field", so a dark form-panel is a defined variant
> and not an invention; two identical form panels on identical grounds is its own
> repetition problem, and differentiating them fixes both at once. That yields dark → pale
> → pale, exactly two. **Alternative:** give #14 the dark field instead, which fits §2's
> "the dark field marks the page's landmarks" more literally since #14 *is* the second
> landmark — but #14's drawn connector already has contrast decisions tuned for the pale
> ground and would need reworking. A separate pre-existing three-run also stands
> downstream at #16 → "advantage" → #19, untouched by this change.

### Minimum viable delivery if time runs out
**#3 header, #7 settlements, #14 sequence.** These three carry the redesign.

---

## 8. RESPONSIVE

| Breakpoint | Width | Key changes |
|---|---|---|
| mobile | < 640px | 1 column everywhere. Header logo 128px. `{component.sticky-call-bar}` active. Figures at clamp minimum. Section padding 88px. |
| tablet | 640–1024px | 2-column grids. Header logo 150px. Split-editorial collapses to stacked. |
| desktop | > 1024px | Full spec. 3-column grids. Container 1200px. |

**Touch targets:** minimum 48×48px on every interactive element.
**Mobile-first is a brief requirement** — design each section at 375px before desktop.

---

## 9. ACCEPTANCE GATE

**Composition**
- [ ] No archetype repeats consecutively
- [ ] **A used ZERO times** — banned outright (§4 Rule 2, amended 2026-08-06)
- [ ] ≤ 2 consecutive pale grounds
- [ ] **No section resembles its treatment in the rejected build**
- [ ] Scrolling the page, no two screens look like the same screen

**System integrity**
- [ ] Every element maps to a component in §3 — nothing invented
- [ ] No box-shadow anywhere
- [ ] No radius above 2px
- [ ] ≤ 2 bronze elements per viewport
- [ ] No one-off type sizes — everything from §2

**Anti-generic (§11)**
- [ ] No decorative icons beyond the five permitted glyphs
- [ ] At least three sections break perfect symmetry
- [ ] Section density varies — landmarks breathe, directories run tight
- [ ] Every photograph is Long Island specific, or duotoned
- [ ] One element removed from each section as a final pass

**Motion**
- [ ] One orchestrated moment (preloader); everything else quiet and consistent
- [ ] One animated element per viewport maximum
- [ ] Reveals fire once, never re-trigger
- [ ] `prefers-reduced-motion` fully respected
- [ ] Legible and usable with JS disabled

**Ten-second test**
- [ ] Scroll top to bottom in ten seconds — does at least one moment feel *designed* rather than formatted?
- [ ] Would this sit believably beside the agency's other injury sites?

**Brief compliance**
- [ ] Logo centered and prominent
- [ ] No attorney portraits on front page
- [ ] Preloader homepage only
- [ ] Hero untouched
- [ ] Verified at 375px, not only desktop
- [ ] Visible keyboard focus everywhere — 2px bronze outline, 2px offset

---

## 10. BUILD DISCIPLINE

1. **Two-iteration cap.** Wrong twice = the archetype assignment is wrong, not the execution.
   Return to §7. Do not sand a third time.
2. Screenshot every archetype pass — desktop and 375px.
3. **impeccable runs after building, as a critic against this spec.** Its approval is not the bar.
4. **Never full-site review.** Header + settlements first, alone.
5. Nothing built after midnight ships without a morning re-check.

---

## 11. ANTI-GENERIC LAW

This palette and typeface pairing (inscriptional serif + gold + navy) is a known cliché cluster
for law firms. The palette is brief-mandated and cannot change — so the escape from generic must
come from **composition, evidence and specificity**, never from color or ornament.

**11.1 — Almost no icons.** The only glyphs permitted on this page: the arrow in
`{component.resource-row}`, the +/− in `{component.accordion-row}`, the 3-line nav mark, stars in
`{component.review-card}`, and the Google mark. **No decorative icon sets. No outline icons above
section headings.** A generic icon library is the fastest AI tell there is.

**11.2 — Deliberate asymmetry.** Do not center everything. At least three sections must break
perfect symmetry: a heading that sits off the container's centre line, a figure that breaks the
container edge, or a grid with an intentionally uneven column split (e.g. 5/7 rather than 6/6).
Perfect balance everywhere reads as generated, not composed.

**11.3 — Vary section density.** Not every section gets the same padding. Landmarks (#7, #14) get
the full `{spacing.section}`; the directory (#10) and the bands (#6, #12) run visibly tighter.
Uniform rhythm top to bottom is the same failure as uniform layout.

**11.4 — Specificity beats decoration.** Where a section can name a real place, a real number, a
real client, or a real road — it does. "Rear-end collision, Long Island Expressway" is worth more
than any ornament. This is the client's genuine advantage and the strongest anti-generic device
available.

**11.5 — Photography must be real.** No generic stock crash imagery. Long Island specifically:
the LIE, Sunrise Highway, Nassau/Suffolk streetscapes, the courthouse. If only generic stock is
available, prefer a duotone treatment in `{colors.stone-deep}` and `{colors.bronze}` over a
literal full-color stock photo.

**11.6 — Remove one thing.** Before declaring any section done, delete its least necessary
element and check whether the section got worse. If it didn't, leave it deleted.

---

## 12. KNOWN GAPS

- **Brand prominence sits with the hero, not the header.** The client brief's "logo centered and
  prominent" (§6) is satisfied by the locked hero's full-scale lockup, which is the first thing
  every visitor sees. `{component.site-header}` is a 72px utility bar that does not appear until
  the hero has left the screen, and its 52px mark is a wayfinding mark rather than the brand
  statement. Recorded 2026-08-06 so the §6 constraint is not read as unmet at review.
- Settlement figures are placeholders pending verified case results from the client
- **No section awaits photography.** Both outstanding debts are **closed, not deferred**: the
  2026-08-06 reassignments removed the images rather than replacing them, so there is nothing to
  source. #5 → C dropped `towers.jpg` (Manhattan corporate glass against Long Island copy); #15 → F
  dropped `winter.jpg` (a Boston MBTA bus with legible destination signage, illustrating none of
  the icy walkways or wet floors the copy describes). Neither file has any consumer on the page.
- **Ground rhythm is in breach at #13–#15** — see the ⚠ note under §7's sequence check. A fix is
  proposed there and has not been applied.
- Practice-area inner-page template is a **separate deliverable** — not built until the homepage
  direction is approved
