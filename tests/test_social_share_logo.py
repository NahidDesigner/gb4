import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOGO_URL = "https://gb.bosseo.dev/assets/GBlogo.png"


class SocialShareLogoTests(unittest.TestCase):
    def test_homepage_uses_logo_for_open_graph_and_twitter(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn(f'<meta property="og:image" content="{LOGO_URL}" />', html)
        self.assertIn('<meta property="og:image:type" content="image/png" />', html)
        self.assertIn('<meta property="og:image:width" content="560" />', html)
        self.assertIn('<meta property="og:image:height" content="406" />', html)
        self.assertIn(f'<meta name="twitter:image" content="{LOGO_URL}" />', html)
        self.assertIn('<meta name="twitter:card" content="summary" />', html)

    def test_generator_keeps_logo_as_sitewide_default(self):
        source = (ROOT / "tools" / "seo_build.py").read_text(encoding="utf-8")
        self.assertNotIn('/assets/og-cover.jpg', source)
        self.assertIn('/assets/GBlogo.png', source)


if __name__ == "__main__":
    unittest.main()
