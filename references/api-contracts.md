# API and contract changes

Load this module for public APIs, SDKs, webhooks, plugins, or service boundaries.

Locate the actual schema, route, generated client, versioning policy, consumers, error model, authentication boundary, and compatibility tests. Define inputs, outputs, optionality, defaults, validation, ordering, idempotency, pagination, rate limits, timeouts, and failure semantics. Separate documented guarantees, observed behavior, assumptions, and unknowns.

Prefer additive evolution. For a breaking change, inventory consumers, propose a compatibility or deprecation path, define rollback or migration, and obtain required approval. Test valid, boundary, malformed, unauthorized, unavailable, duplicate/replayed, and rate-limited cases at the real contract boundary. A mock verifies only the behavior it models.

Review generated clients, documentation, telemetry, and errors together. Do not expose tokens, personal data, internal hostnames, or raw sensitive payloads in responses or logs.
