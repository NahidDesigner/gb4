/* GB LAW FIRM — design-system motion (DESIGN.md v6 §5)
   Homepage only. IntersectionObserver + CSS transitions, no library (§5.6).
   Every animated value lives in CSS; this file only toggles classes and,
   for the counter, writes text. Content is fully legible without it. */
(function () {
  'use strict';

  var doc = document;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || doc).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || doc).querySelectorAll(s)); };
  var isHomePage = doc.body && doc.body.classList.contains('atlas-home')
    && (/\/$|\/index\.html$/).test(window.location.pathname);

  /* ---------- §5.2 The orchestrated moment — preloader --------------------
     0ms    stone-deep field, full bleed
     200ms  logo fades in centered — t-slow, ease-out
     900ms  logo settles; bronze hairline draws outward from centre
     1300ms field lifts, revealing the hero already in place
     Total <= 1.8s. Session-flagged. The hero image is preloaded behind the
     field so the field is never what LCP is waiting on. */

  var pre = $('#dsPreloader');
  if (pre && !isHomePage) {
    pre.remove();
    pre = null;
  }
  if (pre) {
    var seen = false;
    try { seen = sessionStorage.getItem('gb-preloader') === '1'; } catch (e) { seen = false; }

    if (seen) {
      pre.remove();
    } else {
      try { sessionStorage.setItem('gb-preloader', '1'); } catch (e) {}

      // Preload the hero behind the field. Same source rule as the markup's
      // media-conditioned preload so we warm the image the hero will use.
      var img = new Image();
      img.src = window.matchMedia('(max-width: 768px)').matches
        ? 'assets/nyc-hero-sm.jpg' : 'assets/nyc-hero.jpg';

      var done = function () {
        pre.classList.add('is-lifting');
        window.setTimeout(function () { pre.remove(); }, 900);
      };

      if (reduced) {
        // Reduced motion: no choreography, no held page. Show the field only
        // long enough not to flash, then drop it.
        window.setTimeout(done, 200);
      } else {
        window.setTimeout(function () { pre.classList.add('is-mark-in'); }, 200);
        window.setTimeout(function () { pre.classList.add('is-rule-in'); }, 900);
        window.setTimeout(done, 1300);
      }
    }
  }

  /* ---------- §3 site-header — transparent over hero, solid past it -------- */

  var header = $('#dsHeader');
  var hero = $('.hero');
  if (header && hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      var past = !entries[0].isIntersecting;
      header.classList.toggle('is-solid', past);
    }, { rootMargin: '-96px 0px 0px 0px' }).observe(hero);
  } else if (header) {
    header.classList.add('is-solid');
  }

  /* ---------- §5.3 Scroll reveal — one rule for the entire page ------------
     Transform and opacity only. 15% entry. Fires once, never re-animates.
     Children stagger 60ms, capped at 6. */

  var revealables = $$('.ds-reveal');
  if (revealables.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    } else {
      var ro = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var group = $$('[data-ds-stagger]', el);
          el.classList.add('is-in');
          group.slice(0, 6).forEach(function (child, i) {
            child.style.transitionDelay = (i * 60) + 'ms';
            child.classList.add('is-in');
          });
          obs.unobserve(el);           // fires once
        });
      }, { threshold: 0.15 });
      revealables.forEach(function (el) { ro.observe(el); });
    }
  }

  /* ---------- §5.4 Archetype E — the connector draws ----------------------
     Each step's connector draws as that step enters, so the progression builds
     under the reader rather than all at once. Kept separate from the §5.3
     reveal system deliberately: routing it through `.ds-reveal` would fade and
     lift the step as well as draw its line, putting two animated things in one
     viewport (§5.6). Fires once per step. */

  var drawables = $$('[data-ds-draw]');
  if (drawables.length) {
    if (reduced || !('IntersectionObserver' in window)) {
      drawables.forEach(function (el) { el.classList.add('is-drawn'); });
    } else {
      var dobs = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-drawn');
          obs.unobserve(entry.target);
        });
      }, { threshold: 0.15 });
      drawables.forEach(function (el) { dobs.observe(el); });
    }
  }

  /* ---------- §5.5 Signature motion — the settlements counter -------------
     0 -> value, ease-out, once, at 30% entry. Real format, tabular numerals so
     the width never jitters. Reduced motion renders final values at once.
     Nothing else on the page counts.

     AMENDMENT 2026-08-06 — stagger 120ms -> 60ms and per-figure duration
     1400ms -> 680ms, per the §3 `figure-cell` amendment. The grid now holds 14
     cells: at the old timings the last figure started at 1.56s and finished at
     2.96s, well past the 1.6s the sequence is allowed. 13 x 60 + 680 = 1.46s. */
  var COUNT_MS = 680;
  var STAGGER_MS = 60;

  var counters = $$('[data-ds-count]');
  if (counters.length) {
    // Format to the exact shape authored in the HTML: prefix, grouped
    // thousands, optional suffix. The DOM already holds the final string, so
    // a failed or skipped animation still shows the true figure.
    var render = function (el, value) {
      var prefix = el.getAttribute('data-ds-prefix') || '';
      var suffix = el.getAttribute('data-ds-suffix') || '';
      el.textContent = prefix + String(value).replace(/\B(?=(\d{3})+(?!\d))/g, ',') + suffix;
    };

    // cubic-bezier(0.22, 1, 0.36, 1) sampled as its scalar easing — the same
    // curve the CSS transitions use, so the counter feels like the rest.
    var easeOut = function (t) { return 1 - Math.pow(1 - t, 3); };

    var run = function (el, delay) {
      var target = parseInt(el.getAttribute('data-ds-count'), 10);
      if (isNaN(target)) return;
      window.setTimeout(function () {
        var start = null;
        var step = function (now) {
          if (start === null) start = now;
          var t = Math.min((now - start) / COUNT_MS, 1);
          render(el, Math.round(target * easeOut(t)));
          if (t < 1) window.requestAnimationFrame(step);
          else render(el, target);
        };
        window.requestAnimationFrame(step);
      }, delay);
    };

    if (reduced || !('IntersectionObserver' in window) || !window.requestAnimationFrame) {
      counters.forEach(function (el) {
        render(el, parseInt(el.getAttribute('data-ds-count'), 10));
      });
    } else {
      var co = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var i = counters.indexOf(el);
          render(el, 0);
          run(el, Math.max(0, i) * STAGGER_MS);
          obs.unobserve(el);                    // once
        });
      }, { threshold: 0.3 });
      counters.forEach(function (el) { co.observe(el); });
    }
  }
})();
