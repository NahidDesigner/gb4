import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../hero-video.js', import.meta.url), 'utf8');

function createHarness({ mobile = false, reduced = false } = {}) {
  const messages = [];
  const listeners = {};
  const attributes = new Map();
  const contentWindow = {
    postMessage(message, origin) {
      messages.push({ message, origin });
    },
  };
  const frame = {
    contentWindow,
    dataset: { mobileSrc: 'mobile-video', desktopSrc: 'desktop-video' },
    addEventListener(type, listener) { listeners[`frame:${type}`] = listener; },
    getAttribute(name) { return attributes.get(name) ?? null; },
    setAttribute(name, value) { attributes.set(name, value); },
    removeAttribute(name) { attributes.delete(name); },
  };
  const context = vm.createContext({
    document: { querySelector: () => frame },
    matchMedia(query) {
      const matches = query.includes('max-width') ? mobile : reduced;
      return { matches, addEventListener() {} };
    },
    addEventListener(type, listener) { listeners[type] = listener; },
    JSON,
    Number,
  });

  vm.runInContext(source, context);
  return { attributes, contentWindow, frame, listeners, messages };
}

const desktop = createHarness();
assert.equal(desktop.attributes.get('src'), 'desktop-video');
desktop.listeners['frame:load']();
assert.equal(desktop.messages.at(-1)?.message.method, 'addEventListener');
assert.equal(desktop.messages.at(-1)?.message.value, 'timeupdate');
desktop.listeners.message({
  origin: 'https://player.vimeo.com',
  source: desktop.contentWindow,
  data: { event: 'timeupdate', data: { seconds: 6 } },
});
assert.equal(desktop.messages.at(-1)?.message.method, 'setCurrentTime');
assert.equal(desktop.messages.at(-1)?.message.value, 0);

const mobile = createHarness({ mobile: true });
assert.equal(mobile.attributes.get('src'), 'mobile-video');
mobile.listeners['frame:load']();
assert.equal(mobile.messages.length, 0);
mobile.listeners.message({
  origin: 'https://player.vimeo.com',
  source: mobile.contentWindow,
  data: { event: 'timeupdate', data: { seconds: 6 } },
});
assert.equal(mobile.messages.length, 0);

const reduced = createHarness({ reduced: true });
assert.equal(reduced.attributes.has('src'), false);

console.log('Hero video controller runtime: pass');
