# Drunk and Impaired Driving Crashes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Drunk and Impaired Driving Crashes as the fifth existing-style practice area, with a matching image, full detail page, navigation, and sitemap coverage.

**Architecture:** Extend the existing static homepage accordion/panel component and clone the standardized practice-area HTML page. Keep shared CSS/JS and the established section composition; only add the fifth selector branch and topic-specific content/data. Add one Node contract test covering the new surface across the static site.

**Tech Stack:** Static HTML, CSS, vanilla JavaScript, Node.js contract tests, generated WebP photography.

---

### Task 1: Establish the fifth-practice-area contract

**Files:**
- Create: `tools/drunk_impaired_practice_area_contract.mjs`
- Test: `tools/drunk_impaired_practice_area_contract.mjs`

- [ ] **Step 1: Write the failing contract**

Create assertions that require: five homepage radios/panels, the new slug and title, the fifth checked-state CSS selector in desktop/tablet/mobile rules, a non-empty WebP asset, the detail page, matching canonical/FAQ structured data, the link in every drawer that exposes the Practice Areas submenu, and both sitemaps.

- [ ] **Step 2: Run the contract and verify RED**

Run: `node tools/drunk_impaired_practice_area_contract.mjs`

Expected: FAIL because the fifth homepage panel and detail page do not yet exist.

- [ ] **Step 3: Commit the failing contract**

Run: `git add tools/drunk_impaired_practice_area_contract.mjs && git commit -m "test: define fifth practice area contract"`

### Task 2: Generate and install the practice-area image

**Files:**
- Create: `assets/drunk-and-impaired-driving-crashes.webp`
- Create: `assets/drunk-and-impaired-driving-crashes-sm.webp`

- [ ] **Step 1: Inspect incumbent assets**

Review the four current 1500×1000 and mobile images for documentary framing, night/day balance, contrast, and crop behavior.

- [ ] **Step 2: Generate the source image with the built-in image tool**

Use this prompt:

```text
Use case: photorealistic-natural
Asset type: law-firm practice-area website photography
Primary request: a realistic Long Island roadside crash scene that communicates a collision caused by an impaired driver without showing injured people
Scene/backdrop: suburban New York roadway at blue hour, two damaged passenger vehicles safely stopped after impact, distant police emergency lights
Style/medium: restrained documentary editorial photography, natural texture, believable vehicle damage
Composition/framing: landscape 3:2, useful center and edge crops, no dominant person, no readable plates
Lighting/mood: sober, serious, low-key blue-hour light; no sensationalism
Constraints: no alcohol bottles, no visible drinking, no blood, no bodies, no logos, no readable text, no watermark
Avoid: cinematic action, active collision, fire, exaggerated wreckage, generic luxury advertising
```

- [ ] **Step 3: Save and derive responsive files**

Copy the selected generated source into the workspace, convert the final desktop image to 1500×1000 WebP, and create the established mobile crop/size as `drunk-and-impaired-driving-crashes-sm.webp`.

- [ ] **Step 4: Inspect both outputs**

Confirm plausible crash geometry, clean crops, no readable plate/text artifacts, and file dimensions matching incumbent assets.

### Task 3: Extend the homepage component

**Files:**
- Modify: `index.html`
- Modify: `homepage-atlas.css`

- [ ] **Step 1: Add the fifth radio and panel**

Add `ds-pa-5`, number `05`, the generated image, the visible title “Drunk and Impaired Driving Crashes,” the description “Holding impaired drivers accountable for preventable crashes and serious injuries,” and links to `practice-areas/drunk-and-impaired-driving-crashes/`.

- [ ] **Step 2: Extend existing selector lists**

Add the fifth checked-panel selector beside the existing four in the desktop, tablet, and mobile selector groups without changing the component’s visual language.

- [ ] **Step 3: Verify homepage contract and locked regions**

Run: `node tools/homepage_contract.mjs && node tools/preloader_scope_contract.mjs`

Expected: both PASS.

### Task 4: Create the cloned detail page with researched content

**Files:**
- Create: `practice-areas/drunk-and-impaired-driving-crashes/index.html`

- [ ] **Step 1: Clone the standardized page shell**

Copy `practice-areas/distracted-driving-crashes/index.html` because it contains the current claim-stage composition and shared page dependencies.

- [ ] **Step 2: Replace metadata and structured data**

Use title `Drunk and Impaired Driving Crash Lawyers | GB Law Firm`, canonical URL `https://gblawfirm.com/practice-areas/drunk-and-impaired-driving-crashes/`, the generated image preload, topic-specific description, breadcrumb label, FAQ ID, and ten matching FAQ entities.

- [ ] **Step 3: Replace all page-specific visible content**

Rewrite the hero subtitle, overview, two fault/evidence cards, terms wall, six Protecting the Claim cards, related tiles, Why This Firm copy, and ten FAQs. Ground legal statements in current official New York sources: VTL §1192 impairment/intoxication offenses, DMV crash guidance, 11 NYCRR no-fault notice requirements, CPLR §214 limitations, and controlling New York punitive-damages principles. Phrase deadlines with appropriate qualifiers and never suggest a criminal charge or conviction automatically resolves civil liability.

- [ ] **Step 4: Validate the HTML data relationship**

Confirm every visible FAQ question/answer matches the corresponding JSON-LD entity and that no copied distracted-driving topic strings remain outside related-area links.

### Task 5: Add navigation and sitemap discovery

**Files:**
- Modify: all site HTML files containing `<nav class="drawer-nav" aria-label="Practice areas">`
- Modify: `sitemap.xml`
- Modify: `sitemap/index.html`

- [ ] **Step 1: Add the drawer link mechanically**

Insert the new link after Distracted Driving Crashes in each existing Practice Areas submenu, using the correct relative prefix for that page. Mark only the new detail page’s link with `aria-current="page"`.

- [ ] **Step 2: Update stale four-item comments**

Change comments describing the component/menu as four items to five where touched, without changing behavior or client-facing copy.

- [ ] **Step 3: Add sitemap entries**

Add the canonical URL to `sitemap.xml` with `lastmod` `2026-08-12`, monthly frequency, and priority `0.9`; add the corresponding human-readable practice-area entry to `sitemap/index.html`.

- [ ] **Step 4: Run the new contract and verify GREEN**

Run: `node tools/drunk_impaired_practice_area_contract.mjs`

Expected: `Drunk/impaired practice-area contract: pass`.

### Task 6: Visual and final verification

**Files:**
- Verify: `index.html`
- Verify: `practice-areas/drunk-and-impaired-driving-crashes/index.html`

- [ ] **Step 1: Run all automated checks**

Run: `node tools/drunk_impaired_practice_area_contract.mjs && node tools/homepage_contract.mjs && node tools/preloader_scope_contract.mjs && python3 tools/seo_audit.py`

- [ ] **Step 2: Run computed geometry checks**

At 1440px and 375px, measure the homepage Practice Areas section and new page for viewport overflow, panel count, selected-panel sizing, heading/label containment, CTA reachability, sticky call-bar clearance, and focusable controls.

- [ ] **Step 3: Capture paired screenshots**

Capture and review desktop and mobile screenshots of the homepage Practice Areas section plus the new detail page. Batch any defects into one correction pass and perform at most one confirmation screenshot pass.

- [ ] **Step 4: Review scope and diff**

Run: `git diff --check && git status --short && git diff --stat`

Confirm the homepage hero, footer, sticky call bar, unrelated approved copy, other pages’ content, and the section/archetype sequence remain unchanged.
