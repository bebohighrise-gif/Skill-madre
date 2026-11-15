# Workflow routing

Choose the narrowest route that satisfies the request; do not run every checklist.

If the request is unrelated to the skill's domain, do not force activation. Answer briefly and do not inspect a repository. If the request concerns another skill or connector, route to `references/external-skills.md` before any installation or activation decision.

- **Explain:** answer from inspected evidence; research only current, niche, or uncertain claims.
- **Inspect/review:** read-only baseline and findings. Do not edit unless asked.
- **Research:** define questions, prefer primary sources, compare dates/versions, cite claims, and stop when material uncertainty is resolved.
- **Build/modify:** inspect, plan, change one owning boundary at a time, test after each meaningful slice, and review the final diff.
- **Debug:** reproduce or state why reproduction is unavailable, minimize, trace producer-to-consumer, fix the cause, add a regression check, and recheck adjacent consumers.
- **Design:** specify states, interfaces, trade-offs, risks, and acceptance evidence before implementation.
- **Release/recover:** verify package, configuration, compatibility, rollback, and clean-checkout behavior; repair only the affected component.
- **Security/reverse engineering:** load the security lane and pass its authorization gate before probing.

If target, authority, scope, or a product choice could materially change the work, ask one focused question before writing.
