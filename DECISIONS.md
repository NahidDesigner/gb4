# DECISIONS

## 2026-08-06
- Clean-sheet redesign; hero locked, section inventory locked, copy locked
- Archetype system adopted — A capped at 2 uses (see DESIGN.md §4)
- Settlements (#7) is the page signature; #14 sequence is second landmark
- Sections 17 and 18 cut
- Practice-area template deferred until homepage direction is approved
- No shadows, radius ≤2px, ≤2 bronze elements per viewport

### Amendments — build pass 1 (preloader, header, settlements)

- **Fonts.** `source-sans-3-latin-400/600-normal.woff2` added to `assets/fonts/`. Only the 800
  face existed, so every §2 body style resolved to it and rendered bold. Faces are declared in
  `design-system.css`, not `styles.css`, so the other 22 pages are untouched.
- **DESIGN.md §3 `site-header` — amended.** Header is absent over the hero and slides down solid
  on hero exit; never on screen at the same time as the hero, which carries its own brand lockup
  and nav controls. Bar is 72px desktop / 64px mobile, and the logo is now sized by **height**
  (52px / 44px) rather than width. *Why:* every logo asset is 560×406, so the old 180px-wide rule
  computed to 131px tall and overflowed the bar onto the content below — the width rule was not
  buildable with the available assets.
- **DESIGN.md §12 — added.** Brand prominence is carried by the hero, not the header bar, so the
  §6 "logo centered and prominent" constraint is not read as unmet at review.
- **DESIGN.md §2 bronze law — amended.** The two-per-viewport cap now applies to section content
  only; persistent chrome (header call button, sticky call bar) is exempt. *Why:* the fixed header
  CTA is in every viewport, so it spent one of every section's two slots page-wide and made the
  cap unsatisfiable. Settlements landmark stays bronze.
- **DESIGN.md §2 `typography.figure` — amended** 76px → 87px at the desktop maximum (+15%), with
  the vw term 5.5 → 6.3. *Why:* at 1440px the old ceiling was already binding, so raising the
  ceiling alone would have moved the rendered size 4%, not 15%.
- **Settlements landmark is sticky** above 1025px — the "$100M+ / Settlements" block pins while
  the figure cells scroll past, releasing at the section end. Static below 1025px, where the grid
  is single-column and pinning would cover the cells it introduces.
- **Hero bottom scrim added.** A stone-deep gradient rising from the hero's base so it blends into
  `.creds` instead of cutting hard. *Note:* the hero is LOCKED (§0/§6) — this adds no element to
  the hero and changes none of its layout, copy, image or type. It is a pseudo-element authored in
  the design-system layer and lifts out by deleting one block. Final gradient stop is
  **stone-black**, not stone-deep, because `.creds` is `#06101F`; ending on stone-deep would have
  left a step exactly where the amendment exists to remove one.
- **Not instantiated, deliberately:** `nav-overlay` (the existing drawer serves it, driven by
  `app.js`) and `sticky-call-bar` (the existing `#actionbar` serves it). Adding either would
  duplicate a working control.

### Amendments — build pass 2 (settlements proof density)

- **Settlements reworked for proof density.** The right column is now a **two-column grid of 14
  `figure-cell`s**, not five stacked rows. *Why:* five rows undersold the $100M+ claim — the
  section's job is density, and density is a count, not a point size.
- **DESIGN.md §2 `typography.figure` — amended again** to `clamp(28px, 3.2vw, 44px)` (was
  `clamp(40px, 6.3vw, 87px)`, itself amended earlier the same day). Impact now comes from
  quantity, so the figure steps down to sit in a dense grid without crowding.
- **DESIGN.md §3 `figure-cell` — amended.** Two-column grid of 12–16, collapsing to one column
  below 1025px. The no-card rule is unchanged and is load-bearing at this quantity: 14 bordered
  boxes would read as a pricing table. Separation stays `rule-cut` alone — no cards, no shadows,
  no gradients.
- **Counter timing — amended.** Stagger 120ms → **60ms**, per-figure duration 1400ms → **680ms**,
  so the full sequence closes at ~1.46s. *Why:* this supersedes §5.5's 1400ms for this component.
  At 14 cells the old timings put the last figure starting at 1.56s and finishing at 2.96s,
  nearly double the 1.6s budget.
- **Case-count line added** beneath the subhead so the sticky left block earns its height and the
  dead space beside a taller grid closes.
- **⚠ Cells 6–14 are invented placeholders.** Nine settlement amounts were fabricated to build the
  grid density. They are **not client-supplied**. Settlement figures are regulated
  attorney-advertising claims — every one must be replaced with a verified case result or deleted
  before launch, and the same is still true of the original five. Marked in `index.html` with a
  warning comment; the on-page disclaimer covers all fourteen. This raises the launch-blocking
  exposure recorded in DESIGN.md §12 from five fabricated figures to fourteen.

### Amendments — archetype A banned

- **DESIGN.md §4 Rule 2 — amended.** Archetype A goes from "at most twice" to **banned outright,
  zero uses**. *Why:* A is the composition the CD rejected — bronze rule, stacked serif heading
  left, body column right, eight times over. His test for "redesigned" is structural change, not
  polish, and a page still opening two sections with the rejected composition fails that test
  however well those two are executed. Rationing a rejected layout is still shipping it.
- **§4 archetype table and §5.4 motion table** — the A rows are struck through and marked
  inapplicable rather than deleted, so the tables remain a complete key to the letters.
- **§7 reassigned.** Section **#5** (who the firm is + where) A → **D**. Section **#19** (FAQ)
  A → **F**, as a two-column dense accordion wall; §3's "one open at a time" governs the whole
  wall, not each column.
- **Rule 1 re-verified across the full sequence.** Final archetype string, sections 4→20 in render
  order (17 cut, 18 merged into 5, so 16 is adjacent to 19):
  **`F D G B C D F B G C E D B F C`** — 14 transitions, zero adjacent repeats.
  Distribution B×3, C×3, D×3, F×3, G×2, E×1, A×0.
- **§9 acceptance gate** updated from "A used ≤ 2 times" to "A used ZERO times".
- **New photography debt (§12).** #5 as archetype D needs a photograph and has none. It must be a
  **place, not people** — §6 bans attorney portraits on the front page, so the two team images in
  `assets/` are ineligible despite being the obvious "who the firm is" shot. Two sections now
  await photography (#5 and #15), not one.
- **No code change.** None of the three built sections carries an archetype: the settlements
  landmark is B and unaffected; preloader and header have no archetype. This pass is spec-only.

### Amendments — settlements landmark corrections

- **Case-count line removed.** It was new copy and this project's copy is locked. Reverses the
  addition made earlier the same day.
- **Figures sorted strictly descending**, filling left-to-right across the two columns
  ($2,400,000 → $430,000; grid is row-major so DOM order is the fill order). Verified
  programmatically as strictly descending.
- **Cap-height alignment.** The grid's first rule now aligns to the cap height of the $100M+
  figure rather than its line-box top. Offset measured, not guessed: at the desktop clamp the
  figure is 100.8px Cinzel on a 102.82px line box, so half-leading is negative (−16.09px) and the
  glyph ascent sits 18.57px below the font ascent, leaving the cap 2.48px down. Residual
  misalignment after the fix: **0.01px**.
- **Row rhythm equalised.** `figure-cell__case` reserves two lines (`min-height: 2.8em`) whether
  the label wraps or not. The grid alone only equalises the row *box*; it does not align content
  *inside* the cells, so a one-line label beside a two-line one still threw the detail lines out of
  step. Verified: detail lines share a top edge in all 7 rows.
- **CTA moved into the left block** beneath the subhead. This supersedes the earlier client note
  about the CTA sitting "under the register and above the regulated note" — that note no longer
  describes the layout, since the regulated note is also gone from the section. The stale comment
  was replaced rather than left in place.
- **⚠ Visible "Placeholder figures" disclaimer REMOVED from the section, on instruction.**
  - *Retained:* the site-wide footer disclaimer — "Attorney Advertising. Prior results do not
    guarantee a similar outcome." The regulated language is unchanged and still on every page.
  - *Lost:* any on-page indication that these specific figures are illustrative and pending
    verified results. That wording exists nowhere else in the site. **Fourteen fabricated
    settlement amounts now present to visitors as genuine case results.**
  - The only remaining in-page record is an HTML comment at the former disclaimer's location.
  - This does not change the legal disclaimer position; it changes whether the numbers are
    marked as invented. Replace every figure with a verified result, or delete the section,
    before launch. Cross-referenced in DESIGN.md §12.
- **Left-column dead space is NOT meaningfully closed.** The CTA move was near height-neutral —
  removing the case-count line (~40px) and adding the CTA (~45px) left the landmark at 333px
  against a 1159px grid. The block is sticky so it travels rather than sitting as a static hole,
  but the in-viewport emptiness beneath it is essentially unchanged from before this pass.

### Amendments — intra-cell rhythm

- **`min-height: 2.8em` on `figure-cell__case` removed.** It was added a pass earlier to hold row
  rhythm, but it reserved two label lines *inside the label box*, which parked the slack **below**
  the label. In one-line cells that inflated the label→detail gap to ~21px — wider than the 12px
  figure→label gap above it, and the direct cause of the loose intra-cell rhythm.
- **Slack moved above the label** via `margin-top: auto` on `figure-cell__case`. The cell is a flex
  column whose height the grid row already equalises, so this pins the label + detail pair to the
  cell's base and pushes any surplus into the larger of the two gaps.
- **Result, measured across all 14 cells:** label→detail is **4px everywhere**; figure→label is
  **12px** in 11 cells and **28.8px** in the three that sit beside a wrapping neighbour (#3, #9,
  #11 — 12px plus exactly one 16.8px label line). Label→detail is tighter than figure→label in
  every cell. Detail lines share a baseline in all 7 rows, and amounts stay aligned per row too.
  At 375px the grid is single-column so no cell has a neighbour: gaps are a uniform 12/4 throughout.
### Build pass 3 — section #14, "What to do after a crash" (archetype E)

- **Built clean-sheet with `sequence-step`.** The rejected build set this as a plain `<ol>` of
  number + heading + paragraph inside the narrow read column, with **no connector at all** —
  §7's "numbered text list", which RULE 3 forbids reusing. The progression here is three things
  the old treatment did not have: a shared vertical axis, 48px structural numerals, and the
  connector drawing as the reader descends.
- **Copy unchanged.** All seven steps, the heading, the lede and the closing line are carried over
  verbatim; no new copy. The client-requested mynyaccident.com link is preserved and rebuilt as
  §3 `resource-row`.
- **§11.1 — zero icons in this section.** The numerals carry the wayfinding and are structural,
  not ornament. They are `aria-hidden` because `<ol>` already conveys order to assistive tech, so
  exposing "01" would announce the sequence twice. The only `<svg>` in the section is the
  `resource-row` arrow, which §11.1 permits by name.
  - **§3/§11.1 conflict resolved toward §11.1.** §3 describes `resource-row` as carrying a
    document icon, but §11.1's permitted-glyph list is exhaustive and admits only the *arrow*
    from that component. The document icon the old markup used (`#i-doc`) is dropped.
- **§5.4 connector draw** runs on its own observer (`[data-ds-draw]`), deliberately not routed
  through the §5.3 reveal system: `.ds-reveal` would fade and lift the step as well as draw its
  line, putting two animated things in one viewport against §5.6. Each step draws as it enters, so
  the progression builds under the reader. Verified animating rather than toggling — intermediate
  scaleY frames 0.718 → 0.948 → 0.994 → 1. Collapsed state is JS-gated, so a failed script leaves
  every connector drawn.
- **Ground: stone-pale.** #13 is pale and #15 is dark, so this is the second of two consecutive
  pale sections — at §2's limit, not over it. stone-pale specifically rather than the stone-mid
  slab, because §3 specifies `bronze-ink` numerals and §2 pins that token to pale (4.9:1); a mid
  slab would have required substituting `bronze-deep`.
- **Axis alignment** corrected by half a pixel (`calc(rail/2 - 0.5px)`) so the 1px connector centres
  on the numeral axis rather than sitting 0.5px off it. Measured delta now 0px on all six
  connectors, desktop and 375px. Step 07 has no connector — nothing follows it.
- **§5.6 motion budget:** ds.js is 7,367 bytes (7.2 KB) against the 8 KB ceiling.
- **Rule 1 re-verified across all sections** after the build — string unchanged from the previous
  pass, since #14 was already E: **`F D G B C D F B G C E D B F C`**, 14 transitions, 0 violations.
  A count 0.
- **Observation, not changed:** at 1440px the section is markedly left-weighted — the step body
  holds a 62ch measure inside a 1200px container, leaving roughly the right half empty. That is
  typographically correct and consistent with §11.3's "landmarks breathe", but it is the same
  left-weighting flagged on the settlements landmark. Narrowing the container for this section
  would make the negative space read as deliberate rather than as a column that ran out.

### Build pass 4 — section #14 restructured as a centred alternating timeline

- **The first #14 build failed §4 RULE 3 and was rejected.** It was a narrow left-aligned numbered
  column with a rail added — structurally the rejected build's own composition. Adding a rail is
  polish, not structural change. This is attempt 2 of the two-iteration cap.
- **DESIGN.md §3 `sequence-step` — amended** to the centred alternating timeline: connector down
  the **centre** of the container, steps alternating across it, numeral **adjacent to the rail**
  with text running **outward**, numeral at `clamp(64px, 7vw, 120px)` in `bronze-ink` as the
  section's structural device. Heading and lede sit **above** the timeline — recorded explicitly,
  because a heading column with content beside it is archetype A and §4 Rule 2 bans it outright.
  Collapses to a single left-rail column below 1025px.
- **Verified at 1440px:** rail sits on the container's centre line with **0px** deviation on all
  seven segments; sides alternate `LEFT,RIGHT,LEFT,RIGHT,LEFT,RIGHT,LEFT`; the numeral is nearer
  the rail than the body in every step (48px vs ~200px), so numerals are adjacent and text runs
  outward; numeral renders 100.8px (7vw, inside the clamp) in bronze-ink; head sits above the
  timeline; no horizontal overflow.
- **Rail draw preserved (§5.4)** and still progressive — collapsed at 0 before entry, intermediate
  scaleY frames 0.644 → 0.922 → 0.988 → 1 on the entering steps while later steps sit at 0.
- **Copy unchanged**, all seven steps verbatim. **No icons** — the only `<svg>` in the section
  remains the `resource-row` arrow that §11.1 permits by name.
- **Two CSS problems found and fixed during verification, worth recording:**
  1. *Media-query order.* The phone-width rules sat **before** the 1024px collapse block. Both
     match at 375px and they share specificity, so the later block silently won and the phone
     layout never applied. Moved after it. Source order, not specificity, was the bug.
  2. *Measure collapse at 375px.* With the numeral beside the body, the 64px clamp floor plus the
     rail left the text at **~23ch** — not a readable measure. The numeral now stacks above the
     body below 640px, which keeps the specified clamp and restores the body to **36ch**
     (307px, uniform across all seven). Still one side of the rail, numeral still against it.
- **§5.6 motion budget:** ds.js unchanged at 7,367 bytes (7.2 KB) of 8 KB — the restructure was
  layout-only, the draw observer did not change.
- **Archetype sequence re-verified:** `F D G B C D F B G C E D B F C` — 14 transitions,
  0 violations, A count 0. Unchanged, as expected: this altered #14's composition, not its
  archetype.
- **Observation, not changed:** on the left-hand steps the text is right-aligned so it mirrors the
  rail. That is the faithful reading of "text running outward" and gives the stronger symmetry,
  but ragged-left body copy is measurably harder to read across three or four lines. Left-aligning
  every step's text would fix the readability at the cost of the mirror.

### Build pass 5 — section #14 closed

- **All step body text left-aligned**, including the left-side steps. Readability over the mirror:
  these paragraphs run three to four lines, and ragged-left copy is measurably slower to read. The
  alternating sides already carry the symmetry. Numerals stay hard against the rail — verified at a
  uniform **48px** from the centre line on every step.
- **Vertical spacing reduced** from `space-xxl` (80px) to `space-xl` (48px). The worst consecutive
  pair falls from 510px to **446px**, and **three** steps now sit inside a 900px viewport, so each
  step is read against its neighbours instead of alone. Two already fitted before the change; the
  problem was that the gap plus the side-to-side jump broke the spine's continuity, not that the
  pair overflowed.
- **Mobile rail made to read.** `rule-cut` on `stone-pale` measures **1.4:1** — below the threshold
  at which a 1px line is perceptible at all, which is why the spine looked absent on a phone.
  Widening would not have helped; the deficit is contrast, not weight. The rail is now
  `ink-soft` at **6.37:1** in the collapsed layout. `bronze-ink` would also have read (4.91:1) and
  would have tied the rail to the numerals, but it counts against §2's two-bronze-per-viewport
  limit and the collapsed layout already shows bronze numerals — so the neutral won. Scoped to
  ≤1024px; at desktop the rail is a long unbroken central spine, reads at `rule-cut`, and §3's
  token stands unchanged.
- **Cinzel has no tabular-figures table.** `font-variant-numeric: tabular-nums` and
  `font-feature-settings: "tnum"` are both applied and both silently ignored — the numerals set
  proportionally at 101.8px for "01" against 125.7px for "06". That 24px spread was moving the body
  edge from step to step, so the newly left-aligned text had no common start (measured starts of
  224 / 209 / 208px in the left column). Fixed with a `1.32em` numeral box — em, so it tracks the
  clamp — with the digits aligned toward the rail. Text now starts at a single x per column
  (**193px** left, **926px** right) while the digits stay against the rail.
- **Draw preserved** — collapsed at 0 before entry, frames 0.642 → 0.922 → 0.988 → 0.999, later
  steps still at 0. Still progressive, still fires once.
- No other section touched. Archetype sequence unchanged: `F D G B C D F B G C E D B F C`.

### Build pass 6 — sections #5, #9 and #15 (archetype D, image-dominant)

- **All three photographs duotoned per §11.5.** Every image in `assets/` is generic stock: the four
  practice images are literally the "generic stock crash imagery" §11.5 bans by name, `towers.jpg`
  is stock corporate, `winter.jpg` is a snowy street carrying a **Boston MBTA bus** ("504 Watertown
  Express"). §11.5's prescribed fallback is a stone-deep/bronze duotone, so that is what they get.
- **Duotone built as an SVG filter, not CSS blend modes.** A true tonal duotone maps the luminance
  ramp onto two arbitrary colours, which `mix-blend-mode` cannot do. `feColorMatrix` flattens to
  luminance, a gamma pass weights the ramp toward the navy end, then `feComponentTransfer` maps
  0 → stone-deep and 1 → bronze-edge.
- **Highlight endpoint is `bronze-edge` #8A6A12, not `bronze` #C9A227.** Both are §2 tokens so no
  colour is introduced, but mapping to full bronze put large flat areas of every image at full
  signal intensity, and §2 is explicit that **bronze never fills large areas** — it is a rule, a
  figure, a button, an underline. bronze-edge keeps §11.5's duotone while leaving the images below
  the intensity reserved for those. Verified visually: the header's bronze CTA now reads brighter
  than any photograph, which is the correct hierarchy.
- **#5 — who the firm is + where.** Full-bleed duotoned band with the heading overlaid, body copy
  beneath. The photograph is a **place, not people**: §6 bans attorney portraits on the front page,
  so `team-buznik.jpg` and `team-gurevich.webp` are ineligible however obvious they look for a
  "who the firm is" section. Closes the §12 photography debt for this section.
- **#9 — practice areas, §3 `practice-card`.** Full-bleed two-column grid, cards at 4/5 so each is
  720×900 at desktop and **one row fills a 900px screen**. That is also what satisfies §2's bronze
  law: each card carries one bronze rule, and four cards in a viewport would be four bronze
  elements against a limit of two for section content. The scale the brief asked for and the bronze
  cap resolve to the same layout. Verified 1 bronze rule in view at 375px, 2 at desktop.
- **#15 — trip-and-fall / premises.** The photograph is the section's **ground**, not a band inside
  it: full-bleed behind the whole section with the copy overlaid on a scrim. Closes the §12
  photography debt recorded for this section.
- **Copy verbatim across all three. No icons** — verified zero `<svg>` elements in any of the three
  sections. The old map-card pin and arrow and the practice tiles' rollover text were dropped, not
  rewritten; the address survives as a `button-text` link.
- **Bug found and fixed during verification:** the practice-card title and description are `<span>`s
  inside an `<a>` and had no `display: block`, so they set on one running line and their vertical
  margins were ignored. Inline-by-default, caught only by looking at the render.
- **Archetype sequence re-verified:** `F D G B C D F B G C E D B F C` — 14 transitions,
  0 violations, A count 0. Unchanged; this realised three existing D assignments.

### Build pass 7 — #9 practice areas, duotone replaced

- **Duotone removed from #9 only.** Confirmed still applied to #5 and #15, which were not touched.
  §11.5 deliberately **not** amended — the spec fix waits until the treatment is proven here.
- **Diagnosis accepted: this was a spec error, not an execution error.** Bronze is a signal colour;
  mapping it across a full luminance range makes it a surface, and a colour cannot be both. The
  earlier `bronze-edge` change only reduced the symptom.
- **New treatment applied as specified:** original photography at `saturate(0.6)` (40% desaturation,
  mid of the 35–45% range) with a stone-deep scrim, bottom-up, `.70` at the base to fully
  transparent at 50% card height. Card sizing, grid and bronze rules untouched.
- **Card titles and descriptions hold contrast** — measured against the actual composited pixels
  behind each text block, not against a nominal background:
  - Titles (large text, AA needs 3:1): mean **9.19–14.38**, worst pixel **3.34–4.22**. Pass.
  - Descriptions (body, AA needs 4.5:1): mean **8.57–14.38**, worst pixel **4.41–9.58**. Pass on
    mean everywhere; the Intersection card touches **4.41** at its single brightest background
    pixel, marginally under 4.5. Noted, not treated — mean contrast there is 8.57.

- **⚠ THE BRIGHTNESS CHECK FAILS. The section is not closed.**
  Header bronze CTA luminance = **0.384**. Share of card pixels above it:

  | Card | % above CTA | mean lum | max |
  |---|---|---|---|
  | Rear-End Collisions | **43.1%** | 0.321 | 1.000 |
  | Head-On Collisions | 16.0% | 0.151 | 0.938 |
  | Distracted Driving | 16.4% | 0.152 | 0.984 |
  | Intersection / T-Bone | 8.6% | 0.163 | 0.985 |

  By **mean** luminance all four sit below the CTA (0.15–0.32 vs 0.384). By **area** they do not,
  and a 720×900 card with 43% of its pixels brighter than a small button still pulls focus first.

  **Desaturation cannot fix this: it removes chroma, not luminance.** Nor can the scrim — 75.7% of
  the offending pixels are in the card's TOP half, where the scrim is transparent by design.
  Measured on the worst card:

  | Variant | % above CTA |
  |---|---|
  | Spec as written | 43.1% |
  | Scrim extended to full height @ .70 | 44.0% (no effect) |
  | + `brightness(0.85)` | 32.4% |
  | + `brightness(0.75)` | 10.6% |
  | + `brightness(0.65)` | **0%** |

  Only a luminance reduction moves it, and it has to reach roughly **`brightness(0.65)`**. That is
  a third filter term beyond the specified treatment, so it has NOT been applied — the spec was
  explicit and adding to it silently is what produced the duotone problem in the first place.

### Build pass 8 — #9 rebuilt as `practice-index`

- **Diagnosis accepted: the failure was structural.** Four mismatched stock photographs on screen
  simultaneously read as a stock library whatever grade is applied. No treatment fixes that; only
  showing one at a time does. The duotone before it compounded the problem by making a signal
  colour into a surface.
- **New component `practice-index` added to DESIGN.md §3; §7's #9 entry reassigned to it.**
  `practice-card` is retained as a defined component but marked not currently instantiated.
- **Built to spec and measured at 1440px:** columns **55% / 45%**; plate flush right and full
  section height (518×1097); `border-radius: 0`; one grade on all four images
  (`saturate(0.55) contrast(1.06)`); zero `<svg>` in the section; no text over image; no scrim.
- **Active state verified by measurement, not by eye.** Default: image 1 visible, one bronze rule,
  name `on-dark`, the other three `on-dark-soft` with rule opacity 0. Stepping keyboard focus
  through all four: **every focus activates its own image**, and across all four states there is
  never more than **one image** and never more than **one bronze rule** on screen. Pointer hover
  confirmed to drive the identical state.
- **Bronze cap:** exactly one rule at any time, against §2's limit of two. Comfortably inside.
- **Crossfade is `opacity 0.42s cubic-bezier(0.22,1,0.36,1)`** — t-base, ease-out, opacity only,
  `transform: none`. It is the section's only animation.
- **JS-disabled requirement met by construction, not by fallback.** The crossfade is pure CSS via
  `:has()`; the section contains zero script tags, zero inline handlers, zero `.ds-reveal`, zero
  `data-ds-*` hooks, and no CSS rule in it depends on the `.ds-js` class. It renders identically
  with JavaScript off. ds.js is unchanged at 7,367 bytes.
  - A `@supports not selector(:has(*))` block drops older browsers to the collapsed layout, where
    every image is visible and every name reads active — degraded, still complete.
- **Collapsed layout below 1025px verified:** single column, `position: static` images, plate above
  its own name and description in document order, every image visible, every name active — no
  hover dependency anywhere. Achieved with one DOM: the images live inside their own `<li>`, so
  the collapsed order is just document order and nothing is duplicated.
- **Bug found during verification:** `.ds-practice-index` carried `position: relative`, which made
  the `<ul>` the containing block and trapped the plate inside the 55% column instead of spanning
  the layout. Removed.
- **Rule 1 / Rule 2 re-verified:** `F D G B C D F B G C E D B F C` — 14 transitions, 0 violations,
  A count 0. #9 remains D, so the sequence is unchanged.
- **Open, unchanged by this pass:** §11.5 still prescribes duotone and is still wrong; it is left
  alone deliberately pending the spec fix. #5 and #15 still carry the duotone filter and were not
  touched. #9 now sits on stone-deep directly above #10, which is also stone-deep — two adjacent
  dark sections. §2 caps consecutive *pale* sections only, so this breaks no stated rule, but it
  blurs the dark field's role as structural punctuation and is worth a look when #10 is built.

### Build pass 9 — #9 rebuilt as `practice-louver`

Third structure for this section. Card grid read as a stock library; index-and-plate rejected.

- **DESIGN.md §3 gains `practice-louver`; §7's #9 entry reassigned.** `practice-index` and
  `practice-card` are both retained as defined components, marked not instantiated.
- **Mechanic reused from the house Bier widget** (flex-grow redistribution, vertical labels, dimmed
  image behind collapsed panels). **None of its surface treatment**: no shadow, no radius, no
  gradient accent bar, no hover translateY, no accordion, no bottom bar, none of its palette.
- **Measured at 1440px:** panel widths **58 / 14 / 14 / 14** in every state; `gap: 2px`; height 648
  (inside the 560–760 clamp); `border-radius: 0` on every element; **0 shadows; 0 `<svg>`**.
- **The crop, verified.** All four images measure **668px layout width = 58cqw**, the expanded
  width, with `overflow: hidden` on every panel — so collapsing crops the photograph rather than
  squashing it. Implemented with container-query units so the pin tracks the container rather than
  a hard-coded pixel value.
- **State machine verified across all five states** (default, focus 2/3/4, blurred): exactly one
  panel expanded, one bronze numeral, one drawn rule, one visible body, three vertical names.
  Keyboard focus drives the identical state as hover. Redistribution measured at
  `flex-grow 0.62s cubic-bezier(0.65,0,0.35,1)`.
- **Bronze cap held at exactly two** — the drawn rule plus the active numeral — in every state.
- **Mobile verified at 375px:** column direction, expanded 380px, collapsed 76px, tap drives the
  state, labels horizontal, collapsed image `opacity: .14`, full-width tap targets, no overflow.
- **Zero JavaScript.** No script tags, inline handlers, `.ds-reveal` or `data-ds-*` hooks in the
  section, and no CSS rule in it depends on `.ds-js`. Identical with JS disabled. A
  `@supports not selector(:has(*))` block renders every panel open and legible for browsers without
  `:has()`. ds.js unchanged at 7,367 bytes.
- **Rule 1 / Rule 2 re-verified:** `F D G B C D F B G C E D B F C` — 14 transitions, 0 violations,
  A count 0. #9 remains D.

**Three judgment calls, all deviations from the brief as written:**

1. **Panel order, not image order.** "Reorder images so the head-on shot is first, the blue car
   last" was applied by reordering whole panels — moving images alone would have captioned the
   head-on photograph "Rear-End Collisions". This contradicts the brief's ASCII diagram, which
   showed Rear-End expanded; the reorder note is the later instruction and carries a reason.
2. **Inactive numerals are `on-dark-soft`, not bronze.** The brief describes collapsed numerals as
   bronze, but its own constraint caps bronze at "the rule plus the active numeral". Three bronze
   slivers would be four bronze elements on screen. The cap won.
3. **Panels are `<button>`s, not links.** "Driven by tap" requires a tap to expand the panel; an
   anchor navigates away instead. **Consequence: the old tiles' link to `#casetypes` is gone.**
   Restoring it would need a visible affordance inside the expanded panel, which is new text — out
   of scope under "copy verbatim". Flagged for a decision.

**Two items not closed:**

- **Text contrast on the expanded panel is marginal at the worst pixel.** Name (large text, AA 3.0):
  mean **12.33**, worst pixel **2.97**. Description (body, AA 4.5): mean **10.81**, worst pixel
  **4.46**. Both misses are under 1% at the single brightest pixel behind the text and the means are
  comfortable, but neither clears AA outright. Deepening the scrim from 78% to ~85% fixes both; the
  brief specifies 78%, so it was left alone.
- **Collapsed-hover (`opacity .18 → .26`) is unreachable on pointer devices** — hovering a collapsed
  panel also expands it, so the image goes to full opacity instead. The rule is implemented and
  correct; it simply has no state in which it can be seen on a mouse. Worth deleting or rethinking.

### Build pass 10 — #9 louver, four execution defects

Concept kept. Flex mechanic, vertical labels, bronze rule and transition untouched — verified after
the fixes: `flex-grow 0.62s cubic-bezier(0.65,0,0.35,1)`, `writing-mode: vertical-rl`, active rule
at `scaleX(1)`, one bronze numeral.

1. **Full-bleed — fixed.** Louver was 1152px inside a 1440px viewport with 99px of dead band
   beneath. Now `left: 0 → right: 1425`, touching both edges, with **0px** dead space between the
   last panel and the section boundary. Done by moving the louver OUT of `.ds-container` and giving
   it `width: 100%` of the section — deliberately **not** `100vw`, which includes the scrollbar and
   would have overflowed the document by 15px. The heading stays inside the container.
   `padding-bottom` on the section is now 0.

2. **The grade was already applied — the premise was wrong.** Computed filter measured
   `saturate(0.55) contrast(1.06)` on **all four** images both before and after this pass, expanded
   included. Nothing was changed. If the expanded image still reads as full-colour, the lever is a
   stronger `saturate()` value, not a missing declaration — 0.55 is a mild desaturation and these
   photographs are saturated to begin with. Flagged rather than silently re-graded.

3. **Collapsed opacity `.18 → .34` — fixed**, and the label contrast verified against the busiest
   image rather than assumed. Worst case is `rear-end-collisions.webp` at **4.99** against a 3.0
   AA large-text threshold; the other two are 6.21 and 15.83. The panels now read as compressed
   photographs.

4. **Mobile collapsed rows — fixed.** They carried `.14` and a pale blue cast because a bright,
   ungraded-looking image at very low opacity lifts the navy toward blue. Now the same recipe as
   desktop: graded image at **.34** over stone-deep. Numeral logic is already the desktop recipe
   (bronze on the active panel only — three bronze slivers would breach the two-per-viewport cap).
   Label contrast at 375px: **3.61 / 3.16 / 3.16**, all clearing 3.0. Fourth row **not clipped** —
   its bottom edge and the section boundary are the same pixel, 0px dead space.

**Two further defects the measurements exposed, both fixed:**

- **Expanded-panel text failed AA.** At the new full-bleed width the name measured **2.97** against
  3.0 and the description **3.78** against 4.5 — and the description's real figure was worse still,
  because `on-dark-soft` is 66% alpha and my earlier readings had compared the opaque colour. The
  scrim is the lever, so it moved from `.78 → transparent at 52%` to **`.94` held flat to 24%, then
  transparent at 58%** — a plateau rather than a ramp, so the text zone sits on near-solid scrim.
  Now **name 13.42**, **description 6.56** alpha-aware. This is a deviation from the specified
  scrim; it was made because the specified value measurably failed.
- **Mobile expanded numeral floated mid-photograph.** The mobile rule centres the numeral so it
  lines up with the collapsed rows' names, but the expanded row has no name beside it. The active
  panel's numeral now returns to top-left, matching desktop — verified at 20px from the panel top
  when expanded, 30px (centred) on the 76px rows, and it follows the active panel on tap.

**Not a regression, worth recording:** the document carries 8px of horizontal overflow at 1440px.
Hiding `#practice` entirely leaves `scrollWidth` at 1433 either way, so it comes from the old
build's credentials marquee and reviews carousel, not the louver. Earlier passes missed it because
they compared against `innerWidth` (1440) rather than `clientWidth` (1425).

### Build pass 11 — #9 composition

**Failure mode recorded first, because it is the lesson.** Every prior pass on this section verified
by measurement and every measurement passed, but nobody judged the section compositionally. A
63px pale heading band sat between 1092px of navy above and navy panels below — numerically
correct, visually an orphaned strip. Measurement confirms a thing is what you specified; it cannot
tell you the thing is wrong.

1. **Heading moved into the louver.** The pale header row is gone entirely — the section now begins
   at the panel row's top edge. "Practice Areas" sits at 40/40 inset, display-l, on-dark, over the
   photograph. It needed an always-on **top scrim**, because the existing bottom scrim is
   state-driven and vanishes when a panel collapses, and the heading occupies the louver's top-left
   in every state regardless of which panel is there. Heading contrast measured **3.63** against a
   3.0 AA large-text threshold, after deepening the top scrim from .88→.62 to **.93→.74** (at the
   shallower values it measured 2.92 and failed).
   - **Numerals moved to a shared register at y=120px.** The heading now owns the top-left corner,
     so numerals at their panels' own top-left collided with it. Hiding whichever numeral fell under
     the heading would have broken the 01–04 sequence; a common y reads as a deliberate horizontal
     register instead.
   - **Mobile takes the heading in flow, on stone-deep, above the rows** rather than overlaid. An
     overlaid heading covers a 76px collapsed row outright when row 1 is not the active one. Still
     inside the dark object, still no pale strip.

2. **Separation from #8 — chose the pale band, not shifting #8's ground.** The band immediately
   above is `.whyband`, **1092px of stone-deep**, so without separation two navy fields run
   together and the louver stops reading as its own object. Recolouring `.whyband` would have been
   deciding section #8's ground as a side effect of fixing #9 — #8 has not been rebuilt, its
   archetype C treatment is not settled, and that call belongs to #8's own pass. The band is
   `clamp(64px, 8vh, 104px)`, measuring 72px at 1440 and 68px at 393, and is contained entirely
   within #9.

3. **Mobile fourth row — verified not clipped.** Rows measure exactly **[380, 76, 76, 76]** at
   393px, last row bottom == frame bottom == section bottom, 0px gap. The heading move and numeral
   reposition resolved it.

**Compositional judgment, and what it exposed.** With the heading inside the dark field the section
reads as one object and nothing is orphaned — the heading previously belonged to neither the navy
above nor the panels below. The top band works *because it is empty*: an empty band is negative
space, a band with a heading in it was a stranded header row. That distinction is the whole fix.

But judging the object rather than measuring it exposed a defect no measurement had caught: **the
bottom edge dissolved.** The last panel is stone-deep and so is #10, so the only thing marking the
boundary was the photographic texture stopping — a crisp top edge against an undefined bottom one,
the object reading as fading out rather than ending. Fixed with a **2px stone-pale seam** on the
frame's bottom edge: that is exactly the gap already running between the panels, so the object
closes in the rhythm it is built from, at a cost of 2px rather than the band of dead space removed
in the previous pass.

**Mechanic untouched and re-verified after all of it:** `flex-grow 0.62s cubic-bezier(0.65,0,0.35,1)`,
`writing-mode: vertical-rl`, `saturate(0.55) contrast(1.06)` on every image, collapsed opacity .34,
one bronze numeral, panel widths 57.8/13.9/13.9/13.9, full bleed 0 → 1425.

### Build pass 12 — #9 rebuilt from scratch

**Everything for #9 was deleted before anything was written.** 95 CSS rules removed across two
passes (the first missed media blocks whose prelude opened with a comment, so the at-rule test
never fired), plus 6,025 characters of markup. Verified zero references to any prior #9 class
remained before the new block was written. `practice-card` and `practice-index`, both superseded
and uninstantiated, went with it. Stylesheet dropped 70,195 → 49,419 bytes.

**Radio group, not `:has()`.** Single selection is enforced by HTML, so "two expanded" and "none
expanded" are unreachable states rather than defended-against ones — that bug class is gone, not
guarded. Everything keys off `:checked` and nothing else. Radios are visually hidden but not
`display:none`, which would drop them from the tab order; arrow keys move through the group and
check as they go.

**Verification — all five gates:**

| Gate | Result |
|---|---|
| No horizontal overflow | **PASS** — scrollWidth 1425 === clientWidth 1425, zero offenders |
| Exactly one expanded, nine states | **PASS** — 1 in all nine |
| Zero elements between #8 and the panel row | **PASS** — 0 elements, 0px gap |
| Four mobile rows fully visible at 393px | **PASS** — [380, 76, 76, 76], last row flush, 0px gap |
| Heading contrast ≥ 4.5 | **PASS at 6.48** — see below |

Panel widths measure exactly 58 / 14 / 14 / 14; row is full bleed 0 → clientWidth at both widths.

**Two gates failed first and were fixed before reporting:**

- **The 8px page overflow was mine, and my earlier diagnosis of it was wrong.** I had twice
  recorded it as pre-existing marquee overflow. It was `.ds-bleed` on #5's image frame: `100vw`
  includes the scrollbar, so a 100vw child of a 1425px content area is 1440px and overflows by 15px.
  I had read the largest offenders — which were clipped by their parents and harmless — instead of
  the ones whose right edge actually landed in the overflow zone. `.ds-bleed` now uses `width:100%`;
  every element it is applied to is already a direct child of a full-width section.
- **Heading contrast failed at 2.25 against the ≥4.5 gate.** The specified top scrim (.70 →
  transparent at 30%) ramps away too fast: the heading's baseline sits where the gradient has fallen
  to ~.33, over blown-out road. Solved for the minimum effective alpha — **0.615** — then held
  **.72 flat to 18%** before ramping to transparent at 34%. Keeps the specified starting value,
  clears the gate at 6.48.

**Two deviations from the brief, both deliberate:**

1. **Hover does not expand.** The brief's rationale for radios is that they remove a bug class by
   making state single-sourced; layering a parallel hover mechanism on top would reintroduce exactly
   the dual-source problem being eliminated. Hover therefore leaves the invariant untouched —
   verified with a real pointer: hovering panel 4 leaves panel 1, the checked one, as the only
   expanded panel. **If hover-to-expand was wanted, say so** — it is a contained addition, but it
   is the one thing that can reintroduce the failure mode this rebuild was for.
2. **`100vw` not used.** Panels are flex proportions of a 100%-width row, resolving to the specified
   58/14/14/14. Literal `vw` units would have failed the no-overflow gate by the scrollbar's width —
   the same defect just fixed in #5.

**⚠ Bronze cap breached, on instruction.** The brief specifies collapsed numerals in bronze. With
three collapsed panels that is three bronze numerals plus the expanded panel's bronze rule =
**four bronze elements on screen**, against §2's cap of two for section content. This was flagged
twice in earlier passes and resolved each time by making only the active numeral bronze; the brief
has now specified bronze collapsed numerals explicitly, so it is built that way and the breach is
recorded here rather than silently overridden a third time. Either §2's cap or this treatment needs
to give.

**Note on the gate's wording:** `scrollWidth === innerWidth` cannot hold on a browser with a classic
scrollbar — innerWidth (1440) includes the scrollbar, clientWidth (1425) does not, so with zero
overflow scrollWidth equals clientWidth. Satisfying the literal equality would require introducing
15px of real overflow. Verified against the intent: `scrollWidth === clientWidth`, which now passes
exactly.

### Build pass 13 — #9 refinements (links, legibility, edges)

Additive only. Radio mechanic, panel proportions, grade and transition untouched; hover still does
not expand.

**1. Practice-area links.** All four URLs resolve to real pages — **none unresolved**, so the
practice-areas index fallback was not needed (and does not exist):

| Panel | Name | URL |
|---|---|---|
| 01 | Head-On Collisions | `practice-areas/head-on-collisions/` |
| 02 | Intersection and T-Bone Crashes | `practice-areas/intersection-t-bone-crashes/` |
| 03 | Distracted Driving Crashes | `practice-areas/distracted-driving-crashes/` |
| 04 | Rear-End Collisions | `practice-areas/rear-end-collisions/` |

Name is now an `<a>` (on-dark, no rest underline, bronze underline growing 0→100% on hover/focus
over t-fast); a `button-text` "View practice area" with the permitted arrow sits 20px above the
bottom padding. Collapsed panels use `visibility: hidden` on the body, so their links leave the tab
order — **verified: 2 reachable links in the whole section, both in the expanded panel, 0 in each
collapsed one.** Each radio carries an explicit `aria-label`, because `visibility: hidden` also
removes content from accessible-name computation and the radios would otherwise have been unnamed
while collapsed.

**2. Description legibility.** Lifted to `on-dark` — at `on-dark-soft`'s 66% alpha the text itself
was the limiter, so no scrim value could have fixed it. Base scrim now holds flat at .78 across the
whole text block then ramps above it. **Alpha was solved, not nudged:** worst case needs
**α = 0.635** (head-on, whose brightest pixel under the description is pure white); .78 clears it.

Measured on all four images at both widths, worst pixel beneath the description:

| Panel | 1440px | 393px |
|---|---|---|
| Head-On | 7.72 | 8.32 |
| Intersection / T-Bone | 8.75 | 8.45 |
| Distracted Driving | 15.14 | 8.63 |
| Rear-End | 11.87 | 9.14 |

**All eight ≥ 4.5.** The plateau needed different extents per width — the text block is 28.8% of a
648px desktop panel but **49.9%** of a 380px mobile row, so desktop's 34% would have ramped straight
through the name and rule on a phone. Mobile plateau runs to 54%.

**3. Panel edges.** `gap: 0`; 1px `rule-cut-dark` on the left of every panel but the first, 1px on
the section's top and bottom. Mobile takes the same rule between rows. Verified: gap 0px, panel 1
border 0, panels 2–4 at 1px `rgba(198,214,226,0.19)`, section borders 1px/1px, all radii 0, zero
shadows.

**Verification:** `scrollWidth === clientWidth` (1425 = 1425) still holds after the border changes.

**⚠ BRONZE COUNT CHANGED — the §2 exemption recorded last pass no longer covers this.**
On screen now: **6 marks** — three collapsed numerals, the expanded panel's rule, the link label,
and the arrow. Previously recorded at 4, against §2's cap of **2**. The link and arrow the brief
adds are what took it from 4 to 6. This is the third pass in which the cap has been exceeded on
instruction. §2 currently says bronze "is a rule, a figure, a button, an underline" and caps it at
two per viewport for section content; this section now uses it as a wayfinding system. Either the
cap needs a stated exemption for `practice-areas`, or the collapsed numerals need to drop to
`on-dark-soft` — which alone would bring it to 3.

**Harness note, recorded because it produced a false failure.** Setting `input.checked`
programmatically did not reliably flush the sibling-selector recalc, which made the state look
off-by-one across several measurements. Driving the panels with real `label.click()` shows the
mechanic is correct: each click checks its own radio and expands exactly its own panel, one at 380px
in every case. The CSS was never wrong; the measurement was.

### Build pass 14 — #9 heading moved to a navy band

Heading only. Louver, radio mechanic, proportions, grade, links and borders unchanged and
re-verified after the change.

- **Heading lifted out of panel 01 into its own `stone-deep` band above the panels**, centred.
  Inside the panel it read as that panel's caption rather than the section's title, and it needed a
  scrim to survive the photograph's sky.
- **Top scrim removed entirely.** Zero `scrimtop` nodes remain; panel 01's only scrim is the base
  one, whose gradient terminates at `rgba(10,22,40,0)` — transparent at the top edge, so the
  photograph reads clean there with no residue.
- **Band:** 108px at 1440 (`clamp(96px, 12vh, 152px)`), 85px at 393 (`clamp(72px, 10vh, 104px)`).
  Heading `display-l` 56px desktop / `display-m` 24px mobile, `on-dark`. No rule, eyebrow or
  ornament. Copy verbatim.
- **Centring — worth stating precisely.** The heading's centre sits at **712.5px**, which is
  `clientWidth / 2`, not `innerWidth / 2` (720). Those differ by half the scrollbar. `clientWidth`
  is the correct target: centring on `innerWidth` would push the heading 7.5px right of the visible
  centre, because `innerWidth` counts a scrollbar the user cannot see content under. Offset from the
  visible centre is **0.0px** at both widths.
- **Continuity confirmed:** 0px gap #8 → band, 0px gap band → row, and the section's `border-top`
  is now **0**. That border was added in the edges pass and fell exactly at the #8/band junction —
  it was the seam this change exists to remove. The bottom border stays; that one separates #9 from
  #10, which is a real boundary. All three surfaces measure `rgb(10, 22, 40)`.
- **`scrollWidth === clientWidth`** holds at both widths (1425/1425, 393/393).
- **Bronze count unchanged at 6** — rule, link, arrow, three numerals. The heading is `on-dark` and
  adds none. The §2 breach recorded last pass stands, unaltered by this change.

**⚠ I broke the section mid-pass and caught it in verification.** The regex I used to delete the
top-scrim rule matched the *desktop* `.ds-pa__scrimbase, .ds-pa__scrimtop` rule as well, and its
non-greedy run to the next `\n}\n` swallowed the desktop numeral, vname and body positioning, the
desktop `:checked` flex rules, and the media block's closing brace. Panels rendered at
**44.9/18.4/18.4/18.4** instead of 58/14/14/14 — the expanded panel was falling back to the mobile
`flex-basis: 380px` with `flex-grow: 14`. Repaired by rewriting the block; braces re-balanced
(276/276), widths back to **57.9/14/14/14**, and the mechanic re-verified across all four panels
(each click checks its own radio, exactly one expanded every time).

The lesson is the same one as the `.ds-bleed` misdiagnosis: a regex over CSS matches text, not
structure. Both times the damage was invisible until something was measured.

### Build pass 15 — #9 panel clipping: COULD NOT REPRODUCE, no change made

Investigated the reported clipping across the full matrix — four expanded states × three widths,
twelve cells. **All twelve pass.** No code was changed: the widths are already correct, and
changing them would have been a speculative edit against a defect that does not exist in the
geometry.

Every state, every width: the four panels sum to exactly the row's client width, panel 01's left
edge is at **x = 0**, panel 04's right edge is at exactly `clientWidth`, every collapsed panel's
vertical label sits fully inside its panel on **both** axes, and `scrollWidth === clientWidth`.
Minimum slack measured anywhere in the matrix: **76.3px horizontal, 142px vertical** — the labels
are nowhere near their panel edges.

**What the report was almost certainly seeing, and it is worth recording because I reproduced the
appearance exactly.** The panels are `clamp(560px, 72vh, 760px)` tall — 648px at a 900px viewport —
and the vertical labels are centred in that height. At a scroll position where the section is only
partly on screen, the labels run past the **viewport** edge and read as cut off mid-word. My first
capture this pass did exactly that and looked like the described defect; framing the whole section
showed every label complete. The clipping is the window, not the layout.

That is not a layout bug, but it is a real legibility observation: a collapsed panel's label is only
fully readable once most of the section's 757px height is in view. If that is the actual concern,
the fixes are to the label, not the widths — shorten the vertical labels, reduce the panel height
clamp, or anchor the labels toward the panel top instead of centring them in 648px. **None applied**,
since all three change things this pass was told not to touch and none of them is what was asked for.

**Matrix (widths → sum, p01 left / p04 right):**

| Width | State 1 | State 2 | State 3 | State 4 |
|---|---|---|---|---|
| 1025 (client 1010) | 584/142/142/142 → 1010 | 141/585/142/142 → 1010 | 141/142/585/142 → 1010 | 141/142/142/585 → 1010 |
| 1280 (client 1265) | 732/178/178/178 → 1265 | 177/733/178/178 → 1265 | 177/178/733/178 → 1265 | 177/178/178/733 → 1265 |
| 1440 (client 1425) | 825/200/200/200 → 1425 | 199/826/200/200 → 1425 | 199/200/826/200 → 1425 | 199/200/200/826 → 1425 |

p01 left = 0 and p04 right = client width in all twelve; all labels fit; no horizontal scroll.

### Amendments — intra-cell rhythm (earlier pass, continued)

- **Geometric note.** The two requests are in tension: if one label wraps and its neighbour does
  not, and the detail lines must share a baseline, some cell has to absorb a label line's worth of
  height. It cannot be eliminated, only placed. It is placed above the label so the tight
  label/detail pairing holds in every cell — the cost is that in those three cells the amount and
  its case label sit further apart than the "one unit" grouping intends. Making every label fit one
  line would remove the tension outright, but not at §2's label token (12px, 0.14em tracking) —
  the longest, "REAR-END COLLISION, BROOKLYN-QUEENS EXPRESSWAY", cannot fit a 288px column at that
  size without a one-off type size, which §9 forbids.

---

### Build pass 16 — #5 rebuilt clean-sheet as the page's typographic statement

**Archetype reassigned D → C.** Applied in DESIGN.md §7 (row, sequence block, and §12's now-false
photography gap). §4's archetype table was **not** touched — see the proposal at the end.

**Why the reassignment.** #5 as D was the third image-dominant section on the page (#5, #9, #15).
That is the compositional monotony §1 exists to remove: rationing a repeated composition is still
shipping it, the same reasoning §4 Rule 2 applies to archetype A. The photograph was also wrong on
content — `towers.jpg` is generic corporate glass shot from below, which reads Manhattan, while
every word of the copy is Long Island: Copiague, local relationships, neighbours referring
neighbours. Duotoning it did not fix that; it only turned a wrong photograph mustard-yellow.

C is the assignment because #5's job is now to be the page's **typographic moment** and the
deliberate counterweight to #9. #9 is image-dominant with type as caption; #5 is type-dominant with
no image at all. Scrolling between them is a change of register rather than a repeat.

**Rule 1 holds.** Full sequence with #5 as C:

```
 #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15 #16 #19 #20
  F   C   G   B   C   D   F   B   G   C   E   D   B   F   C
```

14 transitions, no adjacent repeats. Both joins clear: #4 is F, #6 is G. A stays at zero (Rule 2).
Nothing resembles its rejected-build treatment (Rule 3) — #5's rejected composition was the banned
A, and its immediately previous treatment was the split image band, neither of which survives.
Distribution moves from B×3 C×3 D×3 F×3 G×2 E×1 to **C×4 B×3 F×3 D×2 G×2 E×1**. C at four uses
breaks no rule — only A is capped — and the four are spread #5, #8, #13, #20.

**The three defects, and what replaced them.**

| Defect | Fix |
|---|---|
| Banned SVG duotone → mustard-yellow skyline | Photograph deleted outright. The `#ds-duotone` reference is gone from #5; the filter itself stays for #9/#15. |
| Split into two half-sections — heading on an image band, its own body copy on a separate pale ground beneath | One full-bleed `stone-deep` field. `rule-cut` hairlines are the section's only structural device. |
| Archetype D, same as #9 and #15 | Reassigned C. D now runs twice, not three times. |

**Build.** Old markup and every rule that styled it were deleted before anything was written —
`.ds-figure-section`, `__frame`, `__img`, `__scrim`, `__overlay`, `__heading`, `__body` and their
two responsive overrides, ~60 lines. Nothing was amended in place.

Heading `display-xl` / `on-dark`, left, taking the top third alone with `{spacing.xxl}` before the
first rule. Body in CSS multi-column — `column-count: 2` above 1025px, `column-gap: 64px`, max
1100px, `orphans: 2; widows: 2` — so the three paragraphs balance as one continuous text rather
than as two hand-split divs. CTA line `body-lead` at 600 spanning the full container. Address as
§3 `resource-row` in a dark form, `label` type in `on-dark-soft`, arrow at the right edge. Four
`rule-cut` hairlines: heading/body, body/CTA, and above and below the address row.

**Motion.** One `data-ds-draw` trigger on the container drives the whole sequence, so the stagger is
real rather than four observers firing at four scroll positions. Heading 0ms, body columns 120ms as
one block, rules `scaleX(0 → 1)` at 0/80/160/240ms, all `t-base` `ease-out`, fires once. Nothing
else animates. Verified: reduced motion → everything instant, all four rules at full 1152px;
JS disabled → nothing hidden, rules full width (the `.ds-js` guard).

**⚠ A page-level grain texture was landing on this section, and I would have shipped it.** The
section rendered with a visible `feTurbulence` noise field over the flat navy. It comes from
`styles.css`'s alternating-grain rule, `main > section:nth-of-type(even):not(...)`, which scores
**0-4-2** against the component's own `background` shorthand at **0-1-0** — so the grain won on
specificity and the shorthand's implicit `background-image: none` never applied. The old
`.ds-figure-section` was silently grained the same way. Fixed by adding `:not(.ds-statement)` to
that rule's existing exclusion list, which is where the other grounds-of-their-own are already
excluded. Position parity is untouched, so no other section's grain changed.

Worth recording as a pattern: **a component setting its own `background` does not make it the
authority on that background.** Two passes have now been bitten by legacy selectors that outrank
the design-system layer, and neither was visible without measuring computed style.

**Deviations, stated rather than buried.**

1. **The heading runs four lines at 1440px, not the three the brief specified.** This is arithmetic,
   not execution. The string is 61 characters; at `display-xl`'s `7vw` = 100.8px it needs ~3382px of
   run against 1152px of container, so three lines would require ~90px — below the token. The two
   requirements cannot both hold. I kept the token, because "tokens only, no type size outside the
   scale" is a stated hard constraint while the line count is a layout descriptor, and because §2's
   own type law permits 2–4 lines. Break falls cleanly at the sentence boundary: *Long Island Car /
   Accident Lawyers. / Trial-Ready / Representation.* Three lines is available only by dropping to
   `display-l`, which is what mobile already uses — desktop would then look identical to a phone.
2. **The phone link has no rest-state underline.** The brief specifies the `button-text`
   underline-grow, which is `scaleX(0)` at rest, so at rest the link is distinguished from its
   paragraph by bronze alone. That is thin against WCAG 1.4.1 for an inline body link. Shipped as
   specified; the mitigation is that the link text is a formatted phone number inside "Call (516)
   444-1000", which is self-identifying as a target independent of colour, and focus-visible carries
   the 2px bronze outline. Flagging rather than silently adding a static underline.
3. **`.ds-resource-row--dark` is a new modifier**, and §3 says do not invent a variant. It is the
   dark-ground form of an existing component — same flex, padding, arrow and hover — not a new
   component, and the brief specified this composition. Recorded so it is a decision, not a drift.
4. **`.ds-bleed` now has no consumer.** #5 was its only one. Left in place as scaffolding rather
   than removed, since deleting a general utility is outside this section's scope.

**Measured.**

| Check | Result |
|---|---|
| `filter: url(#…)` anywhere in #5 | **0** — no computed filter on the section or any descendant, incl. pseudo-elements |
| `<img>` / `background-image` in #5 | **0 / 0** after the grain fix |
| Heading vs `stone-deep` | **15.39:1** |
| Body / CTA vs ground | 15.39:1 · Phone link 7.49:1 · Address row 7.21:1 |
| Column balance at 1440px | **7 lines / 6 lines** — within 1. `column-fill` left at `balance`; no adjustment needed and none made. P2 breaks 4/2 across the gutter, P3 sits whole in column two, no orphan. |
| Bronze in section content | **1** — the phone link. Address row is `on-dark-soft` as specified. |
| Address row hit area | 58px — above the §8 48px minimum |
| Keyboard | Both links tabbable; 2px bronze focus outline |
| Console | No errors |

**Judgment from the screenshots (1440px and 393px).**

*Does it read as one object?* Yes, and this is the clearest gain. One uninterrupted navy field from
the credentials rail to the CTA band, with four hairlines dividing it internally. The old version's
worst failure was that the heading and the copy it introduced sat on different grounds and read as
two sections; that is gone. The hairlines divide without separating — they are internal structure,
not section boundaries.

*Does the heading carry statement weight?* Yes. Cinzel's lowercase is drawn as small capitals, so
the heading sets as a solid inscriptional block without any `text-transform`, and at ~101px across
four lines it occupies the top third alone with roughly 200px of clear field beneath before the
first rule. It reads as an inscription, not a label. The four-line set works in its favour here: it
is a denser block than three lines would be. At 393px it drops to `display-l` and still fills the
measure across four lines.

*Is the transition into #6 clean?* Yes. #5's flat navy runs to its bottom padding and #6 opens on
its 1px bronze hairline, which does all the separating — a hard bronze cut between two dark
grounds. The two navies are tonally adjacent (#6 carries a pinstripe and a top gradient), so
without that hairline the join would be mushy; with it, it reads deliberate. The join *above* is
weaker but acceptable: #4 is `stone-black` against #5's `stone-deep`, a small tonal step, but #4 is
a 96px marquee rail with its own hairlines top and bottom, so it reads as an object sitting on the
field rather than an ambiguous merge.

**Proposed, not applied — §4's archetype C row.** C currently reads "`{layout.container-narrow}`,
centered, generous air, nothing else." #5 as built is left-aligned in the 1200px container, so it
matches C's *spirit* — type only, generous air, nothing else — but not its literal composition
line. Two of C's four uses now diverge from that line. Suggest widening it to "**Statement** —
type-dominant, no image, generous air, nothing else. Centred and `container-narrow` for the short
forms (#13, #20); left-aligned in `container` when the section carries a full argument (#5)." Left
for the CD to accept or reject; §4 is governing law and not mine to edit.

---

### Build pass 17 — #5 refinement: breaking the grid, fixing the break, varying the rhythm

Refinement only. Concept, structure, copy and motion untouched — no rebuild, no new markup beyond
one class on the first rule.

**1 · The heading breaks the grid.** Everything else sits on the container margin; the heading
alone hangs left of it. Implemented as a negative `margin-left` on the heading, which pulls the
text into the gutter *and* widens its measure by the same amount — the box goes 1152 → 1224px at
1440px, so the pull buys the heading more room rather than costing it any.

The pull is `min(72px, max(0px, (100vw - 1200px) / 2))` rather than the two stepped media queries
the brief specified, because **the stepped version overflows.** At exactly 1280px the container's
outer margin is 40px and its content edge is 64px in; a flat −72px puts the heading's left edge at
**−8px**, past the window. The `min()` caps the pull at whatever gutter actually exists, which makes
the ramp continuous and lands on the brief's own numbers where they are geometrically available:

| Viewport | pull | heading L | body L | delta |
|---|---|---|---|---|
| 1440px | −72px | 72 | 144 | **72** |
| 1280px | −40px | 24 | 64 | **40** |
| 1025px | 0 | 24 | 24 | **0** |

1280px resolves to exactly the 40px the brief asks for in the 1025–1279 band — the clamp arrives at
it on its own. **What the brief asks for and geometry does not allow is a constant 40px across that
whole band.** Below 1200px `.ds-container` is full-bleed, there is no outer margin left to hang
into, and a 40px pull at 1100px would put the heading at −16px. The ramp therefore decays to 0
between 1200px and 1025px instead of holding 40px. Recorded as a deviation, not an oversight.

Swept **62 widths from 360px to 1908px**: minimum heading left edge **24px**, maximum document
overflow **0px**, heading never negative and never past the right edge. The pull reaches its full
72px at 1344px and the heading pins to exactly 24px — the `gutter-mobile` token — everywhere below
that. With a **classic 15px scrollbar** (measured in-browser, not emulated) `100vw` overstates the
layout viewport, and the tightest case lands at **21px** clearance around 1352px instead of 24px.
Still air, still no overflow, and correcting it would cost 8px of delta at 1280px on every platform
to buy 3px back on one — left as is, measured rather than assumed.

**2 · The column break is fixed.** `break-inside: avoid` on the paragraphs. P1+P2 now sit whole in
column one, P3 whole in column two, at every width — verified by testing each paragraph's line
rects against the column midpoint, `splitAcross: false` for all three at 1440/1280/1025. The
mid-sentence "Not through a / billboard" orphan is gone.

Column two is now four lines against column one's nine, which leaves a real void at the lower
right. That is the accepted trade and it survives because the section's other asymmetries — the
heading hanging left, the short rule — establish that the composition is deliberately uneven. In a
symmetrical section the same void would read as a mistake.

**3 · Vertical rhythm, and why the first measurement was wrong.**

| Gap | Desktop | Mobile |
|---|---|---|
| heading → rule 1 | **56px** `clamp(56px, 6vh, 88px)` | 40px |
| rule 1 → columns | **40px** | 24px |
| columns → rule 2 | **72px** `clamp(72px, 8vh, 112px)` — the section's largest | 56px |
| rule 2 → CTA | **40px** | 24px |
| CTA → rule 3 | **48px** | 32px |

All ten verified against computed style and box geometry. The brief named four gaps; rule 2 → CTA
was unnamed, and it takes 40px to match rule 1 → columns, so the pattern is consistent: **a rule
sits 40px above the block it introduces.** That is what makes the rules read as belonging to their
blocks rather than floating between them, and it is what produces the three-group read — heading /
body / CTA+address — instead of four evenly spaced blocks.

**⚠ My first measurement pass reported these gaps wrong and I nearly acted on it.** It read
56/40 as **32/64** and I started looking for a margin-collapsing bug that did not exist. The probe
was measuring `getBoundingClientRect()` *before the scroll reveal had fired*, so the heading and
the columns were still carrying the reveal's `translateY(24px)` — the heading sat 24px low, which
subtracted 24 from the gap above it and added 24 to the gap below. The totals were right the whole
time; only the split was displaced. Fixed by scrolling and waiting 1500ms before probing.

Worth recording alongside pass 16's grain finding: **both bugs this section has produced were
measurement artifacts or invisible computed state, and neither was visible by looking.** A
transform that does not affect layout still affects every rect you read.

**4 · The rules are differentiated.** Length is the only variable; all four stay 1px
`rule-cut-dark`.

| Rule | Width @1440 | @1025 | @393 | Role |
|---|---|---|---|---|
| above columns | **160px** | 160px | 96px | marks a start, not a division |
| above CTA | 1152px | 977px | 345px | the section's real break |
| above address | 1152px | 977px | 345px | opens the anchor |
| below address | 1152px | 977px | 345px | closes it |

The short rule aligns to the body margin, not the heading's — so it also reads as the body block's
own mark, which reinforces the heading's offset by contrast. Confirmed the `scaleX` draw still
resolves to the shortened rule's own 160px and not the container width: computed `width: 160px`,
post-reveal transform `matrix(1,0,0,1,0,0)`, measured rect 160px.

**Unchanged and re-verified.** Motion untouched — no new animation, reveal still fires once at
heading 0ms / columns 120ms / rules 0-80-160-240ms. Copy verbatim. No image, background-image,
filter or box-shadow anywhere in the section (all measured at 0). Bronze count in section content
still **1**, the phone link. `scrollWidth === clientWidth` at every width tested.

**Judgment — does it read as art-directed now?** Yes, and the heading offset is what does it. Before
the refinement the section was four full-width blocks on identical margins separated by identical
lines: correct, and inert. The single move of pulling the heading 72px left of the body margin
converts it, because the offset is large enough to be unmistakably intentional — at 1224px wide
against the body's 1152px it is not a rounding error, it is a decision, and it gives the section a
left edge that steps rather than a single ruled margin.

The short rule is the second-strongest move and does more than its size suggests. Sitting on the
body margin, 160px against the full rule's 1152px, it establishes a hierarchy the eye reads without
naming: this line opens something, that line divides something. Three identical hairlines could
never carry that.

The rhythm change is the quietest of the four and the one that makes the others work. The 72px
before the CTA rule against the 40px after it means the CTA and the address now read as one
attached group — action, then reference — while the body sits clearly apart above them. The
section reads as three groups, which is what it always was semantically and now finally is
visually. Mobile keeps the same proportions at 40/24/56/32 and the same three-group read.

The one thing I would flag to the CD: the void at the lower right, from column two ending five
lines short. It is the correct trade against a split sentence and it is defensible as composition,
but it is the section's most arguable surface. It would close if P3 were allowed to break — which
is exactly what the brief ruled out, and rightly.

---

### Build pass 18 — #5 body rebuilt as a three-column argument

Body only. Ground, `display-xl` heading, CTA line, address anchor and the absence of photography
all kept. Two things from pass 17 were **removed**, not adjusted: the heading's negative
`margin-left` and the 160px short rule, along with all their CSS.

**Why the two-column lede failed, and why three columns cannot.** Multicol reflows one continuous
text and balances it, so three paragraphs filling two columns meant column one ran nine lines to
column two's four — a six-line hole that no `column-fill` setting could close, because the content
does not divide by two. The copy is a **three-beat argument** — the problem, the credibility, the
method, one paragraph each — so at three columns the count matches the content and **there is
nothing left to balance.** That is the whole fix: the previous imbalance was a structural mismatch
between a 3-item argument and a 2-column frame, not a typesetting failure.

Grid, not `column-count`, so each paragraph is an addressable item rather than a fragment of a
reflow. `gap: 0` — the division is carried by the rules themselves; a gap plus a rule would put the
line floating in the middle of empty space instead of sitting on the column edge it divides.

**The vertical rules are the section's device and no other section uses them.** They are
pseudo-elements on stretched wrappers, not `border-left`, for two reasons: a border cannot be drawn
on with a transform, and these have to draw top-to-bottom on entry. `align-items: stretch` gives
every wrapper the row height, so both rules measure **280.469px** — the height of the tallest
column, not of the paragraph beside them. Beside column one's five lines the rule continues down
through open field. That is the point. Rules ending at each paragraph's own last line would read as
three underlines; running the full division, they read as architecture.

**Removals, with reasons.**

- **Heading offset gone.** At `display-xl` a 72px pull was too small a fraction of a 1224px block to
  register as a decision; it read as the heading sitting fractionally off the grid everything else
  aligns to. Heading left and CTA left now measure **144px and 144px** — identical, `margin-left: 0`.
- **Short rule gone.** With the body no longer needing a mark to open it — the three columns open
  themselves — a lone 160px hairline was a stray. Three horizontal rules remain, all full width.

**Measured at 1440px.**

| Check | Result |
|---|---|
| Grid | `384px 384px 384px`, `gap: 0`, `align-items: stretch` |
| Column widths | 384 / 384 / 384 — **spread 0.000px** |
| Column heights | 280 / 280 / 280 = row height; paragraphs 140 / 280 / 196 |
| Vertical rules | both **280.469px** tall × 1px, `rule-cut-dark`, delays 120ms / 200ms |
| Text crossing a rule | **0 lines** outside their own column, all three |
| Heading left vs CTA left | **144px / 144px** — exact |
| heading → columns | **72px** `clamp(72px, 8vh, 112px)` |
| columns → CTA rule | **72px** `clamp(72px, 8vh, 112px)` |
| Horizontal rules | 3, all 1152px |
| `scrollWidth` / `clientWidth` | 1425 / 1425 |
| Images · background-images · filters · box-shadows · radii | 0 · 0 · 0 · 0 · all `0px` |
| Bronze in section content | **1** — the phone link (its `::after` underline is the same element) |

At 1025px the columns measure 325.656 / 325.672 / 325.656 — **spread 0.01px**, sub-pixel grid
rounding, inside the 1px tolerance. Rules 336.562px each. At 393px the grid collapses to one column
and the same two pseudo-elements re-lay as 345px horizontal dividers, 32px of air on each side.

**Motion.** No new motion. The vertical rules draw `scaleY(0 → 1)` from the top, staggered 120ms
then 200ms left to right, starting with the body block they divide. On mobile the identical
elements draw `scaleX` instead — same device, rotated with the layout, so the division survives the
collapse rather than disappearing with the columns. Reduced motion: everything instant, both
divisions at full 280.469px, all three rules at full 1152px. JS disabled: nothing hidden, rules at
full extent.

**One thing to flag: the middle column's measure is narrower than its neighbours, and the whole
body is tight at the breakpoint.**

| Viewport | col 1 | col 2 | col 3 |
|---|---|---|---|
| ≥1200px | 344px, ~43 chars | **304px, ~38 chars** | 344px, ~40 chars |
| 1025px | 285.7px, ~36 chars | **245.7px, ~31 chars** | 285.7px, ~35 chars |

This follows directly from the specified padding — 0/40, 40/40, 40/0 — which gives column two 80px
of padding against its neighbours' 40px. The *columns* are exactly equal, which is what was asked
and what the grid guarantees; the *text measures* are not. I kept it because the alternative
(unequal padding to equalise measures) would put the rules at different distances from the text on
either side, and consistent 40px air around every rule is what makes them read as one architectural
system rather than three arbitrary lines. The consistency worth having is the rule's, not the
measure's.

The 1025–1200px band is the section's tightest point at ~31 characters in the centre column. That
is below comfortable reading and it is the cost of holding three columns down to the 1025px
breakpoint the brief specified. If it matters, the fix is to raise the three-column breakpoint to
~1200px and let 1025–1199px stack — **not applied**, since the brief sets three columns at ≥1025px
and this is a judgement for the CD rather than a defect to patch silently.

**Judgment — do the columns read as a structured argument?** Yes, and more clearly than any
previous version of this section. Three columns of visibly different lengths, each holding one
complete thought, reads as three points made in sequence — the eye counts them before it reads
them. The two-column version read as a body of text that had been poured into a container and come
up short. This reads as a text that was *arranged*. The ragged bottoms help rather than hurt: equal
column heights would have looked like a table, and the unevenness is what signals these are
arguments of different weight rather than cells of a grid.

**Do the rules read as architecture?** Yes, and the full-height stretch is the entire reason. A rule
that stops where its paragraph stops is a decoration attached to that paragraph. A rule that runs
the full division and continues past the short column into open field is a structural line the
paragraphs are placed against — the field is divided first, the text sits in it second. That
inversion is what the section needed and it is doing the work `column-count` never could, because
multicol has no element to hang a rule on.

The device is also genuinely unique on the page: every other section divides horizontally, with
`rule-cut` closing bands. #5 is now the only section that divides vertically, which gives it its own
structural signature without adding a colour, a type size, or an ornament.

---

### Build pass 19 — #15 rebuilt clean-sheet as the page's pivot

**Archetype reassigned D → F.** Applied in DESIGN.md §7 (row, sequence block, §12's gaps list, and
a new ⚠ ground-rhythm note). §4's archetype table untouched.

**Why the reassignment.** #15 was the last of three archetype-D sections and the one where the
photograph did least. `winter.jpg` carried a **Boston MBTA bus with legible destination signage** —
unusable on a Long Island firm's homepage — and it illustrated nothing: the copy is about icy
walkways, broken pavement, unmarked steps and wet store floors, none of which were in the frame.
Duotoning it produced a near-black band with an empty right half. As with #5, the picture was the
problem, so the picture was removed rather than replaced. **D now runs once on the whole page (#9),
down from three.** That closes the photo monotony §1 exists to eliminate.

F because the section's new structure *is* a dense wall: five hazards ruled across the full width.

**Rule 1 holds.** Full sequence with #15 as F:

```
 #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15 #16 #19 #20
  F   C   G   B   C   D   F   B   G   C   E   F   B   F   C
```

14 transitions, no adjacent repeats. Both joins clear: #14 is E, #16 is B. A stays at zero.
Distribution **C×4, F×4, B×3, G×2, D×1, E×1, A×0** — only A is capped, and both fours are spread
with at least two sections between uses (C: #5, #8, #13, #20; F: #4, #10, #15, #19).

**The real problem was not the photograph — it was the paragraph.** #15 carries the densest legal
reasoning on the page: duty of care, what the owner knew or should have known, and evidence that
disappears once the ice melts. 547 characters of it, set at `{typography.body}` in a 62ch column
overlaid on a dark photograph. Nobody read it. Two changes fix that:

1. **The copy already named its own contents.** Five hazards were buried mid-sentence in that
   paragraph's opening clause. Pulled out as a ruled band, they give the section something
   scannable *before* the reasoning — the reader learns what the section covers without reading a
   word of legal explanation.
2. **The explanation moved up to `{typography.body-lead}` at 72ch**, the widest measure in the
   section. That is deliberate: it is the one paragraph on the page that most needs the size.

**The hazard band is not new copy, and it is `aria-hidden`.** All five labels are verbatim
substrings of paragraph two, which still appears in full and unaltered beneath the band. Because
the band restates the paragraph's own opening clause and sits directly above it, leaving it exposed
would make a screen reader announce the same five hazards twice in a row — once as a list, then as
the sentence. Hidden, nothing is lost: the paragraph carries every word. Recorded as a decision,
not an oversight.

**Copy verified verbatim by diff against the pre-rebuild markup**, not by eye:

| | before | after | |
|---|---|---|---|
| P1 lede | 193 chars | 193 chars | IDENTICAL |
| P2 explanation | 547 chars | 547 chars | IDENTICAL |
| P3 CTA | 172 chars | 172 chars | IDENTICAL |

All five hazard labels confirmed present verbatim in P2.

**Measured at 1440px.**

| Check | Result |
|---|---|
| `filter: url(#…)` in #15 | **0** — elements and pseudo-elements |
| `<img>` · `background-image` | **0 · 0** |
| Hazard columns | 230.391 / 230.406 / 230.391 / 230.406 / 230.391 — **spread 0.015px** |
| Vertical rules | all **132px** = band height exactly, 1px, `rule-cut`; equal to each other, not to their labels |
| Horizontal rules | 3, all 1152px |
| heading → lede | **32px** |
| lede → band | **64px** `clamp(64px, 7vh, 96px)` |
| band → explanation | **64px** `clamp(64px, 7vh, 96px)` |
| explanation → CTA rule | **56px** `clamp(56px, 6vh, 80px)` |
| CTA rule → CTA | 40px |
| Heading left / CTA left | 144 / 144 |
| Type | display-l 56px · body-lead 19px · display-s 20px Cinzel · explanation 19px · CTA 19px/600 |
| Contrast on `stone-pale` | heading, hazards, explanation **14.60:1** · lede 6.37:1 · phone 4.91:1 |
| Bronze in section content | **1** — the phone link, `bronze-ink` |
| Icons | **0** — no SVG in the section at all |
| box-shadow · radii | 0 · all `0px` |
| `scrollWidth` / `clientWidth` | 1425 / 1425 |

Mobile 393px: single column, items 66px (20 + 26 + 20), dividers 345px horizontal, heading
`display-m` at 24px, body **kept at body-lead** — shrinking the dense paragraph on a phone would
undo the one thing this rebuild was for. Reduced motion: instant, all four verticals at 132px, all
three horizontals at 1152px. JS disabled: nothing hidden, every rule at full extent.

**⚠ THIS REBUILD INTRODUCES A §2 GROUND-RHYTHM BREACH AND I HAVE NOT FIXED IT.** §2 permits at most
two consecutive pale sections. Measured on the rendered page, #15 on `stone-pale` produces **four**:

```
#13 form (pale) → #14 sequence (pale) → #15 pivot (pale) → "What to Expect" (pale) → [dark band]
```

Measured against §7's approved inventory alone — which does not contain the legacy "What to Expect"
section — it is still **three**: #13 → #14 → #15. Either way it exceeds the limit. Before this pass
the run was two, because #15 was dark.

**This is visible, not theoretical.** In the 1440px capture the boundary between #14 and #15 is a
faint texture change and nothing more — #14 carries the alternating grain and #15 does not, and
that is the *only* thing separating them. **The pale ground cannot signal a change of chapter while
the section above it is the same pale.** The pivot's most important job is the one thing the
current ground sequence prevents it from doing.

**Proposed, not applied — give #13 the dark field.** §7 already assigns #20 the same
`{component.form-panel}` "on the dark field", so a dark form-panel is a defined variant rather than
an invention, and two identical form panels on identical grounds is its own repetition problem;
one change fixes both. Result: dark → pale → pale, exactly two, and #15 finally gets a ground
boundary above it. **Alternative:** darken #14 instead, which fits §2's "the dark field marks the
page's landmarks" more literally since #14 *is* the second landmark — but #14's drawn connector
already has contrast decisions tuned for the pale ground (its mobile rail was moved to `ink-soft`
for exactly this reason) and would need reworking. Not applied either way: the brief scoped this
pass to #15, and changing a neighbouring section's ground is the CD's call. A **separate
pre-existing three-run** also stands downstream at #16 → "advantage" → #19, untouched by and
unrelated to this change.

**Hairline contrast, flagged.** `rule-cut` on `stone-pale` measures **1.40:1** — the same number
DECISIONS records for #14's mobile spine, where it was found imperceptible and swapped for
`ink-soft`. That precedent does not transfer here and I checked rather than assumed: captured at
**1× device pixel ratio**, not just at 2×, all four vertical rules and all three horizontals read
clearly. #14's failure case was a single thin spine at phone width; these are a dense repeated
array of short lines on a flat ground, which is the reading case §3's token was written for. If the
band ever reads as missing on a low-quality display, `ink-soft` at 6.37:1 is the same fix already
proven on #14 — but it is not needed on the evidence.

**Judgment — does it read as a deliberate pivot?** **Partly, and the shortfall is not in the
section.** Everything internal to #15 announces a change: the type is black on light after four
dark sections' worth of reversed-out copy, the hazard band is a structure nothing above it uses,
and the heading names the new subject plainly. Scrolled into, it clearly reads as a different kind
of section. What it does not yet get is the *boundary* — the moment of crossing — because #14 hands
it the identical ground. The pivot arrives without a threshold. That is the ground-rhythm breach
above, and it is the one outstanding thing between this section and its brief.

**Does the hazard band read as structure?** Yes, unambiguously, and it is the section's strongest
element. Five equal columns with rules running the full band height between two full-width
horizontals reads as a ruled table of contents for the section — architecture, not decoration —
for the same reason #5's divisions work: the rules span the division, not the text. Setting the
labels in Cinzel at `display-s` is what keeps it from reading as a tag list; they are small
headings, and they carry the same inscriptional register as the section heading above them.

The band also does real editorial work rather than ornamental work. Its five items are the five
concrete things in a section otherwise made of abstractions — duty of care, constructive notice,
spoliation of evidence. A reader who takes nothing else from #15 still learns that the firm handles
falls on ice, on broken pavement, on unmarked steps, in wet stores and in the dark. That is §11.4
specificity, extracted from copy that already contained it.

---

### Build pass 20 — #15 hazard band cut

Deletion plus two consequences. The section itself, the `stone-pale` ground, the heading, the lede,
the explanation, the CTA with its rule and phone link, and the absence of photograph and duotone
are all exactly as built in pass 19.

**What went and why.** The five-item hazard row and its two surrounding rules are gone —
`.ds-premises__band`, `.ds-premises__hazards`, `.ds-premises__hazard`, the vertical-rule
pseudo-element, its four staggered draw delays, its mobile stacking block and its reduced-motion
line. Markup and CSS both, no orphans left. "Icy walkways" now appears **once** in the section's
DOM, in the paragraph, where it always was.

The band was wrong for the reason it was built: it set the paragraph's own opening clause as a
ruled five-column row directly above the sentence that contains it. Pass 19 argued that made the
section scannable. Read back on the page it does the opposite — the same five phrases twice in
eight inches, the second time inside the sentence they came from, in a bordered grid. That is a
table, and tables are for data, not for a clause. The section did not need a summary of its own
next paragraph.

**Consequence 1 — the explanation fills the container.** It carried `max-width: 72ch` while the
band sat above it, which gave it a left column to align under. With the band cut, that measure had
nothing to justify it and read as an indent with no cause. Removed: the paragraph now runs the full
1152px, matching the CTA and the rule exactly.

**Consequence 2 — the rhythm closed.** The band contributed two `clamp(64px, 7vh, 96px)` gaps, one
above and one below. Collapsing them into a single gap left the choice of value; both body gaps are
now `clamp(56px, 6vh, 80px)` so they match:

| Gap | Was (with band) | Now |
|---|---|---|
| heading → lede | 32px | **32px** |
| lede → band | 64px | — |
| band → explanation | 64px | — |
| lede → explanation | — | **56px** |
| explanation → CTA rule | 56px | **56px** |
| CTA rule → CTA | 40px | **40px** |

The two gaps around the explanation are now identical, which is what "even" means in a section with
four elements and no centrepiece.

**Motion.** The reveal was a three-step cascade — heading 0 · lede 120 · band 180 · body 300 — and
the band held the 180ms slot. Rather than leave a dead beat in the middle, the body moved **300 →
240ms**. That is the only motion change; nothing new animates and the CTA rule still draws
`scaleX`. Flagged because it was not asked for, but leaving a 180ms silence in a cascade that no
longer has anything to fill it is not "as built", it is a leftover.

**Measured.**

| Check | 1440px | 393px |
|---|---|---|
| Hazard band in DOM | **absent** | **absent** |
| "Icy walkways" occurrences | **1** (the paragraph) | 1 |
| Rules in section | 1, 1152px | 1, 345px |
| Explanation `max-width` | **none** | none |
| Explanation box vs CTA box | 144 / 1152 — **identical** | 24 / 345 — identical |
| Gaps | 32 · 56 · 56 · 40 | 32 · 56 · 56 · 40 |
| Reveal delays | lede 120ms · explanation, CTA, rule 240ms | same |
| Copy | P1/P2/P3 **byte-identical** at 193 / 547 / 172 chars | — |
| images · background-images · filters · box-shadows · svgs | 0 · 0 · 0 · 0 · 0 | same |
| Bronze | 1 — the phone link, `bronze-ink` | same |
| `scrollWidth` / `clientWidth` | 1440 / 1440 | 393 / 393 |

Section height drops 1079 → **782px**.

**⚠ Flagged: the explanation now runs ~137 characters per line at 1440px.** Four lines at the full
1152px measure. The comfortable range is 45–75 and this is well past it — long enough that the eye
has to hunt for the line return, on the one paragraph the last two passes were specifically trying
to make readable. It is exactly what "fill the container" produces at `body-lead` in a 1200px
container, and it is what was asked for, so it is built that way and reported rather than quietly
narrowed. Mobile is unaffected at 39 chars/line.

Worth noting what filling the container did buy, because it is not nothing: the section now has
**two widths instead of four** — everything at 1152px except the lede's deliberate 68ch column.
Before, the heading was 1152, the lede 642, the explanation 950 and the CTA 1152, and the
explanation's odd measure was the thing that read as an unexplained indent. If the character count
matters more than that alignment, the fix is one declaration — a `max-width` around 90ch keeps the
paragraph visibly wide while halving the tracking distance — but it reintroduces the third width.
CD's call.

**⚠ Flagged: F no longer describes this section.** F is "many small units at once", and the hazard
band was the only thing in #15 that was ever many small units. What remains — heading, lede, one
long paragraph, rule, CTA — has no units at all. The letter and the composition have come apart.

By the reading applied to #5, it is now C: a type-only statement, generous air, nothing else. Rule
1 would still hold — #14 is E, #16 is B, and the nearest other C (#13) is separated by #14 — and it
would put C at five uses and F back at three, which breaks no rule since only A is capped. **Not
applied.** Reassigning an archetype twice in two passes is a decision for the CD, not a cleanup I
should make while deleting a row of text. DESIGN.md §7's row has been corrected to describe what is
actually built and marked ⚠, with the proposal recorded beneath the sequence check alongside the
still-open ground-rhythm breach.

**Judgment.** The section is better without the band, and the reason is worth recording because it
cuts against the last pass's own argument. Pass 19 reasoned that pulling the hazards out gave the
reader something concrete before the abstractions. That reasoning was sound and the execution
still failed, because it ignored where the extracted words *went* — directly above their own
source sentence, eight inches from a verbatim repeat. An extraction only works when it is not
adjacent to its origin. The band would have worked as a section of its own, or above a paragraph
that did not begin with the same five phrases; above this one it could only read as duplication
with rules around it.

What is left is quieter and does the pivot's job better than the band did. The pale ground, the
`display-l` heading naming falls, and a paragraph that finally has room are enough to say the
subject has changed. The band was the loudest thing in the section and it was announcing something
the paragraph beneath it already said.

The ground-rhythm breach from pass 19 is **unchanged and still open** — #13, #14 and #15 remain
three consecutive pale sections, four counting the legacy "What to Expect", and the pivot still
arrives without a boundary above it. That remains the section's largest outstanding problem and it
is not fixable from inside #15.

---

### Build pass 21 — #10 rebuilt clean-sheet as a three-column case index

Archetype unchanged: §7 already assigns #10 **F** and calls it "a directory, not a section." No
reassignment, so §7 needed no edit. Ground stays `stone-deep`; neighbours #9 (D) and #11 (B) are
untouched and Rule 1 is unaffected.

**Deleted first, in full.** `.index-dark`, `.index-head`, `.cindex` and all its descendants,
`.ci-n`, `.index-foot`, plus both responsive blocks — **~110 lines removed from styles.css**, and
the old `<ol class="cindex">` markup with it. Four shared selectors that keyed on `.index-dark`
were rewired rather than orphaned (below). Zero references to any of those class names remain
anywhere in the repo.

**Why a grid and not the register.** The previous treatment set the entries as full-width ruled
rows — the name incised left, the carrier's argument beside it. That is a *register*, and a
register is read **down**, one row at a time. At ~110px a row it ran past two screens, so the
reader had to scroll a list to discover what the list contained. A directory is read **across**:
scan the names, find yours, read one description. Three columns puts all eleven on one screen,
which is the only arrangement where the reader learns the scope before committing to any of it.
Section height drops **from a two-screen register to 1302px**.

**⚠ THERE ARE ELEVEN CASE TYPES, NOT TEN.** The brief specifies ten and a 3×4 grid whose "last row
has one empty cell." The build has always carried eleven, and body copy is locked, so **all eleven
are here verbatim and in their existing order** — dropping one would be a cut, which neither the
brief ("verbatim, in existing order", "no new copy") nor CLAUDE.md permits.

The layout instruction is right and only the count is off: **eleven items in three columns give
exactly one empty cell.** Ten would have left two. The 3×4 grid the brief describes is the eleven-
item grid.

**Copy verified by diff, not by eye** — every name and description captured from the file before
editing and compared after:

```
baseline items 11  ·  rendered items 11
 1..11  IDENTICAL   (names and descriptions)
 lede   IDENTICAL
 foot   IDENTICAL
>>> ALL COPY VERBATIM, ORDER PRESERVED
```

The `01`–`11` numerals from the old register are gone. Numerals are #14's device and these case
types are not ranked — the old CSS had already hidden them with `.ci-n { display: none }` for that
exact reason, so this only removes markup that was never rendering.

**The twelfth cell exists and is empty on purpose.** Without it the rule above row four would stop
two thirds of the way across and the column-three division would end early — a broken table rather
than a full one with a vacancy. It renders as **384 × 192px of empty ground, zero text**, carries
its own two rules, and is `aria-hidden` so it is not announced as a list item. On mobile it has
nothing to divide and is removed outright rather than left drawing a stray rule under the last
entry.

**Measured at 1440px.**

| Check | Result |
|---|---|
| Items rendered | **11**, all names present, order preserved |
| Grid | `384px 384px 384px`, `gap: 0`, `align-items: stretch` |
| Column width spread | **0.000px** |
| Row heights | 214 / 214 / 214 · 192 / 192 / 192 · 192 / 192 / 192 · 192 / 192 / 192 — **every row internally equal** |
| Vertical rules | **8**, each exactly its row's height (214 or 192px), `vRulesSpanRow: true` |
| Horizontal rules | 9 cell-width segments butting into **3 continuous 1152px lines** |
| Empty cell | 384 × 192px, 0 characters, not stretched content |
| heading L · first cell text L · foot L | **144 · 144 · 144** |
| Bracketing rules | 1152px both |
| Gaps | heading→lede 32 · lede→rule 56 · rule→grid 0 · grid→rule 0 · rule→foot 40 |
| Type | display-l 56 · body-lead 19 · display-s 20 Cinzel · body-s 15 · body-lead 19 |
| Bronze in section content | **1** — the phone link |
| svg · img · box-shadow · radii | 0 · 0 · 0 · all `0px` |
| `scrollWidth` / `clientWidth` | 1425 / 1425 |

Mobile 393px: single column, entries divided by horizontal `rule-cut-dark` at 24px vertical
padding, heading `display-m`, names `display-s`, descriptions `body-s`, empty cell `display: none`.
Reduced motion and JS-disabled both hold — every rule at full extent, nothing hidden.

**Deviation, stated: the brief says "cell padding 28px"; column one has no left padding and column
three no right.** A uniform 28px would have inset the case-type names 28px from the heading, the
lede, both rules and the closing paragraph — every other element in the section sits on the
container margin, and the grid alone would have looked accidentally indented. Dropping the outer
padding puts all four text edges on 144px exactly (measured above) while the full 56px survives
between columns, 28px either side of every rule. Same pattern #5 and #15's band already use.

**⚠ A bug I introduced and caught in verification: doubled hairlines on mobile.** The mobile block
killed the row rules with `.ds-caseindex__cell::after { content: none }` — specificity **0-1-1**,
which loses to the base `.ds-caseindex__cell:nth-child(n+4)::after` at **0-2-1**. So from the
fourth entry down every cell rendered **two coincident 1px lines at the same y**: the horizontal
`::before` divider and the still-live row `::after`. Both are `rule-cut-dark` at .19 alpha, so they
composited to roughly .34 and those dividers were visibly brighter than the three above them.
Caught by counting rendered pseudo-elements at 393px — `h-rules 9` where it should have been 0 —
not by looking, because at .19 versus .34 alpha on navy the difference is real but easy to miss.
Fixed by matching the base rule's specificity.

That is the third defect in this section series traceable to **specificity against computed state**
rather than to layout: pass 16's grain, pass 17's mid-reveal rects, and now this. All three were
invisible until something was measured.

**Shared selectors rewired, not orphaned.** Four rules in styles.css keyed on `.index-dark`:

1. **Bronze focus outline on dark grounds** — `.ds-caseindex` added. **And `.ds-statement` added,
   which is a fix to #5 I found while here.** #5 was never in that list, so its phone link took the
   page default `bronze-ink`, which measures **2.94:1 on stone-deep** — under the 3:1 WCAG 1.4.11
   floor for a focus indicator. Both links now resolve to `bronze` at **7.49:1**. (#15's link is on
   pale and correctly keeps `bronze-ink` at 4.91:1.)
2. **Grain alternation** — `.ds-caseindex` added to the exclusion list, so the section is flat
   `stone-deep` like #5 and #15 rather than grained. Verified: the eight grained sections are
   unchanged from before this pass, and #5, #10 and #15 all read `background-image: none`.
3. **The quarried dark wash** (`.dark, .index-dark, .whyband, .foot`) — `.index-dark` removed. The
   section takes flat stone-deep, consistent with the other rebuilt dark sections.
4. **Two dead `.index-dark .wrap--read > .h2::before` descendant rules** — the class and that
   markup are both gone; selectors dropped.

**Judgment.** It reads as a directory now, which is the whole assignment, and the change is
structural rather than cosmetic — the register and the index contain identical words and behave
completely differently. Three columns of ruled cells is a thing you *survey*; eleven stacked rows
is a thing you *read through*. The names in Cinzel at `display-s` carry the scan and the
descriptions in `body-s` sit under them without competing, so the eye can move name-to-name across
the grid and drop into one cell when it finds the right one.

The empty twelfth cell is the detail that makes it work rather than a compromise. A grid that stops
mid-row reads as truncated — as if there were a twelfth case type that failed to load. Completing
the frame and leaving one cell empty reads as a table with a vacancy, which is what a directory of
eleven things in a three-wide frame actually is.

The full-height rules do the same work here as in #5: they divide the field first and the text sits
inside it, rather than underlining each entry. That is what stops eleven cells reading as eleven
cards, which §3 forbids outright and which is the single easiest way this section could have gone
generic.
