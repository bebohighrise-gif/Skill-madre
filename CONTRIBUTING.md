# Contributing

Keep `SKILL.md` as the provider-neutral source of truth. Put installation decisions in `installer/SKILL.md`, deterministic copying in `scripts/install_skill.py`, and variant-specific details in `references/`.

Before opening a change, run:

```bash
python3 scripts/validate_project.py
python3 scripts/package_skill.py --output /tmp/madre.skill
bash -n install.sh
```

Test user, project, custom, force, and package modes in temporary directories. Do not add provider names, vendor paths, credentials, caches, generated archives, or machine-specific configuration to the repository. If a host requires a special adapter, keep it outside the neutral core and document it as an external integration rather than hard-coding it here.
