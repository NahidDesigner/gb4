import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';

const html = fs.readFileSync(new URL('../index.html', import.meta.url), 'utf8');

function extract(pattern, label) {
  const match = html.match(pattern);
  assert.ok(match, `${label} must remain present`);
  return match[0];
}

function sha(value) {
  return crypto.createHash('sha256').update(value).digest('hex');
}

const hero = extract(
  /  <!-- ================= HERO \(locked\) ================= -->[\s\S]*?  <\/header>/,
  'locked hero',
);
const footer = extract(/<footer class="foot">[\s\S]*?<\/footer>/, 'footer');
const actionbar = extract(
  /<div class="actionbar" id="actionbar">[\s\S]*?<\/div>/,
  'sticky mobile call bar',
);

assert.equal(
  sha(hero),
  '9a82a2a655ac161cdc448da69a780550aaa81c31a1326e09fcb33f3fb7fd018c',
  'locked hero markup changed',
);
assert.equal(
  sha(footer),
  '682b4e9ce8da99a6743b92fea6db0e6fe16e259b363e31c72020791ade84b5d4',
  'footer markup changed',
);
assert.equal(
  sha(actionbar),
  '151be79939be316a93766b76f5f906f6ea113cf49b9bb3d342f3af277a83d7cd',
  'sticky mobile call bar markup changed',
);

assert.match(html, /<body class="atlas-home">/, 'homepage must opt into the atlas redesign');
assert.match(
  html,
  /<link rel="stylesheet" href="homepage-atlas\.css(?:\?v=[^"]+)?" \/>/,
  'homepage atlas stylesheet must be linked',
);
assert.match(
  html,
  /<script src="homepage-atlas\.js(?:\?v=[^"]+)?"><\/script>/,
  'homepage atlas behavior must be loaded',
);

for (const id of [
  'creds',
  'firm',
  'settlements',
  'why',
  'practice',
  'casetypes',
  'clients',
  'accident-facts',
  'first48',
  'premises',
  'process',
  'areas',
  'advantage',
  'questions',
  'contact',
]) {
  assert.match(html, new RegExp(`id="${id}"`), `approved section #${id} must remain`);
}

assert.match(
  html,
  /id="clients"[\s\S]*?id="accident-facts"[\s\S]*?<div class="cta-wrap">/,
  'car-accident facts section must sit directly after testimonials and before the existing CTA',
);
assert.match(
  html,
  /<section class="ds-caseindex ds-caseindex--facts" id="accident-facts"[\s\S]*?<img[^>]+class="ds-caseindex__image"[^>]+src="assets\/car-crash-768x406\.webp"[\s\S]*?<h2[^>]+id="accident-facts-h">[\s\S]*?<\/h2>[\s\S]*?<p class="ds-caseindex__lede">A few things every Long Island car accident client should understand before the first call\.<\/p>[\s\S]*?<ul class="ds-caseindex__grid">[\s\S]*?<\/ul>[\s\S]*?<\/section>/,
  'car-accident facts section must reuse the case-index structure with image left and copy right',
);
assert.match(
  html,
  /<h2 class="ds-caseindex__heading" id="accident-facts-h">\s*<span class="ds-caseindex__title-line">What You Actually Need<\/span>\s*<span class="ds-caseindex__title-line">to Know About<\/span>\s*<span class="ds-caseindex__title-line ds-caseindex__title-line--accent">Car Accident Cases in<\/span>\s*<span class="ds-caseindex__title-line ds-caseindex__title-line--accent">New York<\/span>\s*<\/h2>/,
  'car-accident facts title must use the four approved deliberate lines',
);
assert.match(
  html,
  /<svg class="ds-caseindex__route-frame"[\s\S]*?<span class="ds-caseindex__image-dots"[\s\S]*?<aside class="ds-caseindex__protection"[\s\S]*?<strong>Protecting Your Rights<\/strong>[\s\S]*?<span>We fight for the compensation you truly deserve\.<\/span>[\s\S]*?<\/aside>/,
  'car-accident facts image must include the approved route geometry, registration dots, and rights plaque',
);
assert.match(
  html,
  /<span class="ds-caseindex__legal-emblem" aria-hidden="true">[\s\S]*?class="ds-caseindex__legal-emblem-icon"[\s\S]*?<\/span>/,
  'car-accident facts text field must include the shield-and-scales emblem inside its rings',
);
for (const factHeading of [
  'New York is a no-fault state, with a serious injury exception',
  "The carrier's first offer is almost never what the case is worth",
  'You have three years to file most car accident cases',
  'Your social media account is evidence',
  'Most cases settle. The ones that do not, settle higher',
]) {
  assert.ok(html.includes(factHeading), `missing approved car-accident fact: ${factHeading}`);
}

for (const forbidden of [
  'Reviewed where it matters',
  'Case Assembly System',
  'Evidence Current',
  'Verified outcome',
]) {
  assert.doesNotMatch(html, new RegExp(forbidden, 'i'), `invented content detected: ${forbidden}`);
}

const css = fs.readFileSync(new URL('../homepage-atlas.css', import.meta.url), 'utf8');
const js = fs.readFileSync(new URL('../homepage-atlas.js', import.meta.url), 'utf8');
for (const token of [
  '--atlas-paper: #f4f1ea',
  '--atlas-stone: #e3e6e4',
  '--atlas-navy: #0a1628',
  '--atlas-navy-raised: #162840',
  '--atlas-gold: #c9a227',
  '--atlas-display: "atlas display", "archivo narrow"',
  '--atlas-utility: "archivo narrow"',
  '--atlas-body: "source sans 3"',
  '--atlas-frame:',
  '--atlas-section-gap:',
  '--atlas-heading-xl:',
  '--atlas-section-space:',
  '--atlas-copy-measure:',
]) {
  assert.ok(css.toLowerCase().includes(token), `missing design token ${token}`);
}

for (const approvedAtlasColor of ['#e35d2f', '#216b88', '#123d56', '#dce7e7']) {
  assert.ok(
    css.toLowerCase().includes(approvedAtlasColor),
    `missing approved DESIGN.md v7 atlas color: ${approvedAtlasColor}`,
  );
}

assert.match(
  css,
  /EDIT 15 — Locked mobile hero lockup restore[\s\S]*?@media\s*\(max-width:\s*430px\)[\s\S]*?\.atlas-home \.lockup-stack\s*\{[\s\S]*?flex-direction:\s*column[\s\S]*?width:\s*88px[\s\S]*?\.atlas-home \.lockup-menu,[\s\S]*?\.atlas-home \.lockup-search\s*\{[\s\S]*?min-height:\s*0[\s\S]*?font-size:\s*9px/s,
  'locked mobile hero lockup must keep the original vertical Menu/Search stack with visible labels and no forced 44px overflow',
);

assert.match(
  css,
  /\.atlas-home \.ds-site-header\.is-solid\s*\{[^}]*background:\s*var\(--atlas-navy\)/s,
  'solid sticky header must use the brand navy background',
);
assert.match(
  css,
  /\.atlas-home \.ds-site-header\.is-solid \.ds-nav-trigger\s*\{[^}]*color:\s*var\(--atlas-white\)/s,
  'solid sticky header controls must use white text',
);
assert.match(
  css,
  /\.atlas-home \.ds-button-call\s*\{[^}]*background:\s*var\(--atlas-gold\)/s,
  'sticky phone action must use the brand gold background',
);
assert.match(
  css,
  /\.atlas-home \.ds-button-call\s*\{[^}]*color:\s*var\(--atlas-navy\)/s,
  'sticky phone action must use navy text',
);
assert.match(
  css,
  /\.atlas-home \.whyband \.rail-track\s*\{/,
  'commitments section must style the approved rail-track markup',
);
assert.match(
  css,
  /\.atlas-home \.whyband \.wcard\s*\{/,
  'commitments section must style the approved card markup',
);
assert.match(
  css,
  /\.atlas-home #process \.h2\s*\{[^}]*position:\s*static[^}]*top:\s*auto/s,
  'process heading must be explicitly non-sticky',
);
assert.match(
  css,
  /\.atlas-home \.whyband \.rail-track\s*\{[^}]*grid-template-areas:/s,
  'commitments must use a stepped editorial composition',
);
assert.match(
  css,
  /\.atlas-home #process \.steps\s*\{[^}]*grid-template-columns:\s*repeat\(4,\s*minmax\(0,\s*1fr\)\)/s,
  'process must use a four-stage editorial progression',
);
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
  'FAQ must use the approved navy and paper split',
);
assert.doesNotMatch(
  html,
  /<div class="ds-settlements__record" hidden aria-hidden="true">/,
  'dummy settlement register must be visible during the approved design-development stage',
);
assert.match(
  html,
  /<p class="ds-settlements__figure"[^>]*data-ds-counter[^>]*data-ds-count-target="100"[^>]*>\$100<sup>M\+<\/sup><\/p>/,
  'settlement landmark figure must retain its final value in HTML while exposing a counter target',
);
assert.match(
  html,
  /<span class="ds-figure-cell__amount"[^>]*data-ds-counter[^>]*data-ds-count-target="2400000"[^>]*>\$2,400,000<\/span>/,
  'settlement record amounts must retain final HTML values while exposing counter targets',
);
assert.match(
  js,
  /const settlementCounters = Array\.from\(document\.querySelectorAll\('\[data-ds-counter\]'\)\)/,
  'settlement counter script must target only explicit counter elements',
);
assert.match(
  js,
  /requestAnimationFrame\(tick\)/,
  'settlement counters must animate through requestAnimationFrame',
);
assert.match(
  js,
  /prefers-reduced-motion:\s*reduce[\s\S]*?finishSettlementCounters/,
  'settlement counters must respect reduced motion and show final values immediately',
);
assert.match(
  js,
  /const practicePanels = Array\.from\(document\.querySelectorAll\('#practice \.ds-pa__panel\[for\]'\)\)/,
  'practice panel interactions must be scoped to explicit practice panels',
);
assert.match(
  js,
  /practicePanels\.forEach[\s\S]*?const scrollLeft = window\.scrollX[\s\S]*?const scrollTop = window\.scrollY[\s\S]*?event\.preventDefault\(\)[\s\S]*?radio\.checked = true[\s\S]*?radio\.focus\(\{ preventScroll: true \}\)[\s\S]*?window\.scrollTo\(scrollLeft, scrollTop\)[\s\S]*?requestAnimationFrame\(\(\) => window\.scrollTo\(scrollLeft, scrollTop\)\)/,
  'practice panel pointer selection must not scroll hidden radio inputs back to the section title',
);
assert.match(
  js,
  /if \(event\.target\.closest\('a'\)\) return;/,
  'practice panel direct links must remain normal links',
);
assert.match(
  css,
  /EDIT 9 — Settlement counter animation stability[\s\S]*?\.atlas-home #settlements \[data-ds-counter\]\s*\{[\s\S]*?font-variant-numeric:\s*tabular-nums lining-nums/s,
  'settlement counters must use tabular figures to prevent digit jitter',
);
assert.match(
  css,
  /EDIT 10 — Mobile hero lockup fit[\s\S]*?@media\s*\(max-width:\s*430px\)\s*\{[\s\S]*?\.atlas-home \.lockup\s*\{[\s\S]*?height:\s*58px[\s\S]*?\.atlas-home \.lockup-stack\s*\{[\s\S]*?flex-direction:\s*row[\s\S]*?width:\s*104px[\s\S]*?\.atlas-home \.lockup-menu,[\s\S]*?\.atlas-home \.lockup-search\s*\{[\s\S]*?min-width:\s*52px[\s\S]*?font-size:\s*0/s,
  'mobile hero lockup must use a compact horizontal control strip instead of the bulky stacked widget',
);
assert.match(
  css,
  /BRAND EDITORIAL CORRECTION PASS/,
  'final correction pass must be present after the earlier restoration layer',
);
assert.match(
  css,
  /\.atlas-home #settlements \.ds-settlements__record\s*\{[^}]*display:\s*block/s,
  'settlement dummy register must be explicitly displayed',
);
assert.match(
  html,
  /<div class="ds-settlements__controls" aria-label="Settlement result navigation">[\s\S]*?<button class="ds-settlements__arrow ds-settlements__arrow--prev" type="button" data-settlement-scroll="prev" aria-label="Previous settlement result">[\s\S]*?<use href="#i-arrow"\/>[\s\S]*?<button class="ds-settlements__arrow ds-settlements__arrow--next" type="button" data-settlement-scroll="next" aria-label="Next settlement result">[\s\S]*?<use href="#i-arrow"\/>[\s\S]*?<\/div>/,
  'settlement register must expose two real previous/next arrow buttons instead of a decorative span',
);
assert.match(
  css,
  /\.atlas-home #settlements \.ds-settlements__list\s*\{[^}]*scrollbar-width:\s*none/s,
  'settlement register scrollbar must be hidden after replacing it with the arrow affordance',
);
assert.match(
  css,
  /\.atlas-home #settlements \.ds-settlements__list::-\webkit-scrollbar\s*\{[^}]*display:\s*none/s,
  'settlement register webkit scrollbar must be hidden',
);
assert.match(
  css,
  /\.atlas-home #settlements \.ds-settlements__controls\s*\{[^}]*position:\s*absolute[\s\S]*?\.atlas-home #settlements \.ds-settlements__arrow\s*\{[^}]*display:\s*grid[\s\S]*?cursor:\s*pointer/s,
  'settlement register dual arrow controls must be positioned and visibly clickable',
);
assert.match(
  js,
  /const settlementScroller = document\.querySelector\('#settlements \.ds-settlements__list'\)[\s\S]*?const settlementScrollButtons = Array\.from\(document\.querySelectorAll\('\[data-settlement-scroll\]'\)\)[\s\S]*?settlementScrollButtons\.forEach[\s\S]*?button\.addEventListener\('click'[\s\S]*?scrollBy\(\{[\s\S]*?left:\s*direction \* distance[\s\S]*?behavior:\s*reduceMotion\.matches \? 'auto' : 'smooth'/s,
  'settlement register arrow buttons must scroll the results list by one item',
);
assert.match(
  css,
  /EDIT 16 — Mobile settlement one-slide rail[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #settlements \.ds-settlements__record\s*\{[\s\S]*?padding:\s*clamp\(1rem,\s*5vw,\s*1\.3rem\)[\s\S]*?\.atlas-home #settlements \.ds-settlements__list\s*\{[\s\S]*?gap:\s*1rem[\s\S]*?padding:\s*0 0 3\.7rem[\s\S]*?\.atlas-home #settlements \.ds-figure-cell\s*\{[\s\S]*?flex:\s*0 0 100%/s,
  'mobile settlement register must present one full-width slide at a time with breathing space below the card',
);
assert.match(
  css,
  /EDIT 18 — Mobile settlement unboxed case result[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #settlements \.ds-settlements__record\s*\{[\s\S]*?border:\s*0[\s\S]*?background:\s*transparent[\s\S]*?\.atlas-home #settlements \.ds-figure-cell[\s\S]*?\{[\s\S]*?border:\s*0[\s\S]*?background:\s*transparent[\s\S]*?box-shadow:\s*none[\s\S]*?\.atlas-home #settlements \.ds-figure-cell::before\s*\{[\s\S]*?content:\s*""/s,
  'mobile settlement single case result must not render as a boxed card inside the settlement panel',
);
assert.match(
  css,
  /\.atlas-home #casetypes \.ds-caseindex__cell::before\s*\{[^}]*width:\s*var\(--case-tick-width\)/s,
  'case-type mobile tick must be width-controlled instead of crossing headings',
);
assert.match(
  css,
  /@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__cell\s*\{[\s\S]*?--case-tick-width:\s*16px/s,
  'case-type mobile ticks must shrink at phone width',
);
assert.match(
  css,
  /EDIT 2 — Case type tick cleanup[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__cell::before\s*\{[\s\S]*?width:\s*1px[\s\S]*?height:\s*1\.65rem/s,
  'case-type marker must be a vertical side tick, not a horizontal line that can cross titles',
);
assert.match(
  css,
  /EDIT 3 — Case type row balance[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__grid > \.ds-caseindex__cell[\s\S]*?display:\s*grid[\s\S]*?grid-template-columns:\s*1px\s+minmax\(0,\s*1fr\)/s,
  'case-type rows must reserve a structural marker column so title alignment cannot drift',
);
assert.match(
  css,
  /EDIT 3 — Case type row balance[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__grid > \.ds-caseindex__cell::before\s*\{[\s\S]*?position:\s*static[\s\S]*?grid-column:\s*1/s,
  'case-type marker must participate in the row grid instead of being absolutely positioned over text',
);
assert.match(
  css,
  /EDIT 3 — Case type row balance[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__grid > \.ds-caseindex__cell :where\(\.ds-caseindex__name,\s*\.ds-caseindex__desc\)\s*\{[\s\S]*?grid-column:\s*2/s,
  'case-type title and description must share one consistent content column',
);
assert.match(
  css,
  /EDIT 2 — Case type tick cleanup[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #casetypes \.ds-caseindex__cell::before\s*\{[\s\S]*?top:\s*1\.85rem/s,
  'case-type phone marker must sit beside the title block instead of through the title text',
);
assert.match(
  css,
  /@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home \.cta-wrap \.cta\s*\{[\s\S]*?grid-template-columns:\s*1fr/s,
  'phone CTA strips must stack instead of squeezing the button beside the title',
);
assert.match(
  css,
  /@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #advantage \.wrap\s*\{[\s\S]*?overflow:\s*hidden/s,
  'advantage phone layout must contain its decorative field and text',
);
assert.match(
  css,
  /\.atlas-home #areas \.rte-strong\s*\{[^}]*color:\s*var\(--atlas-white\)/s,
  'service-area closing copy must stay readable on navy',
);
assert.doesNotMatch(
  css,
  /main\s*>\s*\.sec--tight\s*\{[^}]*background:\s*var\(--atlas-gold\)/s,
  'mid-page form must not use a full gold surface',
);
assert.match(
  css,
  /EDIT 4 — Mid-page consultation form redesign[\s\S]*?\.atlas-home main > \.sec--tight \.formcard\s*\{[\s\S]*?grid-template-columns:\s*minmax\(280px,\s*0\.72fr\)\s+minmax\(0,\s*1\.08fr\)/s,
  'mid-page form must use a composed consultation-panel split instead of a giant poster/form block',
);
assert.match(
  css,
  /EDIT 4 — Mid-page consultation form redesign[\s\S]*?\.atlas-home main > \.sec--tight \.form-h\s*\{[\s\S]*?font-family:\s*"Atlas Display",\s*sans-serif[\s\S]*?font-size:\s*clamp\(2\.15rem,\s*3\.45vw,\s*3\.45rem\)/s,
  'mid-page form headline must use the body display face and stay scaled down from the oversized poster treatment',
);
assert.match(
  css,
  /EDIT 4 — Mid-page consultation form redesign[\s\S]*?\.atlas-home main > \.sec--tight \.field,\s*[\s\S]*?\.atlas-home main > \.sec--tight \.btn,\s*[\s\S]*?\.atlas-home main > \.sec--tight \.form-status\s*\{[\s\S]*?width:\s*100%[\s\S]*?max-width:\s*100%[\s\S]*?margin-inline:\s*0/s,
  'mid-page form fields and button must not inherit the old side margins that pushed controls out of the panel',
);
assert.match(
  css,
  /EDIT 4 — Mid-page consultation form redesign[\s\S]*?\.atlas-home main > \.sec--tight \.btn\s*\{[\s\S]*?width:\s*100%[\s\S]*?max-width:\s*100%[\s\S]*?background:\s*var\(--atlas-gold\)/s,
  'mid-page form submit button must stay contained in the form column and use the brand action color',
);
assert.match(
  css,
  /EDIT 5 — First48 timeline balance[\s\S]*?@media\s*\(max-width:\s*1100px\)\s*\{[\s\S]*?\.atlas-home #first48 \.ds-sequence\s*\{[\s\S]*?grid-template-columns:\s*1fr[\s\S]*?max-width:\s*760px[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(even\)\s*\{[\s\S]*?transform:\s*none/s,
  'first48 must switch out of the cramped alternating timeline before tablet widths',
);
assert.match(
  css,
  /EDIT 5 — First48 timeline balance[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__slot,[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(odd\) \.ds-sequence-step__slot,[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(even\) \.ds-sequence-step__slot\s*\{[\s\S]*?grid-template-columns:\s*clamp\(3\.6rem,\s*9vw,\s*4\.4rem\)\s+minmax\(0,\s*1fr\)[\s\S]*?text-align:\s*left/s,
  'first48 number and text lanes must not collide on mid and mobile widths',
);
assert.match(
  css,
  /EDIT 12 — First48 phone breathing room[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__slot,[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(odd\) \.ds-sequence-step__slot,[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(even\) \.ds-sequence-step__slot\s*\{[\s\S]*?grid-template-columns:\s*minmax\(3\.95rem,\s*4\.35rem\)\s+minmax\(0,\s*1fr\)[\s\S]*?column-gap:\s*clamp\(1\.25rem,\s*5vw,\s*1\.65rem\)[\s\S]*?padding:\s*clamp\(2\.05rem,\s*7vw,\s*2\.45rem\)\s+0\s+clamp\(2\.25rem,\s*8vw,\s*2\.75rem\)\s+0/s,
  'first48 phone rows must have breathing room between numeral and heading',
);
assert.match(
  css,
  /EDIT 12 — First48 phone breathing room[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__title\s*\{[\s\S]*?margin-top:\s*0\.1rem[\s\S]*?margin-bottom:\s*0\.75rem[\s\S]*?font-size:\s*clamp\(1\.28rem,\s*5\.8vw,\s*1\.58rem\)/s,
  'first48 phone headings must step down slightly so the text block can breathe',
);
assert.match(
  css,
  /EDIT 20 — First48 desktop indexed rows[\s\S]*?@media\s*\(min-width:\s*1101px\)[\s\S]*?\.atlas-home #first48 \.ds-sequence\s*\{[\s\S]*?grid-template-columns:\s*repeat\(2,\s*minmax\(0,\s*1fr\)\)[\s\S]*?\.atlas-home #first48 \.ds-sequence-step:nth-child\(even\)\s*\{[\s\S]*?transform:\s*none[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__slot[\s\S]*?grid-template-columns:\s*minmax\(4\.8rem,\s*5\.4rem\)\s+minmax\(0,\s*1fr\)[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__num[\s\S]*?font-size:\s*clamp\(3\.2rem,\s*4\.8vw,\s*4\.45rem\)[\s\S]*?\.atlas-home #first48 \.ds-sequence-step__body[\s\S]*?max-width:\s*34rem/s,
  'first48 desktop must use stable indexed rows instead of the clipped alternating rail',
);
assert.match(
  css,
  /EDIT 13 — Mobile footer actionbar seam[\s\S]*?\.atlas-home\s*\{[\s\S]*?--ab-h:\s*44px[\s\S]*?background:\s*var\(--stone-black\)[\s\S]*?@media\s*\(min-width:\s*768px\)\s*\{[\s\S]*?\.atlas-home\s*\{[\s\S]*?--ab-h:\s*0px[\s\S]*?background:\s*var\(--atlas-paper\)/s,
  'mobile actionbar reserve must match the actual 44px bar height and inherit the footer-dark surface',
);
assert.match(
  css,
  /EDIT 6 — First48 closing action panel[\s\S]*?\.atlas-home #first48 \.ds-sequence-section__foot\s*\{[\s\S]*?display:\s*grid[\s\S]*?grid-template-columns:\s*minmax\(0,\s*1fr\)\s+minmax\(300px,\s*0\.78fr\)[\s\S]*?background:\s*var\(--atlas-navy\)/s,
  'first48 closing action must be a composed action panel instead of loose horizontal rules',
);
assert.match(
  css,
  /EDIT 6 — First48 closing action panel[\s\S]*?\.atlas-home #first48 \.ds-resource-row\s*\{[\s\S]*?min-height:\s*92px[\s\S]*?background:\s*var\(--atlas-paper\)[\s\S]*?border:\s*1px solid rgba\(201,\s*162,\s*39,\s*0\.45\)/s,
  'first48 accident-report link must read as the secondary action inside the panel',
);
assert.match(
  css,
  /EDIT 7 — Advantage section redesign[\s\S]*?\.atlas-home #advantage \.h2\s*\{[\s\S]*?font-family:\s*"Atlas Display",\s*sans-serif[\s\S]*?font-size:\s*clamp\(2\.05rem,\s*3\.1vw,\s*3\.15rem\)/s,
  'advantage heading must use the body display face and stop the oversized serif treatment',
);
assert.match(
  css,
  /EDIT 7 — Advantage section redesign[\s\S]*?\.atlas-home #advantage \.rte\s*\{[\s\S]*?display:\s*grid[\s\S]*?grid-template-columns:\s*repeat\(2,\s*minmax\(0,\s*1fr\)\)[\s\S]*?background:\s*var\(--atlas-paper\)/s,
  'advantage body copy must sit in a composed reading panel rather than floating beside a billboard headline',
);
assert.match(
  css,
  /EDIT 7 — Advantage section redesign[\s\S]*?\.atlas-home #advantage \.rte-strong\s*\{[\s\S]*?grid-column:\s*1\s*\/\s*-1[\s\S]*?background:\s*var\(--atlas-navy\)[\s\S]*?color:\s*var\(--atlas-white\)/s,
  'advantage closing callout must be an integrated action marker inside the reading panel',
);
assert.match(
  css,
  /EDIT 7 — Advantage section redesign[\s\S]*?\.atlas-home #advantage \.rte p\.rte-strong\s*\{[\s\S]*?color:\s*var\(--atlas-white\)/s,
  'advantage callout paragraph text must stay white against the navy panel',
);
assert.match(
  css,
  /EDIT 8 — FAQ atlas index redesign[\s\S]*?\.atlas-home #questions\s*\{[\s\S]*?background:[\s\S]*?#dce7e7[\s\S]*?#f2f0ea/s,
  'FAQ must use the approved coastal mist and mineral paper surfaces, not the old luxury split',
);
assert.match(
  css,
  /EDIT 8 — FAQ atlas index redesign[\s\S]*?\.atlas-home #questions \.wrap\s*\{[\s\S]*?grid-template-columns:\s*minmax\(260px,\s*0\.34fr\)\s+minmax\(0,\s*1fr\)/s,
  'FAQ must use an asymmetric index layout with a narrower heading field',
);
assert.match(
  css,
  /EDIT 8 — FAQ atlas index redesign[\s\S]*?\.atlas-home #questions summary\s*\{[\s\S]*?display:\s*grid[\s\S]*?grid-template-columns:\s*minmax\(0,\s*1fr\)\s+44px[\s\S]*?min-height:\s*72px/s,
  'FAQ question rows must be structured as accessible index rows with a 44px control lane',
);
assert.match(
  css,
  /EDIT 14 — FAQ brand-flow correction[\s\S]*?\.atlas-home #questions \.h2\s*\{[\s\S]*?margin-top:\s*clamp\(-1\.35rem,\s*-1\.4vw,\s*-0\.75rem\)[\s\S]*?border-bottom:\s*2px solid #216b88/s,
  'FAQ heading must sit higher and use route-blue, not the loud orange underline',
);
assert.match(
  css,
  /EDIT 14 — FAQ brand-flow correction[\s\S]*?\.atlas-home #questions details\[open\] \.acc-body\s*\{[\s\S]*?border-left:\s*2px solid #216b88/s,
  'FAQ open answers must use the route-blue record marker instead of orange',
);
assert.match(
  css,
  /EDIT 19 — FAQ top-header brand field[\s\S]*?\.atlas-home #questions\s*\{[\s\S]*?background:\s*#f2f0ea[\s\S]*?\.atlas-home #questions \.wrap\s*\{[\s\S]*?grid-template-columns:\s*1fr[\s\S]*?\.atlas-home #questions > \.wrap\.wrap--read:has\(> \.h2\):has\(> :not\(\.h2\)\)\s*\{[\s\S]*?grid-template-columns:\s*1fr[\s\S]*?\.atlas-home #questions \.h2\s*\{[\s\S]*?position:\s*static[\s\S]*?max-width:\s*min\(100%,\s*760px\)[\s\S]*?\.atlas-home #questions \.acc\s*\{[\s\S]*?margin-left:\s*auto[\s\S]*?\.atlas-home #questions details\[open\] \.acc-body\s*\{[\s\S]*?border-left:\s*0/s,
  'FAQ must use a top-heading layout on the approved mineral-paper field with no left-sidebar composition or orange/open-answer rail',
);
assert.match(
  css,
  /EDIT 14 — FAQ brand-flow correction[\s\S]*?\.atlas-home #questions details\[open\] \.sign\s*\{[\s\S]*?border-color:\s*rgba\(33,\s*107,\s*136,\s*0\.55\)[\s\S]*?box-shadow:\s*0 0 0 1px rgba\(220,\s*231,\s*231,\s*0\.42\) inset/s,
  'FAQ active controls must remain in the Atlantic/route-blue brand flow',
);
assert.match(
  css,
  /EDIT 8 — FAQ atlas index redesign[\s\S]*?@media\s*\(max-width:\s*700px\)\s*\{[\s\S]*?\.atlas-home #questions \.wrap\s*\{[\s\S]*?grid-template-columns:\s*1fr[\s\S]*?\.atlas-home #questions summary\s*\{[\s\S]*?min-height:\s*64px/s,
  'FAQ mobile must collapse into a composed single-column index without cramped rows',
);
assert.match(
  css,
  /EDIT 11 — Mobile reviews evidence strip[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #clients \.rv-head\s*\{[\s\S]*?background:\s*rgba\(255,\s*255,\s*255,\s*0\.055\)[\s\S]*?\.atlas-home #clients \.rv-score\s*\{[\s\S]*?grid-template-columns:\s*auto\s+auto\s+minmax\(0,\s*1fr\)[\s\S]*?\.atlas-home #clients \.rv-acts\s*\{[\s\S]*?display:\s*grid[\s\S]*?grid-template-columns:\s*1fr\s+auto/s,
  'mobile reviews header must become one composed evidence strip instead of loose stacked controls',
);
assert.match(
  css,
  /EDIT 11 — Mobile reviews evidence strip[\s\S]*?\.atlas-home #clients \.rv-all\s*\{[\s\S]*?min-height:\s*44px[\s\S]*?\.atlas-home #clients \.rv-nav\s*\{[\s\S]*?justify-self:\s*end/s,
  'mobile review links and carousel controls must retain accessible touch targets without full-width divider clutter',
);
assert.match(
  css,
  /EDIT 17 — Mobile reviews compact proof capsule[\s\S]*?@media\s*\(max-width:\s*600px\)[\s\S]*?\.atlas-home #clients \.rv-head\s*\{[\s\S]*?border-bottom:\s*0[\s\S]*?border-radius:\s*16px[\s\S]*?\.atlas-home #clients \.rv-acts\s*\{[\s\S]*?grid-template-columns:\s*minmax\(0,\s*1fr\)\s+auto[\s\S]*?\.atlas-home #clients \.rv-all\s*\{[\s\S]*?border-radius:\s*999px[\s\S]*?\.atlas-home #clients \.rv-nav\s*\{[\s\S]*?grid-column:\s*2[\s\S]*?grid-row:\s*1\s*\/\s*3/s,
  'mobile reviews proof capsule must remove divider clutter, use action pills, and dock arrows beside the links',
);

assert.match(css, /prefers-reduced-motion:\s*reduce/, 'reduced-motion treatment is required');
assert.match(css, /@media\s*\(max-width:\s*600px\)/, '375px-oriented mobile composition is required');
assert.doesNotMatch(
  css,
  /\.atlas-home\.atlas-ready main > section:not\(\.hero, \.office\)[^{]*\{[^}]*opacity:\s*0(?:\.0+)?1?/s,
  'body sections must not depend on JavaScript to become visible',
);
assert.match(
  css,
  /\.ds-js \.atlas-home \.ds-reveal[\s\S]*?opacity:\s*1[\s\S]*?transform:\s*none/s,
  'homepage reveal elements must be visible by default and not depend on IntersectionObserver',
);
assert.match(
  css,
  /EDIT 1 — Opening statement cleanup[\s\S]*?\.atlas-home #creds\s*\{[\s\S]*?border:\s*0/s,
  'credential rail must not reintroduce repetitive top/bottom borders',
);
assert.match(
  css,
  /EDIT 1 — Opening statement cleanup[\s\S]*?\.atlas-home #creds\s*\{[\s\S]*?#06101f/s,
  'credential rail must blend with the hero bottom stone-black scrim',
);
assert.match(
  css,
  /EDIT 1 — Opening statement cleanup[\s\S]*?\.atlas-home #firm::before\s*\{[\s\S]*?content:\s*none/s,
  'firm intro must not show the decorative rule above the heading',
);
assert.match(
  css,
  /EDIT 1 — Opening statement cleanup[\s\S]*?\.atlas-home #firm \.ds-statement__rule\s*\{[\s\S]*?display:\s*none/s,
  'firm intro must not show repeated horizontal statement rules',
);

console.log('Homepage contract: pass');
