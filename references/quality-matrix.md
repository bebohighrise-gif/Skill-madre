# Quality matrix

Use this matrix to choose evidence instead of blindly running every possible command.

| Control | Minimum evidence | Stronger evidence when risk is high |
|---|---|---|
| Behavior | Focused test or reproducible manual check | Unit + integration/E2E against acceptance criteria |
| Regression | Existing relevant tests and diff review | Baseline comparison, contract tests, migration rehearsal |
| Code health | Formatter/linter/types/build available in the project | Static analysis, dependency audit, clean checkout build |
| Security/privacy | Boundary and secret review | Threat model, negative tests, SAST/dependency scan, permission review |
| UX/UI/accessibility | State and interaction review | Keyboard/touch/device matrix, screen reader, contrast and reduced motion checks |
| Performance/reliability | Bounded work, cleanup and timeout review | Representative measurements, profiling, offline/race/load tests |
| Release integrity | Package/config/install review | Reproducible build, signing/package verification, rollback rehearsal |

Record unavailable evidence explicitly. A visual screenshot does not prove accessibility; a passing unit test does not prove packaging; a successful build does not prove runtime behavior.
