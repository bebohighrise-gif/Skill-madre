# Software engineering lane

Before coding, identify the owning module, data flow, state transitions, contracts, dependencies, migration risk, platform differences, and test seam. Read local instructions, manifests, build/test configuration, and current status.

Load only the matching supporting playbook when the change crosses a boundary: `references/api-contracts.md` for APIs, `references/data-migrations.md` for persistent data, `references/dependencies-and-supply-chain.md` for dependencies, `references/observability-and-reliability.md` for operations or performance, and `references/architecture-and-release.md` for broad design or release work.

Use a failing or characterization test when behavior is testable. Implement the minimum fix at the producing boundary. Cover relevant success, empty, malformed, timeout, offline, retry, cancellation, permission, duplicate, race, lifecycle, migration, and rollback paths as applicable.

For dependencies, check existing capabilities, license, maintenance, compatibility, supply-chain risk, bundle impact, and reproducibility. Never silently upgrade unrelated packages.

For APIs and data, preserve compatibility by default. Identify all consumers, stage irreversible migrations, verify recovery, and separate local checks from production evidence. For performance, compare a measured baseline with a comparable post-change measurement.

For bugs, record expected/actual behavior, input, environment, logs, timing, and reproducibility. Classify the failure, fix the owning boundary, add a regression check, and recheck cancellation, permissions, retries, cleanup, and rollback.

**Test-first rule and exceptions.** Write the failing behavior test before the fix. Skip it only when the user explicitly allows it; label that as an exception, implement the minimum, and still run a green verification afterward. Confidence is not a reason to skip the test.

**Bounded parallel workers.** Use several workers only for independent dimensions (for example security, performance, UX, requirements). Give each a narrow scope and read-only default, run dependent steps in order, deduplicate overlapping findings by evidence, and wait for all workers before concluding.

**Automation that writes externally** (labels, comments, merges): default to read-only, scope permissions to the minimum, validate and buffer outputs, require an approval or policy gate for writes, and keep an audit trail and rollback.
