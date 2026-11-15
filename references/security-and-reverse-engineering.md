# Security and authorized reverse-engineering lane

Before testing, record the authority, owner, exact target, version or digest, environment, allowed actions, excluded actions, rate limits, data handling, stop conditions, and required evidence. Written authorization is required; a user request alone is not proof of authority over a third-party target.

Start with passive/static inspection and the smallest useful inventory. Test only within scope. Never bypass authentication, licensing, access controls, anti-tamper protections, vendor restrictions, or rate limits. Never use stolen keys or cracked tools. Stop if scope or ownership is unresolved.

Review identity and authorization, session cookies, password reset, secrets, injection, output encoding, CSRF, uploads, payments, HTTPS, rate limits, CORS, security headers, debug exposure, dependencies, logs, backups, permissions, and data minimization. Mark each item observed, not verified, or not applicable.

For reverse engineering, separate observations from inferences, corroborate important conclusions with a second evidence type when feasible, reconstruct only requested behavior, and document coverage limits. Do not turn a static guess into a runtime claim.
