# Ethical security and authorized reverse engineering

Sources reviewed: 2026-11-01. Standards, laws, third-party notices, REA behavior, and tool prerequisites may change; verify current versions for each engagement.

Use this reference only for systems, applications, networks, and artifacts the user owns or is explicitly authorized to assess. A skill, tool, local file, public URL, bug-bounty listing, or access credential does not by itself establish authority. When authority, target, permitted actions, or stop conditions are unclear, pause and ask; do not probe first and justify later.

This guide synthesizes public methodology from OWASP, NIST, Ghidra/Hex-Rays documentation, and the REA project in original wording. It is not legal advice, an authorization grant, a sandbox, or a substitute for a qualified security professional. Review source versions and local law for each engagement.

## Ethical security assessment

Before any active test, record the written authorization, approving owner, exact assets/accounts/environments, positive scope, exclusions, test window, allowed and prohibited techniques, rate/impact limits, third-party dependencies, data handling, emergency contact, and stop conditions. Confirm the authorization is still valid. Publicly exposed systems and adjacent hosts are out of scope unless named.

Map the application's assets, trust boundaries, data flows, identities, dependencies, plausible abuse cases, and controls. Select only tests that answer a stated security question. Use the applicable version of OWASP WSTG for test methods and ASVS for requirements; record the exact version/identifier because standards change. Run against a test or staging environment with synthetic accounts/data where possible. Keep default activity non-destructive, low-volume, and observable. Do not bypass controls, persist, exfiltrate, delete/alter real data, degrade service, or access private information to prove impact.

A finding should state the affected component, preconditions, safe reproducible steps, observed impact, evidence location, severity and rationale, mitigation, retest result, and residual uncertainty. Minimize and redact evidence; protect it with the engagement's access and retention rules. Report significant issues privately using the owner's disclosed process. Do not publish secrets, private binaries, raw customer data, or exploit details that enable harm. A lack of findings means only that no issue was observed within the tested scope and method.

## Authorized reverse engineering

### Gate and preserve

Obtain explicit authority over the exact artifact and purpose. Record owner/mandate, product and version, source or acquisition, cryptographic digest, platform/architecture, allowed and disallowed analyses, runtime boundaries, storage/retention, distribution limits, and stop/escalation contacts. Reconfirm if the artifact or scope changes.

Preserve an immutable master and work on a copy. Record hashes, timestamps with timezone, acquisition path, tools and versions, settings, transformations, operator, and evidence-file locations. Use a controlled project or disposable lab. Static inspection is preferred for initial inventory; dynamic execution requires additional explicit permission and containment. A VM or analysis framework reduces some risks but is not automatically a security sandbox. Treat an untrusted binary as code that may execute with the local provider's OS-user permissions. Do not use personal accounts, secrets, production data, or open network access in a dynamic lab; define resource and egress limits and a restore path.

### Evidence-led workflow

1. State the behavior or question to establish and the exact target. Separate observed facts, hypotheses, and unknowns.
2. Inventory and hash the artifact. Establish format, architecture, version/build, support files, and available analyzers. Record any unavailable or ambiguous capability rather than silently switching providers.
3. Begin with the smallest useful static view: metadata, sections/resources, imports/exports, symbols, strings, module relationships, entry points, and relevant references. Use decompiler or automated-analysis results as leads, not ground truth.
4. Form a falsifiable hypothesis about the relevant code path or state transition. Trace from entry/input through calls, state and dependencies to output. Keep addresses, symbols, source locations, or artifact offsets linked to each claim.
5. Use dynamic observation only when static evidence cannot answer the question and the authorization explicitly permits it. Execute only in the declared controlled environment, with bounded inputs and a stop condition. Capture the exact stimulus, version, environment, observed events, and known coverage gaps.
6. Corroborate consequential conclusions with another appropriate evidence type when feasible. Do not treat a single path, decompilation, screenshot, or successful run as proof of all behavior.
7. Reconstruct only the requested behavior. Write an independent implementation in the user's project, test its contract, compare observed behavior with the new implementation, and document intentional differences. Do not copy substantial protected code or assets.
8. Deliver the scope, artifact identity, evidence, conditions, method, confidence, alternatives, limitations, and next safe step. Preserve evidence integrity and remove temporary lab state according to the agreed retention policy.

## REA-inspired agent workflow

REA (Reverse Engineer Anything) is a separate public project/tool, not part of Madre and not required for this workflow. Its public README describes an agent calling an MCP server to inspect a target and trace relevant code; REA returns findings with evidence, and the agent asks follow-up questions, explains behavior, or implements and tests a comparable feature. Its CLI uses the same documented workflows. Apply these useful method-level ideas without assuming REA is installed or available:

- Ask a bounded behavior question, name the authorized local target, and choose the least invasive supported analysis.
- Inspect rather than guess. Use the analysis result to select the next question; trace only the relevant path, not every tool or module.
- Keep each conclusion linked to its evidence record and preserve the distinction between normalized findings, provider/raw output, and missing coverage when the interface exposes those concepts.
- Continue with targeted follow-up observations until acceptance criteria are evidenced or a material unknown remains. State provider/tool prerequisites and unverified facets.
- Use the reconstructed behavior to inform a separate design/implementation, then test that implementation against the observed contract.
- Prefer a saved summary or selected page of large analysis results over feeding a huge raw dossier into context; preserve a pointer and enough metadata to reopen the full evidence.

These points describe the README and documentation reviewed on 2026-11-01; REA evolves, and exact tools, providers, schemas, platform prerequisites, and evidence contracts must be checked in its current documentation before any integration. Do not install, configure, invoke, or update third-party analysis tools without the user's task scope and applicable authorization. Never imply that describing REA means the capability was used.

## Stop conditions

Stop before analysis if permission or target ownership cannot be established; before active/dynamic testing if it is not explicitly within scope; when the target appears to be a third party, production service, or shared environment not named by the authorization; when sensitive data or an unintended effect appears; when containment fails; or when a requested action would enable credential theft, persistence, evasion, unauthorized access, exfiltration, destructive changes, or bypass of access/licensing controls. Preserve minimal non-sensitive evidence and use the agreed escalation path.

## Sources reviewed

- OWASP Web Security Testing Guide, testing framework: https://wstg.owasp.org/latest/3-The_OWASP_Testing_Framework/0-The_OWASP_Web_Security_Testing_Framework
- OWASP ASVS: https://asvs.owasp.org/
- NIST SP 800-115, technical guide to security testing and assessment: https://csrc.nist.gov/pubs/sp/800/115/final
- PortSwigger Web Security Academy (learning labs): https://portswigger.net/web-security
- Ghidra official repository: https://github.com/NationalSecurityAgency/ghidra
- Ghidra introductory student guide: https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html
- Hex-Rays/IDA user guide: https://docs.hex-rays.com/user-guide
- REA public repository and README: https://github.com/morluto/rea
- REA MCP runtime contracts: https://github.com/morluto/rea/blob/main/docs/mcp-contracts.md
- REA CLI and Evidence guide: https://github.com/morluto/rea/blob/main/docs/cli.md
- REA security policy: https://github.com/morluto/rea/blob/main/SECURITY.md
- REA responsible-use disclaimer: https://github.com/morluto/rea/blob/main/DISCLAIMER.md
- REA license: https://github.com/morluto/rea/blob/main/LICENSE (REA-authored code states MIT; third-party components retain separate notices/licenses.)

Popularity or repository activity is a discovery signal only. REA's own disclaimer describes its lawful-use boundary, user responsibility, effects of runtime/device/network operations, uncertainty of generated analysis, third-party license limits, and non-endorsement. Review the current disclaimer and exact third-party notices before adopting any artifact.
