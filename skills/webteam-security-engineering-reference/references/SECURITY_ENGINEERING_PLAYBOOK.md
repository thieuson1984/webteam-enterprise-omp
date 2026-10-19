# Security Engineering Playbook — production-grade decision and evidence

**Authoritative scope:** This is reusable technical guidance. It does not override project architecture, approved model/tool policies, or live OMP capabilities. Read the relevant subsection only. Separate `MEASURED`, `OBSERVED`, `INFERRED`, `NOT_RUN`, and `NOT_APPLICABLE`.

## Standards and evidence provenance

- [OWASP Top 10:2025](https://top10.owasp.org/2025/)
- [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS)
- [OWASP API Security Top 10:2023](https://api-security.owasp.org/editions/2023/en/0x11-t10/)
- [SLSA specification 1.2](https://slsa.dev/spec/v1.2/)
- [MDN Trusted Types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/require-trusted-types-for)

## Risk-based secure SDLC protocol

### Threat modeling worksheet

Describe actor→entrypoint→trust boundary→asset; data classification; required control; likely abuse; actual enforcement owner; negative case; evidence. Include user/browser, server/API, storage, provider callback, CI/CD and agent/MCP egress boundaries when applicable. Prioritize known external exposure and business impact; an architectural illustration is not proof the control exists.

### A verifiable authorization control

Take a real endpoint such as `GET /tenants/:tenantId/users/:userId`. Show how authentication claims establish active principal; resolve allowed tenant memberships **server-side**; enforce object/property/function policies after fetching/validating context; prevent cross-tenant cache/key leakage and unauthorized aggregate/export access. QA should run synthetic horizontal/vertical privilege tests. A button hidden in frontend is not an authorization barrier.

```text
DENY when anonymous / suspended / wrong tenant / missing role
DENY over-posted fields or forbidden mutation
DENY cross-tenant search/export/cache and websocket subscription
ALLOW only named capability with sufficient resource ownership
LOG privileged changes without raw credentials, tokens or PII
```

### Layered injection protection

Determine the output context and sink. Parameterized SQL/NoSQL filters, safe shell APIs, strict allowlisted URLs, vetted HTML sanitizers and contextual encoding each address different injection risks. Browser CSP/Trusted Types are defense in depth, with deployment/browser compatibility and reporting plan. Do not disable a protection for a test fixture without approval.

### Supply chain and delivery

Record actual dependency lock/source, SCA finding reachability, CI runner privileges, build provenance and rollback. SLSA v1.2 is a graduated target and cannot be claimed achieved without real build controls and provenance verification. Do not run package install scripts or network scans solely to audit.

### Safe security verification

Read-only source review first; run only authorized local tests. Avoid public target scanning, speculative credentials, brute force, damaging payloads, destructive file writes and live incident containment. A report must distinguish independently reproduced findings vs static indicators, and recommend independent validation for critical changes. Track residual risk approvals with explicit owner, deadline and expiry.

### Authority and safety boundary

Security is a reviewer and sometimes an implementation owner for authorized security-specific changes; it does not grant itself production permissions or regulatory certification. Coordinate fixes with domain code owners and independent QA. Never put exploit secrets or sensitive evidence in repository-visible Markdown.


## Reversible implementation workflow

1. Baseline real behavior / establish a precise gap and target outcome.
2. Record ownership, existing user changes, touched files, anticipated data/security effects and approvals.
3. Compare at least one simpler alternative and explicitly reject unnecessary infrastructure, tool purchases, new packages or frameworks.
4. Make the smallest authorized local change with a single implementation owner; avoid concurrent edits to shared files.
5. Run real tests, capture outputs, check privacy/accessibility/business semantics and compare objective before/after evidence.
6. Request independent QA/reviewer verification proportionate to risk; escalate unknowns, blocking approvals or production effects.
7. Report residual issues, updated contract/docs, evidence links and rollback. Never falsely label tests, scans, monitoring or deployments as completed.

## State and uncertainty labels

| Status | What it means |
|---|---|
| `OBSERVED` | Verified in source or direct tool output, with path/version or artifact ID |
| `MEASURED` | Actual run using documented environment, inputs and method |
| `INFERRED` | Reasoned hypothesis not yet independently demonstrated |
| `NOT_RUN` | Relevant test or measurement omitted, with explicit reason |
| `BLOCKED` | Missing tool/permission/environment/decision |
| `NOT_APPLICABLE` | Excluded because the real project has no such surface |

## Cross-agent handoff

Lead: `webteam-security`. Partners only when justified: webteam-architect (threat boundaries), webteam-backend and webteam-database (server-side enforcement), webteam-frontend (browser boundaries), webteam-devops (secrets/CI), webteam-qa (negative test evidence), webteam-reviewer (independent approval). No tool or reference grants production access; do not send project data to new providers without authorization.
