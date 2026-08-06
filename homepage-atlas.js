(() => {
  const root = document.documentElement;
  const body = document.body;
  const sections = Array.from(document.querySelectorAll('main > section, main > .cta-wrap'))
    .filter((section) => !section.classList.contains('office'));
  const settlementCounters = Array.from(document.querySelectorAll('[data-ds-counter]'));
  const numberFormatter = new Intl.NumberFormat('en-US');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const practicePanels = Array.from(document.querySelectorAll('#practice .ds-pa__panel[for]'));
  const settlementScroller = document.querySelector('#settlements .ds-settlements__list');
  const settlementScrollButtons = Array.from(document.querySelectorAll('[data-settlement-scroll]'));

  const renderSettlementCounter = (counter, value) => {
    const prefix = counter.dataset.dsCountPrefix || '';
    const suffix = counter.dataset.dsCountSuffix || '';
    const formatted = numberFormatter.format(Math.round(value));

    if (counter.classList.contains('ds-settlements__figure')) {
      counter.innerHTML = `${prefix}${formatted}<sup>${suffix}</sup>`;
      return;
    }

    counter.textContent = `${prefix}${formatted}${suffix}`;
  };

  const finishSettlementCounters = () => {
    settlementCounters.forEach((counter) => {
      const target = Number(counter.dataset.dsCountTarget || '0');
      renderSettlementCounter(counter, target);
      counter.classList.add('is-counted');
    });
  };

  const animateSettlementCounters = () => {
    if (!settlementCounters.length) return;

    const duration = 1150;
    let startedAt = null;

    settlementCounters.forEach((counter) => {
      counter.classList.add('is-counting');
      renderSettlementCounter(counter, 0);
    });

    const tick = (timestamp) => {
      startedAt ??= timestamp;
      const progress = Math.min((timestamp - startedAt) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);

      settlementCounters.forEach((counter) => {
        const target = Number(counter.dataset.dsCountTarget || '0');
        renderSettlementCounter(counter, target * eased);
      });

      if (progress < 1) {
        requestAnimationFrame(tick);
        return;
      }

      settlementCounters.forEach((counter) => {
        counter.classList.remove('is-counting');
        counter.classList.add('is-counted');
      });
      finishSettlementCounters();
    };

    requestAnimationFrame(tick);
  };

  body.classList.add('atlas-ready');

  if (settlementScroller && settlementScrollButtons.length) {
    const normalizeWheelDelta = (value, mode) => {
      if (mode === WheelEvent.DOM_DELTA_LINE) return value * 16;
      if (mode === WheelEvent.DOM_DELTA_PAGE) return value * window.innerHeight;
      return value;
    };

    const getSettlementScrollDistance = () => {
      const firstItem = settlementScroller.querySelector('.ds-figure-cell');
      if (!firstItem) return Math.max(260, settlementScroller.clientWidth * 0.82);

      const itemRect = firstItem.getBoundingClientRect();
      const styles = window.getComputedStyle(settlementScroller);
      const gap = Number.parseFloat(styles.columnGap || styles.gap || '0') || 0;

      return itemRect.width + gap;
    };

    settlementScrollButtons.forEach((button) => {
      button.addEventListener('click', () => {
        const direction = button.dataset.settlementScroll === 'prev' ? -1 : 1;
        const distance = getSettlementScrollDistance();

        settlementScroller.scrollBy({
          left: direction * distance,
          behavior: reduceMotion.matches ? 'auto' : 'smooth',
        });
      });
    });

    settlementScroller.addEventListener('wheel', (event) => {
      if (event.ctrlKey) return;

      const deltaX = normalizeWheelDelta(event.deltaX, event.deltaMode);
      const deltaY = normalizeWheelDelta(event.deltaY, event.deltaMode);
      const absX = Math.abs(deltaX);
      const absY = Math.abs(deltaY);
      const hasWheelMotion = absX > 0 || absY > 0;
      if (!hasWheelMotion) return;

      const horizontalIntent = event.shiftKey || absX > absY * 1.15;

      event.preventDefault();

      if (horizontalIntent) {
        const horizontalDelta = absX > 0 ? deltaX : deltaY;
        settlementScroller.scrollLeft += horizontalDelta;
        return;
      }

      window.scrollBy({ top: deltaY, left: 0, behavior: 'auto' });
    }, { passive: false });
  }

  practicePanels.forEach((panel) => {
    panel.addEventListener('click', (event) => {
      if (event.target.closest('a')) return;

      const radio = document.getElementById(panel.getAttribute('for'));
      if (!radio) return;

      const scrollLeft = window.scrollX;
      const scrollTop = window.scrollY;

      event.preventDefault();
      radio.checked = true;
      radio.dispatchEvent(new Event('change', { bubbles: true }));

      try {
        radio.focus({ preventScroll: true });
      } catch {
        radio.focus();
      }

      window.scrollTo(scrollLeft, scrollTop);
      requestAnimationFrame(() => window.scrollTo(scrollLeft, scrollTop));
    });
  });

  if (!('IntersectionObserver' in window) || reduceMotion.matches) {
    sections.forEach((section) => section.classList.add('atlas-visible'));
    root.style.setProperty('--atlas-route-progress', '1');
    finishSettlementCounters();
    return;
  }

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('atlas-visible');
      observer.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });

  sections.forEach((section) => revealObserver.observe(section));

  const settlements = document.getElementById('settlements');
  if (settlements && settlementCounters.length) {
    const settlementCounterObserver = new IntersectionObserver(([entry], observer) => {
      if (!entry.isIntersecting) return;
      animateSettlementCounters();
      observer.disconnect();
    }, { rootMargin: '0px 0px -18% 0px', threshold: 0.2 });
    settlementCounterObserver.observe(settlements);
  }

  const firm = document.getElementById('firm');
  if (firm) {
    const routeObserver = new IntersectionObserver(([entry], observer) => {
      if (!entry.isIntersecting) return;
      root.style.setProperty('--atlas-route-progress', '1');
      observer.disconnect();
    }, { threshold: 0.2 });
    routeObserver.observe(firm);
  }
})();
