# Mobile Hero Short-Viewport Spacing Design

## Scope

Fix the mobile hero overlap visible in Safari-height viewports without changing the approved logo artwork, hero copy, CTA, menu, video, fallback image, or desktop layout.

## Approved behavior

At viewport widths up to 640px and heights up to 760px, the glowing logo scales to `min(88%, 20rem)`, its extra downward translation is removed, and the hero copy begins at `15.75rem`. At a 375 × 667 viewport this must leave positive space between the logo and “INJURED?” and between the phone CTA and scroll cue. Taller mobile layouts retain their existing dimensions and spacing.

## Verification

Add a regression assertion for the short-height rules, run the homepage test suite, and perform computed-geometry plus screenshot checks at 375 × 667, 375 × 812, and desktop width. Publish only after the checks pass.
