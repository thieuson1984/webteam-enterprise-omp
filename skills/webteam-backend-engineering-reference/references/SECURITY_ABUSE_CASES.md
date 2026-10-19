# Backend Security & Abuse Cases — explicit negative-path controls

## S1 — Model the boundary
Document actor, authentication method, audience, trusted issuer, tenant resolution, target object, authorization decision, downstream data store, sensitive output and logs for each operation. Classify endpoints into anonymous, authenticated self, organization member, tenant admin, platform admin and machine-to-machine as appropriate. Never invent roles; map from approved product policy.

## S2 — Authorization decision matrix
| Attack | Expected server behavior | Test proof |
|---|---|---|
| Horizontal ID swap: A requests B's object | Deny before query result disclosed; preserve nonenumeration policy | Same endpoint and method, two tenant IDs, adversarial object IDs |
| Property-level leakage (hidden salary, password hash) | Safe response schema and role-based field authorization | Compare role-specific JSON, including list/export/download paths |
| Mass assignment on PATCH/POST | Privileged attributes rejected or ignored per explicit policy | Send `tenantId`, `ownerId`, `isAdmin`, `status`, nested props |
| Cross-tenant search/filter aggregate | All query joins, summaries, caches and cursors scoped by tenant | Seed conflicting IDs; compare list/count and page 2 |
| Scope upgrade after revoked membership | Revocation policy enforced, caches/session lifetime bounded | Change membership mid-session; repeat access |
| Resource exhaustion | Enforce body/query/file size, rate/concurrency/cost caps | Test oversized and deeply nested payloads in fixture |
| Token confusion/forgery | Verify signature, issuer, audience, expiry, algorithm constraints | Wrong issuer/audience, expired, unexpected alg and key ID |
| CSRF for cookie-auth state change | Origin/CSRF controls appropriate to session strategy | Forged cross-site POST, cookie SameSite coverage |
| SSRF from import/webhook URL | Deny local, link-local, metadata and prohibited destinations, DNS rebinding/redirect | Fake DNS/redirect fixtures; no real internal probing |
| Webhook forgery/replay | Correct signed byte representation, replay window and event dedupe | Mutated payload/signature, old timestamp, duplicate event |
| File processing | Isolated quarantine, type validation, scan where necessary, permission checks | Polyglot/oversize fixture, unauthorized download |

## S3 — Identity and session design
- Choose secure trusted identity: server-side sessions with secure/HttpOnly/SameSite cookies (with contextual CSRF design), or bearer/OIDC with appropriate audience and scope; never require JWT because it is trendy.
- OAuth flows: use PKCE where applicable and RFC 9700 BCP guidance; validate redirect URIs, state, issuer, nonce (OIDC as applicable), token storage and logout/revocation semantics. Do not manually implement cryptographic token validation from scratch when audited providers/libraries suffice.
- Differentiate 401 vs 403 without disclosing resource existence; require MFA/step-up for specifically high-impact actions based on product policy.
- Hash passwords only with supported password-hashing algorithms/parameters appropriate to environment; enforce reset and recovery anti-enumeration and rate-limit.

## S4 — Sensitive data, logging and operations
- Treat secrets/config as runtime-injected. Prohibit raw Authorization/Cookie headers, passwords, OTP, private tokens, payment data and raw files in logs, traces, crash reports, metrics and analytics.
- Identify PII retention, subject access/export/deletion and backup retention based on actual legal/contract scope; never assert GDPR or sector compliance based only on a checklist.
- Threat-model CORS, cross-origin cookies, response cache keys, SSRF, session fixation, WebSocket origin/auth and admin API exposure.
- Verify OWASP ASVS **5.0.0** and API Security Top 10 (2023) as applicable; cite exact requirement numbers only after reading source; a prompt checklist is not a compliance certification.

## S5 — Risk handling
For each finding record `BE-SEC-###`, exploit precondition, affected asset, exact path, observed evidence, likelihood/impact separately, confidence, remediation and safe regression tests. Never assign invented CVSS scores. Human approvals for credential rotation, production auth changes and destructive account operations.

Sources: https://github.com/OWASP/ASVS · https://api-security.owasp.org/editions/2023/en/0x11-t10/ · https://www.rfc-editor.org/rfc/rfc9700.html
