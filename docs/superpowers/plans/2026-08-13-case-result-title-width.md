# Case Result Title Width Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let case titles use the full inner width of result cards on the homepage and Case Results page without changing card alignment or any other styling.

**Architecture:** Keep both existing card implementations intact and change only their final page-specific title-width declarations. Add one focused source-level regression test that checks the two owning selectors so later stylesheet additions cannot silently restore the narrow character measures.

**Tech Stack:** Static HTML/CSS, Python 3 `unittest`, local browser geometry and screenshot QA.

---

### Task 1: Protect the full-width title contract

**Files:**
- Create: `tests/test_case_result_title_width.py`
- Read: `homepage-atlas.css`
- Read: `inner-atlas.css`

- [ ] **Step 1: Write the failing regression test**

```python
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOME_CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
INNER_CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")


def declarations(css: str, selector: str) -> list[str]:
    return re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)


class CaseResultTitleWidthTests(unittest.TestCase):
    def test_homepage_case_titles_use_the_full_card_width(self):
        rules = declarations(
            HOME_CSS,
            ".atlas-home #settlements.settlements-premium .ds-figure-cell__case",
        )
        self.assertTrue(rules)
        self.assertTrue(any("max-width: none" in rule for rule in rules))
        self.assertFalse(any("max-width: 22ch" in rule for rule in rules))

    def test_case_results_page_titles_use_the_full_card_width(self):
        rules = declarations(INNER_CSS, "main:has(#results) .rcard-t")
        self.assertTrue(rules)
        self.assertTrue(any("max-width: none" in rule for rule in rules))
        self.assertFalse(any("max-width: 23ch" in rule for rule in rules))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the regression test and confirm the expected failure**

Run: `python3 -m unittest tests.test_case_result_title_width -v`

Expected: two failures because the homepage selector still contains `max-width: 22ch` and the Case Results selector still contains `max-width: 23ch`.

### Task 2: Remove the two narrow title measures

**Files:**
- Modify: `homepage-atlas.css:10037`
- Modify: `inner-atlas.css:1286`
- Test: `tests/test_case_result_title_width.py`

- [ ] **Step 1: Apply the minimal homepage CSS change**

```css
.atlas-home #settlements.settlements-premium .ds-figure-cell__case {
  display: block;
  max-width: none;
  margin: auto 0 0;
}
```

Keep every declaration not shown above unchanged.

- [ ] **Step 2: Apply the minimal Case Results CSS change**

```css
main:has(#results) .rcard-t {
  max-width: none;
  margin-top: auto;
}
```

Keep every declaration not shown above unchanged.

- [ ] **Step 3: Run the focused and full automated test suites**

Run: `python3 -m unittest tests.test_case_result_title_width -v`

Expected: 2 tests pass.

Run: `python3 -m unittest discover -s tests -v`

Expected: all repository tests pass with zero failures or errors.

### Task 3: Verify responsive geometry and appearance

**Files:**
- Verify: `index.html`
- Verify: `case-results/index.html`
- Verify: `homepage-atlas.css`
- Verify: `inner-atlas.css`

- [ ] **Step 1: Run the layout detector**

Run: `node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json --scope layout homepage-atlas.css inner-atlas.css index.html case-results/index.html`

Expected: no new unexplained layout findings caused by the two declaration changes.

- [ ] **Step 2: Measure desktop and phone geometry**

At desktop and 375px widths on both pages, measure the first card title and its card content box. Confirm the computed `max-width` is `none`, the title has the full available content width, and `document.documentElement.scrollWidth <= document.documentElement.clientWidth`.

- [ ] **Step 3: Capture paired screenshots**

Capture and inspect the homepage settlements section and the Case Results card section at desktop and 375px. Confirm titles wrap naturally to the card padding boundary, desktop stays left-aligned, mobile stays centered, and amount/detail/card geometry remains unchanged.

- [ ] **Step 4: Review the diff and working tree**

Run: `git diff --check && git diff -- homepage-atlas.css inner-atlas.css tests/test_case_result_title_width.py`

Expected: no whitespace errors and only the two title-width declarations plus the focused regression test are changed.
