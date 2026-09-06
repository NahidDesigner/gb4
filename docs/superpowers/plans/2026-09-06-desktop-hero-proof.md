# Desktop Hero Proof Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Match the supplied desktop hero proof hierarchy while preserving the approved mobile hero.

**Architecture:** Reuse the existing semantic hero markup and add a final desktop-only CSS authority block at the 641px breakpoint. Update only the desktop label text and stylesheet cache key; mobile-specific selectors remain authoritative below 641px.

**Tech Stack:** Static HTML, CSS media queries, Python `unittest`, Chrome DevTools Protocol visual QA.

---

### Task 1: Lock the desktop hero contract

**Files:**
- Modify: `tests/test_homepage_mobile_video_hero.py`

- [ ] **Step 1: Write the failing tests**

Add assertions that the hero markup preserves the requested order, uses `Recovered for clients` for both responsive labels, and includes a `DESKTOP HERO PROOF` CSS block scoped to `@media (min-width: 641px)`. Assert that the desktop block displays `.hero-proof__injured`, hides `.hero-h1__injured`, keeps the main figure on one line, and uses the supplied centered hierarchy.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python3 -m unittest tests.test_homepage_mobile_video_hero`

Expected: FAIL because the desktop label is still `in Settlements` and the desktop authority block does not exist.

### Task 2: Implement the desktop-only composition

**Files:**
- Modify: `index.html:20`
- Modify: `index.html:431-437`
- Modify: `homepage-atlas.css` after the mobile hero authority block

- [ ] **Step 1: Update the desktop label and cache key**

Change the desktop label to `Recovered for clients` and bump the stylesheet query to `mobile-video-hero-3` so the live preview receives the new CSS.

- [ ] **Step 2: Add the minimal desktop authority block**

Add `@media (min-width: 641px)` rules that:

- show `.hero-proof__injured` as the leading white serif line;
- create a compact centered grid with deliberate tight/generous gaps;
- scale `$100 Million+` fluidly without wrapping;
- style `Recovered for clients` as small tracked capitals;
- remove the duplicate `Injured?` from the expectation sentence;
- keep `We exceed them.` on its own gold line;
- preserve the existing header, background, scroll cue, and mobile rules.

- [ ] **Step 3: Run the focused tests and verify GREEN**

Run: `python3 -m unittest tests.test_homepage_mobile_video_hero tests.test_homepage_header_logo_call_now`

Expected: all focused tests pass.

### Task 3: Verify behavior and responsive rendering

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Create: `artifacts/homepage-hero-desktop-proof-1440.png`
- Create: `artifacts/homepage-hero-desktop-proof-1024.png`
- Create: `artifacts/homepage-hero-mobile-proof-375.png`

- [ ] **Step 1: Run the full automated checks**

Run: `python3 -m unittest discover -s tests && node tools/homepage_contract.mjs && node --check homepage-atlas.js && git diff --check`

Expected: 82 or more tests pass, the homepage contract passes, JavaScript syntax is valid, and the diff has no whitespace errors.

- [ ] **Step 2: Run the layout detector**

Run: `node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json --scope layout homepage-atlas.css index.html`

Expected: no unexplained findings.

- [ ] **Step 3: Measure desktop and mobile geometry**

Use Chrome DevTools Protocol at 1440×900, 1024×768, and 375×900. Record element rectangles for the logo, menu, proof block, expectation block, and scroll cue. Confirm zero horizontal overflow and no intersections between adjacent hero groups.

- [ ] **Step 4: Review paired screenshots**

Capture desktop and mobile screenshots. Confirm the desktop squint order is `INJURED?` → `$100 MILLION+` → expectation statement, and that the 375px mobile composition is unchanged.
