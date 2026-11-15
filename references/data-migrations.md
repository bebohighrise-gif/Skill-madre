# Data and schema migrations

Load this module for persistent data formats, schemas, backfills, or destructive data operations.

Before mutation, establish current and target schema, data shape and volume, readers and writers, backup/restore capability, locking, downtime, and authorization. Prefer expand-migrate-contract when mixed application versions or rolling deployment are possible: add compatible structures, deploy readers/writers, backfill in bounded resumable batches, verify invariants, switch consumers, and remove obsolete structures later.

Specify idempotency, checkpoints, rate and lock limits, retries, observability, duplicate handling, null/default policy, integrity checks, and stop/resume behavior. Preserve original data until the new state is verified. Test empty, representative, large, malformed, interrupted, retried, and partially applied cases using fixtures or a disposable database. Code rollback is not automatically data rollback; include restore or forward-repair steps.
