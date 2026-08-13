import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")
HTML = (ROOT / "service-areas" / "index.html").read_text(encoding="utf-8")


class ServiceAreasSectionFixesTests(unittest.TestCase):
    def test_counties_heading_has_two_non_wrapping_lines(self):
        self.assertIn(
            '<span class="service-counties-title-line">The Counties</span><br />',
            HTML,
        )
        self.assertIn(
            '<span class="service-counties-title-line">We Serve</span>',
            HTML,
        )
        fix = CSS.split("QUICK FIX 10 — Service Areas section fixes", 1)[1]
        self.assertIn(".service-counties-title-line", fix)
        self.assertIn("white-space: nowrap", fix)

    def test_why_this_firm_uses_dark_text_on_its_light_surface(self):
        fix = CSS.split("QUICK FIX 10 — Service Areas section fixes", 1)[1]
        self.assertIn("#why.dark .h2.h2--light", fix)
        self.assertIn("color: var(--inner-atlantic)", fix)
        self.assertIn("#why.dark .rte.rte--light p", fix)
        self.assertIn("color: #243449", fix)
        self.assertIn("background: rgba(255, 255, 255, 0.58)", fix)

    def test_service_areas_page_requests_current_inner_styles(self):
        self.assertIn("inner-atlas.css?v=service-areas-fixes-2", HTML)


if __name__ == "__main__":
    unittest.main()
