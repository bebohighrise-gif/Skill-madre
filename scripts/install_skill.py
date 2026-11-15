#!/usr/bin/env python3
"""Install the runtime skill graph without executing package validation code."""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "madre"
FRONTMATTER = re.compile(r"^---\nname: ([a-z0-9-]+)\ndescription: .+\n---\n", re.DOTALL)
LOCAL_REF = re.compile(r"(?<![\w./-])(references/[\w./-]+|evidence-ledger\.md)")
FORBIDDEN_NAMES = {".env", ".npmrc", "id_rsa", "id_ed25519"}


def runtime_files(root: Path = ROOT) -> list[Path]:
    return [root / "SKILL.md", root / "evidence-ledger.md"] + sorted((root / "references").rglob("*.md"))


def fail(message: str) -> None:
    raise SystemExit(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest(root: Path = ROOT) -> dict[str, str]:
    files = runtime_files(root)
    if not files or not (root / "SKILL.md").is_file():
        fail("Source runtime graph is incomplete")
    result: dict[str, str] = {}
    root_resolved = root.resolve()
    for path in files:
        if path.is_symlink() or not path.resolve().is_relative_to(root_resolved):
            fail(f"Refusing unsafe runtime path: {path}")
        if not path.is_file():
            fail(f"Missing runtime file: {path.relative_to(root)}")
        result[str(path.relative_to(root))] = sha256(path)
    return result


def validate_graph(root: Path = ROOT) -> dict[str, str]:
    files = runtime_files(root)
    hashes = manifest(root)
    skill_path = root / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")
    if not FRONTMATTER.match(skill):
        fail("SKILL.md frontmatter is invalid")
    if len(skill.splitlines()) >= 500:
        fail("SKILL.md must stay below 500 lines")
    for path in files:
        text = path.read_text(encoding="utf-8")
        for ref in sorted(set(LOCAL_REF.findall(text))):
            if not (root / ref).is_file():
                fail(f"Broken local reference in {path.relative_to(root)}: {ref}")
    for path in root.rglob("*"):
        if path.is_file() and path.name in FORBIDDEN_NAMES:
            fail(f"Forbidden sensitive file present: {path.relative_to(root)}")
    return hashes


def verify_tree(root: Path, expected: dict[str, str]) -> None:
    actual = {}
    for relative in expected:
        path = root / relative
        if not path.is_file() or path.is_symlink():
            fail(f"Installed copy is incomplete or unsafe: {relative}")
        actual[relative] = sha256(path)
    if actual != expected:
        fail("Installed copy does not match the validated source hashes")
    files = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()}
    if files != set(expected):
        fail("Installed copy contains unexpected or missing files")


def destination_for(args: argparse.Namespace) -> Path:
    if args.scope == "user":
        return Path.home() / ".agent" / "skills" / NAME
    if args.dest is None:
        fail(f"--dest is required for --scope {args.scope}")
    base = args.dest.expanduser().resolve()
    return base / ".agent" / "skills" / NAME if args.scope == "project" else base / NAME


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=["user", "project", "custom"], default="user")
    parser.add_argument("--dest", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    expected = validate_graph()
    destination = destination_for(args)
    if destination.exists() and not destination.is_dir():
        fail(f"Destination is not a directory: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging: Path | None = Path(tempfile.mkdtemp(prefix=f".{NAME}.staging-", dir=destination.parent))
    backup: Path | None = None
    try:
        for relative in expected:
            source = ROOT / relative
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        verify_tree(staging, expected)
        if destination.exists() and not args.force:
            fail(f"Destination exists; use --force to back it up: {destination}")
        if destination.exists():
            backup = destination.with_name(destination.name + f".backup.{int(time.time())}")
            destination.rename(backup)
        staging.rename(destination)
        staging = None
        try:
            verify_tree(destination, expected)
        except SystemExit:
            shutil.rmtree(destination, ignore_errors=True)
            if backup is not None and backup.exists():
                backup.rename(destination)
            raise
        print(f"Installed: {destination}")
        print(f"Backup: {backup or 'none'}")
        print(f"Files: {len(expected)}")
    finally:
        if staging is not None and staging.exists():
            shutil.rmtree(staging)


if __name__ == "__main__":
    main()
