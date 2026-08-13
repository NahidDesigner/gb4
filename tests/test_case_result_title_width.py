import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOME_CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
INNER_CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")
HOME_HTML = (ROOT / "index.html").read_text(encoding="utf-8")


def declarations(css: str, selector: str) -> list[str]:
    return re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)


def grouped_rule(css: str, marker: str) -> str:
    start = css.index(marker)
    opening = css.index("{", start)
    closing = css.index("}", opening)
    return css[opening + 1 : closing]


class CaseResultTitleWidthTests(unittest.TestCase):
    def test_case_results_hero_rule_sits_below_the_subtitle(self):
        hero_rule = grouped_rule(
            INNER_CSS,
            "main:has(#results) .sec--tight::after",
        )
        self.assertIn("bottom: clamp(1.75rem, 2.6vw, 2.4rem)", hero_rule)

    def test_homepage_card_content_flows_from_the_top(self):
        final_cards = HOME_CSS.split("EDIT 34 —", 1)[1]
        card = grouped_rule(
            final_cards,
            ".atlas-home #settlements.settlements-premium .ds-figure-cell,\n"
            ".atlas-home #settlements.settlements-premium .ds-figure-cell:nth-child(odd)",
        )
        title_rules = declarations(
            final_cards,
            ".atlas-home #settlements.settlements-premium .ds-figure-cell__case",
        )
        self.assertIn("justify-content: flex-start", card)
        self.assertNotIn("justify-content: space-between", card)
        self.assertTrue(
            any("margin: clamp(1.5rem, 2vw, 1.85rem) 0 0" in rule for rule in title_rules)
        )
        self.assertFalse(any("margin: auto 0 0" in rule for rule in title_rules))

    def test_case_results_card_content_flows_from_the_top(self):
        card = grouped_rule(
            INNER_CSS,
            "main:has(#results) .rcard,\nmain:has(#results) .rcard:nth-child(n)",
        )
        title_rules = declarations(INNER_CSS, "main:has(#results) .rcard-t")
        self.assertIn("justify-content: flex-start", card)
        self.assertNotIn("justify-content: space-between", card)
        self.assertTrue(
            any("margin-top: clamp(1.5rem, 2vw, 1.85rem)" in rule for rule in title_rules)
        )
        self.assertFalse(any("margin-top: auto" in rule for rule in title_rules))

    def test_homepage_bqe_result_uses_the_approved_short_title(self):
        self.assertIn("Rear-end crash, BQE", HOME_HTML)
        self.assertNotIn("Rear-end collision, Brooklyn-Queens Expressway", HOME_HTML)

    def test_homepage_distracted_result_uses_the_approved_short_title(self):
        self.assertIn("Distracted driving, Northern State", HOME_HTML)
        self.assertNotIn("Distracted driving, Northern State Parkway", HOME_HTML)

    def test_homepage_truck_result_uses_the_approved_short_title(self):
        self.assertIn("Southern State truck crash", HOME_HTML)
        self.assertNotIn("Truck collision, Southern State Parkway", HOME_HTML)

    def test_homepage_case_titles_use_the_full_card_width(self):
        rules = declarations(
            HOME_CSS,
            ".atlas-home #settlements.settlements-premium .ds-figure-cell__case",
        )
        self.assertTrue(rules)
        self.assertTrue(any("max-width: none" in rule for rule in rules))
        self.assertFalse(any("max-width: 22ch" in rule for rule in rules))

    def test_case_results_page_titles_use_the_full_card_width(self):
        rules = declarations(INNER_CSS, "main:has(#results) .rcard-t")
        self.assertTrue(rules)
        self.assertTrue(any("max-width: none" in rule for rule in rules))
        self.assertFalse(any("max-width: 23ch" in rule for rule in rules))


if __name__ == "__main__":
    unittest.main()
