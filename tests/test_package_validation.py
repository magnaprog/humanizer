"""Exercise invalid package inputs in isolated copies."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "package"
        shutil.copytree(
            ROOT, self.root,
            ignore=shutil.ignore_patterns(".git", "__pycache__"),
        )

    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts/validate-package.py")],
            capture_output=True, text=True,
        )

    def assert_rejected(self, message):
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(message, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_package(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_duplicate_skill_number(self):
        path = self.root / "SKILL.md"
        path.write_text(path.read_text() + "\n### 1. Not X but Y\n")
        self.assert_rejected("Number SKILL.md patterns")

    def test_duplicate_readme_row(self):
        path = self.root / "README.md"
        text = path.read_text()
        row = next(line for line in text.splitlines() if line.startswith("| 1 |"))
        path.write_text(text + row + "\n")
        self.assert_rejected("once each")

    def test_malformed_marketplace(self):
        (self.root / ".claude-plugin/marketplace.json").write_text("{")
        self.assert_rejected("Fix the JSON in .claude-plugin/marketplace.json")

    def test_missing_supporting_reference(self):
        (self.root / "references/voice-examples.md").unlink()
        self.assert_rejected("Cannot read references/voice-examples.md")

    def test_wrong_plugin_loader(self):
        path = self.root / ".claude-plugin/plugin.json"
        data = json.loads(path.read_text())
        del data["skills"]
        path.write_text(json.dumps(data))
        self.assert_rejected("Point the Claude plugin skill loader")

    def test_mismatched_release_version(self):
        path = self.root / ".claude-plugin/plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "0.0.1"
        path.write_text(json.dumps(data))
        self.assert_rejected("Use one package version")


if __name__ == "__main__":
    unittest.main()
