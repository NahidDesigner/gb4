# Blog Card and Post Header Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace oversized blog archive tiles with compact post cards and reduce individual post titles into centered headers with one short accent rule.

**Architecture:** Keep the current HTML untouched and change only the blog-scoped CSS in `inner-atlas.css`. Add a focused contract test that verifies the archive grid, compact typography, centered post header, absent side border, and inset rules.

**Tech Stack:** Static CSS, Python `unittest`, in-app browser geometry and screenshot checks.

---

### Task 1: Add the blog visual contract test

**Files:**
- Create: `tests/test_blog_editorial_layout.py`

- [ ] Assert that the archive post list uses a responsive grid, cards have compact minimum height and title sizing, and the single-post page head is centered without a left border.
- [ ] Assert that surrounding single-post header rules are removed, one short rule appears below the title, and mobile title sizing is independently constrained.
- [ ] Run `python3 -m unittest tests.test_blog_editorial_layout -v` and confirm the assertions fail against the oversized current layout.

### Task 2: Implement the approved CSS composition

**Files:**
- Modify: `inner-atlas.css`

- [ ] Convert the archive post list to a two-column grid at desktop and one-column stack below 900px.
- [ ] Restyle each archive link as a compact warm-paper card containing the existing date, title, description, and action.
- [ ] Center the single-post page head, remove every surrounding rule, reduce its title scale, and create one short centered rule below the title.
- [ ] Run `python3 -m unittest tests.test_blog_editorial_layout -v` and confirm the contract passes.

### Task 3: Verify the site

**Files:**
- Verify: `blog/index.html`
- Verify: both `blog/*/index.html` article pages

- [ ] Run the full Python test suite, SEO audit, `git diff --check`, and the Impeccable detector.
- [ ] Measure card count, card geometry, overflow, title alignment, title size, and rule width at desktop and mobile widths.
- [ ] Capture and review paired desktop/mobile screenshots for the archive and an individual post, perform at most one batched correction, and confirm once.
