---
name: madre
description: Evidence-first engineering workflow for coding, debugging, research, creative production, UX, security review, and authorized reverse engineering. Use when a task needs disciplined inspection, bounded changes, honest verification, or a safe handoff.
---

# Madre

Use this skill as a routing layer, not as a universal checklist. Keep the active process proportional to risk and scope. If the request is clearly unrelated to engineering, research, creative work, UX, security review, or authorized reverse engineering, do not activate this workflow, inspect a repository, or load references; answer briefly using the smallest appropriate process.

## Load order

1. Resolve every relative reference from the skill root, not from the current working directory, unless the host explicitly documents another skill root.
2. Read `references/system-contract.md` for non-negotiable truthfulness, scope, authorization, and data-safety rules.
3. Read `references/workflow-routing.md` and select exactly the narrowest lane that fits the request. If no lane fits, stop without repository inspection.
4. Read only the lane file(s) named by that route:
   - `references/software-engineering.md` for code, bugs, architecture, dependencies, APIs, data, or releases.
   - `references/security-and-reverse-engineering.md` for security reviews, penetration testing, OSINT involving people, or authorized reverse engineering.
   - `references/research-and-creative.md` for research, image/video, UX/UI, or context-heavy work.
   - `references/platforms.md` when a web, desktop, Android, iOS, 3D, animation, or media-specific check is required.
   - `references/privacy-and-data.md` when personal data, tenant isolation, telemetry, or logging is involved.
   - `references/external-skills.md` when selecting, installing, or activating another skill.
5. Read `references/quality-gates.md` before delivery. Apply only the gates relevant to the task and mark unavailable checks as unavailable.
6. For installation or packaging of this skill, read `references/installation.md` and use the repository scripts. Do not improvise paths or copy rules.

## Minimal operating loop

1. Define acceptance criteria, constraints, non-goals, authority, and unknowns.
2. Inspect repository status, local instructions, manifests, affected boundaries, and the baseline.
3. Form a testable hypothesis or design decision from evidence.
4. Make the smallest reversible change at the owning boundary.
5. Run the narrowest meaningful check immediately.
6. Review the diff, consumers, security impact, user-facing states, and rollback.
7. Report observed facts, derived conclusions, inferences, unavailable checks, and remaining unknowns separately.

## Completion contract

Never claim that a build, test, runtime behavior, source, credential, integration, screenshot, or tool result exists unless it was actually observed. A plan is not an implementation; static inspection is not runtime proof; a mock is not proof of a real provider.

Do not reset, clean, overwrite, publish, access production, handle secrets, test a third-party target, bypass controls, or make an irreversible change without the required scope and authorization. Preserve unrelated user work. Use project conventions and the least powerful tool that answers the question.

## Handoff format

Return: what changed and why; affected files; exact validation commands and results; unavailable checks; security/privacy, UX/accessibility, performance, compatibility, and rollback notes; remaining unknowns; and the smallest next check.
