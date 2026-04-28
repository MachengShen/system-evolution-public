# Security Policy

## Status

This repo is currently a public stub for the user-agency substrate's eventual public release. **The substrate code itself is not yet here**; it lives across various private repos and Macheng's local environment, pending consolidation into a clean public-ready monorepo.

When the substrate code lands here (or in a successor repo such as `MachengShen/user-agency-substrate`), this file will be updated with a full vulnerability disclosure policy. Until then, this is a placeholder per day-1 hygiene best practices.

## Reporting (interim)

If you have a security concern about anything Macheng's substrate touches — including this repo, related infrastructure (memory hub, chat server, fleet nodes), or the architectural design — please reach out via:

- Email: macshen93@gmail.com
- Subject prefix: `[security]`

Do **not** open public issues for security matters until a formal disclosure policy is in place.

## Scope (interim)

- The substrate handles user data, tools, browsers, credentials, payments, email, files
- This is recognized as a high-value attack surface
- Defense-in-depth is in progress (per-role tool scoping, scope isolation, sediment-grounding rule, memory-audit cron)
- Formal threat model + signed releases + audit logs + insurance are pending

## Response expectations

Best-effort reply within 5 business days. Macheng is one person + an agent stack — not a 24/7 security team.

## Why this file exists at v0

Per GPT Pro Bridge cross-model calibration 2026-04-28: agent substrates touching user data + tools + credentials are high-value attack surfaces. Day-1 SECURITY.md is hygiene, not premature optimization. Refer to `MachengShen/system-evolution-archive` `DOCTRINE.md` (private) for the full security-related caveats sedimented at architecture-v0.
