# Fastify + Node.js + TypeScript — current-runtime implementation guide

## F1 — Version and layering checks
- Inspect `node -v`, installed Fastify major, plugins, TS module configuration, lockfile and Node LTS support status; never auto-upgrade based on sample snippets. As of Oct 2026, Node 24 is LTS and Node 26 is Current (verify release status again at actual deployment).
- Preserve existing valid backend framework; these are **Fastify-specific** guidance only when project uses Fastify.
- Build typed modules around capabilities (`users`, `membership`, `reporting`), each exposing narrow routes, service policy and persistence adapter. Do not import Fastify request objects into core domain logic.

## F2 — Fastify plugin encapsulation
- `register()` creates encapsulated scopes by default: a child can inherit ancestor decorators/hooks; siblings are isolated. Ensure auth, tenant context, error handlers and serialization are registered at correct boundary.
- Verify handler lifecycle and `onRequest`, `preValidation`, `preHandler`, `onSend`, etc. A hook declared in one sibling is **not** a global security boundary.
- Do not mix `async` hooks with `done` callback. Avoid mutating shared request-scoped properties on global objects.

## F3 — Validation and response safety
- Fastify JSON Schema route schemas compile via Ajv and fast-json-stringify. **Treat schema definitions as trusted application code**, never accept user-supplied schemas into compiler.
- Request validation protects syntax, not object-level authorization or domain invariants. DB lookups do not belong in initial async Ajv validation; move them to suitable guarded service/preHandler code.
- Declare response schemas for protected routes to constrain serialized fields. Confirm both success and error status variants. A `passwordHash` missing only from frontend type does not prove it cannot leak.
- If using Zod, verify selected type-provider/compiler/serializer integration actually handles validation at runtime and produces contract/OpenAPI parity. Avoid drifting parallel schemas.

## F4 — Example route blueprint (pseudocode, not drop-in code)
1. `register(featurePlugin, { prefix: '/api/v1/...' })` under verified auth+tenant scope.
2. `route.schema` has `params`, `querystring`, `body` and `response` schemas as applicable.
3. `preHandler` authenticates and resolves trusted tenant; policy checks actor/action/resource.
4. Handler parses validated DTO, calls application service with explicit transaction/operation key, maps typed result to safe output DTO.
5. Global/scope-correct error handler emits RFC 9457-safe error, context ID and sanitized logs.
6. Instrument low-cardinality route template. Testing via `fastify.inject()` exercises denied/allowed paths and verifies JSON responses.

## F5 — Configuration and process lifecycle
- Validate environment variables/config at startup and fail safely. Secrets injected externally, never hard-coded. Make TLS/proxy-trust/CORS/cookie options explicit per deployment; use `trustProxy` only for a trusted proxy chain.
- Bound request body, header counts, timeouts, external fetch bytes, upload size, HTTP keep-alive/connection pools and worker concurrency according to actual traffic.
- Graceful shutdown: stop accepting requests, set readiness false, drain existing HTTP/workers within budget, flush telemetry/outbox safely; verify with signal tests in disposable environment.

## F6 — Fastify failure modes to detect
- No response schema on sensitive route.
- Privileged hook registered in sibling scope rather than ancestor.
- Throwing from custom validators instead of returning supported `{error}` shape.
- Compiling dynamically supplied JSON Schema.
- Awaiting DB queries in the initial validator.
- Conflicting plugin versions / unsupported Node runtime.

Sources: https://fastify.dev/docs/latest/Reference/Encapsulation/ · https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/ · https://fastify.dev/docs/latest/Reference/Hooks/ · https://nodejs.org/en/about/previous-releases
