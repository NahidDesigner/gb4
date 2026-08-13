import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
JS = (ROOT / "app.js").read_text(encoding="utf-8")


def css_rule(css: str, selector: str) -> str:
    matches = re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)
    if not matches:
        raise AssertionError(f"Missing CSS rule: {selector}")
    return "\n".join(matches)


def production_pages() -> list[Path]:
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
    return sorted(pages)


class DrawerSearchControlTests(unittest.TestCase):
    def test_every_drawer_has_one_accessible_search_control(self):
        pages = production_pages()
        self.assertEqual(25, len(pages))

        for page in pages:
            html = page.read_text(encoding="utf-8")
            with self.subTest(page=page.relative_to(ROOT)):
                self.assertEqual(1, html.count('id="drawerSearch"'))
                self.assertIn(
                    '<button type="button" class="drawer-search" id="drawerSearch" aria-label="Search">',
                    html,
                )
                self.assertIn('<use href="#i-mag"/>', html)
                self.assertIn("styles.css?v=mobile-header-static-3&amp;drawer-search=1", html)
                self.assertRegex(html, r'app\.js\?v=[^"&]+&amp;drawer-search=1')

    def test_drawer_search_control_is_touch_safe_and_uses_the_icon_system(self):
        control = css_rule(CSS, ".drawer-search")
        icon = css_rule(CSS, ".drawer-search .ic")

        self.assertIn("min-width: 44px", control)
        self.assertIn("min-height: 44px", control)
        self.assertIn("display: inline-flex", control)
        self.assertIn("width: 18px", icon)
        self.assertIn("height: 18px", icon)

    def test_drawer_search_swaps_overlays_and_preserves_return_focus(self):
        self.assertIn("function swapPanel(from, to, focusTarget)", JS)
        self.assertIn("from.hidden = true", JS)
        self.assertIn("to.hidden = false", JS)
        self.assertIn("var drawerSearch = $('#drawerSearch')", JS)
        self.assertIn("swapPanel(drawer, search, $('#searchInput'))", JS)


if __name__ == "__main__":
    unittest.main()
