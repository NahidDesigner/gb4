# GB Law Firm Design Authority Reset

Status: approved approach, proposal only. This document does not supersede `DESIGN.md` and is not implementation authority.

## Purpose

Reset the homepage design process so creative decisions are made from product truth and approved visual evidence, not inherited from a long history of rejected section treatments. Preserve the client's facts and locked elements while reopening the visual world outside them.

## Problem Being Solved

The current `DESIGN.md` is both a design system and a chronological repair log. It contains valuable constraints, superseded components, preassigned section compositions, implementation tactics, historical explanations, and unresolved contradictions in one binding document. This causes every implementation attempt to converge on the same family of outcomes even when the request asks for a new design.

The reset separates three kinds of information:

1. Product truth belongs in `PRODUCT.md`.
2. Durable, approved visual decisions belong in `DESIGN.md`.
3. Temporary experiments, rejected treatments, and implementation history do not belong in either authority.

## Preserved Requirements

The reset cannot alter these facts:

- Homepage scope only.
- Existing hero layout, image, copy, heading, and typography remain untouched.
- Existing footer and mobile sticky call bar remain.
- Client-approved body copy remains verbatim.
- The approved section inventory may be cut or merged, but not expanded with invented sections.
- No attorney portraits appear on the homepage.
- The homepage presents GB Law Firm as one institution.
- The GB logo remains a confirmed brand asset.
- SEO metadata, structured data, analytics, forms, handlers, and existing functionality remain intact.
- The preloader remains homepage-only.
- The experience remains responsive, keyboard-accessible, reduced-motion aware, and usable without JavaScript.
- Unsupported settlement figures, outcomes, testimonials, or legal claims cannot be invented.

## Reopened Decisions

Unless the client confirms otherwise, the following are creative choices rather than permanent requirements:

- Page-wide use of navy, gold, pale gray, or any existing color ratio.
- Cinzel, Source Sans 3, and Archivo Narrow outside the locked hero.
- Hard corners, the universal shadow ban, and fixed border treatments.
- Existing spacing tokens and container widths.
- Existing component definitions and interaction recipes.
- The archetype-letter system and all preassigned section archetypes.
- Section-specific background colors, layouts, grids, marquees, louvers, timelines, cards, and motion.
- Numerical limits such as two bronze elements or one animated element per viewport.

The logo's navy and gold may inform the new visual world, but the logo does not require the entire page to be navy-and-gold.

## New Design Authority Model

The replacement `DESIGN.md` will be concise and evidence-based. It will be written only after the visual direction and representative homepage compositions have been approved. It will contain:

1. **Visual thesis** — one specific idea the site owns and the category-default look it refuses.
2. **Brand constants** — approved logo usage, locked hero boundary, palette roles, typography roles, imagery principles, and voice.
3. **Composition principles** — scroll pacing, density changes, asymmetry, transitions between sections, and rules that describe perceived variety rather than archetype labels.
4. **Reusable primitives** — only components proven useful in approved compositions.
5. **Interaction and motion** — one coherent motion language with progressive enhancement and reduced-motion behavior.
6. **Responsive and accessibility requirements** — behavior at small-phone, tablet, laptop, and wide-screen widths.
7. **Acceptance criteria** — visual specificity, conversion clarity, factual integrity, accessibility, performance, and cross-viewport quality.

The replacement will not contain a change log, superseded components, rejected layouts, implementation diaries, or paragraph-by-paragraph defenses of prior decisions.

## Homepage Design Process

### 1. Direction round

Develop three materially different visual worlds from the firm's real context, not from generic law-firm references. Each direction must show how it meets the locked hero without imitating it, how proof is presented, how Long Island specificity appears, and what makes the scroll memorable.

No direction may rely on the default luxury-law combination of navy fields, gold rules, centered serif headings, and repeated rectangular cards as its primary identity.

### 2. Composition round

After one visual world is selected, create three representative homepage compositions before coding:

- the first transition immediately after the locked hero;
- the strongest proof or credibility section;
- one content-heavy mobile section.

These compositions establish the system's range. They must feel related without sharing the same structural skeleton.

### 3. Homepage map

Map the approved content inventory into a deliberate emotional sequence:

1. orient the visitor;
2. establish institutional and local credibility;
3. show real proof;
4. explain services and useful next steps;
5. resolve objections;
6. close with a clear call or evaluation path.

Section layouts are derived during this step. They are not assigned in advance by archetype letter.

### 4. Implementation

Implement the approved homepage while preserving locked content and functionality. Design primitives may be reused, but no section is forced into a component simply because it exists.

### 5. Validation

Inspect desktop and phone screenshots together after the first complete pass. Correct material issues in one batch, then run one confirmation pass. The project-wide two-iteration cap remains in force.

## Composition Quality Rules

- Adjacent sections cannot reuse the same perceived hierarchy, silhouette, or interaction pattern.
- At least one memorable homepage moment must come from the firm's real evidence or local context, not decoration.
- Density must vary intentionally across the scroll.
- Repetition must build recognition; it cannot substitute for composition.
- Typography must create clear hierarchy without turning every heading into a monument.
- Photography, illustration, mapping, or data treatment must be specific to the content it supports.
- Calls to action must remain obvious without appearing as identical interruption bands throughout the page.
- Mobile is a designed composition, not a collapsed desktop layout.
- The visual system must still look specific when logos and copy are temporarily removed.

## Failure Conditions

The reset has failed if any of these are true:

- The result could be mistaken for a generic navy-and-gold law-firm template.
- Most sections are heading-plus-copy arrangements wearing different backgrounds.
- The new system is another exhaustive rulebook written before visual evidence exists.
- Visual novelty obscures the firm's offer, proof, phone number, or evaluation path.
- A direction depends on fabricated results, people, testimonials, or legal claims.
- Desktop looks composed but the 375px version reads as a stack of unrelated blocks.
- Rejected or superseded experiments return as active component definitions.

## Approval and Authority Boundary

This proposal authorizes the creative reset process, not a visual style. `DESIGN.md` remains unchanged until:

1. the user selects a visual direction;
2. the representative compositions are approved;
3. the replacement design system can be documented from those approved decisions; and
4. the user explicitly authorizes replacing the current `DESIGN.md`.

Until those gates are complete, this file remains a proposal and cannot be used as competing implementation guidance.
