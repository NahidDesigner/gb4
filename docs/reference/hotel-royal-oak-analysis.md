# Reference: hotelroyaloak.com — the reviewer's own taste, measured

Live review, 2026-08-05, desktop 1440px and mobile 390px, DOM + stylesheet
inspection. This is the site Haris built himself and cited as his standard.
DESIGN.md §1 and §7 rest on these findings.

## Stack — the part that matters most

- **No animation library. No framework. Not WordPress.** No GSAP, AOS, jQuery,
  Elementor, Swiper — nothing. Hand-written HTML/CSS/JS.
- **27 bespoke keyframe animations**, every one named for the object it
  animates: `sunSpin` (90s/120s counter-rotating hero rays), `coindrop` (with
  overshoot bounce, on a parking-meter module), `tvsnow` (`steps(3)` static on
  a TV module), `qrlaser` (scanning line on a QR), `storyBulb` (marquee bulbs),
  `tick` (news ticker), `marquee`, `blink` (live dots), `cardIn`, plus swipe
  hints for touch. Zero generic fade-up-only sections.
- `prefers-reduced-motion` handled (6 rules).
- No preloader/splash of any kind — his instruction to remove ours matches his
  own baseline.

## Motion physics (imported into DESIGN.md §7 verbatim)

Transitions 0.12s–0.25s on `cubic-bezier(0.2, 0.8, 0.2, 1)`. Snappy,
purposeful, never languid. Long durations exist only on ambient loops
(90s sun, 60s marquee).

## Type

- Display: **Dela Gothic One** — heavy geometric, uppercase, 72px H1,
  letter-spacing −1.08px, line-height 1.0.
- Body: Outfit. Condensed: Big Shoulders Display. Data/labels: **DM Mono**
  (we share this family deliberately).
- **Headline formula, used everywhere: 2–3 tight lines, one word switches
  colour/style.** "A 1954 motor inn, REBUILT for how people travel now." /
  "Not the same box you'd get DOWNTOWN" (italic gold). DESIGN.md §4 adopts the
  formula, re-voiced.

## Palette (NOT imported — register is wrong for law)

Warm brown-black `#1A1612`, cream `#FEFAE0`, orange `#E85D04`, red-orange
`#FF4D26`, yellows/ambers. Radii everywhere: 4–999px, pills and stickers.
What transfers is the *warmth* (his grounds are warm, v1's were cold grey) —
not the hues, not the corners.

## The design philosophy — the actual lesson

**Every section is a built object, not a layout:**

- Comparison section = **two paper receipts** in monospace with dotted leaders,
  "THE LOCAL PICK" vs "THE OTHER ONE", a VS badge between.
- History = a **scrapbook**: masking tape, postcards, clickable year nodes
  (1954 BUILT → HEYDAY → LOCAL STOP → FADED → REBORN).
- **Live weather module** (Open-Meteo, cached 30 min) on a hotel homepage —
  useful, diegetic, unexpected. Our Clock (DESIGN.md §8.5) is the answer to it.
- Stay-builder, live events feed, social feed, 8 mega menus, 4 videos.
- Homepage: **16,914px tall, ~14 distinct invented modules.**
- Conversion furniture never absent: sticky BOOK NOW, TEXT US chip, phone in
  nav, a video concierge widget.

## What this means (already encoded in DESIGN.md)

He measures **craft density and intent**, not a particular style. v1 failed his
eye because ~0 sections named an object. The rebuild imports: ideas-per-section,
object-named animations, his motion physics, confident type scale, one live
module, hand-built stack, ever-present conversion furniture. It leaves: orange,
pills, stickers, the playful voice — his own words ("old money means classy")
forbid porting his register onto a law firm.
