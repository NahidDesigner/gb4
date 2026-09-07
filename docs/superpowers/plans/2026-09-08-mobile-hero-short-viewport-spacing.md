# Mobile Hero Short-Viewport Spacing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent the glowing mobile hero logo from overlapping “INJURED?” in short browser viewports.

**Architecture:** Keep the existing responsive hero composition intact and override only the existing `(max-width: 640px) and (max-height: 760px)` rule. A CSS regression test records the approved short-height geometry, while browser measurements validate the rendered gaps.

**Tech Stack:** Static HTML, CSS media queries, Python `unittest`, browser computed geometry.

---

### Task 1: Lock the short-height spacing contract

**Files:**
- Modify: `tests/test_homepage_mobile_video_hero.py`

- [ ] Add a test asserting `translateY(0)`, `width: min(88%, 20rem)`, and `top: 15.75rem` inside the short-height media query.
- [ ] Run `python3 -m unittest tests.test_homepage_mobile_video_hero` and confirm it fails because the current rule still uses `top: 14.8rem` and has no short-height logo overrides.

### Task 2: Apply the minimal responsive fix

**Files:**
- Modify: `homepage-atlas.css`
- Modify: `index.html`
- Modify: `tests/test_homepage_header_logo_call_now.py`
- Modify: `tests/test_homepage_mobile_video_hero.py`

- [ ] Add the approved logo and copy overrides only inside the short-height media query.
- [ ] Change the stylesheet cache key to `mobile-short-spacing-1` and update its assertions.
- [ ] Run `python3 -m unittest tests.test_homepage_mobile_video_hero tests.test_homepage_header_logo_call_now` and confirm it passes.

### Task 3: Verify and publish

**Files:**
- Verify: `homepage-atlas.css`
- Verify: `index.html`

- [ ] Run the full unit and homepage contract suites.
- [ ] Measure the logo-to-copy and CTA-to-scroll gaps at 375 × 667, confirm the 375 × 812 layout remains separated, and review paired mobile/desktop screenshots.
- [ ] Commit and push the validated source, update the existing GPT Sites mirror, save a Sites version, and publish it to the current public URL.
