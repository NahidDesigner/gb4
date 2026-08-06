# Homepage Clean-Sheet CSS Replacement

Status: approved through the user's direct corrective instruction on 2026-08-06.

## Purpose

Replace the current homepage override stylesheet with one coherent, section-scoped implementation. The replacement must remove cascade conflicts with `styles.css` and `design-system.css`, produce a premium institutional presentation, and leave no broken typography, spacing, color, or composition at desktop or phone widths.

The existing homepage override is not a source of design inspiration. It is replaced as a failed implementation. Existing HTML is used only as the approved content and functionality contract.

## Preserved Elements

- Locked hero layout, image, copy, heading, and typography.
- Approved homepage copy and section inventory.
- Footer markup and mobile sticky call bar.
- Existing forms, links, reviews, badges, SEO, schema, analytics, and interaction behavior.
- No attorney portraits and no additional factual or promotional content.

## Brand System

- Primary navy: `#0A1628`.
- Raised navy: `#162840`.
- Brand gold: `#C9A227`.
- Warm paper: `#F4F1EA`.
- Cool stone: `#E3E6E4`.
- Ink: `#172329`.
- White: `#FFFFFF`.

Orange, teal, route blue, and other non-brand accents are removed. Gold is used for actions, active markers, and short rules. Navy is used for major fields, headers, and high-confidence typography. Paper and stone carry long-form reading content.

## Typography

- Archivo Narrow 600–700 for body-section headings and compact display text.
- Source Sans 3 400–800 for paragraphs, controls, labels, and navigation.
- Cinzel remains only inside the locked hero and existing logo artwork.
- Desktop body-section headings generally stay between 52px and 76px. Only the settlements proof figure may exceed that range.
- Phone headings generally stay between 38px and 52px.
- Body copy remains at least 16px with a target measure of 60–72 characters.
- Heading columns may not become so narrow that ordinary titles wrap into four or more short lines.

## Header

The homepage header remains hidden over the locked hero. Once the hero exits, it becomes a solid navy bar. Menu and Search use white text, the centered reverse logo remains legible, and the phone action uses brand gold with navy text. The header must never render as a transparent gray gradient over body sections.

Drawer and search overlays use the same navy, white, and gold system. No verdigris or legacy stone tokens may leak into these header-owned surfaces.

## Layout System

- `homepage-atlas.css` is replaced, not incrementally patched.
- Every homepage section receives an explicit layout, foreground, background, type scale, and responsive rule.
- Section selectors use the homepage body class plus the section ID or an equally specific structural selector so legacy `:has()`, sticky-heading, serif, uppercase, and direct-child color rules cannot win.
- No heading uses `position: sticky` except where intentionally specified; this replacement specifies none.
- Desktop section spacing generally ranges from 88px to 128px. Phone spacing generally ranges from 60px to 80px.
- Content width is capped at 1360px, with readable sub-measures inside it.
- Repeated CTA content is presented as a compact action strip, not a large gold slab.
- Gold is scarce. Large gold section backgrounds are prohibited.

## Section Compositions

1. **Credentials:** compact warm-paper evidence rail with monochrome marks and one short gold route accent.
2. **Firm:** editorial paper field; balanced headline, three readable columns, clear call and address rows.
3. **CTA strips:** slim navy action bands with a gold button and existing two-line content.
4. **Settlements:** compact navy proof field; large `$100M+` on the left and supporting copy/action on the right.
5. **Why GB:** balanced heading/lead followed by a stable 2×2 commitment grid. No vertical staggering, giant blank areas, or narrow text wells.
6. **Practice areas:** navy heading band and functional photographic louver. The selected panel is visibly dominant; all labels remain legible.
7. **Case types:** stone directory in two columns at desktop and one column on phones.
8. **Reviews:** navy evidence field with a clearly visible Google score and readable horizontal cards.
9. **Mid-page form:** paper or stone split composition with a navy heading field and a contained form. No full-section gold fill.
10. **First 48 hours:** compact route sequence with seven readable records and restrained gold numerals. It must not consume several empty screen heights.
11. **Premises:** clean navy split composition with no diagonal overlay crossing the text.
12. **Process:** stone field with a separate heading/lead followed by a 2×2 process grid. The heading must never overlap the steps.
13. **Service areas:** raised-navy location field with explicit white body text, four route entries, and a compact accident-report action.
14. **Advantage:** paper editorial composition with a moderate headline and two readable text columns.
15. **FAQ:** stone two-column composition with a moderate non-sticky heading and full-width readable accordion rows.
16. **Contact:** compact navy split form with balanced heading, lead, form, and closing call statement.
17. **Office/footer boundary:** existing map, footer, and sticky mobile action bar remain unchanged.

## Section Quality Rules

- Every section receives an explicit background and foreground pair from the brand palette.
- Adjacent sections retain distinct compositions and density.
- No inherited `ds-on-dark`, serif, uppercase, sticky-position, or legacy pseudo-rule may create unreadable or overlapping content.
- The unverified placeholder settlement records stay hidden. The remaining verified/locked settlement claim is presented as a deliberate compact landmark.
- Forms, practice controls, reviews, timelines, service areas, FAQs, and contact actions remain functional at desktop and 375px.
- No horizontal overflow at 375px, 768px, 1280px, or wide desktop widths.
- No section may contain a visible text collision, clipped heading, unreadable direct-child color, or unexplained empty region larger than its primary content block.
- Adjacent sections retain different silhouettes: editorial, proof field, grid, photographic louver, directory, evidence rail, sequence, process board, location field, accordion, and form.

## Verification

Rebuild in page order: header, credentials/firm, CTA and settlements, why, practice areas, case types, reviews, mid-page form, first 48 hours, premises, process, service areas, advantage, FAQ, contact, office/footer boundary.

Automated contract checks must verify preserved hero/footer/action-bar hashes, approved section inventory, brand tokens, no obsolete colors, no JavaScript-dependent hidden content, explicit non-sticky section headings, controlled heading scales, and responsive breakpoints. Final verification includes JavaScript syntax, CSS structure, SEO audit, Impeccable detection, and desktop/phone visual review when the browser surface permits it.
