import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const slug = 'drunk-and-impaired-driving-crashes';
const label = 'Drunk and Impaired Driving Crashes';
const homepage = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const css = fs.readFileSync(path.join(root, 'homepage-atlas.css'), 'utf8');
const designSystem = fs.readFileSync(path.join(root, 'design-system.css'), 'utf8');
const practiceCss = fs.readFileSync(path.join(root, 'practice-areas', 'practice-atlas.css'), 'utf8');
const practiceAreas = [
  'rear-end-collisions',
  'head-on-collisions',
  'intersection-t-bone-crashes',
  'distracted-driving-crashes',
  slug,
];

assert.equal(
  (homepage.match(/class="ds-pa__radio"/g) || []).length,
  5,
  'homepage Practice Areas must expose five radio controls',
);
assert.equal(
  (homepage.match(/class="ds-pa__panel"/g) || []).length,
  5,
  'homepage Practice Areas must expose five panels',
);
assert.match(homepage, new RegExp(`aria-label="${label}"`), 'fifth practice-area radio must use the approved label');
assert.match(homepage, new RegExp(`href="practice-areas/${slug}/"`), 'fifth homepage panel must link to its detail page');
assert.match(homepage, new RegExp(`src="assets/${slug}\\.webp"`), 'fifth homepage panel must use its generated image');

assert.ok(
  (css.match(/nth-of-type\(5\):checked\s*~\s*\.ds-pa__panel:nth-of-type\(5\)/g) || []).length >= 3,
  'desktop, tablet and mobile selector groups must support the fifth checked panel',
);
assert.ok(
  (designSystem.match(/nth-of-type\(5\):(?:checked|focus-visible)\s*~\s*\.ds-pa__panel:nth-of-type\(5\)/g) || []).length >= 7,
  'shared practice-panel sizing, reveal, image, label and focus selectors must support the fifth item',
);

for (const filename of [`${slug}.webp`, `${slug}-sm.webp`]) {
  const asset = path.join(root, 'assets', filename);
  assert.ok(fs.existsSync(asset), `${filename} must exist`);
  assert.ok(fs.statSync(asset).size > 10_000, `${filename} must be a non-placeholder image`);
  assert.equal(fs.readFileSync(asset, { encoding: 'ascii', flag: 'r' }).slice(0, 4), 'RIFF', `${filename} must be WebP`);
}

const detailPath = path.join(root, 'practice-areas', slug, 'index.html');
assert.ok(fs.existsSync(detailPath), 'drunk/impaired practice-area detail page must exist');
const detail = fs.readFileSync(detailPath, 'utf8');

assert.match(detail, /<title>Drunk and Impaired Driving Crash Lawyers \| GB Law Firm<\/title>/, 'detail title must be topic-specific');
assert.match(detail, new RegExp(`<link rel="canonical" href="https://gblawfirm\\.com/practice-areas/${slug}/"`), 'detail canonical must use the new slug');
assert.match(detail, new RegExp(`<h1 class="page-title">${label}</h1>`), 'detail H1 must use the approved label');
assert.match(detail, new RegExp(`--pa-hero-img:url\\('../../assets/${slug}\\.webp'\\)`), 'detail hero must use the generated image');
assert.doesNotMatch(detail, /<h1[^>]*>Distracted Driving Crashes<\/h1>/, 'cloned H1 must be rewritten');

for (const currentSlug of practiceAreas) {
  const page = fs.readFileSync(path.join(root, 'practice-areas', currentSlug, 'index.html'), 'utf8');
  assert.match(
    page,
    /href="\.\.\/practice-atlas\.css\?v=related-media-five-2"/,
    `${currentSlug} must request the image-and-four-card stylesheet revision`,
  );
  const hero = page.match(/<section class="sec sec--tight"[\s\S]*?<\/section>/)?.[0];
  assert.ok(hero, `${currentSlug} must include the shared practice-area hero`);
  assert.match(
    hero,
    new RegExp(`<picture class="pa-hero-media"[\\s\\S]*?${currentSlug}-sm\\.webp[\\s\\S]*?${currentSlug}\\.webp`),
    `${currentSlug} hero must expose explicit desktop and mobile image layers`,
  );

  const related = page.match(/<section class="sec" id="related">([\s\S]*?)<\/section>/)?.[1];
  assert.ok(related, `${currentSlug} must include Other Practice Areas`);
  const cards = [...related.matchAll(/<a class="tile" href="\.\.\/([^/]+)\/"[\s\S]*?<\/a>/g)];
  assert.equal(cards.length, 4, `${currentSlug} must show four other practice areas`);
  assert.deepEqual(
    cards.map((match) => match[1]).sort(),
    practiceAreas.filter((candidate) => candidate !== currentSlug).sort(),
    `${currentSlug} must link to every other practice area and must not link to itself`,
  );
  for (const card of cards) {
    const cardSlug = card[1];
    assert.match(
      card[0],
      new RegExp(`<picture class="tile-media"[\\s\\S]*?${cardSlug}-sm\\.webp[\\s\\S]*?${cardSlug}\\.webp`),
      `${currentSlug} related card for ${cardSlug} must expose explicit desktop and mobile images`,
    );
    assert.doesNotMatch(
      card[0],
      /loading="lazy"/,
      `${currentSlug} related card for ${cardSlug} must be ready when the section enters the viewport`,
    );
  }
}

assert.match(
  practiceCss,
  /main #related \.tiles\s*\{[\s\S]*?grid-template-columns:\s*repeat\(4,\s*minmax\(0,\s*1fr\)\)/,
  'wide related-practice layout must provide four equal tracks',
);
assert.match(
  practiceCss,
  /main #related \.tile-media\s*\{[\s\S]*?background-image:\s*var\(--img\)/,
  'related-card media layer must retain a CSS background fallback',
);
assert.match(
  practiceCss,
  /@media \(max-width:\s*900px\)[\s\S]*?main #related \.tile-media\s*\{[\s\S]*?background-image:\s*var\(--img-sm,\s*var\(--img\)\)/,
  'related-card media layer must use the mobile fallback image below 900px',
);

const jsonLdText = detail.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)?.[1];
assert.ok(jsonLdText, 'detail page must include JSON-LD');
const graph = JSON.parse(jsonLdText)['@graph'];
const faqSchema = graph.find((entry) => entry['@type'] === 'FAQPage');
assert.ok(faqSchema, 'detail page must include FAQPage structured data');
assert.equal(faqSchema.mainEntity.length, 10, 'detail page must include ten structured FAQs');

const visibleFaqs = [...detail.matchAll(/<details(?: open)?><summary><span>(.*?)<\/span>[\s\S]*?<div class="acc-body"><p>(.*?)<\/p><\/div><\/details>/g)]
  .map((match) => ({ question: match[1], answer: match[2] }));
assert.equal(visibleFaqs.length, 10, 'detail page must include ten visible FAQs');
assert.deepEqual(
  visibleFaqs,
  faqSchema.mainEntity.map((entry) => ({ question: entry.name, answer: entry.acceptedAnswer.text })),
  'visible FAQs and FAQPage structured data must match exactly',
);

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    if (entry.name.startsWith('.') || entry.name === 'docs' || entry.name === 'mockups' || entry.name === 'restore-points') return [];
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(full);
    return entry.isFile() && entry.name.endsWith('.html') ? [full] : [];
  });
}

for (const file of walk(root)) {
  const html = fs.readFileSync(file, 'utf8');
  if (!html.includes('aria-label="Practice areas"')) continue;
  assert.match(
    html,
    new RegExp(`href="[^"]*practice-areas/${slug}/"`),
    `${path.relative(root, file)} must link to the fifth practice area in its drawer`,
  );
}

const xmlSitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
const htmlSitemap = fs.readFileSync(path.join(root, 'sitemap', 'index.html'), 'utf8');
const llms = fs.readFileSync(path.join(root, 'llms.txt'), 'utf8');
assert.match(xmlSitemap, new RegExp(`https://gblawfirm\\.com/practice-areas/${slug}/`), 'XML sitemap must list the new page');
assert.match(htmlSitemap, new RegExp(`href="../practice-areas/${slug}/"`), 'HTML sitemap must list the new page');
assert.match(llms, new RegExp(`https://gblawfirm\\.com/practice-areas/${slug}/`), 'llms.txt must list the new page');

console.log('Drunk/impaired practice-area contract: pass');
