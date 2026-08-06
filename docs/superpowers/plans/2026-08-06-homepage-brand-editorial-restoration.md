# Homepage Brand Editorial Restoration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore a premium, logo-aligned Brand Editorial visual system across the homepage while preserving the locked hero, approved content, working interactions, Where We Work composition, map, footer, and sticky mobile call bar.

**Architecture:** Retain `index.html`, shared `styles.css`, shared `design-system.css`, and the current stable homepage markup. Refine `homepage-atlas.css` in place using section-scoped `.atlas-home` rules so each approved section receives a distinct composition without destabilizing shared pages or existing behavior. Extend the homepage contract before each CSS group so visual-system requirements fail before implementation and pass afterward.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, self-hosted Cinzel/Archivo Narrow/Source Sans 3, Node contract assertions, Python SEO audit, in-app browser screenshots.

**Workspace note:** This directory is not a Git repository, so worktree and commit steps are unavailable. All edits remain in the shared workspace and must be recoverable through the existing `.impeccable/archive/` snapshot plus explicit verification.

---

### Task 1: Extend the Brand Editorial contract

**Files:**
- Modify: `tools/homepage_contract.mjs`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Add failing typography and geometry assertions**

Add CSS checks for the approved user override:

```js
for (const token of [
  '--atlas-display: "Cinzel"',
  '--atlas-utility: "Archivo Narrow"',
  '--atlas-body: "Source Sans 3"',
  '--atlas-frame:',
  '--atlas-section-gap:',
]) {
  assert.ok(css.includes(token), `missing Brand Editorial token ${token}`);
}

assert.match(
  css,
  /\.atlas-home \.cta-wrap\s*\{[^}]*padding-block:[^}]*margin-block:/s,
  'CTA wrappers must own vertical isolation',
);
assert.match(
  css,
  /\.atlas-home #firm\s*\{[^}]*border-block:/s,
  'firm statement must use structural borders',
);
assert.match(
  css,
  /\.atlas-home #questions\s*\{[^}]*background:\s*linear-gradient\(/s,
  'FAQ must use the approved navy/paper split',
);
```

- [ ] **Step 2: Replace obsolete flat-layout assertions**

Remove the requirements that Why GB and Process must use identical stable two-column boards. Replace them with checks that their composition selectors differ:

```js
assert.match(css, /\.atlas-home \.whyband \.rail-track\s*\{[^}]*grid-template-areas:/s);
assert.match(css, /\.atlas-home #process \.steps\s*\{[^}]*grid-template-columns:\s*repeat\(4,/s);
```

- [ ] **Step 3: Run the contract and verify RED**

Run: `node tools/homepage_contract.mjs`

Expected: FAIL on the first missing Brand Editorial token.

### Task 2: Restore the foundation, header, awards, firm, CTAs, and settlements

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Add explicit Brand Editorial type roles**

Define the self-hosted display, utility, and body roles without changing the locked hero:

```css
.atlas-home {
  --atlas-display: "Cinzel", "Trajan Pro", Georgia, serif;
  --atlas-utility: "Archivo Narrow", "Arial Narrow", Arial, sans-serif;
  --atlas-body: "Source Sans 3", -apple-system, BlinkMacSystemFont, sans-serif;
  --atlas-frame: rgba(201, 162, 39, 0.52);
  --atlas-section-gap: clamp(3.5rem, 6vw, 6rem);
}

.atlas-home :where(#firm, #settlements, #why, #practice, #first48, #premises, #areas, #advantage, #questions, #contact) h2 {
  font-family: var(--atlas-display);
  font-weight: 600;
  letter-spacing: -0.02em;
}
```

Keep long case names, process steps, form controls, buttons, and index labels in Archivo Narrow or Source Sans 3.

- [ ] **Step 2: Fix the awards rail**

Set `#creds` to a tighter framed evidence strip, remove the short isolated rule, increase logo opacity/contrast, and add an inset gold/navy boundary. Do not change badge assets or markup.

- [ ] **Step 3: Restore the firm statement borders**

Give `#firm` a fine top/bottom structure, an inset gold measure, and staggered copy columns. Use existing heading and copy only. Ensure the heading remains proportionate and does not collide at 1024px.

- [ ] **Step 4: Isolate all CTA strips**

Use:

```css
.atlas-home .cta-wrap {
  padding-block: clamp(2.25rem, 4vw, 4rem);
  margin-block: 0;
  background: var(--atlas-paper);
}
.atlas-home .cta-band {
  border: 1px solid var(--atlas-frame);
  border-radius: 2px;
  box-shadow: 0 18px 45px rgba(10, 22, 40, 0.12);
}
```

Verify no CTA visually touches the preceding or following section.

- [ ] **Step 5: Compose settlements as a framed proof field**

Retain `$100M+`, heading, copy, and results link. Add a gold vertical measure, stronger number/heading relationship, and controlled background geometry without adding factual content.

- [ ] **Step 6: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: typography, firm-border, and CTA-isolation assertions pass.

### Task 3: Restore Why GB, Practice Areas, Case Types, and Reviews

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Convert Why GB into a stepped commitment field**

Use named grid areas with asymmetric spans:

```css
.atlas-home .whyband .rail-track {
  display: grid;
  grid-template-columns: 1.08fr 0.92fr;
  grid-template-areas: "a b" "c d";
}
.atlas-home .whyband .wcard:nth-child(1) { grid-area: a; }
.atlas-home .whyband .wcard:nth-child(2) { grid-area: b; transform: translateY(2.5rem); }
.atlas-home .whyband .wcard:nth-child(3) { grid-area: c; }
.atlas-home .whyband .wcard:nth-child(4) { grid-area: d; transform: translateY(2.5rem); }
```

Use sharp structural boundaries and reset transforms on mobile.

- [ ] **Step 2: Integrate the Practice Areas title**

Reduce empty navy above the louver, use Cinzel for the section title, add a full-width gold measure, and align the utility label with the title. Retain the existing radio-driven louver and repository imagery. Increase inactive-label legibility without changing copy.

- [ ] **Step 3: Convert Case Types into an indexed directory**

Use two asymmetrical columns, gold route ticks, a persistent vertical spine, stronger title/body contrast, and precise row hover/focus states. Collapse to one column below 760px. Do not add numbers because the case list is not a sequence.

- [ ] **Step 4: Strengthen Reviews**

Increase review metadata size and contrast, emphasize one leading review at desktop through width and border treatment, preserve carousel behavior and all review text, and keep Google attribution visible.

- [ ] **Step 5: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: Why GB, practice, case index, and review structural checks pass.

### Task 4: Restore the mid-page form, First 48 Hours, premises liability, and process

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Reframe the mid-page form**

Use an editorial navy statement panel, a sharp gold edge, visible field labels from existing markup, clear focus states, and restrained depth. Preserve form handlers and field inventory.

- [ ] **Step 2: Build the First 48 Hours stepped route**

Retain the seven numbered steps. Use a continuous central/spanning spine, large gold numerals, alternating offsets, and explicit source order. At mobile, reset to a single left-spine sequence.

- [ ] **Step 3: Build a dramatic premises editorial split**

Use a framed Cinzel heading field and stagger the existing lede, explanation, and CTA along a vertical gold measure. Keep white/navy contrast and do not use the Firm statement silhouette.

- [ ] **Step 4: Convert Process into a four-step progression**

Use four desktop columns with staggered vertical placement and a continuous top rule:

```css
.atlas-home #process .steps {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  position: relative;
}
.atlas-home #process .steps li:nth-child(even) {
  margin-top: 4.5rem;
}
```

Reset to one column below 760px and preserve step-number reading order.

- [ ] **Step 5: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: process progression and body-visibility assertions pass.

### Task 5: Preserve Where We Work and restore Advantage, FAQ, and final contact

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Protect Where We Work**

Do not change its contour geometry, road grouping, color field, resource action, or composition. Limit changes to approved typography integration and contrast corrections.

- [ ] **Step 2: Recompose Advantage**

Use a framed asymmetric heading field, stagger the two existing copy columns, and elevate the existing callout with a gold vertical rule. Ensure it does not repeat the Firm statement’s silhouette.

- [ ] **Step 3: Modernize FAQ**

Use a desktop split surface with a navy title field and warm-paper accordion field:

```css
.atlas-home #questions {
  background: linear-gradient(90deg, var(--atlas-navy) 0 38%, var(--atlas-stone) 38% 100%);
}
```

Increase row height, question size, plus/minus clarity, open-state contrast, and keyboard focus visibility. Stack navy above paper below 860px.

- [ ] **Step 4: Refine final contact**

Use visible labels, precise framed controls, strong gold submit emphasis, and a balanced Cinzel title. Preserve form behavior, map, footer, and sticky call bar.

- [ ] **Step 5: Run the contract**

Run: `node tools/homepage_contract.mjs`

Expected: full contract passes.

### Task 6: Responsive and accessibility hardening

**Files:**
- Modify: `homepage-atlas.css`
- Test: `tools/homepage_contract.mjs`

- [ ] **Step 1: Add tablet composition rules**

At 980px and 860px, collapse only the sections whose asymmetry would squeeze body copy. Keep headings below 6rem and paragraph measures below 75 characters.

- [ ] **Step 2: Add 375px composition rules**

At 600px:

```css
.atlas-home { --atlas-gutter: 1.25rem; }
.atlas-home main p { font-size: max(1rem, 16px); }
.atlas-home :where(a, button, summary, input, textarea) { min-height: 44px; }
.atlas-home .whyband .wcard,
.atlas-home #process .steps li { transform: none; margin-top: 0; }
```

Remove all vertical writing, prevent horizontal overflow, and ensure CTA strips keep independent margins.

- [ ] **Step 3: Preserve reduced-motion behavior**

Keep all content visible under `prefers-reduced-motion: reduce`; disable decorative transitions without removing state changes.

- [ ] **Step 4: Run automated checks**

```sh
node tools/homepage_contract.mjs
node --check homepage-atlas.js
python3 tools/seo_audit.py
```

Expected: all exit 0.

### Task 7: Complete visual verification

**Files:**
- Verify: `index.html`
- Verify: `homepage-atlas.css`
- Verify: `homepage-atlas.js`
- Update screenshots: `screenshots/homepage-brand-editorial-desktop.png`
- Update screenshots: `screenshots/homepage-brand-editorial-mobile-375.png`

- [ ] **Step 1: Run one complete desktop and mobile inspection**

Open the homepage at desktop width and 375px. Capture full-page screenshots. Check every section against the approved proposal in one batched inspection.

- [ ] **Step 2: Apply one batched correction pass**

Correct all observed overlap, spacing, clipping, contrast, font-loading, title-wrapping, and CTA-isolation defects together.

- [ ] **Step 3: Run one confirmation pass**

Capture desktop and 375px again. Confirm the hero/footer remain unchanged, Where We Work retains its composition, and all other sections meet the Brand Editorial acceptance criteria.

- [ ] **Step 4: Run final deterministic checks**

```sh
node tools/homepage_contract.mjs
node --check homepage-atlas.js
python3 tools/seo_audit.py
node /Users/nahid/.agents/skills/impeccable/scripts/detect.mjs --json index.html
```

Expected: all structural checks pass and the detector returns no unreviewed findings.
