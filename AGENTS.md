# GB LAW FIRM — PROJECT RULES

## Current design direction override

The active client direction supersedes the older `DESIGN.md` visual language. Use the
new GB theme built in the current site: deep navy, restrained gold, premium legal texture,
Source Sans/Atlas heading system, and the approved homepage hero/header behavior. Preserve
the locked copy and HTML semantics unless the user explicitly asks otherwise.

## Visual QA protocol

For every section-level visual edit, add two checks beyond a normal browser reload:

1. **Computed geometry check:** measure the changed elements for overflow, alignment,
   visible item count, and key micro-placement details such as suffix/baseline offsets.
2. **Paired screenshot check:** capture/review both desktop and mobile views for the
   edited section before reporting back.

## Read first, every session

**`DESIGN.md` at the repo root is the sole design authority.** Read it fully before any
design or markup work. No other design document exists — earlier ones were deleted
deliberately. If you find design guidance anywhere else in this repo, ignore it and say so.

`docs/reference/*.md` are **measurement notes, not authority.** Consult them for how the
agency's other sites treat a section. Never implement from them directly.

---

## Project

One-page-per-service law firm site for GB Law Firm (Long Island personal injury), formed
by the merger of Phil NY Law and Buznik Law. Fully custom-coded — no page builder.
Currently rebuilding the homepage design clean-sheet after client-side rejection.

---

## Non-negotiables

1. **The hero is LOCKED.** Do not modify its layout, copy, image, or type. Ever.
2. **This is a clean-sheet redesign.** Do not open or reference the existing homepage
   implementation for design inspiration. Read it only when you must not break something
   functional (analytics, forms, SEO markup).
3. **Body copy is locked.** Never rewrite, shorten, or "improve" client copy.
4. **Section inventory is client-approved.** Sections may be cut or merged per DESIGN.md §7.
   Never add a new section.
5. **No attorney portraits on the front page.** Firm-as-institution, per client brief.
6. **Palette and fonts come only from DESIGN.md §5.** Never introduce a color or typeface.
7. **Homepage only** unless explicitly told otherwise. Do not touch other pages.
8. **Preloader on the homepage only.** Removed from every other page.

---

## Working rules

- **Build only what was asked.** If the instruction names two sections, build two sections.
  Do not continue into the rest of the page.
- **Two-iteration cap.** If a section is wrong twice, stop and report. Do not attempt a third
  variation — the spec assignment is wrong, not the execution.
- **Never rewrite `DESIGN.md`.** Propose changes; don't apply them.
- **Report spec compliance.** After each pass, state which DESIGN.md sections you applied
  and confirm the §6 archetype rules still hold across the page.
- **Preserve what works.** SEO markup, schema, analytics, form handlers, and the build
  pipeline are not part of the redesign. Do not refactor them.
- Screenshot after each pass — desktop and phone width.

---

## The failure to avoid

The rejected build failed because **eight of fourteen sections shared one composition**
(gold rule, left serif heading, right text column). It read as a formatted document, not a
designed site.

DESIGN.md §6 exists to prevent this. Its three rules are acceptance criteria:
no archetype twice consecutively, archetype A at most twice per page, and no section may
reuse its composition from the rejected build.

**Check these before declaring any pass complete.**

---

## Stack

Static custom-coded HTML/CSS/JS. No framework, no build step, no animation library.
Motion budget: ≤ 8KB JS, IntersectionObserver plus CSS transitions only (DESIGN.md §9.7).
