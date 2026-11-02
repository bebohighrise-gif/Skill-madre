# Research and context efficiency

Sources reviewed: 2026-11-01. Provider APIs, retention/compaction behavior, legal guidance, and archive coverage can change; verify current documentation before relying on them.

Read this reference for web research, OSINT from lawful public sources, evidence synthesis, or long tasks constrained by context, token, latency, or cost budgets. Saving tokens is a quality optimization only if material claims, uncertainty, safety constraints, and source paths remain recoverable.

## Research workflow

1. Define the question, intended decision, scope, exclusions, jurisdiction, time window, and “enough evidence” threshold. Separate known facts, hypotheses, and open questions.
2. Search broadly enough to discover the source landscape, then narrow to primary sources and authoritative documentation. Open the source pages and verify context; search snippets alone are not evidence. For current or version-sensitive claims, record publication/update date and retrieval date.
3. Trace important claims to their nearest original source. Several articles repeating one release, report, or social post form one source chain, not independent corroboration. Seek independent evidence where the claim's importance warrants it.
4. Keep a claim ledger: claim, status (supported, contradicted, unresolved), exact source and locator, source type, event/publication/retrieval dates, what the evidence establishes, what it does not establish, and confidence with reason.
5. Preserve disagreement, counterevidence, missing data, and alternative explanations. Do not turn a conflict into a false consensus or an absence of evidence into evidence of absence.
6. Present claims next to useful citations. Distinguish fact from inference and estimate; state material uncertainty beside the affected conclusion. Report coverage and exclusions accurately.
7. For OSINT, apply necessity and minimization: use only data needed to answer the question, assess risks to people and sources, respect access boundaries, site terms, law, and rights, and avoid doxxing, stalking, impersonation, or unauthorized access. Public availability is not automatic ethical permission to aggregate or publish.

For images, video, archives, and other digital evidence, distinguish the provenance/integrity of an artifact from the truth of the caption or claim associated with it. Record capture time, original and archive URLs, transformation, and relevant context. A missing archive snapshot does not prove a page never existed.

## Context and token budget

Treat context as a limited working set, not a filing cabinet. Apply progressive disclosure: keep the task trigger and essential global rules compact; load one task-specific procedure; retrieve reference sections and source pages by need; avoid dumping whole repositories, giant logs, or entire API schemas when a bounded view will answer the question.

Before reading a large resource, inspect its size and structure. Use headings, indexes, grep/search, bounded ranges, pages, or summaries to locate the relevant passage. Expand the range when details or neighboring context can change the interpretation. State what was not read. Do not silently omit high-risk sections or use a partial extraction as proof that the full file contains no contrary evidence.

Reduce tool output at its source when possible: request relevant fields, filter by query, set safe page/range limits, or produce structured summaries with links to original evidence. Keep references reopenable: retain source URL or file path, version/commit, date, locator, and an evidence ID or digest where appropriate. A shortened answer with no trail is not a good compression.

For long-running work, persist a compact continuation record with: goal and acceptance criteria; locked constraints; facts with references; decisions and reasons; current branch/project state; changed files; commands/results; unresolved questions; risks; next action. Separate confirmed facts from assumptions, and revalidate a saved note against the current project before acting on it.

Compact near a measured operational threshold, not after critical context has already been lost. Preserve exact identifiers, numeric limits, decisions, security/authorization gates, and pending failures. Drop stale, duplicated, or recoverable raw tool output only after preserving a pointer to the source and the information needed to continue. Some model/API compaction mechanisms have product-specific contracts; follow that provider's current documentation rather than assuming formats are interchangeable.

## Measure the trade-off

Track input/output tokens or best available estimate, cost, latency, reading/tool calls, claim coverage, citation accuracy, critical-fact retention, uncertainty retention, and follow-up correction rate. Compare methods on the same task set. A token estimate is not a canonical tokenizer count unless the actual tokenizer is used. Prefer the smallest context that preserves the evidence necessary for a correct decision.

Test summaries with questions about dispersed facts, exact IDs/values, negative constraints, disputed evidence, task state, and unresolved issues. If a compressed context changes a conclusion or drops a safety boundary, revise the summary schema or avoid that compression for the task.

## Sources reviewed

- Berkeley Protocol on Digital Open Source Investigations: https://www.ohchr.org/en/publications/policy-and-methodological-publications/berkeley-protocol-digital-open-source (also https://www.ohchr.org/sites/default/files/2024-01/OHCHR_BerkeleyProtocol.pdf)
- Bellingcat's Online Open Source Investigation Toolkit: https://bellingcat.gitbook.io/toolkit (the toolkit itself warns that inclusion is not endorsement)
- Internet Archive, Wayback search guide: https://help.archive.org/help/search-a-basic-guide/
- European Journalism Centre, Verification Handbook 1: https://ejc.net/resources/verification-handbook-1
- Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents
- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI compaction guide: https://developers.openai.com/api/docs/guides/compaction
- Agent Skills for Context Engineering: https://github.com/muratcankoylan/agent-skills-for-context-engineering (repository activity and stars are discovery signals, not validation of the practices)
- REA CLI and Evidence guide: https://github.com/morluto/rea/blob/main/docs/cli.md (documents bounded summary/page views for large analysis outputs; verify current behavior before integration)

These sources are method references, not endorsements of every tool or universal performance evidence. Version, availability, license, retention behavior, and product-specific compaction semantics can change; verify them at use time.
