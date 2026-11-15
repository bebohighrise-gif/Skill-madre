# Quality gates

Apply relevant gates and record command, result, and coverage. An unavailable gate is **unavailable**, never **passed**.

1. **Behavior:** acceptance criteria plus focused test or reproducible manual check.
2. **Regression:** baseline comparison and relevant existing tests.
3. **Code health:** formatter, linter, type checker, compiler/build, and static checks available in the project.
4. **Security/privacy:** validation, authorization, secrets, injection, unsafe deserialization, dependencies, logs, storage, transport, permissions, and exposure.
5. **UX/accessibility:** hierarchy, copy, loading/error/empty/success states, focus, keyboard/touch, contrast, semantics, localization, responsiveness, and reduced motion.
6. **Performance/reliability:** bounded CPU/memory/I/O, network calls, leaks, races, retries, timeouts, cancellation, offline recovery, and lifecycle cleanup.
7. **Release integrity:** package/install, configuration, routes/assets, migrations, signing assumptions, compatibility, clean checkout, rollback, final diff, and absence of secrets or temporary noise.

Use an evidence row when the task is material:

```text
Question | Evidence | Conclusion | Confidence | Remaining unknown | Next check
```
