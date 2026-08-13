import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class SitewideMobileHeaderTests(unittest.TestCase):
    def test_mobile_header_is_absolute_and_cannot_stick(self):
        fix = CSS.split("SITEWIDE FIX — Non-sticky mobile header", 1)[1]
        self.assertIn("@media (max-width: 768px)", fix)
        self.assertIn(".railhead.is-up", fix)
        self.assertIn("position: absolute !important", fix)
        self.assertIn("transform: none !important", fix)
        self.assertIn(".atlas-home .ds-site-header", fix)
        self.assertIn("top: 100svh !important", fix)
        self.assertIn("visibility: visible !important", fix)

    def test_all_production_pages_request_the_current_shared_styles(self):
        pages = [ROOT / "index.html"]
        for folder in (
            "blog",
            "case-results",
            "contact",
            "our-team",
            "practice-areas",
            "service-areas",
            "sitemap",
            "testimonials",
        ):
            pages.extend(
                path
                for path in (ROOT / folder).rglob("*.html")
                if not path.name.startswith("._")
            )

        pages_with_header = []
        for path in pages:
            html = path.read_text(encoding="utf-8")
            if 'class="railhead"' not in html and 'class="ds-site-header' not in html:
                continue
            pages_with_header.append(path)
            with self.subTest(page=path.relative_to(ROOT)):
                self.assertIn("styles.css?v=mobile-header-static-3", html)

        self.assertGreaterEqual(len(pages_with_header), 25)


if __name__ == "__main__":
    unittest.main()
