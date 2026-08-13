import os
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HEADER_CSS = ROOT / "site-header.css"
SHARED_CSS = (ROOT / "styles.css").read_text(encoding="utf-8")


def css_rule(css: str, selector: str) -> str:
    matches = re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)
    if not matches:
        raise AssertionError(f"Missing CSS rule: {selector}")
    return "\n".join(matches)


def inner_pages() -> list[Path]:
    pages = []
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
        for path in (ROOT / folder).rglob("*.html"):
            if path.name.startswith("._"):
                continue
            html = path.read_text(encoding="utf-8")
            if 'class="railhead"' in html:
                pages.append(path)
    return sorted(pages)


class InnerPageHeaderRefinementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = (
            HEADER_CSS.read_text(encoding="utf-8") if HEADER_CSS.exists() else ""
        )

    def test_desktop_header_has_prominent_logo_and_premium_non_glass_surface(self):
        header = css_rule(self.css, ".railhead,\n.railhead.is-up")
        logo = css_rule(self.css, ".railhead .rh-mark img")

        self.assertIn("height: 136px", header)
        self.assertIn("min-height: 136px", header)
        self.assertIn("rgba(242, 240, 234, 0.92)", header)
        self.assertIn("rgba(18, 61, 86, 0.32)", header)
        self.assertIn("height: 128px", logo)
        self.assertIn("-webkit-backdrop-filter: none", header)
        self.assertIn("backdrop-filter: none", header)

    def test_call_now_is_an_atlantic_action_with_survey_orange_signal(self):
        call = css_rule(self.css, ".railhead .rh-call")
        hover = css_rule(
            self.css,
            ".railhead .rh-call:hover,\n.railhead .rh-call:focus-visible",
        )

        self.assertIn("background: #123d56", call)
        self.assertIn("border: 1px solid #e35d2f", call)
        self.assertIn("color: #fff", call)
        self.assertIn("background: #216b88", hover)

    def test_mobile_header_is_larger_touch_safe_and_non_sticky(self):
        mobile = self.css.split("@media (max-width: 768px)", 1)[1]
        self.assertIn("height: 96px", mobile)
        self.assertIn("min-height: 96px", mobile)
        self.assertIn("height: 86px", mobile)
        self.assertIn("min-height: 44px", mobile)
        self.assertIn(".railhead .rh-call", mobile)
        self.assertIn("display: none", mobile)

        non_sticky = SHARED_CSS.split(
            "SITEWIDE FIX — Non-sticky mobile header", 1
        )[1]
        self.assertIn("position: absolute !important", non_sticky)
        self.assertIn("transform: none !important", non_sticky)

    def test_every_inner_page_loads_the_current_shared_header_layer(self):
        pages = inner_pages()
        self.assertEqual(24, len(pages))

        for page in pages:
            relative_css = Path(os.path.relpath(HEADER_CSS, page.parent)).as_posix()
            expected = f'href="{relative_css}?v=inner-header-premium-1"'
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertIn(expected, page.read_text(encoding="utf-8"))

        self.assertNotIn(
            "site-header.css",
            (ROOT / "index.html").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
