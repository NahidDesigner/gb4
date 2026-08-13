# Homepage Desktop Header Refinement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hide the redundant homepage header on mobile while making the desktop logo exactly 128px tall and refining the translucent header surface.

**Architecture:** Keep the current homepage header markup for desktop and control its responsive presence entirely in the homepage stylesheet. Extend the existing source contract before changing production CSS; inner-page headers remain governed by the existing sitewide non-sticky rule.

**Tech Stack:** Static HTML/CSS, Python `unittest`, local browser geometry and screenshots.

---

### Task 1: Update the header contract

**Files:**
- Modify: `tests/test_homepage_header_logo_call_now.py`

- [ ] **Step 1: Replace the former mobile-header expectations with the new behavior**

```python
def test_homepage_header_is_hidden_on_mobile(self):
    self.assertIn("@media (max-width: 768px)", self.refinement)
    self.assertIn(".atlas-home .ds-site-header", self.mobile)
    self.assertIn("display: none !important", self.mobile)

def test_desktop_logo_is_128px_and_stylesheet_cache_is_busted(self):
    self.assertIn("height: 128px", self.refinement)
    self.assertIn('homepage-atlas.css?v=desktop-header-premium-2', HTML)
```

- [ ] **Step 2: Run the focused contract and observe the expected failure**

Run: `python3 -m unittest tests.test_homepage_header_logo_call_now -v`

Expected: FAIL because the logo is 104px, the mobile header remains visible, and the old cache-buster is present.

### Task 2: Implement the desktop-only homepage header

**Files:**
- Modify: `homepage-atlas.css`
- Modify: `index.html`
- Test: `tests/test_homepage_header_logo_call_now.py`

- [ ] **Step 1: Apply the desktop geometry and premium paper surface**

```css
.atlas-home .ds-site-header,
.atlas-home .ds-site-header.is-solid {
  height: 136px;
  min-height: 136px;
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.2), rgba(220, 231, 231, 0.08)),
    rgba(242, 240, 234, 0.92);
  border-bottom: 1px solid rgba(18, 61, 86, 0.32);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.7),
    0 22px 52px rgba(23, 35, 41, 0.14);
}

.atlas-home .ds-site-header__mark img {
  height: 128px;
  width: auto;
}
```

- [ ] **Step 2: Hide the redundant homepage header at mobile widths**

```css
@media (max-width: 768px) {
  .atlas-home .ds-site-header,
  .atlas-home .ds-site-header.is-solid {
    display: none !important;
  }
}
```

- [ ] **Step 3: Bump the homepage stylesheet cache key**

Change the homepage stylesheet URL to `homepage-atlas.css?v=desktop-header-premium-2`.

- [ ] **Step 4: Run the focused contract**

Run: `python3 -m unittest tests.test_homepage_header_logo_call_now -v`

Expected: all focused tests pass.

### Task 3: Regression and visual QA

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `styles.css`
- Verify: `tests/`

- [ ] **Step 1: Run all source tests and the homepage contract**

Run: `python3 -m unittest discover -s tests -v`

Run: `node tools/homepage_contract.mjs`

Expected: all Python tests and the homepage contract pass.

- [ ] **Step 2: Run the UI detector**

Run: `node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html homepage-atlas.css`

Expected: no findings introduced by the changed targets.

- [ ] **Step 3: Check computed geometry and screenshots**

At desktop, confirm the logo is 128px tall, centered, contained, clear of both utility groups, and causes no overflow. At 375px and 768px, confirm `#dsHeader` is not rendered and the locked hero plus bottom action bar remain visible. On a representative inner page at 375px, confirm `.railhead` is positioned at the top with `position: absolute` and does not remain in view after scrolling.

- [ ] **Step 4: Review the final diff**

Confirm the locked hero, sticky mobile action bar, footer, inner pages, and all section compositions remain unchanged.
