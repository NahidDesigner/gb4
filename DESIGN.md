# GB Law Firm — Homepage Design Authority

Status: binding  
Version: 7  
Approved direction: Long Island Atlas and Coastal Survey

## 1. Visual thesis

GB Law Firm presents Long Island personal-injury work through the visual language of useful local infrastructure: an atlas, a route index, a field survey, and a well-organized public record.

The site must feel contemporary, highly composed, direct, and specific to Long Island. It must not resemble the rejected luxury-law template of repeated navy fields, gold rules, centered serif headings, and interchangeable rectangular cards. It must also avoid legal-tech dashboard styling, glass effects, neon gradients, and invented data visualizations.

The system earns memorability from real locality, real content, and clear information architecture—not decoration or fabricated proof.

## 2. Non-negotiable boundaries

1. The existing homepage hero is locked. Do not alter its layout, image, copy, heading, or typography.
2. Existing client-approved body copy remains verbatim.
3. The existing footer and sticky mobile call bar remain unchanged.
4. Homepage only. Do not change other pages.
5. Do not add sections, attorney portraits, claims, results, reviews, endorsements, locations, process stages, or factual copy.
6. Use only existing homepage content, form fields, review data, badges, phone details, and repository assets.
7. Preserve analytics, schema, SEO markup, form behavior, and the build pipeline.
8. The homepage preloader remains homepage-only.

## 3. Color system

The locked hero retains its current colors as an isolated established composition. The redesigned body uses the following roles:

- **Mineral paper — `#F2F0EA`:** primary reading surface.
- **Coastal mist — `#DCE7E7`:** secondary geographic and informational surface.
- **Atlantic blue — `#123D56`:** major dark fields, links, and institutional emphasis.
- **Route blue — `#216B88`:** active route geometry and interactive emphasis.
- **Carbon — `#172329`:** primary text and high-contrast structure.
- **Survey orange — `#E35D2F`:** scarce signal color for active markers and key actions.
- **White — `#FFFFFF`:** text and controls on dark fields.

The logo keeps its native brand colors. Gold may appear inside the logo and existing locked hero, but it is not the body system's decorative accent.

Color must meet WCAG AA contrast. Secondary text is tinted from its surface color, never generic low-contrast gray.

## 4. Typography

- **Locked hero:** unchanged.
- **Display and navigational headings:** self-hosted Archivo Narrow, weights 600–700.
- **Body and controls:** self-hosted Source Sans 3, weights 400–800.
- **Cinzel:** limited to the locked hero and any existing logo artwork. Do not carry it into new body sections.

Headings are compact, direct, and proportionate to their content. Do not add eyebrow copy above headings. Display text never exceeds 6rem and tracking never goes below `-0.04em`. Body copy targets a 65–75 character measure.

## 5. Composition language

The body is organized like a useful atlas rather than a stack of content cards.

- Route lines connect real content across sections and indicate reading direction.
- Index bands group existing labels, badges, questions, and services.
- Large county-scale fields provide breathing room between dense reading sections.
- Measured geometry, coordinates, ticks, and contours are permitted only when they organize supplied information. They must not imply exact geographic or legal data.
- Asymmetry is deliberate: a dominant text or proof field is balanced by a narrower route, index, or action field.
- Adjacent sections may not repeat the same hierarchy, silhouette, or interaction pattern.
- Density varies across the scroll: orientation, credibility, service exploration, objection resolution, and contact each receive a distinct rhythm.

Do not use equal card grids as the page scaffold. Do not wrap every piece of copy in a rectangle. Borders and rules are structural and sparse.

## 6. Reusable primitives

Only these primitives are approved:

- **Route line:** a thin authored SVG or CSS path that connects supplied content and may draw once on entry.
- **Index row:** an existing label or question aligned to a clear interaction target.
- **Location field:** a pale or dark surface using real Long Island place names already present in approved copy.
- **Evidence strip:** existing badges or reviews presented with source attribution and without invented seals or metrics.
- **Action marker:** the existing phone or case-review action, using survey orange sparingly.
- **Reading panel:** a long-form text area with strong measure and spacing; not a generic card.

These primitives may recur, but adjacent sections cannot share the same full composition.

## 7. Imagery

Use repository imagery only. No attorney portraits on the homepage. Photography must support the supplied subject and should be cropped with documentary clarity rather than overlaid with generic prestige effects.

Authored SVG is for exact geometry, route lines, markers, and diagrams—not faux hand-drawn illustration. Decorative maps must remain abstract and must not present fabricated geography as fact.

## 8. Interaction and motion

The main authored motion is the post-hero route transition. It may use stroke drawing, clipping, and a small marker movement to connect the locked hero to the body system.

Elsewhere:

- Use restrained progressive disclosure for existing accordions, practice-area controls, and content reveals.
- Use exponential ease-out timing from an already-visible default.
- Avoid identical reveal animations on every section.
- Preserve keyboard operation and visible focus.
- Respect `prefers-reduced-motion`; content must remain fully visible and usable without animation.
- Use IntersectionObserver plus CSS transitions only. No animation library.

## 9. Responsive behavior

Mobile is a designed composition.

- At 375px, route geometry simplifies and labels move into the reading order rather than overlapping content.
- Body text remains at least 16px with comfortable line height.
- Tap targets are at least 44px.
- No horizontal page overflow.
- Service controls, FAQs, phone actions, and form controls remain reachable by keyboard and touch.
- The sticky mobile call bar remains unchanged and must not cover the final form actions.

Tablet and laptop layouts preserve asymmetry without squeezing body copy. Wide layouts increase breathing room, not text measure.

## 10. Acceptance criteria

The homepage passes only when all are true:

1. The locked hero, footer, sticky call bar, approved copy, and functionality are preserved.
2. No additional factual or promotional content has been introduced.
3. The first post-hero viewport clearly establishes the Long Island atlas world.
4. The result cannot be mistaken for a generic navy-and-gold law-firm template.
5. Adjacent sections do not reuse the same perceived composition.
6. Existing calls and case-review actions remain obvious.
7. Desktop and 375px screenshots both look intentionally composed.
8. Contrast, focus, keyboard behavior, reduced motion, and responsive layout meet the craft floor.
9. No verified-content boundary is crossed: no fabricated outcomes, seals, reviews, metrics, or locations.
10. A complete first inspection is followed by at most one batched correction and one confirmation pass.
