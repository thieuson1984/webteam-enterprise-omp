# Acceptance Matrices — Test the Interaction, Not Just the Screenshot

This reference is an **example matrix generator**. Adapt to the actual product, usage and risk. `NOT_APPLICABLE` is valid; `NOT_RUN` is not `PASS`. QA owns actual execution evidence; Designer owns contract and visual intent; Frontend implements; Accessibility checks WCAG/APG expectations.

## Standard matrix for every complex component

| Dimension | Example acceptance question | Evidence |
|---|---|---|
| Core task | Can the user complete the intended action and tell whether it succeeded? | E2E test, API observation, manual task |
| Semantics | Is the appropriate native element or APG pattern actually implemented? | DOM/role inspection |
| Keyboard | Tab/Shift+Tab, Enter/Space, arrows, Escape, focus return where relevant? | Keyboard trace |
| Screen reader | Accessible name, state, error/recovery, announcement cadence understandable? | AT manual check when feasible |
| Touch | Are controls discoverable, non-hover-dependent and operable? | Touch/viewport test |
| Resize | Mobile, landscape, text reflow, zoom 200–400%; no hidden essential action? | Browser screenshots, geometry |
| States | Loading, empty, no-results, error, unauthorized, success, conflict, disabled? | Fixture/test coverage |
| Data | Correct source, permission scope, sort/filter on full result set, freshness? | Integration/contract tests |
| Resilience | Slow network, retry, cancel, duplicate actions, concurrency, offline as relevant? | Network/failure simulation |
| Design fidelity | Correct semantic tokens, type rhythm, density, visual alignment and approved Design DNA? | Actual screenshot comparison |
| Privacy/security | Sensitive data masked, auth enforced by backend, no fake trust signals? | Security/backend review |

## Contract A — searchable combobox
- Choose selection contract: free-text suggestion vs constrained select-only; committed choice vs highlighted candidate.
- Run tests: typing and IME composition, arrow navigation, Enter commit, Escape close/revert per contract, blur, clear, zero results, delayed server response, keyboard, AT label.
- Failure signals: custom select styled beautifully but no correct focus, screen-reader option state, or mobile behavior.

## Contract B — editable multi-select grid with filters
- Clarify semantic table versus `role=grid`; table alone for reading, grid only for application-style cell focus navigation.
- Test: column header association; sort direction announcement; select all **page** vs all **matching filtered records**; bulk permission and cancel; virtualization; pagination; long names and missing values; export actual subset.
- Failure signals: header clicks visually change arrows but not data; row checkboxes change across pages unexpectedly; hidden bulk action has no discoverable alternative.

## Contract C — create/edit wizard with unsaved changes
- Test: route enters with clean state; back/forward; invalid fields; error summary focus; save as draft only if truly available; session expiry; conflict from another editor; submit idempotency.
- Failure signals: next-step validation wipes previous entries; saved toast shown before server acknowledgement; exit loses content without warning.

## Contract D — modal confirmation of destructive action
- Test: opener keyboard focus; modal initial focus; Escape/cancel policy; labelled consequence; confirm loading/error/success; focus restored after close or relocated appropriately after deletion.
- Failure signals: backdrop click deletes; toast is only alert; no keyboard escape; invisible focus behind dialog.

## Contract E — calendar/time-range booking
- Test: locale/week start, start/end semantics, disabled dates, DST and user timezone, no-slot state, double-book conflict, alternative list/keyboard selection.
- Failure signals: visually marked available slot without authoritative confirmation; drag is the only way to reschedule.

## Contract F — file upload and preview
- Test: permission, type/size checks and user explanation, progress/retry/cancel, antivirus/scanning pending state, duplicate filename, limited preview fallback and accessible dropzone.
- Failure signals: preview implies uploaded or safe; 100% progress implies processed even though server scan pending.

## Contract G — dashboard KPI and chart
- Test: source and denominator; zero/negative/missing values; local time boundaries; chart data versus accompanying values; no fabricated activity.
- Failure signals: every card uses interchangeable gradient and meaningless trend arrow or hides the method of calculation.

## Contract H — auth/session and identity
- Test: sign-in/MFA/passkey flow if supported, recovery and expired link, autocomplete/password manager, safe error text, redirect-after-login, session-expiry recovery and logout server acknowledgement.
- Failure signals: login UI with decorative SSO action not wired to provider; logout only hides frontend view while session remains active.

## Contract I — notification and message center
- Test: unread/delivered distinction, keyboard reader/thread, content sanitization, delayed send, subscription/notification privacy and error recovery.
- Failure signals: notification list full of fictitious events or an inaccessible “mark all as read” control.

## Contract J — responsive mobile navigation
- Test: open/close, focus trap only when appropriate, back navigation, selected route indication, narrow text, overlay keyboard behavior, 200–400% zoom, sticky controls not obscuring focus.
- Failure signals: desktop sidebar simply scaled to 320 px, core actions pushed offscreen, hidden overflow menus that do not work with touch.

## Audit/report contract
Each finding MUST include `ID | page/route/component | observed actual evidence | expected job/behavior | severity | objective vs subjective | design approval requirements | repair owner | verification command/status`. Never substitute an AI-generated numerical design score for observed errors, accessibility evidence or human aesthetic review.
