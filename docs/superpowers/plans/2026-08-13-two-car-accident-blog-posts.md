# Two Car-Accident Blog Posts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the placeholder “Hello World” post with two useful, current New York car-accident articles and publish them through every existing blog discovery surface.

**Architecture:** Reuse the existing static article shell without visual or behavioral changes. Add one directory per post, keep recent-post lists synchronized across the blog index and both articles, register both pages in the SEO generator, and replace the old URL in both XML and HTML sitemaps.

**Tech Stack:** Static HTML, existing CSS/JavaScript, Python SEO generator, XML sitemap.

---

### Task 1: Publish both articles

**Files:**
- Create: `blog/what-to-do-first-48-hours-after-long-island-car-accident/index.html`
- Create: `blog/new-york-no-fault-serious-injury-threshold/index.html`

- [ ] Reuse the existing post shell and preserve all header, navigation, sidebar, CTA, footer, and script behavior.
- [ ] Write the first article around immediate safety, medical care, evidence, insurance notice, the MV-104 deadline, and early legal review.
- [ ] Write the second article around basic no-fault benefits, claim deadlines, the serious-injury threshold, the May 2026 statutory change, and the difference between economic and non-economic loss.
- [ ] Include plain-language disclaimers and link legal claims to current New York DMV, DFS, and Senate sources.

### Task 2: Replace the placeholder throughout the blog

**Files:**
- Modify: `blog/index.html`
- Modify: both new post pages
- Delete: `blog/hello-world/index.html`

- [ ] Replace the single placeholder row with two dated article rows.
- [ ] Replace every “Recent Posts” reference with the two new articles and mark the current article correctly on each post page.
- [ ] Remove comments that describe the blog as a one-entry placeholder.

### Task 3: Update crawl and metadata surfaces

**Files:**
- Modify: `tools/seo_build.py`
- Modify: `sitemap.xml`
- Modify: `sitemap/index.html`

- [ ] Replace the Hello World registry entry with two `BlogPosting` entries, including canonical URLs, titles, descriptions, publication dates, and breadcrumbs.
- [ ] Run `python3 tools/seo_build.py` and confirm generated metadata matches the source registry.
- [ ] Replace the old post URL in both sitemaps with the two new URLs.

### Task 4: Verify the finished blog

- [ ] Run the repository SEO audit and confirm every sitemap URL resolves to a local page.
- [ ] Scan for any remaining `Hello World` or `hello-world` references.
- [ ] Start the local site and inspect the blog index plus both posts at desktop and phone widths.
- [ ] Check computed widths, overflow, title wrapping, sidebar placement, and current-page states.

