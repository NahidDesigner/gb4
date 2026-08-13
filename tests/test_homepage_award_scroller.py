import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOME_CSS = (ROOT / "homepage-atlas.css").read_text(encoding="utf-8")


def declarations(css: str, selector: str) -> list[str]:
    return re.findall(re.escape(selector) + r"\s*\{([^}]*)\}", css, re.S)


class HomepageAwardScrollerTests(unittest.TestCase):
    def test_larger_desktop_logos_keep_the_existing_rail_height(self):
        final_layer = HOME_CSS.split("EDIT 1 — Opening statement cleanup", 1)[1]
        desktop_layer = final_layer.split("@media (max-width: 600px)", 1)[0]
        section = declarations(desktop_layer, ".atlas-home #creds")[0]
        track = declarations(desktop_layer, ".atlas-home #creds .creds-track")[0]
        logos = declarations(
            desktop_layer,
            ".atlas-home #creds .creds-run img,\n"
            ".atlas-home #creds .creds-run img.cr-emblem",
        )[0]
        emblems = declarations(
            desktop_layer,
            ".atlas-home #creds .creds-run img.cr-emblem",
        )[-1]

        self.assertIn("min-height: clamp(104px, 9vw, 128px)", section)
        self.assertIn("min-height: clamp(96px, 8vw, 116px)", track)
        self.assertIn("height: 42px", logos)
        self.assertIn("height: 64px", emblems)

    def test_mobile_logos_grow_without_changing_the_mobile_rail_height(self):
        final_layer = HOME_CSS.split("EDIT 1 — Opening statement cleanup", 1)[1]
        mobile_layer = final_layer.split("@media (max-width: 600px)", 1)[1]
        section = declarations(mobile_layer, ".atlas-home #creds")[0]
        track = declarations(mobile_layer, ".atlas-home #creds .creds-track")[0]
        logos = declarations(
            mobile_layer,
            "  .atlas-home #creds .creds-run img,\n"
            "  .atlas-home #creds .creds-run img.cr-emblem",
        )[0]

        self.assertIn("min-height: 84px", section)
        self.assertIn("min-height: 78px", track)
        self.assertIn("max-width: 78px", logos)
        self.assertIn("max-height: 50px", logos)


if __name__ == "__main__":
    unittest.main()
