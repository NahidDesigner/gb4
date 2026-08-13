import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOME_CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")
INNER_CSS = (ROOT / "inner-atlas.css").read_text(encoding="utf-8")


def declarations(css: str, selector: str) -> list[str]:
    return re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)


class CaseResultTitleWidthTests(unittest.TestCase):
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
