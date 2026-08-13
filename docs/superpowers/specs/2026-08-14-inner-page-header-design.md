# Inner-page header refinement

## Approved direction

Extend the approved homepage header hierarchy to every non-homepage page without changing page content or hero composition.

- Desktop header: 136px tall with a proportionally scaled 128px logo.
- Mobile header: visible once at the top of the page, 96px tall with an 86px logo, and never sticky.
- Surface: premium translucent mineral paper with a restrained Atlantic divider and soft depth; no glass blur.
- Actions: menu and search remain available, while Call Now uses Atlantic blue with a survey-orange outline on desktop and remains hidden on mobile where space is constrained.
- Homepage: unchanged; its mobile header remains hidden as already approved.

## Architecture

Add one `site-header.css` layer after each inner page's theme stylesheet. This consolidates the duplicated header refresh currently present in `inner-atlas.css` and `practice-areas/practice-atlas.css` without touching their page-section styling or markup hooks.

## Acceptance checks

- All 24 inner pages load the current shared header layer; the homepage does not.
- At desktop width the computed header/logo heights are 136px/128px.
- At 375px the computed header/logo heights are 96px/86px, menu and search targets are at least 44px, and there is no horizontal overflow.
- After scrolling on mobile, the header moves out of the viewport rather than sticking.
- Desktop and mobile screenshots are reviewed in one paired pass, with at most one correction pass.
