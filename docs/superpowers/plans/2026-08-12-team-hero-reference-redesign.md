# Team Hero Reference Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the `/our-team/` hero to match the supplied navy-and-gold split reference with the requested attorney photograph and a deliberate mobile layout.

**Architecture:** Replace the current title-only section with one semantic `.team-hero` component in `our-team/index.html`. Add route-scoped styles at the end of `inner-atlas.css`, using a 600px desktop height, the single supplied full-bleed image, a translucent navy pseudo-element, shared CSS seam variables, and a two-column lower content row so no new JavaScript or runtime dependency is introduced. Mobile places the content over the same top-anchored image with a continuous navy overlay.

**Tech Stack:** Static HTML5, CSS custom properties, CSS Grid, `clip-path`, Python standard-library contract tests, browser screenshot QA.

---

### Task 1: Pin the hero contract

**Files:**
- Create: `tests/test_team_hero.py`
- Read: `our-team/index.html`
- Read: `inner-atlas.css`

- [x] Write tests that require the new semantic section, the exact requested image path, one H1, the reference copy, route-scoped desktop styles, and a mobile breakpoint.
- [x] Run `python3 -m unittest tests/test_team_hero.py -v` and confirm it fails because `.team-hero` does not exist yet.

### Task 2: Implement the semantic hero

**Files:**
- Modify: `our-team/index.html`

- [x] Replace only the title-band section with the `.team-hero` structure.
- [x] Keep “Our Legal Team” as the only H1, use the user-supplied wording verbatim, and provide useful image alt text.

### Task 3: Implement the responsive composition

**Files:**
- Modify: `inner-atlas.css`

- [x] Add scoped desktop layout, photo crop, navy overlays, diagonal seam, typography, and promise lockup styles.
- [x] Add tablet adjustments and a below-720px stacked mobile composition.
- [x] Run `python3 -m unittest tests/test_team_hero.py -v` and confirm all contract tests pass.

### Task 4: Visual and geometry QA

**Files:**
- Verify: `our-team/index.html`
- Verify: `inner-atlas.css`

- [x] Serve the static site and capture one desktop plus one 375px screenshot.
- [x] Measure overflow, hero and image bounds, H1 line count, copy containment, and mobile action-bar clearance.
- [x] Apply at most one batched correction, then run one confirmation pass.
- [x] Run the Impeccable detector once on the changed HTML and CSS.
