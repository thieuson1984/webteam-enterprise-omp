# High-value failure scenarios

1. Concurrent edits: two writes both pass validation and one silently wins.
2. Cross-tenant ID: valid session reaches object belonging to another organization.
3. Commit-before-response: client retries after network failure and duplicates side effect.
4. Stale cache key: cached result crosses role or tenant boundary.
5. Contract drift: response omits field older client still requires.
6. Migration overlap: old instance writes data invalid for new schema.
7. Async duplicate/out-of-order delivery: webhook or queue event processed twice.
8. Empty/partial/error UI: screen hangs or hides data when one API fails.
9. Keyboard trap and lost focus after dialog/route transition.
10. PII in structured logs or diagnostic response.
11. Unbounded queries and N+1 under realistic record counts.
12. False-green tests due to mocks that bypass authorization or transaction paths.

Use only scenarios plausible in changed modules; require actual reachability checks. Do not fabricate a reproduction.
