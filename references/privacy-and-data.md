# Privacy, tenant isolation, and logging

Load this module when a task handles personal data, support data, telemetry, logs, analytics, or multiple tenants/users.

Define the data purpose, minimum fields, sensitivity, tenant or user boundary, retention, deletion, export, access roles, storage, transport, and redaction rules before changing collection or logging. Verify authorization and isolation at the owning server or data boundary; filtering a UI is not tenant isolation. Do not use secrets, raw personal data, or high-cardinality identifiers as ordinary log fields.

Prefer stable non-sensitive correlation IDs, bounded-cardinality labels, structured logs, explicit redaction, and access-controlled retention. Test cross-tenant denial, malformed or missing identity, support access, export/deletion, and log redaction where relevant. Do not claim legal, regulatory, privacy, or compliance certification from a checklist. Report what was verified, what remains unknown, and who must approve retention or access decisions.
