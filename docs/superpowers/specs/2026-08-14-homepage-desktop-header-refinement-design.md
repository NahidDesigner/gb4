# Homepage Desktop Header Refinement

## Scope

Correct the homepage header behavior and refine its desktop presentation only. The locked homepage hero, the existing bottom mobile Call Now / Free Case Review bar, footer, inner-page markup, and inner-page mobile header behavior remain unchanged.

## Responsive behavior

At viewport widths up to and including 768px, the homepage's full `#dsHeader` is not rendered. The locked hero already contains the homepage Menu and Search controls, and the unchanged bottom action bar provides the two mobile conversion actions. This removes the redundant header shown immediately after the hero.

Inner pages retain their existing `.railhead` at the top of the page with `position: absolute`; they do not become sticky.

## Desktop geometry

At ordinary desktop widths, render the homepage header logo at exactly 128px tall with proportional width. Increase the header to 136px so the mark has deliberate breathing room and remains vertically centered. Larger viewports may step the logo up modestly rather than scaling text measure or utility controls.

## Premium translucent surface

Keep the mineral-paper translucency, but give it more material definition through a subtle white-to-coastal-mist tonal layer, a fine Atlantic-blue lower rule, and controlled soft depth. Do not use `backdrop-filter`, glass blur, decorative gold, or a generic navy-and-gold luxury treatment. The logo remains the only gold-bearing visual in the header; the telephone action continues to use Atlantic blue with the restrained survey-orange action edge.

## Verification

- Extend the existing homepage header contract first and observe it fail for the current 104px logo and visible mobile header.
- Verify the homepage header is hidden at both 375px and 768px.
- Verify a representative inner page still has a top-positioned, non-sticky mobile rail header.
- At desktop, measure the 128px logo, centered placement, containment, utility clearance, and page overflow.
- Capture and review paired desktop and 375px homepage screenshots, plus a mobile inner-page geometry check.
- Preserve the hero, footer, bottom mobile action bar, page copy, section inventory, and `DESIGN.md` §6 composition rules.
