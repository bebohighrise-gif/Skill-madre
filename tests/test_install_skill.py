#!/usr/bin/env python3
"""Black-box tests for the portable skill installer."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
INSTALLER = Path("scripts/install_skill.py")


class InstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="madre-installer-test-")
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        shutil.copytree(PROJECT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))
        self.destination_base = self.root / "destination"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_installer(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.repo / INSTALLER), *args],
            cwd=self.repo,
            text=True,
            capture_output=True,
        )

    def test_install_rejects_existing_destination_without_force(self) -> None:
        first = self.run_installer("--scope", "custom", "--dest", str(self.destination_base))
        self.assertEqual(first.returncode, 0, first.stderr)
        second = self.run_installer("--scope", "custom", "--dest", str(self.destination_base))
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("use --force", second.stderr + second.stdout)

    def test_force_install_creates_backup_and_no_unexpected_files(self) -> None:
        self.run_installer("--scope", "custom", "--dest", str(self.destination_base)).check_returncode()
        installed = self.destination_base / "madre"
        (installed / "unexpected.txt").write_text("must not survive replacement", encoding="utf-8")
        result = self.run_installer("--scope", "custom", "--dest", str(self.destination_base), "--force")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((installed / "unexpected.txt").exists())
        backups = list(self.destination_base.glob("madre.backup.*"))
        self.assertEqual(len(backups), 1)
        self.assertTrue((backups[0] / "SKILL.md").is_file())

    def test_broken_reference_is_rejected_before_destination_creation(self) -> None:
        skill = self.repo / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8") + "\nRead `references/missing.md`.\n", encoding="utf-8")
        result = self.run_installer("--scope", "custom", "--dest", str(self.destination_base))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.destination_base / "madre").exists())

    def test_symlink_runtime_file_is_rejected(self) -> None:
        link = self.repo / "references" / "unsafe-link.md"
        link.symlink_to(self.root / "outside.md")
        result = self.run_installer("--scope", "custom", "--dest", str(self.destination_base))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unsafe runtime path", result.stderr + result.stdout)

    def test_destination_inside_source_is_rejected(self) -> None:
        result = self.run_installer("--scope", "custom", "--dest", str(self.repo))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("inside the skill source", result.stderr + result.stdout)

    def test_symlink_destination_is_rejected(self) -> None:
        real = self.root / "real-destination"
        real.mkdir()
        self.destination_base.mkdir()
        (self.destination_base / "madre").symlink_to(real, target_is_directory=True)
        result = self.run_installer("--scope", "custom", "--dest", str(self.destination_base))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink destination", result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
