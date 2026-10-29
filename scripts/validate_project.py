#!/usr/bin/env python3
"""Validate the neutral portable skill package."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "README.md", "LICENSE", "ATTRIBUTIONS.md", "AGENTS.md",
    "SECURITY.md", "CONTRIBUTING.md", "CHANGELOG.md", "evidence-ledger.md",
    "install.sh", "install.ps1", "installer/SKILL.md",
    "references/platform-adapters.md", "references/platform-playbooks.md",
    "references/portable-installation.md", "references/quality-matrix.md",
    "evals/evals.json", "scripts/package_skill.py", "scripts/install_skill.py",
]
missing = [p for p in required if not (ROOT / p).is_file()]
if missing:
    raise SystemExit("Missing: " + ", ".join(missing))

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
if not re.match(r"^---\nname: [a-z0-9-]+\ndescription: .+\n---\n", skill):
    raise SystemExit("SKILL.md frontmatter is invalid")
if len(skill.splitlines()) >= 500:
    raise SystemExit("SKILL.md must stay below 500 lines")
if any(p.name.lower().startswith("promot") for p in ROOT.iterdir()):
    raise SystemExit("Promot must not be present")
for forbidden in (".env", ".npmrc", "id_rsa"):
    if (ROOT / forbidden).exists():
        raise SystemExit(f"Forbidden sensitive file present: {forbidden}")

evals = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
if not evals.get("cases"):
    raise SystemExit("No evaluation cases found")
print(f"OK: {len(required)} required package files and {len(evals['cases'])} evaluation cases")
