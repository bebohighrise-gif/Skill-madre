#!/usr/bin/env python3
"""Regression tests for the project validator."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="madre-validator-test-")
        self.repo = Path(self.temp.name) / "repo"
        shutil.copytree(PROJECT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_validator(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(self.repo / "scripts" / "validate_project.py")], cwd=self.repo, text=True, capture_output=True)

    def test_valid_project_passes(self) -> None:
        self.assertEqual(self.run_validator().returncode, 0)

    def test_missing_evals_file_does_not_crash(self) -> None:
        (self.repo / "evals" / "evals.json").unlink()
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_overlong_description_is_rejected(self) -> None:
        skill = self.repo / "SKILL.md"
        text = skill.read_text(encoding="utf-8")
        skill.write_text(text.replace("description: ", "description: " + "x" * 1100 + " ", 1), encoding="utf-8")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("1024", result.stderr + result.stdout)

    def test_trigger_evals_need_both_classes(self) -> None:
        (self.repo / "evals" / "trigger-evals.json").write_text('[{"query": "fix bug", "should_trigger": true}]', encoding="utf-8")
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
