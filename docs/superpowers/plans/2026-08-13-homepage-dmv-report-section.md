# Homepage DMV Report Resource Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the approved responsive MyNYAccident.com resource section after the homepage's post-crash sequence while preserving the reference composition and using the site's real fonts.

**Architecture:** Replace the small `#first48` resource row with a standalone semantic `#dmv-report` section before `#premises`. Compose the client-supplied `assets/report-onlybg.webp` and transparent `assets/report-phone.webp` as independent decorative layers, keep meaningful copy and links in HTML, and trigger the phone's one-shot perspective settle from the existing homepage observer.

**Tech Stack:** Static HTML5, CSS, Web Animations API, existing IntersectionObserver, authored inline SVG icons, self-hosted Atlas font aliases, Python `unittest`, Node homepage contract, and local browser geometry and screenshot QA.

---

### Task 1: Protect the section contract

**Files:**
- Create: `tests/test_homepage_dmv_report_section.py`
- Read: `index.html`
- Read: `homepage-atlas.css`

- [ ] **Step 1: Write a source-level regression test**

Create tests that require one `#dmv-report` section between `#first48` and `#premises`, the MyNYAccident.com and official DMV external links, the non-affiliation disclosure, the supplied asset path and dimensions, no live phone-screen overlay, Atlas Display/Text ownership, and a 760px responsive composition.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: failures because the standalone section, asset, and scoped rules do not exist.

### Task 2: Validate the initial supplied image plate

**Files:**
- Verify: `assets/report-onlybg.webp`
- Verify: `assets/report-phone.webp`

- [ ] **Step 1: Inspect the supplied plate**

Confirm the background includes the courthouse, damaged car, navy copy field, and intended navy/gold lighting. Confirm the phone asset has transparency and contains the complete phone mockup.

- [ ] **Step 2: Record intrinsic dimensions**

Use the assets' intrinsic `1774 × 887` and `1024 × 1536` dimensions in the image markup and ensure no separate phone-screen text or button is layered over the phone.

### Task 3: Add the semantic section

**Files:**
- Modify: `index.html`
- Test: `tests/test_homepage_dmv_report_section.py`

- [ ] **Step 1: Replace the old resource row**

Remove only `.ds-sequence-section__foot` from `#first48`. Insert `#dmv-report` immediately after the closing `</section>` for `#first48` and before `#premises`.

- [ ] **Step 2: Build the approved content hierarchy**

Add the heading, introduction, four icon-led benefits, bordered MyNYAccident.com action, accurate disclosure, official DMV information link, decorative background image, and bottom closing band. Use authored inline SVG with `aria-hidden="true"`; keep content in semantic headings, paragraphs, lists, and anchors.

- [ ] **Step 3: Run the focused test**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: placement and HTML assertions pass; CSS assertions still fail.

### Task 4: Match the approved desktop and mobile design

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tests/test_homepage_dmv_report_section.py`

- [ ] **Step 1: Add desktop composition rules**

Scope all rules beneath `.atlas-home #dmv-report`. Use `Atlas Display` for headings and `Atlas Text` elsewhere; implement the navy field, gold rules, 48/52 split that clears the baked phone, four benefit columns, image treatment, bordered CTA panel, disclosure block, and bottom band.

- [ ] **Step 2: Add tablet and phone rules**

At `max-width: 1000px`, reduce heading scale and wrap benefits two-by-two. At `max-width: 760px`, stack the composition, make the media a bounded full-width scene, preserve 44px targets, and prevent horizontal overflow.

- [ ] **Step 3: Run focused and full automated checks**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: all focused tests pass.

Run: `node tools/homepage_contract.mjs`

Expected: homepage contract passes after its obsolete `#first48` closing-row expectations are updated to require the new standalone section.

Run: `python3 -m unittest discover -s tests -v`

Expected: all repository tests pass with zero failures or errors.

### Task 5: Verify layout and appearance

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `assets/report-onlybg.webp`
- Verify: `assets/report-phone.webp`

- [ ] **Step 1: Run the Impeccable detector**

Run: `node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html homepage-atlas.css`

Expected: no new unexplained high-severity findings in the changed section.

- [ ] **Step 2: Run desktop and phone geometry checks**

At 1440px and 375px, confirm `scrollWidth <= clientWidth`, the section and its inner grid do not clip, all four benefits are visible, the CTA and disclosure are visible, and the desktop/mobile image placement preserves the car and phone focal points.

- [ ] **Step 3: Capture paired screenshots**

Capture and review the complete `#dmv-report` section at 1440px and 375px. Apply at most one batched CSS correction, then capture one confirmation pair if needed.

- [ ] **Step 4: Review the diff**

Run: `git diff --check && git diff -- index.html homepage-atlas.css tests/test_homepage_dmv_report_section.py docs/superpowers/specs/2026-08-13-homepage-dmv-report-section-design.md docs/superpowers/plans/2026-08-13-homepage-dmv-report-section.md`

Expected: no whitespace errors and no unrelated homepage, hero, footer, form, SEO, or inner-page changes.

### Task 6: Separate the background and phone layers

**Files:**
- Modify: `tests/test_homepage_dmv_report_section.py`
- Modify: `index.html`
- Modify: `homepage-atlas.css`
- Verify: `assets/report-onlybg.webp`
- Verify: `assets/report-phone.webp`

- [ ] **Step 1: Write failing source-contract tests**

Require a `.dmv-report__visual` wrapper containing `report-onlybg.webp` at `1774 × 887` and `report-phone.webp` at `1024 × 1536`. Require the phone element to precede `.dmv-report__inner` in source order, require the mobile wrapper to precede content in layout, and reject `assets/report.webp` plus any `.dmv-report__phone-ui` overlay.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: failures for the missing two-layer wrapper and old combined asset.

- [ ] **Step 3: Implement the two-layer markup and CSS**

Replace the combined scene image with a decorative visual wrapper. On desktop, make the wrapper cover the section, keep the background full-bleed, and position the phone with a contained width/height inside the right media field. At `max-width: 760px`, make the wrapper static and first, center the entire phone over the background, then render `.dmv-report__inner` below it.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: all focused tests pass.

### Task 7: Add the perspective-settle entrance

**Files:**
- Modify: `tests/test_homepage_dmv_report_section.py`
- Modify: `homepage-atlas.js`

- [ ] **Step 1: Write a failing motion-contract test**

Require `homepage-atlas.js` to select `#dmv-report .dmv-report__phone`, use the existing section observer to call `Element.animate`, use a `700ms` duration and `cubic-bezier(0.16, 1, 0.3, 1)`, choose desktop and phone keyframes by the `760px` media query, and bypass animation when reduced motion or the Web Animations API is unavailable.

- [ ] **Step 2: Run the motion test and verify RED**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: failure because the phone entrance is not implemented.

- [ ] **Step 3: Implement the minimal one-shot entrance**

Add a small `animateDmvPhone()` helper to `homepage-atlas.js`. Call it when the existing reveal observer first intersects `#dmv-report`; the observer already unobserves each section, so the entrance runs once. Keep the phone visible by default and return without animation for reduced motion, missing observer support, or missing `Element.animate`.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run: `python3 -m unittest tests.test_homepage_dmv_report_section -v`

Expected: all focused tests pass.

### Task 8: Responsive and motion verification

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `homepage-atlas.js`
- Update: `mockups/dmv-report-section-desktop.png`
- Update: `mockups/dmv-report-section-mobile.png`

- [ ] **Step 1: Run automated verification**

Run: `python3 -m unittest discover -s tests -v && node tools/homepage_contract.mjs && git diff --check`

Expected: zero failures, homepage contract pass, and no whitespace errors.

- [ ] **Step 2: Run paired computed-geometry checks**

At desktop and 375px, confirm no horizontal overflow; the phone's rendered bounds stay inside `.dmv-report__visual`; all four benefits, CTA, disclosure, and closing band remain present; and no content overlaps the phone.

- [ ] **Step 3: Verify animation and fallback**

Confirm the phone receives one running animation on first entry, settles at its CSS resting transform, and does not animate when reduced motion is active. Confirm the direct homepage console has no warnings or errors.

- [ ] **Step 4: Capture and review paired screenshots**

Capture the whole section on desktop and mobile. Use at most one batched correction pass and one confirmation pass.
