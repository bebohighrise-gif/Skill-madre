#!/usr/bin/env python3
"""Install the validated skill without guessing paths or losing the old copy."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "madre"


def files_to_install() -> list[Path]:
    files = [ROOT / "SKILL.md", ROOT / "evidence-ledger.md"]
    files += sorted((ROOT / "references").rglob("*.md"))
    return [p for p in files if p.is_file()]


def reject_unsafe_source(paths: list[Path]) -> None:
    for path in paths:
        if path.is_symlink():
            raise SystemExit(f"Refusing symlink in skill source: {path.relative_to(ROOT)}")
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise SystemExit(f"Refusing source path escape: {path}")


def destination_for(args: argparse.Namespace) -> Path:
    if args.scope == "user":
        return Path.home() / ".agent" / "skills" / NAME
    if args.dest is None:
        raise SystemExit(f"--dest is required for --scope {args.scope}")
    base = args.dest.expanduser().resolve()
    return base / ".agent" / "skills" / NAME if args.scope == "project" else base / NAME


def validate() -> None:
    subprocess.run(["python3", str(ROOT / "scripts" / "validate_project.py")], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=["user", "project", "custom"], default="user")
    parser.add_argument("--dest", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    validate()
    source_files = files_to_install()
    reject_unsafe_source(source_files)
    if not source_files:
        raise SystemExit("No installable skill files found")

    destination = destination_for(args)
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging: Path | None = Path(tempfile.mkdtemp(prefix=f".{NAME}.staging-", dir=destination.parent))
    backup: Path | None = None
    try:
        for source in source_files:
            relative = source.relative_to(ROOT)
            target = staging / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        if not (staging / "SKILL.md").is_file():
            raise SystemExit("Staged copy is incomplete")
        if destination.exists() and not args.force:
            raise SystemExit(f"Destination exists; use --force to back it up: {destination}")
        if destination.exists():
            backup = destination.with_name(destination.name + f".backup.{int(time.time())}")
            destination.rename(backup)
        staging.rename(destination)
        staging = None
        print(f"Installed: {destination}")
        print(f"Backup: {backup or 'none'}")
        print(f"Files: {sum(1 for p in destination.rglob('*') if p.is_file())}")
    finally:
        if staging is not None and staging.exists():
            shutil.rmtree(staging)


if __name__ == "__main__":
    main()
