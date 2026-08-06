# Homepage Clean CSS Replacement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the failed homepage override with one stable, premium, brand-consistent stylesheet while preserving approved content, functionality, the locked hero, footer, and sticky mobile call bar.

**Architecture:** Keep `styles.css` and `design-system.css` for shared structure and behavior, then make `homepage-atlas.css` the sole final homepage design authority. Every override is scoped through `.atlas-home` plus a section ID or explicit structural class so legacy sticky, color, font, and pseudo-element rules cannot win.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Node contract assertions, Python SEO audit.

---

### Task 1: Strengthen the homepage contract before replacement

**Files:**
- Modify: `tools/homepage_contract.mjs`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Add failing structural assertions**

Add assertions requiring a moderate heading token, an explicit non-sticky reset, compact CTA treatment, a stable 2×2 commitment grid, a two-column process board, explicit white service-area copy, and a no-large-gold-surface rule:

```js
for (const token of ['--atlas-heading-xl:', '--atlas-section-space:', '--atlas-copy-measure:']) {
  assert.ok(css.includes(token), `missing layout token ${token}`);
}
assert.match(css, /\.atlas-home #process \.h2\s*\{[^}]*position:\s*static[^}]*top:\s*auto/s);
assert.match(css, /\.atlas-home \.whyband \.rail-track\s*\{[^}]*grid-template-columns:\s*repeat\(2,\s*minmax\(0,\s*1fr\)\)/s);
assert.match(css, /\.atlas-home #process \.steps\s*\{[^}]*grid-template-columns:\s*repeat\(2,\s*minmax\(0,\s*1fr\)\)/s);
assert.match(css, /\.atlas-home #areas \.rte-strong\s*\{[^}]*color:\s*var\(--atlas-white\)/s);
assert.doesNotMatch(css, /main\s*>\s*\.sec--tight[^}]*background:\s*var\(--atlas-signal\)/s);
```

- [ ] **Step 2: Run the contract and verify RED**

Run: `node tools/homepage_contract.mjs`

Expected: failure on the first missing clean-replacement layout token.

- [ ] **Step 3: Preserve the existing immutable hashes**

Do not change the existing hero, footer, or action-bar hashes. Keep the approved section inventory and forbidden invented-content checks unchanged.

### Task 2: Replace the foundation, header, and shared action strips

**Files:**
- Archive: `.impeccable/archive/homepage-atlas-failed-2026-08-06.css`
- Replace: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Archive the failed override recoverably**

Copy the current stylesheet byte-for-byte to `.impeccable/archive/homepage-atlas-failed-2026-08-06.css`, then replace the active file through `apply_patch`.

- [ ] **Step 2: Define the authoritative tokens and global reset**

The replacement begins with self-hosted Archivo Narrow and Source Sans 3 faces plus:

```css
.atlas-home {
  --atlas-paper: #f4f1ea;
  --atlas-stone: #e3e6e4;
  --atlas-navy: #0a1628;
  --atlas-navy-raised: #162840;
  --atlas-gold: #c9a227;
  --atlas-gold-soft: #f3df94;
  --atlas-ink: #172329;
  --atlas-muted: #465466;
  --atlas-white: #ffffff;
  --atlas-heading-xl: clamp(3.25rem, 5vw, 4.75rem);
  --atlas-section-space: clamp(5.5rem, 8vw, 8rem);
  --atlas-copy-measure: 68ch;
  font-family: "Atlas Text", sans-serif;
}
```

Reset legacy heading pseudo-elements, sticky positions, transforms, inherited dark-mode colors, and JavaScript reveal opacity only inside the approved homepage body sections.

- [ ] **Step 3: Rebuild header and overlays**

Set `.ds-site-header.is-solid` to navy, nav controls to white, phone action to gold/navy, and drawer/search surfaces to navy/white/gold. Preserve the existing `is-solid`, drawer, search, and button IDs.

- [ ] **Step 4: Rebuild CTA strips**

Use a compact raised-navy strip, moderate heading, existing supporting line, and gold call button. Remove large gold slab backgrounds and excessive vertical padding.

- [ ] **Step 5: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: foundation/header assertions pass; later section assertions may still fail.

### Task 3: Rebuild credentials through case types

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Implement credentials and firm**

Credentials remain a compact evidence rail. Firm uses a balanced heading and three columns at desktop, one column below 900px, with explicit navy/ink text and Source Sans body copy.

- [ ] **Step 2: Implement settlements**

Use a compact two-column navy proof field. Keep `.ds-settlements__record[hidden] { display: none; }`. Place `$100M+` in a broad left column and the existing heading, lead, and action in a right column without narrow wrapping.

- [ ] **Step 3: Implement Why GB**

Set the introduction to a balanced two-column header row and `.whyband .rail-track` to `repeat(2, minmax(0, 1fr))`. Remove transforms, negative margins, carousel widths, narrow `max-width` headings, and oversized card padding.

- [ ] **Step 4: Implement practice areas**

Keep radio behavior. At desktop, use a horizontal flex louver where the checked panel grows to 52% and the other three share the remainder. At phone widths, stack four readable panels and keep checked content visible.

- [ ] **Step 5: Implement case types**

Use a two-column stone directory with explicit Archivo Narrow names and Source Sans descriptions; collapse to one column at 760px.

- [ ] **Step 6: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: top-half structural assertions pass.

### Task 4: Rebuild reviews through process

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Implement reviews**

Explicitly set `.rv-score > b`, review labels, actions, and stars so no legacy black or bronze-ink values leak onto navy. Keep the existing horizontal review interaction and cards.

- [ ] **Step 2: Implement the mid-page form**

Use a navy heading panel beside a warm-paper form panel. Keep all fields and handlers. Set explicit input, placeholder, focus, error, status, and button colors.

- [ ] **Step 3: Implement First 48**

Use a compact two-column record grid at desktop with seven existing steps. Each item has a restrained gold numeral, readable heading, and body. Collapse to one column on phones. Keep the existing closing call and accident-report row.

- [ ] **Step 4: Implement premises**

Use one navy field with a two-column inner grid and no diagonal gradient. Keep all existing copy and call action, with explicit white and gold text.

- [ ] **Step 5: Implement process**

Set `.atlas-home #process .h2 { position: static; top: auto; }`. Keep heading and lede above a `repeat(2, minmax(0, 1fr))` step grid. Remove transforms and sticky behavior so no text collision is possible.

- [ ] **Step 6: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: process and visibility assertions pass.

### Task 5: Rebuild service areas through contact

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Implement service areas**

Use raised navy with explicit white heading, lede, cards, closing statement, and gold phone link. Set `.atlas-home #areas .rte-strong { color: var(--atlas-white); }`. Keep the accident-report action compact and high contrast.

- [ ] **Step 2: Implement advantage**

Reset the legacy rail grid and sticky heading. Use a moderate headline above a two-column text block, with the closing statement aligned under the second column without overlap.

- [ ] **Step 3: Implement FAQ**

Use a non-sticky moderate heading beside the accordion at desktop and above it on smaller screens. Explicitly reset summary colors, signs, open-body spacing, and copy measure.

- [ ] **Step 4: Implement contact**

Use a compact two-column navy layout with balanced heading/lead/closing statement on the left and the existing form on the right. Set all controls, placeholders, focus rings, errors, and the gold submit button explicitly.

- [ ] **Step 5: Preserve office/footer boundary**

Do not style `.office`, `.foot`, or `#actionbar` in the replacement stylesheet.

- [ ] **Step 6: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: pass.

### Task 6: Responsive and accessibility hardening

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Add tablet and phone rules**

At 980px, collapse editorial splits where necessary. At 760px, switch directories and boards to one column. At 600px, use 64px header height, 1.2rem gutters, 38–52px headings, at least 16px body copy, 44px controls, and no negative horizontal margins.

- [ ] **Step 2: Add reduced-motion handling**

Disable transitions and animations under `prefers-reduced-motion: reduce` without hiding content.

- [ ] **Step 3: Verify no overflow-prone rules remain**

Run:

```sh
rg -n "translateY\(|position:\s*sticky|max-width:\s*16ch|background:\s*var\(--atlas-gold\)" homepage-atlas.css
```

Expected: no unintended section transforms, sticky headings, narrow title measures, or large gold section surfaces.

### Task 7: Final verification

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `homepage-atlas.js`
- Verify: `tools/homepage_contract.mjs`

- [ ] **Step 1: Run all automated checks**

```sh
node tools/homepage_contract.mjs
node --check homepage-atlas.js
python3 tools/seo_audit.py
```

Expected: all pass.

- [ ] **Step 2: Verify CSS structure, IDs, and motion budget**

Run the existing brace check, duplicate-ID check, and confirm `homepage-atlas.js` remains at or below 8192 bytes.

- [ ] **Step 3: Run Impeccable detection once after UI edits finish**

```sh
node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html homepage-atlas.css homepage-atlas.js
```

Expected: `[]`.

- [ ] **Step 4: Perform visual confirmation when available**

Inspect desktop and 375px views through the supported in-app browser surface. If the selected `file://` tab remains blocked, report that limitation and use the user's supplied screenshots as the defect baseline without claiming a fresh screenshot pass.

