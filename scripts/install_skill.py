#!/usr/bin/env python3
"""Install this skill into a neutral user, project, or custom skill directory."""
from __future__ import annotations

import argparse
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "madre"
ALLOW = [
    "SKILL.md",
    "evidence-ledger.md",
    "references",
    "installer",
]

parser = argparse.ArgumentParser()
parser.add_argument("--scope", choices=["user", "project", "custom"], default="user")
parser.add_argument("--dest", type=Path)
parser.add_argument("--force", action="store_true")
args = parser.parse_args()

if args.scope == "user":
    destination = Path.home() / ".agent" / "skills" / NAME
elif args.scope == "project":
    if not args.dest:
        raise SystemExit("--dest is required for --scope project")
    destination = args.dest.expanduser().resolve() / ".agent" / "skills" / NAME
else:
    if not args.dest:
        raise SystemExit("--dest is required for --scope custom")
    destination = args.dest.expanduser().resolve() / NAME

if not (ROOT / "SKILL.md").is_file():
    raise SystemExit("Source SKILL.md is missing")
if destination.exists() and not args.force:
    raise SystemExit(f"Destination exists; use --force to back it up: {destination}")
if destination.exists():
    backup = destination.with_name(destination.name + f".backup.{int(time.time())}")
    destination.rename(backup)
else:
    backup = None

destination.mkdir(parents=True, exist_ok=True)
for relative in ALLOW:
    source = ROOT / relative
    target = destination / relative
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)

print(f"Installed: {destination}")
print(f"Backup: {backup or 'none'}")
print(f"Files: {sum(1 for p in destination.rglob('*') if p.is_file())}")
