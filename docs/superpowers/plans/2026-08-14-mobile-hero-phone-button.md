# Mobile Homepage Hero Phone Button Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an attractive, accessible, mobile-only telephone button directly below “We exceed them” in the homepage hero.

**Architecture:** Add one semantic `tel:` anchor to the existing `.hero-copy` and style it as a gold action marker using the existing phone SVG sprite. Hide the anchor by default, show it only below 641px, and verify it through a static contract test plus paired browser geometry and screenshot checks.

**Tech Stack:** Static HTML5, CSS media queries and interaction states, existing SVG sprite, Python `unittest`, in-app browser QA.

---

### Task 1: Pin the mobile-only telephone contract

**Files:**
- Create: `tests/test_homepage_mobile_hero_phone.py`
- Read: `index.html:413-433`
- Read: `styles.css:2468-2617`

- [ ] **Step 1: Write the failing contract test**

```python
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")

class HomepageMobileHeroPhoneTests(unittest.TestCase):
    def test_phone_link_is_inside_hero_copy_after_headline(self):
        hero_copy = re.search(r'<div class="hero-copy">(.*?)</div>', HTML, re.S)
        self.assertIsNotNone(hero_copy)
        fragment = hero_copy.group(1)
        self.assertRegex(fragment, r'class="hero-h1".*?class="hero-phone" href="tel:\+15164441000"')
        self.assertIn('(516) 444-1000', fragment)
        self.assertIn('<use href="#i-phone"', fragment)

    def test_phone_button_is_hidden_by_default_and_mobile_only(self):
        self.assertRegex(CSS, r'\.hero-phone\s*\{[^}]*display:\s*none')
        mobile = re.search(r'@media\s*\(max-width:\s*640px\)(.*)', CSS, re.S)
        self.assertIsNotNone(mobile)
        self.assertRegex(mobile.group(1), r'\.hero-phone\s*\{[^}]*display:\s*inline-flex[^}]*min-height:\s*48px')

    def test_phone_button_has_focus_and_reduced_motion_rules(self):
        self.assertIn('.hero-phone:focus-visible', CSS)
        reduced = re.search(r'@media\s*\(prefers-reduced-motion:\s*reduce\)(.*)', CSS, re.S)
        self.assertIsNotNone(reduced)
        self.assertIn('.hero-phone', reduced.group(1))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused test and confirm RED**

Run: `python3 -m unittest tests/test_homepage_mobile_hero_phone.py -v`

Expected: three failures because `.hero-phone` does not exist in the current HTML or CSS.

### Task 2: Add the semantic hero phone action

**Files:**
- Modify: `index.html:425-431`
- Test: `tests/test_homepage_mobile_hero_phone.py`

- [ ] **Step 1: Insert the telephone anchor after `.hero-h1`**

```html
<a class="hero-phone" href="tel:+15164441000">
  <svg class="ic" aria-hidden="true"><use href="#i-phone"/></svg>
  <span>(516) 444-1000</span>
</a>
```

- [ ] **Step 2: Preserve the locked content**

The new anchor is the only markup added. Do not edit `.hero-proof`, `.hero-h1`, `.hero-scroll`, the hero image layers, or action-bar markup.

### Task 3: Style the interactive mobile-only control

**Files:**
- Modify: `styles.css:2549-2617`
- Test: `tests/test_homepage_mobile_hero_phone.py`

- [ ] **Step 1: Add the hidden default and mobile interaction states**

```css
.hero-phone { display: none; }
.hero-phone:focus-visible { outline: 3px solid #fff; outline-offset: 3px; }

@media (max-width: 640px) {
  .hero-phone {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    min-height: 48px;
    margin: 18px auto 0;
    padding: 11px 22px;
    border: 1px solid rgba(255, 244, 199, 0.8);
    border-radius: 10px;
    background: var(--c-gold);
    color: var(--c-navy);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.38), 0 10px 28px rgba(0, 0, 0, 0.32);
    font-family: var(--f-ui);
    font-size: 16px;
    font-weight: 800;
    letter-spacing: 0.035em;
    line-height: 1;
    text-decoration: none;
    transition: transform 180ms var(--ease), box-shadow 180ms var(--ease), background-color 180ms var(--ease);
  }
  .hero-phone .ic { width: 18px; height: 18px; }
  .hero-phone:hover,
  .hero-phone:active {
    background: var(--c-gold-soft);
    color: var(--c-navy);
    transform: translateY(1px);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.28), 0 6px 18px rgba(0, 0, 0, 0.3);
  }
}
```

- [ ] **Step 2: Add reduced-motion coverage**

Inside the existing `@media (prefers-reduced-motion: reduce)` block, add `.hero-phone { transition: none; }`.

- [ ] **Step 3: Run the focused test and confirm GREEN**

Run: `python3 -m unittest tests/test_homepage_mobile_hero_phone.py -v`

Expected: all three tests pass.

### Task 4: Browser and regression verification

**Files:**
- Verify: `index.html`
- Verify: `styles.css`
- Create: `artifacts/homepage-hero-mobile-phone.png`
- Create: `artifacts/homepage-hero-desktop-phone-hidden.png`

- [ ] **Step 1: Run all static and mechanical checks**

Run `python3 -m unittest discover -s tests -v`, then run `node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html styles.css`, then run `git diff --check`.

Expected: all tests pass, detector returns `[]`, and the diff check produces no output.

- [ ] **Step 2: Capture and measure the 375px mobile hero**

Verify the button is visible below `.hero-h1`, is at least 48px tall, stays inside `.hero-copy`, clears `.hero-scroll`, contains one phone icon and the exact number, and causes zero horizontal overflow. Save `artifacts/homepage-hero-mobile-phone.png`.

- [ ] **Step 3: Capture and measure the 1440px desktop hero**

Verify `.hero-phone` computes to `display: none`, has no rendered geometry, the hero retains its previous layout, and the document has zero horizontal overflow. Save `artifacts/homepage-hero-desktop-phone-hidden.png`.

- [ ] **Step 4: Confirm browser diagnostics**

Verify the browser console contains no errors or warnings, reset the temporary viewport override, and close the QA tabs.

### Task 5: Commit the focused implementation

**Files:**
- Add: `tests/test_homepage_mobile_hero_phone.py`
- Modify: `index.html`
- Modify: `styles.css`
- Add: `docs/superpowers/plans/2026-08-14-mobile-hero-phone-button.md`

- [ ] **Step 1: Stage only these four files**

Run: `git add index.html styles.css tests/test_homepage_mobile_hero_phone.py docs/superpowers/plans/2026-08-14-mobile-hero-phone-button.md`

- [ ] **Step 2: Commit**

Run: `git commit -m "Add mobile homepage hero phone button"`

- [ ] **Step 3: Confirm unrelated work remains untouched**

Run: `git status --short`

Expected: pre-existing team-page files remain uncommitted; no homepage phone-button file remains modified.
