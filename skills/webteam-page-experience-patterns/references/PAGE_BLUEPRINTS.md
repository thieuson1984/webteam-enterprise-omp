# Page Experience Blueprints — purpose before style

Use only the section relevant to the current feature. These are **decision checklists**, not mandatory templates, exhaustive feature requirements, or authority to implement business functionality. A page may combine multiple patterns. Existing approved Design DNA and actual product requirements take precedence. Where a requested category is not used by the product, mark `NOT_APPLICABLE`, not a defect.

## Core choices for every page
- **Job:** the user's decision, frequency, risk, skill level and device; state why a page exists rather than repeating an industry template.
- **Reading order:** first meaningful content, one prominent next action when warranted, contextual secondary operations; preserve scannability in dense products.
- **Truth:** field/data source, units and currency, freshness timestamps/time zone, ownership, permission scope, long and missing values.
- **Structure:** layout fit, density modes, responsive re-prioritization, blank/partial/full states, navigation and scroll restoration.
- **Feedback:** action initiation, waiting/progress, success, failure, conflict, offline/retry, cancellation/undo and irreversible steps.
- **Audit evidence:** actual route/component, viewport, fixture, screenshot or code location, state observed, keyboard trace and test status.

## P01 — Search, discovery, filtered results
**Job:** efficiently find an entity, document, person or item and know which results are relevant.
- Structure: query with visible label, result summary/count, meaningfully ordered filters/facets, sort, result list/table/card selection by content, clear/undo filter, pagination or justified incremental loading.
- State: initial, typing, debounced loading, no initial records, zero matching results (different copy), stale results, server failure, no access, saved filter, previous query URL/restoration.
- Precision: define match semantics, filters applied to entire dataset, total/result count provenance, timestamps, highlighted snippet semantics; no fictional hits or deceptive rank.
- Accessibility: form submit via Enter, clear focus behavior, result-count announcement without chatter, meaningful headings, keyboard-safe filter popover, link to result.
- Mobile: collapsible facet panel with applied-filter chips and visible result count; do not bury all filtering behind ambiguous icon.
- Tests: query with diacritics/Vietnamese, long queries, multi-facet combinations, zero results, keyboard and back/forward state preservation.

## P02 — Entity/record detail, 360° profile, master–detail
**Job:** understand identity/status/history and choose the correct next action.
- Structure: unambiguous title and identifiers, status+last updated, primary action, summary or facts, meaningful related objects, change history and contextual tabs when content warrants.
- State: missing/deleted, forbidden/partial access, stale/deferred sections, concurrently edited, archived, sensitive/redacted fields, unsaved local changes.
- Interaction: link back to filtered collection, preserve selection/scroll, avoid destructive action beside harmless navigation, show action result in context.
- Mobile: collapse secondary metadata; avoid unusable side panels; maintain return path.
- Tests: record switching, large values, cross-tenant access and unauthorized action omissions verified server-side by Backend/Security.

## P03 — Create/edit forms and multi-step wizards
**Job:** enter correct data without losing work or being punished for errors.
- Structure: clear page intent; logically chunked fieldsets; visible labels and examples; conditional fields explained; summary/confirmation for consequential submissions.
- State: pristine, touched invalid, loading/validating, server conflict, draft, autosaved vs unsaved, expired session, successful submission, partial/retry.
- Interaction: clear save/cancel/back semantics; preserve values when stepping back; recover after error; optional draft/resume only if backend supports it.
- Accessibility: error summary linked to specific fields, reliable focus after submit, keyboard-safe date/combobox/upload inputs, no placeholder-as-label.
- Mobile: native keyboards by `inputmode`, show units, large targets; do not require a horizontal wizard stepper.
- Tests: duplicate submit, slow network, optional fields, long locale strings, cancel with unsaved changes and cross-step validation.

## P04 — First-run onboarding, activation, invitations and workspace selection
**Job:** accomplish a first meaningful task, not fill an ornamental walkthrough.
- Structure: concise benefit/setup checklist, optional versus blocking tasks, invite role explanation, workspace/tenant context, “skip for now” where legitimate.
- State: accepted/expired invite, existing account, no permissions, resumed progress, partially configured workspace, help and retry.
- Interaction: handoff after SSO/MFA or invite acceptance without losing context; safe tenant switch visibility.
- Mobile: short achievable steps; avoid tutorial carousels hiding essential setup.
- Tests: fresh account, invited account, multi-org membership, expired links and a user returning halfway through.

## P05 — Organization admin, permissions, roles and member management
**Job:** safely assign rights and understand their consequences.
- Structure: member/role inventory, explicit scope, effective permissions, role definitions, sensitive action confirmations, invitation states.
- State: pending invitation, revoked role, last administrator, inherited role, permission denied, conflict with another admin, audit trail.
- Interaction: require confirmation for high-impact access; distinguish proposed from saved rights; never imply UI hides are backend enforcement.
- Accessibility: matrix/checklist with comprehensible row/column labels and keyboard access, not color-only permission grid.
- Tests: authorized vs unauthorized operation, last-admin protection, cross-workspace/tenant containment; involve Security/Backend.

## P06 — Approval queues, case handling and operational workflows
**Job:** review evidence, make a defensible decision, and see state transition.
- Structure: priority/age and SLA if real, assignment, case identity, evidence/provenance, escalation, decision actions, chronological activity.
- State: unassigned, blocked, partial documentation, conflict, reassignment, withdrawn, rejected, approved, expired, retried.
- Interaction: review-before-approve, reason capture, high-risk confirmation, no silent bulk approval, optimistic state only with rollback.
- Mobile: action panels cannot hide deciding evidence; maintain queue-return context.
- Tests: race where two reviewers act, permission changes mid-flow, auditability, cancellation and idempotent submissions.

## P07 — Calendar, timetable, bookings and resource scheduling
**Job:** see availability accurately and book/reschedule without conflict.
- Structure: day/week/month/list choice appropriate to task, timezone and week-start, resource capacity, recurrence, conflicts, explicit start/end.
- State: no availability, DST ambiguity, past slot, overlap, recurrence exception, tentative vs confirmed, cancellation, offline.
- Interaction: never imply a tentative hold is confirmed; avoid color-only status and drag-only scheduling.
- Mobile: agenda/list alternative; accessible non-drag entry and rescheduling.
- Tests: DST and timezone conversion, multi-resource overlaps, permissions, keyboard-only create/edit and recurring exceptions.

## P08 — Inbox, messaging, notifications and activity feeds
**Job:** triage events, reply, find the source of a notification and avoid losing context.
- Structure: unread/priority and subject, sender identity, timestamp, filters, thread or timeline, destination and contextual actions.
- State: muted, unread, delivered/failed/queued, attachments blocked, deleted thread, permissions changed, offline composition.
- Interaction: read receipt and undo semantics, accessible toast/announcement, no unrequested cross-channel notifications.
- Mobile: responsive thread/detail navigation; preserve draft and return position.
- Tests: long messages, mention filtering, time zone, delayed delivery, malicious HTML/attachments and keyboard shortcuts where documented.

## P09 — File/document library, uploads, previews and versions
**Job:** locate, view, share and modify a file without damaging content or privacy.
- Structure: filename/type/size/owner/modification timestamp, list-grid toggle only if useful, search/filter, upload, preview/version/sharing context.
- State: upload progress, quota, unsupported type, scanning pending, interrupted upload, version conflict, locked file, removed access, empty folder.
- Interaction: distinguish upload succeeded vs pending processing; preview fallback; careful drag/drop targets, keyboard alternative, explicit delete/share intent.
- Security: show access scope and external sharing; backend handles antivirus/scanning, signed URLs, quotas, content policy.
- Tests: duplicate filenames, large file, network interruption, invalid MIME, permissions and long localized names.

## P10 — Analytics, reports, drill-down and exports
**Job:** interpret a trustworthy measure and act with appropriate uncertainty.
- Structure: question-first headline, filter/time range, units and denominator, source and last refreshed, comparisons only when valid, charts connected to source table/details.
- State: no data, sparse periods, partially available metrics, delayed refresh, permission-filtered totals, export generating/failing.
- Interaction: meaningful legend/color alternatives, chart keyboard/table fallback, accessible tooltip, clear drill-down and export scope.
- Mobile: retain key values/context; charts may simplify, never hide crucial denominators or exact values.
- Tests: zero/negative/extreme values, time zone/date boundary, aggregate mismatch, uncertainty notes and format correctness.

## P11 — Content management, rich editors and publishing
**Job:** draft, preview, collaborate and publish intended content safely.
- Structure: content hierarchy, editorial status, author, preview, revision history, scheduled vs published, SEO/metadata if required.
- State: autosave lag, conflict, unsaved changes, validation errors, failed asset upload, scheduled publication, rollback.
- Interaction: keyboard editor and toolbar discoverability, reliable undo, save/publish separation, meaningful revision diffs.
- Security: XSS-safe rendering; no rich-editor content treated as trusted instructions.
- Tests: copy/paste, inline links, headings, images alt text, keyboard actions, HTML sanitization and concurrent edits.

## P12 — Product/catalogue, checkout, subscriptions and billing
**Job:** compare options, understand total cost and complete a transaction with confidence.
- Structure: clear price units, tax/fees/shipping/renewal, plan comparison by consequential differences, line-item summary and accessible payment errors.
- State: out of stock, unavailable region, promotion expired, payment declined, invoice pending, failed renewal, trial ending, refund/dispute.
- Interaction: explicit recurring terms and consent, irreversible/costly actions confirm, no dark-pattern opt-ins, accurate refund/cancel path.
- Security: payment sensitive data never handled insecurely in UI state; backend is financial truth; meet relevant legal/payment obligations.
- Tests: locale/currency, double-charge prevention (backend), failure/retry and responsive forms.

## P13 — API/developer portal, integration setup and secrets
**Job:** safely connect a system and debug integration health.
- Structure: prerequisites, credential scope/expiry, copy-once secret affordance, endpoint examples, rate limits and status, logs with redaction.
- State: invalid credentials, revoked key, expired token, webhook failure/retry, partial verification, disconnected connection.
- Interaction: no hardcoded sample secrets, masked displays, explicit destructive revoke, sensitive copy behavior, test mode versus production label.
- Tests: role-scoped secret visibility, failures, keyboard copy buttons, redacted logs; Security/Integration own truth.

## P14 — AI-assisted/copilot/chat and human review
**Job:** draft/interpret content with verifiable context and retain human agency.
- Structure: task-specific input, origin of suggestions, sources if available, confidence/uncertainty wording, editable draft, review/apply/undo controls.
- State: running, partial streaming, stale context, no grounded answer, policy refusal, failure, hallucination dispute, cancelled generation.
- Interaction: clearly mark AI-generated vs authoritative product data; require review for consequential edits; never auto-publish/execute high-risk action.
- Privacy: show data-sharing or retention choices when relevant; no secret-bearing prompts in shared logs.
- Tests: malformed output, slow stream, blocked tool, keyboard announcement noise, undo and source validity.

## P15 — Map, geospatial and location-based experiences
**Job:** find an item in space, inspect details and navigate alternatives.
- Structure: labeled map plus equivalent searchable list/table; scale/legend, geographic bounds, address precision and accessibility fallback.
- State: location denied, weak GPS, missing coordinates, stale geodata, clustered markers, unavailable map tiles, offline.
- Interaction: no invented pins, navigation avoids map-only actions, keyboard-accessible result list and text alternatives.
- Tests: accessible list parity, zoom/reflow, touch gestures and permissions.

## P16 — Knowledge center, help/support, documentation, feedback
**Job:** resolve a question and find a legitimate escalation path.
- Structure: task-oriented navigation, article recency/owner, anchored sections, related content, contact/support and feedback utility.
- State: empty search, outdated article, service unavailable, no matching rights, draft saved, support request pending.
- Interaction: usable in-page links and headings, code-copy state, avoid fake human live-chat availability.
- Tests: external link behavior, accessible anchors, long code blocks on mobile and language fallback.

## P17 — Kanban, boards, task/planning and collaborative workspaces
**Job:** inspect ownership, status, dependencies and safely change assignment/state.
- Structure: actual grouping model, clear priority/status, task counts, filters, board↔list parity, detail drawer/page.
- State: archived, blocked dependency, stale record, concurrent edit, drag cancellation, no permission, large board.
- Interaction: do not make drag-and-drop mandatory; include keyboard/menu move alternatives, undo and explicit server sync status.
- Tests: focus after move, status consistency across board/list, high item counts, touch and concurrent edits.

## P18 — System-state pages: 401/403/404/409/429/500, offline and maintenance
**Job:** understand why the journey cannot proceed and recover appropriately.
- Structure: clear problem label (without internal secrets), retained app/site identity, one useful recovery action and support route.
- State: expired session, no permission, missing item, conflict, throttling, downtime, offline, unsaved work.
- Interaction: do not mislead into repeated submissions, preserve safe user state, show retry only when viable.
- Tests: direct deep-link, unknown route, network toggling, localization and keyboard return path.

## P19 — Mobile-first/adaptive workspaces and split-view experiences
**Job:** preserve key workflows across desktop and mobile without hiding capabilities.
- Structure: intentional desktop sidebar, mobile primary navigation, detail drill-in, suitable touch surfaces, persistent task location.
- State: keyboard open, rotation, reduced viewport, large text, zoom to 400%, split-pane absent, offline.
- Interaction: scroll/focus restoration and responsive overlays, sticky bars must not cover focused controls.
- Tests: device emulation and at least one real small viewport, 200/400% zoom and text-size expansion.

## P20 — Sector-specific pages (education, health, finance, government, operations)
**Job:** respect domain semantics and the user's real decisions; never force a generic SaaS template.
- Examples: education attendance/gradebook/timetable/inventory; health appointment/clinical documentation; finance reconciliation/ledger/approval; government application/case tracking; operations alert/incident/dispatch.
- Identify mandatory domain invariants with Product/Architect/Security. Do **not** infer legal/compliance status or regulatory requirements purely from UI appearance.
- Use specialized data types, status meaning, role constraints, traceability and audit logs; determine applicable local laws with qualified review when necessary.
- Test sensitive data handling, high-consequence confirmation and clear human accountability.

## P21 — Comparison, pricing, decision and selection pages
**Job:** choose between meaningful alternatives without manipulative defaults.
- Structure: decisive comparable attributes, limits, total cost/terms if applicable, pros/cons, transparent missing features, one coherent selection path.
- State: option unavailable, capability varies by plan, stale quote, selected item incompatible, partial data.
- Accessibility: proper comparison table with responsive alternative; no color-only differentiation.
- Tests: long feature labels, two vs many options, keyboard comparison and mobile scanning.

## P22 — Audit/history, incidents and observability consoles
**Job:** reconstruct what happened and decide what needs attention.
- Structure: trustworthy chronology, actor, scope, event type, source/correlation IDs as allowed, filtering, retention boundaries, sensitive redaction.
- State: delayed event ingestion, duplicate signals, partial outages, incident active/resolved, retention expiration.
- Interaction: distinguish a visual alert from an actual monitored/acknowledged event, avoid fake realtime animations.
- Tests: data provenance, time-zone ordering, accessible statuses, large event volumes and permission constraints.

## Evidence-oriented page review example
For `/cases/:id`:

| Concern | Minimum evidence |
|---|---|
| Primary job | Reviewer identifies case and can approve/reject only when authorized |
| Page structure | Identity/status, evidence, decision rationale and chronology visible without ambiguous cards |
| Data fidelity | Actual backend case status + timestamp origin + declared permissions |
| Critical states | Loading, incomplete evidence, conflict, unauthorized, action pending, resolved |
| A11y | Keyboard decision path, focus return after dialog, error summary/announcement |
| Responsive | Evidence before irreversible decision even on narrow viewport |
| Tests | Approve, reject, duplicate click, concurrent update, no-rights user |

No screenshot, style rubric, or persona alone proves these checks passed; record actual execution separately.
