# Portable installation reference

A portable skill is a folder whose canonical entry point is `SKILL.md`. A host may discover it from a user directory, project directory, custom skill root, uploaded folder, `.zip`, or `.skill` archive. This repository does not assume which mechanism a host provides.

## Scope rules

- **User:** install under the user's documented skill root. This affects that user's projects.
- **Project:** install under a dedicated hidden skill folder inside the selected project. Commit it only when the project owner wants shared behavior.
- **Custom:** install only to an explicit absolute destination supplied by the user or host.
- **Archive:** package the allowlisted folder and let the host import/upload it.

## Required package shape

```text
skill-name/
├── SKILL.md
├── references/       optional, loaded on demand
├── scripts/          optional, deterministic helpers
├── templates/        optional, reusable output assets
└── installer/        optional, installation subagent instructions
```

Keep `SKILL.md` concise, imperative, and below the host's context budget. Put variant-specific material in references. Never treat an archive extension as proof that a host accepts it; verify the host's import mechanism.

## Idempotence and rollback

An installation is idempotent when running it twice with the same source and destination produces the same content without deleting unrelated files. Before replacement, rename the existing directory to a timestamped backup. A rollback restores that backup only after checking destination identity and avoiding a newer user change.

## Activation truthfulness

Copying files is installation. A host showing the skill in its selector, loading its metadata, or executing a test invocation is activation. Report those as separate facts. If activation cannot be tested, say that the user must select, reload, restart, or configure the host manually.
