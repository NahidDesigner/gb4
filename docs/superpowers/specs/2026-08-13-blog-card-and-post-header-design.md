# Blog Card and Post Header Design

## Scope

Refine only the blog archive post presentation and the title area shared by individual blog posts. Preserve all HTML, copy, links, metadata, article layout, sidebar, header, footer, and sticky mobile call bar.

## Blog archive

- Replace the oversized poster-style entries with compact reading cards.
- Use a two-column card grid inside the existing main blog column on desktop and a one-column stack on narrower screens.
- Each card contains the existing date, title, description, and “Read this post” action in that order.
- Cards use the existing warm paper, Atlantic navy, gold, and typography tokens. They have a quiet one-pixel border, restrained elevation, and a gold top rule rather than a full navy field.
- Titles remain prominent but proportionate: approximately 30–34px on desktop and 26–30px on mobile.
- The entire card remains clickable, with visible hover and keyboard-focus feedback.

## Single-post title area

- Center the publication date and title.
- Remove the left/side border and the date’s leading rule.
- Reduce the desktop title to a maximum around 68px and the mobile title to approximately 36–42px.
- Remove all rules surrounding the title group.
- Add one short centered gold rule directly below the title. It uses softly faded ends, measures no more than 7rem on desktop, and contracts to 4.5rem on mobile.
- Retain the existing dark photographic header surface and all content below it.

## Responsive and acceptance criteria

- Two archive cards appear side by side when the main content column can support them; otherwise they stack.
- Cards maintain equal visual weight without forcing equal-height copy truncation.
- At desktop and 375px widths, the page has no horizontal overflow.
- Single-post titles remain centered and legible without dominating the entire first viewport, with exactly one centered accent rule below the title.
- Existing page semantics, focus order, links, and mobile actions remain unchanged.
