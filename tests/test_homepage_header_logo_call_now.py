import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
SHARED_CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


class HomepageHeaderLogoCallNowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header = HTML.split(
            '<header class="ds-site-header ds-on-dark" id="dsHeader">', 1
        )[1].split("</header>", 1)[0]
        cls.refinement = CSS.split("/* EDIT 50 — Homepage-only", 1)[1].split(
            ".atlas-home .cta-wrap .btn", 1
        )[0]

    def test_header_uses_one_phone_link_with_responsive_labels(self):
        self.assertEqual(self.header.count('href="tel:+15164441000"'), 1)
        self.assertIn('class="ds-button-call__desktop"', self.header)
        self.assertIn('class="ds-button-call__mobile"', self.header)
        self.assertIn("(516) 444-1000", self.header)
        self.assertIn("Call Now", self.header)

    def test_header_logo_links_to_the_site_root(self):
        self.assertIn('class="ds-site-header__mark" href="/"', self.header)
        self.assertNotIn('class="ds-site-header__mark" href="#top"', self.header)

    def test_homepage_header_is_hidden_on_mobile(self):
        self.assertIn("@media (max-width: 768px)", self.refinement)
        mobile = self.refinement.split("@media (max-width: 768px)", 1)[1]
        self.assertIn(".atlas-home .ds-site-header", mobile)
        self.assertIn("display: none !important", mobile)

    def test_header_is_translucent_without_a_glass_filter(self):
        self.assertIn("rgba(242, 240, 234, 0.92)", self.refinement)
        self.assertIn("rgba(220, 231, 231, 0.08)", self.refinement)
        self.assertNotIn("backdrop-filter", self.refinement)

    def test_desktop_logo_is_128px_and_stylesheet_cache_is_busted(self):
        self.assertIn("height: 128px", self.refinement)
        self.assertIn(
            'homepage-atlas.css?v=desktop-header-premium-2',
            HTML,
        )

    def test_inner_page_mobile_headers_remain_top_positioned_and_non_sticky(self):
        fix = SHARED_CSS.split("SITEWIDE FIX — Non-sticky mobile header", 1)[1]
        self.assertIn(".railhead", fix)
        self.assertIn("position: absolute !important", fix)
        self.assertNotIn(".railhead {\n    position: fixed", fix)

    def test_locked_hero_and_mobile_actionbar_remain_present(self):
        self.assertIn('<!-- ================= HERO (locked) ================= -->', HTML)
        self.assertIn('<header class="hero">', HTML)
        self.assertIn('<div class="actionbar" id="actionbar">', HTML)
        self.assertIn(
            '<a class="ab ab--call" href="tel:+15164441000">',
            HTML,
        )


if __name__ == "__main__":
    unittest.main()
