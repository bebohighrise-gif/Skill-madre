#!/usr/bin/env python3
"""Create a portable .skill zip from the neutral package allowlist."""
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "ATTRIBUTIONS.md",
    "evidence-ledger.md",
    "references/platform-adapters.md",
    "references/platform-playbooks.md",
    "references/portable-installation.md",
    "references/quality-matrix.md",
    "installer/SKILL.md",
]

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", type=Path, required=True)
args = parser.parse_args()
missing = [p for p in INCLUDE if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Missing package files: " + ", ".join(missing))
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
    for relative in INCLUDE:
        archive.write(ROOT / relative, relative)
print(f"Created {args.output} with {len(INCLUDE)} files")
