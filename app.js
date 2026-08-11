/* GB Law Firm — behaviour
   Content is fully visible without JS; everything here is enhancement. */
(function () {
  'use strict';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Legacy splash cleanup ----------------------------------------
     DESIGN.md keeps the logo preloader on the homepage only, and the homepage
     uses `#dsPreloader` from ds.js. If an old inner-page `#splash` block ever
     survives in markup, remove it immediately instead of animating it. */

  var splash = $('#splash');
  if (splash) splash.remove();

  /* ---------- Overlays ---------------------------------------------------- */

  // The opening control is recorded explicitly rather than read from
  // document.activeElement, which is not reliably the trigger.
  var lastFocus = null;

  function openPanel(el, focusTarget, trigger) {
    lastFocus = trigger || document.activeElement;
    el.hidden = false;
    document.body.classList.add('is-locked');
    var target = focusTarget || el.querySelector('button, a, input');
    if (target) target.focus();
  }
  function closePanel(el) {
    // Closing the drawer collapses its branch too, or reopening the menu lands
    // you in the Practice Areas list you left rather than at the top of it.
    if (el === drawer) resetSub();
    el.hidden = true;
    document.body.classList.remove('is-locked');
    if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
    lastFocus = null;
  }

  var drawer = $('#drawer');
  var search = $('#search');

  $$('#menuOpen, #menuOpen2').forEach(function (b) {
    b.addEventListener('click', function () { openPanel(drawer, $('#drawerClose'), b); });
  });
  $$('#searchOpen, #searchOpen2').forEach(function (b) {
    b.addEventListener('click', function () { openPanel(search, $('#searchInput'), b); });
  });
  var dc = $('#drawerClose');
  if (dc) dc.addEventListener('click', function () { closePanel(drawer); });
  if (drawer) {
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer) closePanel(drawer);
    });
  }
  var sc = $('#searchClose');
  if (sc) sc.addEventListener('click', function () { closePanel(search); });

  $$('.drawer-nav a, .drawer-tool, .drawer-sub-all').forEach(function (a) {
    a.addEventListener('click', function () { closePanel(drawer); });
  });

  /* ---------- Practice Areas: the drawer's one branch -----------------------
     Deliberately not routed through openPanel/closePanel. Those share a single
     `lastFocus` slot, so opening the branch would overwrite the menu button that
     opened the drawer, and closing the drawer afterwards would drop focus. The
     branch keeps its own, which is also the honest model: it is a step inside an
     overlay that is already open, not a second overlay.

     `body.is-locked` is likewise left alone — the drawer set it and the drawer
     clears it. Setting it twice and clearing it once is how a page ends up
     unable to scroll. */

  var sub = $('#drawerSub');
  var subTrigger = $('#paOpen');
  var subBack = $('#drawerSubBack');

  function resetSub() {
    if (!sub || sub.hidden) return;
    sub.hidden = true;
    if (subTrigger) subTrigger.setAttribute('aria-expanded', 'false');
  }

  if (sub && subTrigger) {
    subTrigger.addEventListener('click', function () {
      sub.hidden = false;
      subTrigger.setAttribute('aria-expanded', 'true');
      if (subBack) subBack.focus();
    });
    if (subBack) {
      subBack.addEventListener('click', function () {
        resetSub();
        subTrigger.focus();
      });
    }
  }

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (drawer && !drawer.hidden) closePanel(drawer);
    if (search && !search.hidden) closePanel(search);
  });

  /* ---------- Hero parallax --------------------------------------------------
     Transform-only, rAF-throttled, and only while the hero is on screen.
     background-attachment: fixed is not used — it is broken on iOS. */

  var heroBg = $('.hero-bg');
  if (heroBg && !reduced) {
    var ticking = false;
    var visible = true;

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; })
        .observe($('.hero'));
    }

    function park() {
      ticking = false;
      if (!visible) return;
      var y = window.pageYOffset || document.documentElement.scrollTop;
      // 0.28 keeps the layer inside its 124% height at any viewport
      heroBg.style.transform = 'translate3d(0,' + (y * 0.28).toFixed(1) + 'px,0)';
    }

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(park);
    }, { passive: true });
    park();
  }

  /* ---------- Sticky masthead + action bar --------------------------------- */

  var railhead = $('#railhead');
  var actionbar = $('#actionbar');
  var hero = $('.hero');

  if (hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      var past = !entries[0].isIntersecting;
      if (railhead) railhead.classList.toggle('is-up', past);
      if (actionbar) actionbar.classList.toggle('is-up', past);
    }, { rootMargin: '-70% 0px 0px 0px' }).observe(hero);
  } else {
    if (railhead) railhead.classList.add('is-up');
    if (actionbar) actionbar.classList.add('is-up');
  }

  /* ---------- Premium FAQ heading accents ---------------------------------
     The FAQ sections keep their existing headings in the HTML for no-JS users.
     When JS is available, split only the subject after "About" into the gold
     display span used by the current GB visual language. */

  $$('#questions .h2, #faq .h2').forEach(function (heading) {
    if (heading.querySelector('.faq-title-accent')) return;
    var text = heading.textContent.trim().replace(/\s+/g, ' ');
    var marker = ' About ';
    var i = text.indexOf(marker);
    if (i === -1) return;
    var lead = text.slice(0, i + marker.length);
    var subject = text.slice(i + marker.length);
    if (!subject) return;
    heading.textContent = '';
    heading.appendChild(document.createTextNode(lead));
    var accent = document.createElement('span');
    accent.className = 'faq-title-accent';
    accent.textContent = subject;
    heading.appendChild(accent);
  });

  /* ---------- Carousels ----------------------------------------------------
     A scroll-snap track that already works with swipe, trackpad and keyboard
     before any of this runs. The buttons are an addition, not the mechanism. */

  $$('[data-carousel]').forEach(function (rail) {
    var track = $('[data-track]', rail);
    var prev = $('[data-prev]', rail);
    var next = $('[data-next]', rail);
    var count = $('[data-count]', rail);
    if (!track) return;

    function step() {
      var first = track.firstElementChild;
      if (!first) return 300;
      var gap = parseFloat(getComputedStyle(track).columnGap || '0') || 0;
      return first.getBoundingClientRect().width + gap;
    }

    function slideIndex() {
      return Math.round(track.scrollLeft / step()) + 1;
    }

    var dotWrap = $('[data-dots]', rail);
    var dots = [];
    if (dotWrap) {
      Array.prototype.forEach.call(track.children, function (child, i) {
        var b = document.createElement('button');
        b.type = 'button';
        b.setAttribute('aria-label', 'Go to item ' + (i + 1));
        b.addEventListener('click', function () {
          track.scrollTo({ left: i * step(), behavior: reduced ? 'auto' : 'smooth' });
        });
        dotWrap.appendChild(b);
        dots.push(b);
      });
    }

    function sync() {
      // The track carries a bleed padding-right, which inflates scrollWidth.
      // Subtract it, or Next stays enabled with nothing left to reach.
      var pad = parseFloat(getComputedStyle(track).paddingRight) || 0;
      var max = track.scrollWidth - track.clientWidth - pad - 2;
      var scrollable = max > 4;
      if (rail.querySelector('.rail-foot')) {
        rail.querySelector('.rail-foot').hidden = !scrollable;
      }
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max;
      var total = track.children.length;
      var first = Math.min(slideIndex(), total);
      if (count) {
        // Report the range actually on screen, not a single index, or the
        // label contradicts what the visitor can see.
        var visible = Math.max(1, Math.round(track.clientWidth / step()));
        var last = Math.min(first + visible - 1, total);
        count.textContent = (first === last ? first : first + '–' + last) + ' of ' + total;
      }
      dots.forEach(function (d, i) {
        d.setAttribute('aria-current', i === first - 1 ? 'true' : 'false');
      });
    }

    if (prev) prev.addEventListener('click', function () { track.scrollBy({ left: -step(), behavior: reduced ? 'auto' : 'smooth' }); });
    if (next) next.addEventListener('click', function () { track.scrollBy({ left: step(), behavior: reduced ? 'auto' : 'smooth' }); });

    track.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); track.scrollBy({ left: step(), behavior: reduced ? 'auto' : 'smooth' }); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); track.scrollBy({ left: -step(), behavior: reduced ? 'auto' : 'smooth' }); }
    });

    var tick;
    track.addEventListener('scroll', function () {
      window.clearTimeout(tick);
      tick = window.setTimeout(sync, 90);
    }, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  });

  /* ---------- Search --------------------------------------------------------
     A real index over this page's own sections. The page is long; jumping to
     the right section is the actual job. A control that does nothing is worse
     than no control. */

  var searchForm = $('#searchForm');
  var searchInput = $('#searchInput');
  var searchOut = $('#searchOut');
  var searchHint = $('#searchHint');

  if (searchForm && searchInput && searchOut) {
    var searchPanel = $('#search');
    if (searchPanel && !searchPanel.querySelector('.search-shortcuts')) {
      var shortcuts = document.createElement('nav');
      shortcuts.className = 'search-shortcuts';
      shortcuts.setAttribute('aria-label', 'Helpful links');
      shortcuts.innerHTML = [
        '<p class="search-shortcuts__label"><span></span>Helpful Links<span></span></p>',
        '<div class="search-shortcuts__links">',
        '<a href="/">Home</a>',
        '<a href="/#firm">About Us</a>',
        '<a href="/#practice">Practice Areas</a>',
        '<a href="/our-team/">Our Attorneys</a>',
        '<a href="/contact/">Contact Us</a>',
        '</div>'
      ].join('');

      var homeLink = document.createElement('a');
      homeLink.className = 'search-home';
      homeLink.href = '/';
      homeLink.innerHTML = 'Return to Homepage<span aria-hidden="true"></span>';

      searchForm.insertAdjacentElement('afterend', shortcuts);
      shortcuts.insertAdjacentElement('afterend', homeLink);
    }

    // Only sections with a real heading are addressable; otherwise a result
    // renders with a raw class name as its title.
    var index = $$('main section[id], main header[id]').map(function (sec) {
      var head = sec.querySelector('h1, h2');
      if (!head) return null;
      return {
        id: sec.id,
        title: head.textContent.trim().replace(/\s+/g, ' '),
        text: (sec.textContent || '').replace(/\s+/g, ' ').toLowerCase()
      };
    }).filter(Boolean);

    function render(q) {
      var query = q.trim().toLowerCase();
      searchOut.innerHTML = '';
      if (query.length < 2) {
        searchHint.textContent = 'Type to jump to a section.';
        return;
      }
      var hits = index.filter(function (s) {
        return s.title.toLowerCase().indexOf(query) > -1 || s.text.indexOf(query) > -1;
      }).slice(0, 8);

      searchHint.textContent = hits.length
        ? hits.length + (hits.length === 1 ? ' section' : ' sections') + ' match “' + q.trim() + '”'
        : 'Nothing matches “' + q.trim() + '”. Call (516) 444-1000 and ask us directly.';

      hits.forEach(function (h) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.title;
        a.addEventListener('click', function () { closePanel(search); });
        li.appendChild(a);
        searchOut.appendChild(li);
      });
    }

    searchInput.addEventListener('input', function () { render(searchInput.value); });
    searchForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var first = searchOut.querySelector('a');
      if (first) { closePanel(search); first.click(); }
    });
  }

  /* ---------- Contact forms (there are three) ------------------------------- */

  function digits(v) { return v.replace(/\D/g, ''); }

  var RULES = {
    name: function (v) { return v.trim().length >= 2 ? '' : 'Please enter your name.'; },
    phone: function (v) { return digits(v).length >= 10 ? '' : 'Please enter a phone number we can reach you on.'; },
    email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? '' : 'Please enter a valid email address.'; }
  };

  $$('[data-form]').forEach(function (form) {
    var status = $('.form-status', form);
    var btn = form.querySelector('button[type="submit"]');
    var label = btn ? btn.textContent : '';

    function check(input) {
      var rule = RULES[input.name];
      if (!rule) return true;
      var field = input.closest('.field');
      var msg = rule(input.value);
      field.classList.toggle('is-bad', !!msg);
      var err = $('.err', field);
      if (err) err.textContent = msg;
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      return !msg;
    }

    $$('input[name]', form).forEach(function (input) {
      input.addEventListener('blur', function () { check(input); });
      input.addEventListener('input', function () {
        if (input.closest('.field').classList.contains('is-bad')) check(input);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = $$('input[name]', form).map(check).every(Boolean);
      if (!ok) {
        if (status) status.textContent = '';
        var bad = $('.field.is-bad input', form);
        if (bad) bad.focus();
        return;
      }

      // TODO(deploy): point this at the firm's intake endpoint or form service.
      // Until then nothing is delivered, and the message below says so.
      btn.disabled = true;
      btn.textContent = 'Sending…';
      window.setTimeout(function () {
        btn.disabled = false;
        btn.textContent = label;
        if (status) status.textContent = 'This form is not yet connected to the firm’s inbox. Please call (516) 444-1000 so we can start right away.';
      }, 600);
    });
  });

  /* ---------- The testimonial wall: revealed in batches ---------------------
     102 reviews is a lot of page to hand someone at once, so the wall opens on
     18 and grows on request.

     It is subtractive, not additive: every review is in the HTML and visible
     before this runs, and what the script does is HIDE the tail and reveal the
     button. That order matters. Building it the other way — 18 in the markup and
     the rest injected — would mean a visitor without script, and any crawler
     that does not execute one, sees 18 of the firm's 102 reviews. This way the
     page degrades to the complete wall.

     No scroll is moved. The button travels down the page as the wall grows,
     which is what a reader expects and what DESIGN.md's no-scroll-hijack rule
     requires. Focus stays on the button while there is one, and lands on the
     count when the last batch removes it, so keyboard focus is never dropped
     onto a hidden element. */

  var wall = $('[data-reveal]');
  if (wall) {
    var batch = parseInt(wall.getAttribute('data-reveal'), 10) || 18;
    var items = $$(':scope > li', wall);
    var moreBox = $('.rvmore');
    var moreBtn = $('[data-more]', moreBox || document);
    var moreCount = $('.rvmore-count', moreBox || document);

    if (items.length > batch && moreBox && moreBtn) {
      var shown = 0;

      var reveal = function (n) {
        shown = Math.min(n, items.length);
        items.forEach(function (li, i) { li.hidden = i >= shown; });

        var left = items.length - shown;
        if (left > 0) {
          moreCount.textContent = 'Showing ' + shown + ' of ' + items.length;
          moreBtn.textContent = 'Load ' + Math.min(batch, left) + ' more';
        } else {
          moreCount.textContent = 'Showing all ' + items.length + ' testimonials';
          // Focus is moved before the button goes, not after.
          if (document.activeElement === moreBtn) moreCount.focus();
          moreBtn.hidden = true;
        }
      };

      moreBox.hidden = false;
      reveal(batch);
      moreBtn.addEventListener('click', function () { reveal(shown + batch); });
    }
  }

  /* ---------- Practice-page Terms stage motion -----------------------------
     Progressive enhancement only: the section is fully visible without JS.
     The observer adds one quiet legal-exhibit entrance and then stops. */

  var termsStages = $$('.terms-stage');
  if (termsStages.length) {
    termsStages.forEach(function (stage) {
      stage.classList.add('terms-motion-ready');
    });

    if (reduced || !('IntersectionObserver' in window)) {
      termsStages.forEach(function (stage) {
        stage.classList.add('is-in');
      });
    } else {
      var termsObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-in');
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.18, rootMargin: '0px 0px -14% 0px' });

      termsStages.forEach(function (stage) {
        termsObserver.observe(stage);
      });
    }
  }

  /* ---------- Year ----------------------------------------------------------- */

  var yr = $('#yr');
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
