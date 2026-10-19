# Performance capability blueprints — practical selection catalog

Select a **single relevant** entry rather than loading the entire document. Each entry applies conditionally; identify `NOT_APPLICABLE` features. Baseline and evidence must be real. The table and skills are reference artifacts, not automatically executed tools.

**Source standards (verify applicability and versions):**
- [Web Vitals](https://web.dev/articles/vitals)
- [React Compiler](https://react.dev/learn/react-compiler/introduction)
- [OpenTelemetry JavaScript status](https://opentelemetry.io/docs/languages/js/)
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## PERF01 — Real-user monitoring, Web Vitals and performance budgets
- **Trigger:** loading/interactivity regressions, UX goals.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Define critical journeys, device/network cohorts, lab/field distinction, sample size, p75 segments and privacy.
- **Contract/design:** Use LCP≤2.5s, INP≤200ms, CLS≤0.1 as current web.dev good CWV reference thresholds; select project budgets with baseline.
- **Bounded change:** Segment route, device, geography and cohort; account for caching and seasonal traffic before claiming improvement.
- **Verification including negative cases:** Compare before/after field data where available and reproducible lab checks otherwise, labeling source.
- **Evidence to hand off:** CWV budget sheet, cohort dashboard, measurement protocol and uncertainty.
- **Reject:** Claiming Lighthouse scores are real-user metrics, relying on averages, assigning invented baselines.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF02 — Rendering, animation and interaction latency profiling
- **Trigger:** slow input, long task, re-render spikes.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Capture interaction trace at representative device; locate event→JS→style/layout→paint critical path.
- **Contract/design:** Analyze DOM complexity, layout thrash, compositing, virtual lists, event listener scope and commit timing.
- **Bounded change:** Fix root cause conservatively; protect focus, reduced-motion, responsive and functional behavior.
- **Verification including negative cases:** Compare INP/profile trace + accessible interaction tests under same conditions.
- **Evidence to hand off:** Trace slices, root cause, code diff and functional/UX regressions.
- **Reject:** Turning off a11y behavior for speed, will-change everywhere, speculative React memo.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF03 — Critical rendering path, media, font and LCP engineering
- **Trigger:** slow route first load, hero, font FOIT.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Find actual LCP element and network request waterfall on mobile/desktop; distinguish TTFB/load/render delay.
- **Contract/design:** Prioritize genuine critical resources, image formats/sizes and responsive srcsets; measure preloads and font strategies.
- **Bounded change:** Use caching priorities and route-specific lazy loading without hiding key content from crawlers/users.
- **Verification including negative cases:** Collect reproducible throttled waterfall and layout-shift evidence after change.
- **Evidence to hand off:** Resource priority map, LCP cause attribution, visual QA results.
- **Reject:** Preloading everything, lazy-loading LCP, removing content to improve metric.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF04 — Bundling, HTTP delivery and CDN cache policy
- **Trigger:** JS bundle size, delivery, cache invalidation.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Audit real route chunks, unused packages, module duplication and critical CSS/font/image bytes.
- **Contract/design:** Compare code splitting and modern build output; design content hashing, immutable asset cache and HTML freshness.
- **Bounded change:** Coordinate CDN/cache-control with Security (privacy) and Backend (personalized content), preserve rollout/rollback.
- **Verification including negative cases:** Record transfer/execution size and cold/warm repeat loads with same configuration.
- **Evidence to hand off:** Bundle analysis, cache matrix and verified rollback.
- **Reject:** Caching private responses publicly, eager import explosion, regression from over-splitting.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF05 — Client CPU, memory, long-task and lifecycle optimization
- **Trigger:** long-running SPA, tabs, realtime updates.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Profile heap growth, detached DOM, timers, subscriptions, worker memory and retained closures.
- **Contract/design:** Bound watchers/polling, cancel obsolete requests, cleanup listeners, use virtualization only with proven need.
- **Bounded change:** Protect background tab and mobile battery, prevent runaway rendering and rehydration loops.
- **Verification including negative cases:** Compare heap timelines and interaction traces across repeated navigation flows.
- **Evidence to hand off:** Leak reproduction, memory budget and regression tests.
- **Reject:** Shifting expensive work to client worker without budget, hiding leaked timers in tests.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF06 — Service latency, throughput, queues and API hot-path tuning
- **Trigger:** p95/p99 HTTP latency, timeouts, node CPU.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Instrument end-to-end request path with trace correlation and safe cardinality; capture throughput, errors and saturation.
- **Contract/design:** Break down gateway/auth/serialization/network/DB/external time; consider N+1, payload compression and pagination.
- **Bounded change:** Optimize only measured hot path and preserve authz and semantics; introduce concurrency limits where needed.
- **Verification including negative cases:** Benchmark identical load, capture p50/p95/p99, error rates and CPU/memory before/after.
- **Evidence to hand off:** Latency budget breakdown, bottleneck and load-test evidence.
- **Reject:** Caching authorization away, claiming p99 from insufficient samples, optimizing wrong endpoint.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF07 — Database workload and query plan performance
- **Trigger:** slow query, locking, DB pools, tenant hotspot.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Select real or synthetic representative query patterns with cardinality, selectivity and safe EXPLAIN plans.
- **Contract/design:** Inspect indexes, scans, joins, transactions, lock wait, pool contention and query fan-out.
- **Bounded change:** Propose schema/index changes only with Database approval and migration/rollback plans; use engine-specific choices.
- **Verification including negative cases:** Measure representative distribution including writes and failure modes, not one happy query.
- **Evidence to hand off:** Plan comparison, DB metrics, data-consistency validation.
- **Reject:** Index every column, query plan from toy dataset, modifying production schema automatically.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF08 — Load, stress, soak and capacity engineering
- **Trigger:** expected peak, launch, scalability, overload.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Define realistic traffic and transactions with percentile objectives, test environment size and dependency limits.
- **Contract/design:** Choose steady load, burst, stress, soak and concurrency tests proportionate to risk; bound traffic and cost.
- **Bounded change:** Track latency/errors/saturation, DB pools, queue depth, memory and external service quotas.
- **Verification including negative cases:** Verify threshold breaches, recovery and autoscaling using controlled non-production environment.
- **Evidence to hand off:** Load profile, saturation threshold, capacity assumptions, rollback trigger.
- **Reject:** DDoS-like tests without approval, default localhost metrics claimed as production capacity.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF09 — Async queue latency, backpressure and distributed workflow tuning
- **Trigger:** jobs, webhooks, outbox, event-driven system.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Map enqueue→wait→attempt→dependency→completion, lag distribution and retry/dead-letter rates.
- **Contract/design:** Tune concurrency and retry/backoff by downstream quota, dedupe semantics and business delivery deadlines.
- **Bounded change:** Model poison messages, outage recovery, bursts and eventual consistency; protect correctness above throughput.
- **Verification including negative cases:** Measure queue lag and end-to-end completion under authorized failure tests.
- **Evidence to hand off:** Queue SLI, concurrency budget, failure recovery tests.
- **Reject:** Unbounded retries or concurrency, measuring handler duration instead of user completion.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF10 — Cache strategy, invalidation and privacy consistency
- **Trigger:** expensive reads, CDN, Redis, client cache.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Classify data freshness, security sensitivity, tenant scoping, cache key dimensions and invalidation triggers.
- **Contract/design:** Compare read-through, write-through, TTL, stale-while-revalidate only against requirements; design stampede protection.
- **Bounded change:** Verify purge/invalidation, session logout/tenant switch, authorization updates and partial outage consistency.
- **Verification including negative cases:** Measure hit rate, tail latency, stale-data incidents and cache cost.
- **Evidence to hand off:** Cache contract, tenant tests, cold/warm benchmark and rollback.
- **Reject:** Cross-tenant keys, caching sensitive responses in public edge cache, TTL as correctness substitute.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF11 — Observability and performance profiling evidence
- **Trigger:** telemetry gaps, tail latency, performance investigations.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Define high-value SLIs, trace spans, metric dimensions and data sensitivity; avoid high-cardinality identifiers.
- **Contract/design:** Instrument end-to-end behavior with supported OpenTelemetry SDKs or project stack; browser OTel status must be verified.
- **Bounded change:** Tune sampling, dashboards and exemplars, correlate metrics/traces/logs only with appropriate redaction.
- **Verification including negative cases:** Validate real data capture, minimal overhead and missing spans; never claim tracer available without runtime check.
- **Evidence to hand off:** Telemetry map, sample trace/metrics, overhead assessment.
- **Reject:** Instrument everything, collect PII, assume OTel browser experimental SDK production-stable.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF12 — Continuous performance gates and causal experiments
- **Trigger:** CI budgets, release regression, experiment.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Define comparable baseline by commit, fixture, device, warm/cold cache, repeat count and test condition.
- **Contract/design:** Set warning/fail thresholds based on noise and business objectives; triage flakiness and unrelated environment changes.
- **Bounded change:** Apply one targeted remediation at a time; evaluate confidence and UX correctness after optimization.
- **Verification including negative cases:** Run regression checks and record actual before/after with artifact hashes and environment.
- **Evidence to hand off:** Perf evidence packet, CI gates, false-positive protocol.
- **Reject:** Gaming Lighthouse, asserting improvement from 1 run, tuning to synthetic metric only.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF13 — Performance SLO, capacity economics and scaling decisions
- **Trigger:** service sizing, architecture review, release planning.
- **Discovery question:** What existing behavior and user outcome proves this change is needed? Which real module, route, trust boundary or metric is impacted?
- **Analyze:** Choose user-facing SLOs, error budget, traffic forecast uncertainty and resource spending constraints.
- **Contract/design:** Review scaling options (vertical, caching, batching, DB pool, async) by measured workload and operational cost.
- **Bounded change:** Model saturation headroom, deployment reliability, carbon/compute cost where relevant and failure blast radius.
- **Verification including negative cases:** Present low-cost incremental plan, evidence requirements and stop/rollback conditions.
- **Evidence to hand off:** SLO proposal, capacity/cost tradeoffs, action priorities.
- **Reject:** Inventing traffic projections, buying infrastructure before profiling, breaking consistency for latency.
- **Partner/owner:** `webteam-performance` leads with conditional consultation from existing specialists; one writer per path. Escalate before irreversible or external side effects.

## PERF14 — Mobile thermal constraints
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Use realistic low-end device and background throttling profiles; avoid only desktop cold-load scores.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## PERF15 — Reporting/export workloads
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Measure memory and async completion of large exports without unlimited buffering.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## PERF16 — Search and pagination scalability
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Test realistic cardinality, cursor semantics and consistency under concurrent writes.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## PERF17 — Performance and reliability tension
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Compare p99/circuit breaker/backpressure tradeoffs, never optimize away retries/authorization.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

## PERF18 — Performance cost review
- **Applicability:** Only when the repository actually contains or requires this behavior.
- **Design/review focus:** Estimate CPU/memory/egress cost from verified billing/usage, do not invent savings.
- **Acceptance:** Record a project-specific measurable/observable goal, one functional or failure test, actual execution status and rollback condition. Cross-check Security and QA where relevant.

