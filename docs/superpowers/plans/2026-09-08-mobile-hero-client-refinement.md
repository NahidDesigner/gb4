# Mobile Hero Client Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** Refine the client-approved mobile hero hierarchy by reducing the logo and “INJURED?” line, lowering the mobile video/poster crop, and lifting the menu while preserving glow, copy, desktop behavior, and accessibility.

**Architecture:** Keep the existing semantic hero intact and implement the refinement in the final authoritative mobile cascade in homepage-atlas.css. Extend the existing Python CSS contract so the four coordinated mobile changes and cache revision cannot regress.

**Tech Stack:** Static HTML, CSS media queries, Python unittest, browser computed-geometry and screenshot QA.

---

### Task 1: Lock the requested mobile composition in tests

**Files:**
- Modify: tests/test_homepage_mobile_video_hero.py
- Modify: tests/test_homepage_header_logo_call_now.py

- [ ] **Step 1: Write the failing assertions**

Add assertions scoped after “This guard is intentionally last in the cascade” for:

    self.assertIn('width: min(92%, 22rem)', final_mobile_guard)
    self.assertIn('font-size: clamp(2.35rem, 11.5vw, 3.15rem)', final_mobile_guard)
    self.assertIn('top: -0.65rem', final_mobile_guard)
    self.assertIn('translate(-50%, calc(-50% + 1rem))', final_mobile_guard)
    self.assertIn('background-position: center calc(50% + 1rem)', final_mobile_guard)
    self.assertIn('homepage-atlas.css?v=mobile-client-refinement-1', HTML)

Retain the assertion that the logo content URL is assets/gb-logo-empire-glow.png and assert a nonzero vertical drop shadow on the image.

- [ ] **Step 2: Run the targeted tests and verify RED**

Run:

    python3 -m unittest tests.test_homepage_mobile_video_hero tests.test_homepage_header_logo_call_now

Expected: failures for the new logo size, heading size, crop offsets, menu position, shadow, and cache revision.

### Task 2: Implement the final mobile-only cascade

**Files:**
- Modify: homepage-atlas.css
- Modify: index.html

- [ ] **Step 1: Apply the minimal mobile rules**

Inside the final max-width: 640px guard:

    .atlas-home .hero-video__frame {
      height: calc(100% + 44px);
      transform: translate(-50%, calc(-50% + 1rem));
    }

    .atlas-home .hero-bg {
      background-position: center calc(50% + 1rem);
    }

    .atlas-home .lockup-mark img {
      width: min(92%, 22rem);
      filter:
        drop-shadow(0 12px 24px rgba(232, 180, 60, 0.26))
        drop-shadow(0 8px 18px rgba(7, 48, 82, 0.24));
    }

    .atlas-home .lockup-stack {
      top: -0.65rem;
    }

    .atlas-home .hero-proof__injured {
      font-size: clamp(2.35rem, 11.5vw, 3.15rem);
    }

In the final short-height guard, reduce the logo to min(84%, 18.5rem) while preserving its positive separation from the copy. Update the stylesheet revision in index.html to mobile-client-refinement-1.

- [ ] **Step 2: Run the targeted tests and verify GREEN**

Run:

    python3 -m unittest tests.test_homepage_mobile_video_hero tests.test_homepage_header_logo_call_now

Expected: all targeted tests pass.

### Task 3: Verify visual and functional safety

**Files:**
- Verify: homepage-atlas.css
- Verify: index.html
- Verify: tests/test_homepage_mobile_video_hero.py
- Verify: tests/test_homepage_header_logo_call_now.py

- [ ] **Step 1: Run complete automated verification**

Run:

    python3 -m unittest discover -s tests
    node tools/homepage_contract.mjs
    node tests/hero_video_controller_runtime.mjs
    node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html homepage-atlas.css
    git diff --check

Expected: 0 failures, both Node contracts pass, detector returns [], and diff check is empty.

- [ ] **Step 2: Run computed geometry and paired screenshot QA**

At 375 × 667 and 375 × 812, confirm:

- logo bottom is above copy top;
- menu top is above its previous 32px position while its box remains at least 64 × 64;
- no horizontal overflow;
- CTA and scroll cue do not collide.

At 1440 × 900, confirm the desktop logo source, background crop, header, and proof hierarchy are unchanged. Capture and review all three screenshots in one inspection pass, then use at most one batched correction.

- [ ] **Step 3: Commit the verified local preview**

    git add homepage-atlas.css index.html tests/test_homepage_mobile_video_hero.py tests/test_homepage_header_logo_call_now.py docs/superpowers/specs/2026-09-08-mobile-hero-client-refinement-design.md docs/superpowers/plans/2026-09-08-mobile-hero-client-refinement.md
    git commit -m "Refine mobile hero composition"

Do not publish or push until the user reviews the local preview.
