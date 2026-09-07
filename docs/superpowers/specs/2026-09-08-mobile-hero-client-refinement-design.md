# Mobile Hero Client Refinement Design

## Goal

Refine the homepage hero on mobile so the client logo, “INJURED?” line, moving/static background, and menu control reproduce the hierarchy in the supplied reference without changing copy, markup, desktop behavior, or any post-hero section.

## Approved direction

- Reduce the mobile logo artwork by approximately 8–10 percent at both regular and short phone heights.
- Preserve the supplied transparent assets/gb-logo-empire-glow.png artwork and its baked gold/blue glow. Because the baked glow loses contrast over the bright sky, place a soft mobile-only radial glow behind the artwork: gold behind the G, blue behind the B, and a restrained dark center for separation. Keep the existing offset drop shadow for edge depth.
- Reduce only .hero-proof__injured; keep “Over,” “$100 Million+,” the recovery label, body statement, phone action, and scroll cue unchanged unless collision prevention requires positioning.
- Move the mobile Vimeo frame and the matching fallback poster downward by the same optical amount so loading, reduced-motion, and playback states share one crop.
- Move only the mobile menu stack upward. Keep its 64px touch target and focus behavior unchanged.
- Apply the refinement only at max-width: 640px; desktop remains governed by the existing desktop rules.

## Responsive targets

- Regular mobile (375 × 812): the logo remains dominant but clearly separated from “INJURED?”; the menu sits closer to the safe top edge; the building/sky crop reads lower.
- Short mobile (375 × 667): the reduced logo and heading preserve a positive visual gap, and the call action and scroll cue remain reachable without horizontal overflow.
- Desktop (1440 × 900): logo, background, copy, menu/header, and spacing remain unchanged.

## Verification

- Add CSS contract assertions for the smaller mobile logo, smaller mobile “INJURED?” size, downward video/poster crop, upward menu position, preserved glow artwork, and new cache revision.
- Prove the new assertions fail before editing production CSS, then pass after the minimal implementation.
- Run the complete Python suite, homepage contract, hero-video runtime, CSS quality detector, and git diff check.
- Perform computed-geometry checks and paired screenshots at 375 × 667, 375 × 812, and 1440 × 900.

## Scope and authority

This is an explicit client-directed exception to the normally locked hero boundary in DESIGN.md §2. All other DESIGN.md rules remain active. No copy, HTML semantics, section inventory, body archetype, analytics, form behavior, footer, or sticky action bar changes are authorized.
