import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLES = (ROOT / "styles.css").read_text(encoding="utf-8")
SITE_ROOTS = {
    "blog",
    "case-results",
    "contact",
    "our-team",
    "practice-areas",
    "service-areas",
    "sitemap",
    "testimonials",
}
HTML_FILES = [ROOT / "index.html"] + sorted(
    path
    for path in ROOT.rglob("*.html")
    if path.relative_to(ROOT).parts[0] in SITE_ROOTS
    and not path.name.startswith("._")
)


class SitewideMobileFooterTests(unittest.TestCase):
    def test_every_footer_uses_the_shared_two_row_colophon_markup(self):
        pages_with_footer = []
        for path in HTML_FILES:
            html = path.read_text(encoding="utf-8")
            if 'class="foot-copy"' not in html:
                continue
            pages_with_footer.append(path)
            with self.subTest(page=path.relative_to(ROOT)):
                self.assertIn('class="foot-copy-main"', html)
                self.assertIn('class="foot-copy-credit"', html)
                self.assertIn('class="foot-sep foot-sep--credit"', html)
                self.assertIn("styles.css?v=mobile-header-static-3", html)

        self.assertGreaterEqual(len(pages_with_footer), 25)

    def test_mobile_colophon_layout_is_shared_not_homepage_scoped(self):
        fix = STYLES.split("SITEWIDE FIX — Mobile footer colophon", 1)[1]
        self.assertIn("@media (max-width: 760px)", fix)
        self.assertIn(".foot-copy-main", fix)
        self.assertIn(".foot-copy-credit", fix)
        self.assertIn("white-space: nowrap", fix)
        self.assertIn("text-align: center", fix)
        self.assertNotIn(".atlas-home", fix.split("}", 5)[0])


if __name__ == "__main__":
    unittest.main()
