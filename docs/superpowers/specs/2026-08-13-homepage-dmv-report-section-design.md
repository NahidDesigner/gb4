# Homepage DMV Report Resource Section

## Job and placement

Add one responsive MyNYAccident.com resource section to the homepage. Place it immediately after `#first48` and before `#premises`, because the preceding section tells an injured visitor what to do after a crash and the following section changes subject from motor-vehicle collisions to premises liability.

The new section replaces the compact MyNYAccident.com resource row currently inside `#first48`. Existing drawer, service-area, and footer links remain unchanged.

## Approved visual direction

Reproduce the supplied ChatGPT reference composition as closely as a responsive web section allows:

- full-bleed deep-navy field with restrained gold rules;
- large left-aligned report heading and two-line supporting copy;
- four icon-led benefit columns;
- a bordered MyNYAccident.com action panel;
- a right-side collision/courthouse/phone scene;
- a compact closing band along the bottom;
- independently composed mobile layout rather than a scaled desktop canvas.

Use the site's self-hosted type system: `Atlas Display` for headings and `Atlas Text` for body, controls, and labels. Do not use the serif type baked into the reference.

## Image treatment

Use two client-supplied decorative layers:

- `assets/report-onlybg.webp` (`1774 × 887`) supplies the courthouse, damaged car, light, and navy copy field;
- `assets/report-phone.webp` (`1024 × 1536`, transparent) supplies the complete phone mockup.

Keep both images as separate `<img>` elements inside one decorative media wrapper. The background covers the wrapper while the phone remains an independently positioned, fully visible `object-fit: contain` layer. The section's meaningful heading, benefits, CTA, and disclosure remain semantic HTML.

## Perspective-settle motion

The phone is the section's single authored focal entrance. When `#dmv-report` first enters the viewport, the phone settles into the scene over approximately `700ms` with `cubic-bezier(0.16, 1, 0.3, 1)`:

- desktop and tablet begin about `72px` right and `24px` low, with `0.92` scale, `2deg` clockwise rotation, and zero opacity;
- phone width begins about `36px` above its resting position, with `0.92` scale, `1deg` rotation, and zero opacity;
- the final state uses the authored responsive placement with full opacity and no additive rotation.

Use the existing homepage `IntersectionObserver` and the Web Animations API. The visible resting state is the CSS/default state, so a failed or missing script cannot hide the phone. The entrance runs once. If `prefers-reduced-motion: reduce` is active, if `IntersectionObserver` is unavailable, or if `Element.animate` is unavailable, show the final state immediately with no animation. Do not animate the section copy, benefits, CTA, or background.

## Content and accuracy boundary

The linked site identifies itself as an attorney-advertising incident-intake platform that is not affiliated with the NYS DMV or a government agency. Preserve the requested headline and action, but do not reproduce the reference's unsupported `Official`, `DMV Compliant`, `officially report`, secure-storage, or rights-protection claims.

Use accurate interface copy:

- heading: `Report Your Accident to the DMV`;
- introduction explaining that New York drivers may need to file after certain crashes and that MyNYAccident.com is an independent incident-intake resource;
- benefits: `Guided Intake`, `Private Submission`, `MV-104 Guidance`, and `Available Online`, each with restrained descriptive copy;
- action: `Start your accident intake at MyNYAccident.com`;
- disclosure title: `Independent website`, followed by `Not affiliated with the NYS DMV or any government agency.`;
- official-resource link: `View official NY DMV filing information`;
- closing line: `Get organized. Document what happened. Review the filing requirements.`

The main action opens `https://mynyaccident.com/` in a new tab with safe external-link attributes. The official information link opens the NY DMV filing-information page in a new tab.

## Responsive and accessible behavior

- Desktop uses an approximately 48/52 content-to-media split. The phone sits fully inside the right field above the background, while the four benefits remain in one row.
- Tablet keeps the split, scales the phone with `clamp()`, and allows benefits to wrap two-by-two without cropping the phone.
- At phone width, the decorative media wrapper becomes the first item inside the section. The centered phone appears over a bounded background scene, followed by the eyebrow, heading, introduction, benefits, CTA, disclosure, and closing band.
- Body text stays at least 16px, links and controls provide at least 44px touch targets, focus is visible, and no content is hidden behind the sticky call bar.
- Both image layers are decorative; the section's meaning remains in HTML.

## Verification

- Source contract covers unique section ID, placement, external links, disclosure, approved fonts, both supplied image layers, mobile media-first order, perspective-settle hook, reduced-motion behavior, and absence of a live phone-screen overlay.
- Existing homepage contract and full unit suite remain green.
- Desktop and 375px computed geometry confirm no page overflow, no section clipping, a fully visible phone layer, sensible content/media placement, and visible action/disclosure content.
- Paired screenshots are reviewed at desktop and phone width, with at most one batched correction pass.
- The homepage hero, footer, sticky call bar, forms, SEO/schema, analytics, and all other pages remain unchanged.
