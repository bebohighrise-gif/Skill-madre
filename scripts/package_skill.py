#!/usr/bin/env python3
"""Create a safe skill archive from the validated runtime resource graph."""
from __future__ import annotations

import argparse
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def runtime_files() -> list[Path]:
    return [ROOT / "SKILL.md", ROOT / "evidence-ledger.md", ROOT / "LICENSE", ROOT / "ATTRIBUTIONS.md"] + sorted((ROOT / "references").rglob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.expanduser().resolve()
    if output.parent == ROOT.resolve() or output.is_relative_to(ROOT.resolve()):
        raise SystemExit("Output archive must be outside the source directory")
    subprocess.run(["python3", str(ROOT / "scripts" / "validate_project.py")], check=True)
    files = runtime_files()
    missing = [str(p.relative_to(ROOT)) for p in files if not p.is_file()]
    if missing:
        raise SystemExit("Missing package files: " + ", ".join(missing))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT))
    print(f"Created {output} with {len(files)} files")


if __name__ == "__main__":
    main()
