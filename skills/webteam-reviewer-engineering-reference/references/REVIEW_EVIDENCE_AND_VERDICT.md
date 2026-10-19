# Evidence, Findings and Verdict Contract

## Finding schema

Each actionable finding **REV-NNN** includes: severity (`BLOCKER`, `HIGH`, `MEDIUM`, `LOW`, `NIT`); confidence (`HIGH`, `MEDIUM`, `LOW`); kind (`OBSERVED`, `REPRODUCED`, `INFERRED`, `BLOCKED`); exact file/line or trace; condition and counterexample; expected vs actual; impact and affected actor/tenant; minimal remediation; responsible writer; acceptance test; reviewer/retest identity; residual risk.

Avoid claiming an inferred issue is exploited. Do not include secrets, raw private records or unnecessary source copies. Multiple tools agreeing is not independent proof when they used the same stale input.

## Gate statuses

- `PASS_VERIFIED`: covered changed risk, actual checks at exact revision, no unresolved blocker, independence established.
- `CHANGES_REQUESTED`: one or more reproducible actionable findings affect correctness or agreed quality gates.
- `BLOCKED`: mandatory evidence, permission, trusted source or independent approval is missing, or an unsafe side effect is unresolved.
- `UNVERIFIED`: insufficient testing/review coverage but no independently proven defect; cannot be advertised as release-ready.

`NIT` or unapproved subjective style preference is nonblocking. Blockers depend on real impact and risk, not aesthetic score or quantity. Quality gate inputs are advisory until the actual owner/human makes approval decisions.

## One-page review report

Metadata; change/base/head revisions; review scope and skipped paths; requirements; affected business flows; concrete findings with location; checks executed and statuses; CI/browser/contract evidence; security/data/compatibility decisions; residual risks; verdict; next action; reviewer independence declaration. Create uniquely named markdown under `docs/reviews/` or return in chat when write not approved.
