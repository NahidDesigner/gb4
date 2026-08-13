import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")


def rule(selector: str) -> str:
    matches = re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", CSS, re.S)
    if not matches:
        raise AssertionError(f"Missing CSS rule: {selector}")
    return "\n".join(matches)


class BlogEditorialLayoutTests(unittest.TestCase):
    def test_blog_pages_load_the_current_editorial_stylesheet(self):
        pages = [
            ROOT / "blog/index.html",
            ROOT / "blog/what-to-do-first-48-hours-after-long-island-car-accident/index.html",
            ROOT / "blog/new-york-no-fault-serious-injury-threshold/index.html",
        ]
        for page in pages:
            with self.subTest(page=page):
                self.assertIn(
                    'href="../../inner-atlas.css?v=inner-page-26"',
                    page.read_text(encoding="utf-8").replace(
                        'href="../inner-atlas.css?v=inner-page-26"',
                        'href="../../inner-atlas.css?v=inner-page-26"',
                    ),
                )

    def test_archive_uses_compact_two_column_cards(self):
        postlist = rule("main:has(#posts) .postlist")
        card = rule("main:has(#posts) .post-row > a")
        title = rule("main:has(#posts) .post-t")

        self.assertIn("display: grid", postlist)
        self.assertIn("repeat(2, minmax(0, 1fr))", postlist)
        self.assertIn("min-height: 20rem", card)
        self.assertIn("background: var(--inner-page)", card)
        self.assertIn("font-size: clamp(1.75rem, 2.4vw, 2.15rem)", title)

    def test_single_post_header_has_one_centered_rule_below_title(self):
        page_head = rule("main:has(#post) .page-head")
        title = rule("main:has(#post) .page-title")
        title_rule = rule("main:has(#post) .page-title::after")
        section = rule("main:has(#post) .sec--tight")
        section_rule = rule("main:has(#post) .sec--tight::before")
        inherited_section_rule = rule("main:has(#post) .sec--tight::after")
        top_rule = rule("main:has(#post) .page-head::before")
        bottom_rule = rule("main:has(#post) .page-head::after")

        self.assertIn("text-align: center", page_head)
        self.assertIn("border-left: 0", page_head)
        self.assertIn("margin-inline: auto", page_head)
        self.assertIn("font-size: clamp(2.75rem, 5vw, 4.25rem)", title)
        self.assertIn('content: ""', title_rule)
        self.assertIn("display: block", title_rule)
        self.assertIn("width: clamp(4.5rem, 8vw, 7rem)", title_rule)
        self.assertIn("height: 2px", title_rule)
        self.assertIn("border-bottom: 0", section)
        self.assertIn("content: none", section_rule)
        self.assertIn("content: none", inherited_section_rule)
        self.assertIn("content: none", top_rule)
        self.assertIn("content: none", bottom_rule)

    def test_mobile_keeps_cards_and_post_title_compact(self):
        mobile = re.search(r"@media \(max-width: 560px\)\s*\{(.*?)\n\}", CSS, re.S)
        self.assertIsNotNone(mobile)
        block = mobile.group(1)
        self.assertIn("main:has(#post) .page-title", block)
        self.assertIn("font-size: clamp(2.25rem, 11vw, 2.7rem)", block)
        self.assertIn("main:has(#posts) .post-t", block)
        self.assertIn("font-size: clamp(1.65rem, 8vw, 1.95rem)", block)


if __name__ == "__main__":
    unittest.main()
