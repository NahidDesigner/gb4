# Inner-page Header Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every non-homepage page the approved premium, prominent, non-sticky responsive header.

**Architecture:** A new `site-header.css` owns all inner-page header presentation and is loaded after the existing inner-page theme CSS. Existing markup, JS hooks, page content, and homepage behavior remain unchanged.

**Tech Stack:** Static HTML, CSS, Python `unittest`, in-app browser geometry and screenshot QA.

---

### Task 1: Lock the shared header contract

**Files:**
- Create: `tests/test_inner_page_header_refinement.py`

- [ ] Add tests for the 136px/128px desktop geometry, premium non-blurred surface, Atlantic/orange Call Now treatment, 96px/86px mobile geometry, 44px targets, and sitewide stylesheet coverage.
- [ ] Run `python3 -m unittest tests.test_inner_page_header_refinement -v` and confirm it fails because `site-header.css` and its page links do not exist.

### Task 2: Add the shared header layer

**Files:**
- Create: `site-header.css`
- Modify: the 24 production inner-page HTML files containing `class="railhead"`

- [ ] Implement the desktop, mobile, interaction, and wide-screen rules in `site-header.css`.
- [ ] Add a depth-correct relative link to `site-header.css?v=inner-header-premium-1` after each inner page's theme stylesheet.
- [ ] Run the focused test and confirm it passes.

### Task 3: Verify behavior and presentation

**Files:**
- No additional source changes expected.

- [ ] Run `python3 -m unittest discover -s tests -p 'test_*.py'` and confirm zero failures.
- [ ] Run the Impeccable detector once over the new stylesheet and representative inner pages.
- [ ] Inspect computed desktop and 375px geometry, including overflow, alignment, target sizes, and post-scroll mobile position.
- [ ] Capture and review paired desktop/mobile screenshots; apply at most one batched correction and rerun verification.
