#!/usr/bin/env python3
"""Validate the repository and the complete runtime resource graph."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER = re.compile(r"^---\nname: ([a-z0-9-]+)\ndescription: .+\n---\n", re.DOTALL)
LOCAL_REF = re.compile(r"(?<![\w./-])(references/[\w./-]+|evidence-ledger\.md)")


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> None:
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        fail("SKILL.md is missing")
    skill = skill_path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(skill)
    if not match:
        fail("SKILL.md frontmatter is invalid")
    if len(skill.splitlines()) >= 500:
        fail("SKILL.md must stay below 500 lines")
    description = re.search(r"^description: (.+)$", skill, re.MULTILINE).group(1)
    if len(description) > 1024:
        fail(f"description is {len(description)} characters; the Agent Skills limit is 1024")

    package_files = [skill_path, ROOT / "evidence-ledger.md"] + sorted((ROOT / "references").rglob("*.md"))
    missing = [str(p.relative_to(ROOT)) for p in package_files if not p.is_file()]
    if missing:
        fail("Missing runtime files: " + ", ".join(missing))
    for path in package_files:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT.resolve()):
            fail(f"Unsafe runtime path: {path}")

    for source in package_files:
        text = source.read_text(encoding="utf-8")
        for ref in sorted(set(LOCAL_REF.findall(text))):
            if not (ROOT / ref).is_file():
                fail(f"Broken local reference in {source.relative_to(ROOT)}: {ref}")

    forbidden = {".env", ".npmrc", "id_rsa", "id_ed25519"}
    for path in ROOT.rglob("*"):
        if path.is_file() and path.name in forbidden:
            fail(f"Forbidden sensitive file present: {path.relative_to(ROOT)}")

    evals_path = ROOT / "evals" / "evals.json"
    if evals_path.is_file():
        evals = json.loads(evals_path.read_text(encoding="utf-8"))
        cases = evals.get("cases")
        if not isinstance(cases, list) or not cases:
            fail("No evaluation cases found")
        ids = [case.get("id") for case in cases if isinstance(case, dict)]
        if len(ids) != len(cases) or any(not value for value in ids) or len(set(ids)) != len(ids):
            fail("Evaluation cases must have unique, non-empty IDs")
        for case in cases:
            if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
                fail(f"Evaluation case {case.get('id')} has no prompt")
            if not isinstance(case.get("must_include"), list) or not case["must_include"]:
                fail(f"Evaluation case {case.get('id')} has no must_include criteria")

    trigger_path = ROOT / "evals" / "trigger-evals.json"
    if trigger_path.is_file():
        queries = json.loads(trigger_path.read_text(encoding="utf-8"))
        if not isinstance(queries, list) or not queries:
            fail("trigger-evals.json must be a non-empty list")
        for item in queries:
            if not isinstance(item.get("query"), str) or not isinstance(item.get("should_trigger"), bool):
                fail("Each trigger eval needs a string query and a boolean should_trigger")
        if not any(q["should_trigger"] for q in queries) or all(q["should_trigger"] for q in queries):
            fail("trigger-evals.json needs both should_trigger and should-not-trigger queries")

    print(f"OK: {len(package_files)} runtime files and valid local references")


if __name__ == "__main__":
    main()
