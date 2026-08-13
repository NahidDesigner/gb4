# Homepage Header Logo and Mobile Call Now

## Scope

Refine only the homepage site header that appears immediately after the locked hero. Keep the hero, mobile sticky call bar, footer, body copy, analytics, schema, search overlay, and every inner-page header unchanged.

## Visual direction

Use a restrained translucent mineral-paper header so the native navy-and-gold logo remains the visual anchor. The surface may let a small amount of the underlying page tone show through, but it must not use blur, saturation, or other glass-effect treatment prohibited by `DESIGN.md` §1.

Increase the logo's rendered size within a proportionately taller header. Preserve its intrinsic aspect ratio, center alignment, native colors, and accessible home-link label. Header utilities remain visually subordinate to the mark.

## Responsive controls

Desktop and tablet retain the existing Menu, Search, and visible phone-number call action.

At phone widths, retain Menu on the leading side, hide Search, and show the existing telephone link as a concise `Call Now` button on the trailing side. Use one semantic `tel:+15164441000` anchor with responsive labels rather than duplicate call links. The button must provide a minimum 44px touch target and a visible keyboard focus state.

The bottom mobile action bar remains unchanged, as required by `DESIGN.md` §§2 and 9.

## Implementation boundary

- `index.html` receives only the responsive call-label spans and the stylesheet cache-buster change.
- `homepage-atlas.css` receives only homepage-scoped header refinements and phone-width visibility/geometry rules.
- A focused source contract verifies the requested semantics and guards the locked elements.
- No JavaScript changes are required; desktop Search keeps its existing `searchOpen2` binding.

## Verification

- Run the new focused source contract through a red-green cycle.
- Run the full Python test suite and existing homepage Node contract.
- At desktop and 375px, measure header height, logo bounds, centered logo alignment, utility overflow, visible control count, call target size, and page overflow.
- Capture and review paired desktop and mobile screenshots. Make at most one batched correction pass and one confirmation pass.
- Confirm the hero, footer, sticky mobile call bar, and `DESIGN.md` §6 section-composition rules remain unaffected.
