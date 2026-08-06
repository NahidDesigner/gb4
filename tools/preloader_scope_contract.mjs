import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    if (entry.name.startsWith('._')) return [];
    if (entry.name === 'docs' || entry.name === '.superpowers') return [];

    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(full);
    return entry.isFile() && entry.name.endsWith('.html') ? [full] : [];
  });
}

const pages = walk(root).sort();
const homepage = path.join(root, 'index.html');

assert.ok(pages.includes(homepage), 'homepage index.html must be present');

for (const file of pages) {
  const html = fs.readFileSync(file, 'utf8');
  const rel = path.relative(root, file);

  if (file === homepage) {
    assert.match(
      html,
      /<div class="ds-preloader" id="dsPreloader" aria-hidden="true">/,
      'homepage must keep the DESIGN.md homepage-only preloader',
    );
    assert.doesNotMatch(html, /<div class="splash" id="splash"/, 'homepage must not use the legacy splash preloader');
    continue;
  }

  assert.doesNotMatch(
    html,
    /\bid="(?:dsPreloader|splash)"/,
    `${rel} must not include any logo preloader id`,
  );
  assert.doesNotMatch(
    html,
    /\bclass="[^"]*(?:ds-preloader|splash|splash-lockup)[^"]*"/,
    `${rel} must not include any logo preloader markup`,
  );
}

const ds = fs.readFileSync(path.join(root, 'ds.js'), 'utf8');
assert.match(
  ds,
  /var isHomePage =[\s\S]*?classList\.contains\('atlas-home'\)[\s\S]*?window\.location\.pathname[\s\S]*?if \(pre && !isHomePage\)[\s\S]*?pre\.remove\(\)/,
  'preloader runtime must remove/skip preloaders outside the homepage',
);

const app = fs.readFileSync(path.join(root, 'app.js'), 'utf8');
assert.doesNotMatch(
  app,
  /Splash: navy → logo → page[\s\S]*?new Image\(\)/,
  'legacy global splash animation must not run on inner pages',
);
assert.match(
  app,
  /var splash = \$\('#splash'\);[\s\S]*?if \(splash\) splash\.remove\(\);/,
  'legacy splash markup must be removed immediately when encountered',
);

console.log('Preloader scope contract: pass');
