# Contributing

Keep `SKILL.md` as a small routing layer. Put invariant safety rules in `references/system-contract.md`, route selection in `references/workflow-routing.md`, and domain-specific procedures in the lane files. Do not duplicate the same rule across modules.

The runtime package is the graph formed by `SKILL.md`, `evidence-ledger.md`, and Markdown files under `references/`. The installer and packager are repository tooling; they are not copied into the installed skill.

Run these checks before proposing a change:

```bash
python3 scripts/validate_project.py
python3 scripts/package_skill.py --output /tmp/madre.skill
bash -n install.sh
```

Keep claims evidence-based. Do not add provider-specific behavior, credentials, fixed paths, or external instructions unless the source and scope are explicit. If a new reference is added, link it from the route that needs it and ensure the validator sees it in the archive.
