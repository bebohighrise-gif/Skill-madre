# Open Quality Engineering project

This repository distributes a neutral portable Agent Skill. The canonical workflow is [SKILL.md](SKILL.md). The installation subagent is [installer/SKILL.md](installer/SKILL.md), and the deterministic installer is [scripts/install_skill.py](scripts/install_skill.py).

Keep the package independent from providers, models, account names, fixed host paths, credentials, and proprietary commands. Preserve YAML frontmatter with `name` and `description`. Put reusable details in `references/` and keep the core below 500 lines.

Run the validator and package command after changes. Test installation in a temporary directory, protect existing destinations by default, and remove temporary archives or caches before delivery.
