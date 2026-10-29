# Research-derived methods

This reference records method-level patterns distilled from a broad review of public skill specifications, coding-agent workflow repositories, rule systems, and structured delivery toolkits. It does not copy source code, prompts, documentation prose, branding, templates, or proprietary assets. The review is a dated research snapshot; host behavior, licenses, repository contents, and recognition signals can change.

## Selection and evidence boundary

The reviewed set covered: an open skill-format specification; multiple official skill collections; a composable development-workflow collection; community skill catalogs; structured requirements/specification toolkits; a terminal coding workflow; and persistent rule systems. The sources were selected because their public documentation exposed reusable mechanics such as activation, progressive disclosure, planning, testing, review, packaging, security, or artifact-backed execution. Repository stars, forks, commits, and listed integrations were treated only as visibility signals, never as proof of quality, safety, adoption, or efficacy.

The integrated content below is an independent synthesis. No source is treated as universally correct, and no host-specific path, command, model, tool name, or permission declaration is required by Madre.

## Patterns integrated into Madre

### 1. Metadata-first activation

Expose only a compact identity and trigger description during discovery. The description must state what the skill does, when to use it, what it does not do, and any important risk boundary. Support both explicit invocation and relevance-based activation, but allow implicit activation to be disabled for consequential procedures. Log the selected skill, reason, source, and version so activation is auditable.

### 2. Progressive disclosure

Load the core instructions only after activation. Load references, templates, assets, and scripts individually when the active procedure needs them. Resolve relative paths from the skill root, keep references shallow and bounded, avoid eager repository-wide reads, deduplicate activation, and preserve the active instructions through context compaction. A resource manifest may be listed without reading every resource.

### 3. Context and scope precedence

Separate user, project, directory, and custom scopes. Define deterministic precedence and warn on collisions or shadowing. Treat project-provided content as untrusted until the user or host authorizes it. Filter disabled or inaccessible skills from the active catalog instead of advertising capabilities that cannot run.

### 4. Risk-based process routing

Use the smallest safe process. Trivial or read-only work can use a short path; ambiguous, architectural, multi-file, public, destructive, or high-risk work needs clarification, planning, approval, review, and stronger evidence. Do not force every request through a heavyweight specification workflow, but do not bypass gates just to be fast.

### 5. Durable handoffs

Do not rely on hidden conversation history. Persist the active work item, assumptions, decisions, plan, task status, changed files, commands, exit statuses, review findings, unresolved risks, and next action. Use explicit states such as `draft`, `ready`, `in-progress`, `in-review`, `built`, `done`, and `blocked`. Keep reviewer-owned decisions separate from agent suggestions.

### 6. Plan, execute, review, finish

For meaningful changes, clarify intent and non-goals; inspect the repository; propose options and a plan; obtain approval when the risk or ambiguity warrants it; execute in small bounded tasks; review both requirement compliance and code quality; run fresh verification; and finish with an explicit keep/merge/rollback/discard decision. Separate worker execution from orchestration, backlog selection, retries, and final acceptance.

### 7. Read before write

Establish prerequisites, access, identifiers, current behavior, and affected consumers before mutation. Use read/list/search/get operations to construct context, then perform writes in logical batches. Never guess IDs, permissions, routes, API contracts, or configuration. Authentication and permission failures are blockers, not invitations to bypass controls.

### 8. Evidence before completion

Every completion claim needs a fresh command, test, runtime observation, review, or other evidence appropriate to the claim. Use test-first work for behavior when practical, run the relevant existing suite, inspect the final diff, and report unavailable checks. A passing test does not prove UX, security, packaging, performance, or migration safety unless those claims have their own evidence.

### 9. Independent review and bounded repair

Use separate requirement/specification and implementation-quality reviews. Classify findings by severity, block on high-severity issues, fix only in-scope findings, and cap repair loops. When the defect is upstream of the code, revise the plan or requirement rather than layering patches. Preserve a deferred-findings list instead of expanding scope silently.

### 10. Validation layers

Combine deterministic schema/frontmatter/structure checks, link and reference checks, workflow and trigger evaluations, clean-context baselines, adversarial cases, project tests, security review, and human inspection where judgment cannot be automated. Track time, token/context cost, tool failures, and regressions. Treat model-generated scores and repository popularity as supplementary signals only.

### 11. Security as host enforcement

Skill text is not a sandbox. Enforce trust, tool capabilities, file and network boundaries, secret redaction, command approval, external-action confirmation, isolation, and audit logs in the host or installer. Review scripts, hooks, connectors, dependencies, templates, and fetched content. Prefer immutable source references and distinguish discovery from trusted installation.

### 12. Portable adapters

Keep the canonical workflow neutral. Put host-specific invocation syntax, directory conventions, model tiers, hook behavior, connector setup, and tool vocabulary into external adapters generated or maintained separately. Validate adapters against the canonical source and report capability mismatches instead of silently degrading or pretending that a declaration grants permission.

## What Madre deliberately does not adopt

Madre does not force a single planner, command syntax, model tier, project state format, subagent topology, branch strategy, test framework, tool permission model, or host directory. It does not copy a catalog, marketplace, plugin, prompt, command, agent persona, or branded workflow. It does not claim that a skill can provide tools, sandboxing, authentication, or runtime evidence by itself.

## License and provenance policy

When an external method inspires an integration, preserve the source URL and research date in project history or release notes, and record any applicable license or attribution requirement before copying code or expressive material. Prefer an independent implementation of method-level ideas. Never infer a repository-wide license from a missing or ambiguous license field. Review each file, dependency, asset, and external connector separately.
