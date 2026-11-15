# Software engineering lane

Before coding, identify the owning module, data flow, state transitions, contracts, dependencies, migration risk, platform differences, and test seam. Read local instructions, manifests, build/test configuration, and current status.

Use a failing or characterization test when behavior is testable. Implement the minimum fix at the producing boundary. Cover relevant success, empty, malformed, timeout, offline, retry, cancellation, permission, duplicate, race, lifecycle, migration, and rollback paths as applicable.

For dependencies, check existing capabilities, license, maintenance, compatibility, supply-chain risk, bundle impact, and reproducibility. Never silently upgrade unrelated packages.

For APIs and data, preserve compatibility by default. Identify all consumers, stage irreversible migrations, verify recovery, and separate local checks from production evidence. For performance, compare a measured baseline with a comparable post-change measurement.

For bugs, record expected/actual behavior, input, environment, logs, timing, and reproducibility. Classify the failure, fix the owning boundary, add a regression check, and recheck cancellation, permissions, retries, cleanup, and rollback.
