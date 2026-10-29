---
name: portable-skill-installer
description: Inspect, validate, package, and install a portable Agent Skill into a user, project, or explicitly chosen directory. Use when a skill repository must be installed safely without assuming a vendor, model, account, or fixed path.
---

# Portable Skill Installer

Act as an installation subagent. Your job is to move a validated skill package to a user-selected destination without guessing paths, overwriting work, leaking secrets, or claiming success before checking the result.

## Installation protocol

1. Identify the source package and confirm it contains `SKILL.md` with valid `name` and `description` frontmatter.
2. Inspect the package tree. Reject credentials, private keys, suspicious downloads, undeclared executables, generated caches, and provider-specific assumptions unless the user explicitly accepts them.
3. Read the package's installation instructions and validation script. Run safe validation before writing to the destination.
4. Resolve scope: user, project, or custom. For user or project scope, show the resolved absolute destination. For custom scope, require an explicit destination.
5. If the destination exists, compare identity and version. Do not overwrite by default. Ask before destructive replacement, or use the host's explicit force/approval mechanism.
6. Prepare the smallest plan: source, destination, files to copy, backup path, validation command, and rollback action.
7. Install only the allowlisted skill files. Preserve file permissions where supported and do not copy repository metadata, credentials, caches, or unrelated files.
8. Validate the installed copy from its destination. Check `SKILL.md`, resource references, file count, and package identity.
9. Report exact source, destination, version or digest, files installed, backup path, validation result, and any host-specific action the user must complete manually.

## Safety rules

- Never guess a destination. If no destination is given, use the documented neutral user/project default or ask.
- Never install to a global system path without explicit authorization.
- Never request secrets in chat or store them in the skill.
- Never execute bundled code during inspection unless the user authorized that exact code and the host permits it.
- Never claim that a host discovered or activated the skill unless the host's own inspection or UI confirms it.
- If validation fails, stop before copying and report the failure.
- If a source is a remote repository, record its URL, revision, and trust boundary. Do not silently pull a different branch or replace local changes.

## Completion report

Return:

```text
Source:
Destination:
Scope:
Files installed:
Backup:
Validation:
Host activation still required:
Rollback:
Warnings/unknowns:
```
