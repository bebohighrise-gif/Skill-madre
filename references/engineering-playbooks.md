# Engineering playbooks

Use this reference only for the playbook that matches the active change. These are decision aids, not mandatory ceremony. Start from repository conventions, select the smallest useful checks, and keep claims tied to fresh evidence. Do not infer runtime, provider, compliance, or production readiness from source text alone.

## Contents

- [Playbook selection](#playbook-selection)
- [API and contract changes](#api-and-contract-changes)
- [Data and schema migrations](#data-and-schema-migrations)
- [Dependencies and supply chain](#dependencies-and-supply-chain)
- [Security and privacy review](#security-and-privacy-review)
- [Observability and incident debugging](#observability-and-incident-debugging)
- [Performance and reliability](#performance-and-reliability)
- [Release and deployment readiness](#release-and-deployment-readiness)
- [Architecture decisions](#architecture-decisions)
- [Evidence and handoff](#evidence-and-handoff)

## Playbook selection

| Change or symptom | Read and apply | Minimum evidence to seek |
|---|---|---|
| Public API, SDK, webhook, plugin, or service boundary | API and contract changes | Contract tests, compatibility review, error semantics |
| Persistent data format, schema, or backfill | Data and schema migrations | Upgrade/downgrade or recovery plan, representative migration test |
| New or upgraded package, image, action, or tool | Dependencies and supply chain | Exact version/source, license and advisory check, lockfile/build result |
| Identity, permissions, personal data, secrets, or untrusted input | Security and privacy review | Threat boundary, negative authorization/input tests, data-flow review |
| Production failure, missing signal, or hard-to-reproduce defect | Observability and incident debugging | Timestamped evidence, correlation path, reproducible or bounded hypothesis |
| Latency, memory, battery, frame rate, or scaling concern | Performance and reliability | Comparable baseline and post-change measurement under stated conditions |
| User-visible deployment, packaging, or rollout | Release and deployment readiness | Artifact/build identity, environment/config checks, rollback and health signal |
| Broad structural change or competing designs | Architecture decisions | Constraints, alternatives, trade-offs, decision record and revisit triggers |

Combine only the relevant playbooks. If the change crosses boundaries, identify ordering and rollback dependencies before editing.

## API and contract changes

1. Locate the actual contract: schema, route, generated client, versioning policy, consumers, error model, authentication boundary, and compatibility tests. Consult current authoritative documentation when external behavior is version-sensitive.
2. Define inputs, outputs, optionality, defaults, validation, ordering, idempotency, pagination, rate limits, timeout behavior, and failure semantics. Distinguish documented guarantees from observed behavior and assumptions.
3. Inventory consumers and compatibility requirements. Prefer additive evolution. For a breaking change, propose a migration path, deprecation window or compatibility layer, consumer coverage, and rollback before implementation; get approval where the product or release policy requires it.
4. Test representative valid, boundary, malformed, unauthorized, unavailable, duplicate/replayed, and rate-limited cases. Contract tests should use the real schema or protocol boundary. A mock verifies only the behavior it models.
5. Review generated clients, docs, examples, telemetry, and error messages together. Avoid leaking tokens, personal data, internal hostnames, or raw sensitive payloads into responses and logs.

## Data and schema migrations

Treat persisted data as a compatibility contract. Before mutation, establish the current and target schema, data volume/shape, writers/readers, backup and restore capability, locking behavior, and allowed downtime. Never run a production migration or destructive data operation without explicit authorization and a verified target.

Prefer staged expand-migrate-contract when mixed application versions or rolling deployment are possible: add backward-compatible structures, deploy compatible readers/writers, backfill in bounded resumable batches, verify invariants, switch consumers, then remove obsolete structures in a later safe release. Use a simpler atomic migration only when transaction and deployment semantics prove it safe.

Specify idempotency, checkpoints, rate/lock limits, retry behavior, observability, duplicate handling, null/default policy, integrity checks, and a stop/resume strategy. Preserve the original data until the new state is verified. Test empty, representative, large/boundary, malformed, interrupted, retried, and partially applied cases with fixtures or a disposable database. Distinguish rollback of code from rollback of irreversible data transformations; include restore or forward-repair steps when reversal is not safe.

## Dependencies and supply chain

Before adding or changing a dependency, search the project for an existing capability and inspect the package's exact registry, owner, version, maintenance activity, license, platform support, transitive footprint, install scripts/native code, known advisories, and lockfile effect. Use official package metadata and advisory sources where available; record the check date for security-sensitive decisions.

Pin or constrain versions according to repository policy and preserve reproducible lockfiles. Do not upgrade unrelated packages or execute newly fetched install hooks merely to inspect a package. Evaluate vendoring, checksums/signatures, provenance, and automated update controls when the threat model warrants them. If a source, license, or integrity signal cannot be established, mark it unknown and do not present the dependency as approved.

## Security and privacy review

Map assets, actors, trust boundaries, entry points, data flows, privileges, and plausible misuse for the changed surface. Prioritize user-controlled input, authorization, tenant isolation, deserialization, command/query construction, file paths, redirects/URLs, uploads, secrets, and output encoding. Verify permission checks at the owning boundary; hiding a UI control is not authorization.

Review collection, purpose, minimization, retention, deletion, export, encryption, access, and logging for personal or sensitive data. Keep secrets out of source, tests, screenshots, URLs, crash reports, and ordinary logs. Redact examples and preserve useful diagnostic context without exposing payloads. Apply project threat models and applicable security policies; do not claim legal or regulatory compliance from a checklist.

Test both allowed and denied paths, boundary values, malformed input, and cross-user/cross-tenant access where relevant. Report code-level findings separately from runtime penetration testing, formal audits, or compliance review that was not performed. Stop rather than probing systems without authorization.

## Observability and incident debugging

For an incident, preserve the timeline, affected versions, scope, symptoms, recent changes, and exact evidence source. Use the least sensitive relevant logs and traces. Correlate request, job, or transaction paths with stable IDs where possible; do not use personal data or secrets as identifiers. Separate user impact, confirmed cause, contributing factors, and unknowns.

Define signals around user-visible outcomes and service boundaries: errors, latency distributions, saturation/resource pressure, queue age, retries, and failed or stuck work as appropriate. Metrics need bounded-cardinality labels. Logs should be structured, actionable, access-controlled, and retained only as policy allows. Traces should preserve causal context while avoiding sensitive attributes.

Instrument only enough to answer an operational question. Check that dashboards, alerts, runbooks, and recovery actions correspond to the behavior changed. A metric name or emitted log line in source does not prove collection, alert delivery, or operational usefulness; verify the deployed path when authorized, otherwise mark runtime integration unverified.

## Performance and reliability

Translate a performance complaint into a measurable outcome, workload, device/runtime, environment, sample size, and acceptable budget. Record a comparable baseline before optimizing. Profile or measure the suspected bottleneck, change one meaningful variable at a time, and compare under the same conditions. Include variance and warm/cold effects where relevant; do not treat one noisy run as a win.

Bound queues, concurrency, payloads, memory, retries, and time. Use deadlines, cancellation, backoff with jitter, idempotent retry boundaries, and circuit breaking only where the failure model warrants them. Avoid retry storms and unbounded buffering. Verify cleanup across cancellation, process shutdown, navigation, backgrounding, and partial failure. Test overload and degraded dependencies where feasible.

Retain an optimization only when the improvement is meaningful and correctness is preserved. Report the measurement method and its limitations; source-level reasoning is not a benchmark.

## Release and deployment readiness

Establish the exact source revision, artifact identity, target environment, configuration source, rollout mechanism, health checks, and owner of the release. Validate production configuration without exposing secrets. Review migrations, feature flags, permissions, routes, assets, signing, supported platforms, and backward compatibility.

Use staged rollout, canaries, feature flags, or a maintenance window when the risk and infrastructure justify them. State measurable stop/rollback criteria and verify that the rollback path works for both code and data. Do not deploy, publish, tag, release, or alter production without the required explicit authorization. A successful local build is not proof that a release was deployed or healthy.

After deployment, verify the declared health signals and user-critical journeys when access and authorization permit. Record the revision, commands, environment, observations, and unresolved checks. If live verification is unavailable, deliver a release candidate with that boundary stated plainly.

## Architecture decisions

For a decision with meaningful long-term cost, write a short decision record: context and constraints; the decision; viable alternatives; consequences and trade-offs; security, accessibility, performance, operations, migration, and reversibility considerations; and triggers for revisiting it. Keep evidence and assumptions distinct. Prefer the least complex option that meets established constraints, not novelty or speculative scale.

Do not write a decision record for a trivial local change. Revisit a decision when new evidence violates a stated assumption, a constraint changes, or measured operational cost exceeds the threshold—not merely because another pattern is fashionable.

## Evidence and handoff

For each applied playbook, record: the question; inspected boundary; selected approach and alternatives rejected; exact checks and results; unverified assumptions; affected consumers; recovery/rollback path; and owner or next action if unfinished. Include dates and revisions for externally sourced, time-sensitive facts. If evidence is unavailable, narrow the claim rather than filling the gap with confidence.
