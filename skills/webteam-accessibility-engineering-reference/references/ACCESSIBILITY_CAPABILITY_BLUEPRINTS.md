# Principal Accessibility and Inclusive Interaction Specialist — Capability Blueprints

Apply only to relevant product features; do not infer that unused domains exist. Each entry is a workflow, not proof of implementation.

## A01 — WCAG 2.2 AA Scoping and Assessment

**Activate when:** A digital product needs accessible release evidence.

**Workflow:** Map relevant WCAG criteria to page/component states and documented automated plus manual tests.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** No false claim of certification from automated scan.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A02 — Semantic Information Structure and Navigation

**Activate when:** Applications have multiple routes, landmarks, headings and nested navigation.

**Workflow:** Use native semantics, heading order, route/page title, skip links and meaningful content groups.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Primary content and navigation discoverable with assistive technology.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A03 — Keyboard and Focus Engineering

**Activate when:** Dialogs, menus and SPA navigation create focus bugs.

**Workflow:** Define Tab/Shift+Tab, Escape, focus entry/return, visible focus and logical reading order; avoid traps.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Core tasks can be completed keyboard-only.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A04 — ARIA Widget Interaction Patterns

**Activate when:** Combobox, tree, grid and tabs require complex interaction patterns.

**Workflow:** Follow applicable WAI-ARIA APG behavior; distinguish selected item, focus, active descendant and typeahead.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Keyboard and screen reader interactions match implemented pattern.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A05 — Accessible Data Tables, Grids and Charts

**Activate when:** Dense administrative data needs correct semantics and actionable summaries.

**Workflow:** Use HTML table by default, ARIA grid only when necessary; accessible headers, sort/filter, chart summaries and export.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Data relationships and actions remain clear with AT and keyboard.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A06 — Inclusive Forms, Validation and Authentication

**Activate when:** Complex validation and auth can block users.

**Workflow:** Associate labels/errors/help; manage error summary and focus; support password managers/autofill and accessible auth.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Errors are recoverable without visual-only cues.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A07 — Contrast, Text Spacing, Reflow and Zoom

**Activate when:** Theme, font, zoom or compact layout may obscure content.

**Workflow:** Test text/non-text contrast, 200–400% zoom where appropriate, spacing, responsive overflow, focus not obscured.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** No loss of task-critical information at target viewports.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A08 — Live Updates, Alerts and Dynamic Status

**Activate when:** Saves, searches, notifications and status changes need announcements.

**Workflow:** Choose appropriate polite/assertive live regions, dedupe messages, persist important status visually and semantically.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Changes are discoverable without disruptive announcement storms.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A09 — Touch, Mobile and Multi-input Accessibility

**Activate when:** Responsive apps must work across mouse, touch and keyboard.

**Workflow:** Check target size/spacing exceptions, gestures, hover alternatives and orientation/reflow.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Users can complete tasks with supported input modes.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A10 — Inclusive High-density Enterprise Workflows

**Activate when:** Frequent-action admin screens combine large data grids, dialogs, charts and long forms.

**Workflow:** Optimize logical task order, grouping, high zoom, shortcut discoverability, focus and error prevention with real workflow scenarios.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Dense UIs remain understandable and navigable without sensory or input exclusions.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A11 — Cognitive Accessibility and Error Prevention

**Activate when:** Dense actions, destructive operations and long forms create cognitive burden.

**Workflow:** Use clear language, progressive disclosure, confirmations proportional to risk, undo and consistent affordances.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Users can predict action outcome and recover from mistakes.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A12 — Localization, Language and Numeric Semantics

**Activate when:** Multilingual apps include Vietnamese labels, currency, dates, plurals and number formatting.

**Workflow:** Set language tags, date/time/unit formats, meaningful localized error descriptions and directional layout as needed.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** AT reads language correctly; content remains usable after localization.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## A13 — Assistive Technology Manual Test Matrix

**Activate when:** Automated scans miss real interaction defects.

**Workflow:** Record browser/OS/screen reader and interaction outcomes for priority journeys; include limitations if AT unavailable.

**Scenario contract:** identify actor, authorized actions, source of truth, input/output, error and recovery behavior. Capture observed evidence from the actual repository, not generic checklists.

**Representative tests:** successful path, invalid/boundary, unauthorized or cross-tenant, duplicate/retry, partial failure, concurrent or delayed behavior, empty content and accessibility where relevant. Mark exclusions N/A.

**Acceptance:** Manual evidence is reproducible and not falsely claimed.

**Evidence:** `path:line` or actual test/run output; state `OBSERVED`, `INFERRED`, `NOT_RUN`, or `BLOCKED` and identify next safe verification step.

## Cross-domain anti-patterns

- Treating a template workflow as the actual product requirement.
- Marking scanner, document, or prompt execution as proof tests passed.
- Performing production mutations to satisfy a command.
- Loading the entire blueprint catalog into one task rather than the relevant headings.
