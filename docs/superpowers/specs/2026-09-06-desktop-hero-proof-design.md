# Desktop Hero Proof Composition

## Scope

Update only the homepage hero's desktop proof and expectation copy at viewports wider than 640px. Preserve the approved mobile Vimeo hero, mobile logo and menu placement, all copy, links, semantics, and every post-hero section.

## Composition

The desktop copy follows the supplied client reference in one centered, compact stack:

1. `INJURED?` is the leading white serif line.
2. `OVER` sits directly below in small tracked white capitals, framed by restrained gold rules.
3. `$100 MILLION+` is the dominant gold serif proof line.
4. `RECOVERED FOR CLIENTS` replaces the desktop-only `IN SETTLEMENTS` label.
5. `YOUR EXPECTATIONS SHOULD BE MET.` and `WE EXCEED THEM.` form the closing two-line statement, with the final line in gold.

Sizing is fluid across desktop widths and capped to preserve the reference proportions. The stack remains centered and crop-safe at laptop heights. The existing desktop logo/header and scroll cue remain in place.

## Implementation boundary

- Reuse the existing semantic hero elements and desktop/mobile label spans.
- Change the desktop label text to `Recovered for clients`; the mobile label remains the same.
- Apply all layout and typography changes inside a `min-width: 641px` media query.
- Keep the desktop Vimeo layer hidden and the mobile Vimeo behavior unchanged.
- Do not alter factual claims, phone details, analytics, forms, navigation, footer, or sticky mobile actions.

## Verification

- Contract tests assert the exact proof order, desktop label, and desktop-only CSS scope.
- Computed geometry confirms centered alignment, no overlap, and no horizontal overflow at 1440px and a narrower laptop width.
- Paired screenshots confirm the desktop reference treatment and the unchanged 375px mobile composition.
- Reduced-motion and keyboard behavior remain unchanged because the edit adds no interaction or motion.
