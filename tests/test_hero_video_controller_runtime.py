from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class HeroVideoControllerRuntimeTests(unittest.TestCase):
    def test_desktop_six_second_loop_and_mobile_full_loop(self):
        result = subprocess.run(
            ["node", "tests/hero_video_controller_runtime.mjs"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)


if __name__ == "__main__":
    unittest.main()
