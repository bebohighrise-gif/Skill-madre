# Madre

Madre is a provider-neutral Agent Skill for evidence-first engineering and creative workflows. The package uses a small router in `SKILL.md` and loads only the module needed for the current task.

## Structure

- `SKILL.md`: trigger, load order, minimal operating loop, and completion contract.
- `references/`: system contract, routing, software, security/reverse engineering, research/creative, platform adapters, quality gates, and installation.
- `scripts/`: repository-only validation, installation, and packaging tools.
- `evidence-ledger.md`: optional durable record for material tasks.

The skill does not grant tools, credentials, authorization, runtime access, or host activation. Static instructions never replace the host's permissions or actual tests.

## Validate and package

```bash
python3 scripts/validate_project.py
python3 scripts/package_skill.py --output /tmp/madre.skill
```

## Install

Use the wrapper for an explicit scope:

```bash
./install.sh --scope user
./install.sh --scope project --dest /path/to/project
./install.sh --scope custom --dest /path/to/skills
```

The installer stages and validates the copy before replacing an existing destination. It refuses overwrite unless `--force` is supplied, and reports a timestamped backup when replacement occurs. The host may still require a separate activation or discovery step.

See [LICENSE](LICENSE) and [ATTRIBUTIONS.md](ATTRIBUTIONS.md) for licensing and attribution.
