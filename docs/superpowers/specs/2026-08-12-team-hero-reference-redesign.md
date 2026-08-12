# Team Hero Reference Redesign

## Scope

Replace only the first hero section on `/our-team/`. Preserve the existing masthead, team roster, CTA, footer, action bar, metadata, schema, and JavaScript behavior.

## Direction

The supplied screenshot is the visual authority for this section. The supplied `assets/imgi_40_GW-Law_about_main_img.webp` photograph fills the hero, a translucent deep-navy field overlays its left side, and a narrow gold diagonal seam shares the same clipping geometry. The site’s self-hosted typography remains in use: Atlas Display for the title and Atlas Text for supporting copy.

The reference wording is treated as user-supplied hero content. “Our Legal Team” remains the only H1 and is split visually so “Team” receives the restrained gold emphasis.

## Desktop composition

- The hero starts directly below the existing fixed masthead and is exactly 600px tall at desktop widths.
- The eyebrow and two-line H1 lead the left field; the description and promise lockup use a balanced two-column lower row instead of being compressed into one narrow stack.
- The requested photograph is full-bleed, cropped to keep both attorneys visible and dominant, and remains visible beneath the translucent left overlay.
- A clipped navy overlay and 1px gold diagonal line share the same seam variables, keeping the gold edge aligned between the attorneys without adding JavaScript.
- No secondary photograph is loaded inside the hero. The requested attorney photograph is the only image.

## Mobile composition

- Below 720px, the diagonal split resolves into one layered hero.
- The attorney photograph is anchored at the top, a continuous navy overlay fades down the image, and all hero content sits above that media layer.
- Body text stays at least 16px, the H1 fits without clipping, the page has no horizontal overflow, and the existing sticky action bar remains unchanged.

## Verification

- Static contract tests confirm the requested asset, semantic structure, reference wording, and responsive selectors.
- Browser QA captures desktop and 375px screenshots.
- Computed geometry checks confirm no horizontal overflow, hero bounds, title wrapping, content containment, and both attorneys’ image visibility.
