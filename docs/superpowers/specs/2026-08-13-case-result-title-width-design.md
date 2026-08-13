# Case Result Title Width

## Scope

Adjust only the case-title measure inside the existing result cards on the homepage and the dedicated Case Results page. Preserve all copy, markup, card dimensions, spacing, typography, colors, alignment, carousel behavior, and responsive structure.

## Design

Remove the fixed character-based `max-width` from the title element on both card implementations. Each title will then use the full available inner width of its card and wrap naturally at the card padding boundary.

Desktop titles remain left-aligned. The existing phone treatment remains centered. Amounts and detail copy retain their current measures and styling.

## Implementation

- Homepage: override `.ds-figure-cell__case` to `max-width: none` in the final settlement-card rules.
- Case Results page: override `.rcard-t` to `max-width: none` in the final page-specific card rules.
- Do not modify HTML or client copy.

## Verification

- Add a source-level regression check that fails while either final title constraint remains.
- Measure title width against card content width at desktop and phone sizes on both pages.
- Confirm no horizontal overflow and review paired desktop/mobile screenshots for each edited section.
- Confirm the homepage section inventory and composition remain unchanged, so DESIGN.md composition acceptance criteria are unaffected.
