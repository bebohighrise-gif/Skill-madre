# Evidence ledger template

Copy this template into a task when a change needs an auditable trail.

| Question | Evidence | Conclusion | Confidence | Remaining unknown |
|---|---|---|---|---|
|  |  |  |  |  |

## Seven-control record

- [ ] Behavior: observed result and acceptance criteria.
- [ ] Regression: baseline comparison and tests.
- [ ] Code health: format, lint, types, build, dependency checks.
- [ ] Security/privacy: threat surface, secrets, authorization, data handling.
- [ ] UX/UI/accessibility: states, keyboard/touch, contrast, motion, responsive layout.
- [ ] Performance/reliability: bounded work, cancellation, races, measurements if needed.
- [ ] Release integrity: packaging, config, clean diff, rollback.

## Evidence language

- **Observed:** direct file, command, test, measurement, URL, or tool result.
- **Derived:** mechanical consequence of observations.
- **Inferred:** hypothesis supported by evidence; include confidence.
- **Unknown:** not established; name the next useful check.
