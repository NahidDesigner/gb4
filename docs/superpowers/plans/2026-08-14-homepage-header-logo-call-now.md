# Homepage Header Logo and Mobile Call Now Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the homepage header logo more prominent, replace mobile Search with Call Now, and use restrained translucency without changing the locked hero or sticky mobile call bar.

**Architecture:** Keep the current semantic header and its single telephone anchor. Add responsive label spans in the homepage markup, then use homepage-scoped CSS to refine the surface and switch the trailing control at phone widths; no JavaScript behavior changes.

**Tech Stack:** Static HTML, CSS media queries, Python `unittest`, local browser geometry and screenshot checks.

---

### Task 1: Header source contract

**Files:**
- Create: `tests/test_homepage_header_logo_call_now.py`
- Read: `index.html`
- Read: `homepage-atlas.css`

- [ ] **Step 1: Write the failing contract**

Add tests that require one homepage telephone anchor with desktop and mobile labels, hide `#searchOpen2` at phone width, expose `Call Now` at phone width, remove `backdrop-filter` from the final header block, enforce a 44px minimum mobile call target, and preserve `#actionbar` plus the locked hero markup.

- [ ] **Step 2: Verify the contract fails for the missing responsive labels**

Run: `python3 -m unittest tests.test_homepage_header_logo_call_now -v`

Expected: FAIL because `ds-button-call__desktop` and `ds-button-call__mobile` do not yet exist.

### Task 2: Minimal homepage header implementation

**Files:**
- Modify: `index.html`
- Modify: `homepage-atlas.css`
- Test: `tests/test_homepage_header_logo_call_now.py`

- [ ] **Step 1: Add responsive labels to the existing telephone anchor**

Keep `href="tel:+15164441000"`, wrap `(516) 444-1000` in `.ds-button-call__desktop`, and add `.ds-button-call__mobile` containing `Call Now`.

- [ ] **Step 2: Refine the homepage-scoped header CSS**

Use a high-opacity mineral-paper background without backdrop blur, increase the desktop and mobile header/logo geometry proportionately, hide the mobile label by default, then at `max-width: 760px` hide `#searchOpen2`, show the mobile label, hide the desktop label, and keep the call anchor at least 44px tall.

- [ ] **Step 3: Verify the focused contract passes**

Run: `python3 -m unittest tests.test_homepage_header_logo_call_now -v`

Expected: PASS with all focused tests green.

### Task 3: Regression and visual QA

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `tests/`

- [ ] **Step 1: Run regression tests**

Run: `python3 -m unittest discover -s tests -v`

Expected: all tests pass.

- [ ] **Step 2: Run the homepage contract**

Run: `node tools/homepage_contract.mjs`

Expected: pass, or report any previously recorded unrelated baseline failure exactly.

- [ ] **Step 3: Measure desktop and 375px geometry**

Serve the static site locally and measure the header, logo, utilities, mobile call target, and document width. Confirm no overflow, a centered unclipped logo, and the intended visible control set.

- [ ] **Step 4: Capture paired screenshots**

Capture and inspect the header at desktop and 375px. Apply no more than one batched correction if needed, then confirm once.

- [ ] **Step 5: Review the final diff**

Confirm only the homepage header, focused test, cache buster, and planning documents changed. Confirm the hero, footer, sticky mobile call bar, and page section compositions are unchanged.
