# Production Component Catalog — Behavior Before Decoration

**Selection rule:** Choose only components that serve an observed task. Reuse stable accessible primitives when appropriate; inventing a custom widget increases keyboard/screen-reader/security/test obligations. Each item below specifies the key *failure mode* to prevent. Component names are not implementation authorization or a requirement to install a UI library.

## A. Information architecture and navigation

### C01 Header/app shell/sidebar/mobile navigation
- Clear product and workspace identity; location/selection state; stable active route; responsive grouping; actionable account menu.
- For nested nav, preserve meaningful hierarchy and avoid six equal-weight primary sections.
- Test keyboard/mobile drawer focus return, zoom, permissions and screen-reader landmark names; do not use `menu` role for ordinary site navigation without correct menu-keyboard semantics.

### C02 Breadcrumbs, back links, in-page navigation
- Show genuine hierarchy (not full URL segments), current page, and predictable navigation; preserve filtered return context where useful.
- Use labelled `nav` landmark for breadcrumbs, `aria-current` on active link where appropriate.
- Test deep links, hidden intermediate items, narrow layouts and long names.

### C03 Tabs, segmented controls and accordions
- Tabs select peer views with one clear active state; segmented controls select a value/view mode; accordion discloses content. Do not interchange solely for appearance.
- Specify manual or automatic activation, focus behavior, linked content, lazy-load states, meaningful accessible names and initial selection.
- Test arrow keys and panel focus according to chosen APG pattern; long labels and nested disclosure.

### C04 Command palette, action menu and context menu
- Action discovery matters more than decorative search box. Group and label action verbs; show shortcuts only if they function.
- Provide escape/return focus and shortcut conflicts, disabled reasons, accessible search results, scope-sensitive permissions.
- Distinguish command execution from route navigation; dangerous actions require safeguards.

### C05 Navigation tree, split pane and resizable panels
- Prefer simple lists until hierarchy/side-by-side comparison is justified. Expose expand state, selected item and current path.
- Keyboard hierarchy navigation and accessible resize alternative; never force drag.
- Test deep nesting, long strings, no child items and responsive single-pane fallback.

## B. Forms, input and choices

### C06 Text field, textarea, search and inline validation
- Visible label; optional hint and required indication; explicit units/format; error anchored to field, not placeholder-only guidance.
- Support input methods/composition (including Vietnamese), autofill, paste, mobile keyboard and delayed server validation.
- Test empty, min/max, multiline, unicode, failed submit and loss-of-focus behavior.

### C07 Native select, listbox, combobox and autocomplete
- Native select for simple fixed options; custom combobox only for searchable/complex options. Define editable vs select-only, highlighted vs committed option.
- Specify expanded/listbox semantics, arrow/Enter/Escape behavior, suggestions unavailable, async search cancellation, creation of new option policy.
- Test IME composition, huge list, invalid/no matches, screen reader and mobile fallback. Follow WAI APG rather than generic ARIA hacks.

### C08 Checkbox, radio, switch, tri-state and segmented choices
- Radio = one of a set; checkbox = optional/multiple/tri-state; switch = immediate on/off *only when operation truly fits*.
- Explicit effect and persistence; do not use switch for actions requiring separate Save unless clearly explained.
- Test disabled rationale, indeterminate state, label click and color-independent checked status.

### C09 Date/time/date-range, timezone and recurrence picker
- Show human-readable formatting, validation, locale/first day of week and timezone; allow typed entry where appropriate.
- Handle start>end, blocked dates, ambiguous DST times, recurring exceptions and unavailable time slots.
- Calendar keyboard/focus behavior is complex: prefer verified implementation and APG examples; test screen-reader month/day announcements.

### C10 Number, currency, percentage, quantity, stepper and slider
- State units/currency and min/max/precision; use localized grouping and decimal formats.
- A slider is appropriate only when approximate selection matters; do not hide precise values or create inaccessible multi-thumb controls.
- Test keyboard increment semantics, boundary values, pasted text, rounding and server validation.

### C11 File input, dropzone, image/video uploader
- Click/keyboard selection alternative to drag/drop; allowed type/size/quantity, progress, upload vs processing, cancel/retry.
- Handle malware scanning/permission decisions in trusted backend; UI must not claim file safe solely because preview rendered.
- Test long filenames, invalid file, interrupt/resume, image alt/crop and inaccessible drop target.

### C12 Form field group, summary, stepper, OTP/code input
- Use logical fieldsets and sensible progressive disclosure; users must know where they are and what remains.
- One-time codes must support paste, password manager/autofill, resend timing and recovery; don't force segmented digits if one accessible input works better.
- Test submit success/failure, navigation back, error summary, lost focus and screen reader.

## C. Feedback, overlays and transient states

### C13 Button, icon button, link, split button and destructive action
- Button performs action; link navigates. Label specific verbs, distinguish hierarchy; icon-only actions need accessible names/visible affordance.
- Visual size/weight derived from information hierarchy; avoid huge pill buttons everywhere.
- All actions have loading, double-activation/idempotency, disabled reason, focus and outcome; destructive action needs confirmation proportional to consequence.

### C14 Dialog, alert dialog, drawer and bottom sheet
- Use modal only when focused interruption justified; non-modal drawer when context benefits from parallel reference.
- Define initial focus, focus trap where modal, Escape/backdrop policy, focus restoration, scroll lock and unsaved changes.
- Test dialog nesting avoidance, small screen, soft keyboard, responsive resizing and long form errors.

### C15 Tooltip, popover, hover card and contextual help
- Tooltips are supplementary, not the only route to essential information; touch/keyboard access needed.
- Popover requires focus/close behavior; do not use hover alone for destructive actions or keyboard shortcuts.
- Test clipped viewport edges, zoom, Escape, screen reader and mobile.

### C16 Alert/banner/inline status/toast/live region
- Choose persistent alert for consequences, inline field errors for corrections, optional toast for transient confirmation.
- Never use toast as sole evidence of critical success; announce asynchronous statuses without repetitive live-region spam.
- Test network failures, retry, close/undo, focus retention and non-color cues.

### C17 Loading skeleton, progress, empty state and retry surface
- Skeleton should preserve expected geometry without faux shimmer overload; progress should convey known vs unknown duration.
- Distinguish empty collection from no matching search, no rights, no connection and failed fetch; each needs a truthful next action.
- Test layout shift, delayed response, cancellation, reduced motion and screen-reader status.

### C18 Badge/tag/chip/avatar/status indicator
- Semantic distinction: selected filter chip, tag, status badge and button must look and behave differently.
- Initials/avatar fallbacks, high-contrast label, status meaning in words, responsive truncation with full accessible name.
- Test localization, color blindness, long statuses and unknown values.

## D. Dense data, visualization and navigation within data

### C19 Semantic table, sortable table and interactive data grid
- Prefer `<table>` for reading tabular data. Use `role=grid` only for application-like keyboard navigation with fully implemented roving focus.
- Define sorting persistence, column priorities, row identity, pagination vs virtualization, bulk selection scope (page/all filtered) and export accuracy.
- Test keyboard across action cells, screen-reader headers, dynamic counts, empty/partial data, 1,000+ rows and column overflow.

### C20 Filter toolbar, facets, active filter chips, saved views
- Filters reveal active criteria, change counts and offer clear/reset; avoid duplicated controls and hidden filter state.
- Define server/client semantics, debounce, loading, URL shareability and scoped saved view privacy.
- Test multi-filter combinations, back/forward, mobile panel and removed/inaccessible facets.

### C21 Cards, list items, definition lists and metadata panels
- Choose card for a coherent actionable entity; list for repeatable scanning; definition list for labeled facts.
- Avoid every tile having same shadow/gradient/call-to-action. Title/value/action precedence depends on content.
- Test mixed text lengths, missing icon/image, click target boundaries, focus order and responsive list-to-detail behavior.

### C22 Tree view, treegrid and nested rows
- Use hierarchy only if genuinely meaningful. Treegrid demands compound grid + expansion keyboard behavior—do not approximate with indented spans.
- Define expansion, row selection, multi-select, keyboard arrow/Home/End, focus after deletion and lazy branch loading.
- Test deep nesting, very large trees, screen-reader reporting and reparent conflicts.

### C23 Timeline, audit log, step/progress tracker and activity feed
- Labels, dates and actor/source must be truthful; distinguish chronological history from guided steps and real-time activity.
- Clarify status changes, timestamp precision/timezone, truncation and pagination.
- Test dense historic data, delayed events, long explanations and screen reader chronological context.

### C24 Chart, legend, tooltip, sparkline, heatmap and KPI
- Choose chart by user question (trend, part-to-whole, correlation, distribution), data quality and comparison semantics.
- Use explicit units/axes/source/time frame, visible totals/context and accessible tabular/summary alternative.
- Test 0/negative/null/outlier, label collisions, color-blind safe cues, mobile legibility and unverified numbers.

### C25 Calendar/schedule view, slot picker and Gantt/timeline
- Show visible timezone/resource context, events with type/status alternatives to color, unavailable slots and conflict indicator.
- Offer keyboard/list alternative to drag-resize; preserve time accuracy and confirm reservations from authoritative backend.
- Test DST, overlap, all-day boundaries, week start and touch.

### C26 Kanban, drag-and-drop lists and sortable columns
- Provide keyboard action menu alternative, status semantics, reorder feedback, concurrency and undo where possible.
- Test virtualized items, touch scroll vs drag, lost focus and failed persistence.

### C27 Map, cluster/list synchronized selection and location pin
- Map supplements, never replaces, accessible list/filter and textual location details.
- Accessible pin alternatives, loading tiles, zoom limits, denied geolocation and untrusted location metadata.
- Test list/map synchronization, keyboard results and mobile constraints.

## E. Content, media and complex editing

### C28 Rich-text editor, Markdown editor and content toolbar
- Select by workflow; visible publishing state, preview, heading hierarchy and keyboard formatting.
- Paste sanitization, real undo/redo, image alt text, link safety, large content and autosave conflicts.
- Test keyboard and screen readers; prevent XSS at trusted renderer boundary.

### C29 File preview, media player, lightbox, image cropper
- Provide file identity, download rights, captions/transcripts/alt text and fallback for unsupported media.
- Modal focus behavior and close/return location; no autoplay-with-sound or essential content rendered only in an image.
- Test unsupported media, large files, permission revocation and touch/keyboard.

### C30 Comments, mentions, reactions and collaboration presence
- Distinguish current presence vs confirmed realtime; user identity, relative timestamps with accessible absolute alternatives, edit/delete controls.
- Manage optimistic updates, failed send, stale mentions, harassment/moderation states and privacy.
- Test multi-user concurrency, offline, keyboard reply, screen-reader feed and long threads.

### C31 Code viewer/diff, logs, command snippets and copy actions
- Syntax theme must not hide contrast; line numbers, wrapping, search, truncation warnings, redaction and provenance.
- Copy buttons provide feedback and preserve code integrity; avoid copyable sample secrets.
- Test large content, long unbroken tokens, mobile horizontal scroll and keyboard navigation.

## F. Responsive structure, settings and system controls

### C32 Theme toggle, language switcher, density controls and preference panels
- Preferences reflect scope (user/device/workspace), save state, persistence and accessible labeling.
- Theme change keeps semantic contrast in light/dark/high-contrast; density never removes actions or minimum target size.
- Test OS preference, session sync, localization, keyboard focus and reduced motion.

### C33 Pagination, infinite loading, virtual scrolling and load-more
- Pick strategy by navigation and dataset goals; preserve findability, return location and total counts where known.
- Infinite scrolling requires accessible progress, error recovery and reachable footer; virtualization must preserve accessible item counts/focus.
- Test deep result links, history, screen-reader behavior and focus on new items.

### C34 Table of contents, anchors, side index and sticky controls
- Scroll sections with headings and URL fragment; sticky elements may not cover keyboard focus or critical text.
- Test anchor from external link, `prefers-reduced-motion`, 200/400% zoom and heading hierarchy.

### C35 Password, passkey, session timeout and sensitive action controls
- Support password managers, show/hide safely, accessible validation; never design OTP/paste prevention as security theatre.
- Confirm session-expired and account-changing actions; provide recovery without exposing sensitive internal data.
- Security must validate actual authentication, rate limit and reauthentication behavior; UI alone cannot enforce it.

### C36 Notification preference, consent, cookies and privacy choices
- Plain-language scopes and consequences, no deceptive defaults or prechecked consent where inappropriate.
- Preferences should persist, allow review/revocation when applicable; no false compliance badges.
- Tests: opt-out, nested controls, localization and server-side enforcement.

### C37 Pricing comparison, plan selector and checkout summary
- Explain the price and renewal unit, trial/cancellation terms, taxes/fees, disabled options and consequences.
- Preserve selected plan across redirect safely; never represent a payment attempt as settled without backend success.
- Test declines, duplicate submits, international formatting and assistive navigation.

### C38 AI response viewer, source citation, approval/apply and undo
- Clearly label generated output, cite sources if genuinely provided, highlight uncertainty, edit/review before applying consequential changes.
- Show progress/partial state, failed generation, stale information, cancellation and audit trail as needed.
- Test Markdown rendering safely, long streaming output, keyboard live-announcement pace and undo.

## Common component craft checks
- **Typography:** choose sizes/weights by hierarchy and content, correct baseline alignment, 0/large data values and Vietnamese diacritics; avoid visual monotony across every headline/card/button.
- **Spacing:** intentional density tokens; coherent optical grouping; avoid stacking 3 nested outlines and identical 16 px padding on all regions.
- **Color:** semantic states, limited decorative accents, meaningful light/dark surface ladder, non-color status labels and measured contrast.
- **Motion:** communicates state/space only where useful; reduced motion and stable focus; no ornamental bouncing on every interaction.
- **A11y:** WCAG 2.2 AA target (not automatic certification); valid labels/semantics/focus, minimum pointer target or documented exceptions, zoom and text reflow.
- **Truth:** no fabricated metrics, synthetic endorsements, fake export action, non-existent notifications, unimplemented OAuth buttons or claimed real-time statuses.
- **Evidence:** test run or screenshot paths must exist and correspond to exact viewport/content; manual claims labeled explicitly.

## Reference patterns (not clone targets)
- WAI APG: https://www.w3.org/WAI/ARIA/apg/patterns/
- GOV.UK components: https://design-system.service.gov.uk/components/
- MOJ components: https://design-patterns.service.justice.gov.uk/components/
