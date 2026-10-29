# Responsive web/PWA execution plan — amendment 2026-10-20

Scope: one responsive web product across phone, tablet and desktop, optionally installable as a PWA. Native iOS/Android applications are `NOT_APPLICABLE` to this package. Implementation and browser/device evidence are `NOT_CHECKED`.

## 1. Normative basis and interpretation

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the accessibility conformance basis. Critical implications include reflow at 320 CSS px, orientation support, visible/unobscured focus, non-drag alternatives, minimum target sizing, accessible authentication and programmatically determinable status messages.
- [W3C WAI mobile accessibility guidance](https://www.w3.org/WAI/standards-guidelines/mobile/) confirms that WCAG applies to mobile web and applications; this plan does not invent a separate “mobile WCAG.”
- [Web App Manifest](https://www.w3.org/TR/appmanifest/) supplies install metadata such as name, icons, start URL, display and scope. The referenced document is a Working Draft, so feature support must be verified in the agreed browser matrix rather than asserted universally. Scope is explicit to avoid accidental out-of-scope navigation.
- [Service Workers](https://www.w3.org/TR/service-workers/) require secure contexts for normal web use. CacheStorage is application-managed and does not automatically expire or update; every cached class therefore needs an owner, version, expiry/cleanup rule and privacy review.

Target conformance is WCAG 2.2 AA for released critical journeys, with manual keyboard/screen-reader/zoom/high-contrast/reduced-motion checks in addition to automation.

## 2. Reference viewport and interaction matrix

These are test anchors, not device detection rules. Layout uses available space, container queries where appropriate and content reflow without horizontal two-dimensional scrolling except truly tabular data with an accessible alternative.

| Anchor | CSS viewport | Required behavior |
|---|---:|---|
| narrow phone | 320×568 | single column; no clipped action, focus or error; compact persistent context; no forced orientation |
| reference phone | 390×844 | bottom/compact navigation where applicable; one primary action; sheets become full-screen dialogs |
| tablet portrait | 768×1024 | navigation rail or compact sidebar; forms remain readable-width; no desktop hover dependency |
| desktop | 1280×800 | sidebar plus bounded content; optional contextual panel; keyboard order follows reading order |
| wide desktop | 1440×900 | max-width containers; no stretched prose; comparison panes only when both remain usable |
| zoom/reflow | 1280 at 400% ≈ 320 CSS px | same task completes without lost content or two-axis scrolling |

Touch targets have 44×44 CSS px preferred interaction boxes. The conformance floor is WCAG 2.2 Target Size (Minimum), including its exceptions; tests must not treat the preference as a false universal requirement. Safe-area insets, on-screen keyboard, 200% text spacing, 400% zoom and portrait/landscape are explicit cases.

## 3. Component transformations

| Pattern | Phone | Desktop | Invariants |
|---|---|---|---|
| global navigation | bottom bar for top tasks plus “More”; install state never blocks navigation | left rail/top bar with labels | same destinations, current-location semantics, keyboard access |
| multi-step intake | one step/section, sticky summary action that never covers fields | stepper with summary panel | draft/version, error summary, data-purpose copy and back behavior identical |
| tables | prioritized cards or column chooser; downloadable accessible table | semantic table with sticky header where usable | no data removed; headers/captions; sort state announced |
| report reader | section index drawer; readable single column; claim detail accordion | persistent index and optional evidence panel | same claims, lineage, limitations, correction and version controls |
| comparisons | sequential version cards with changed-field summary | split view when width permits | differences available as text, not color alone |
| admin/workspace | task queue cards and filters in drawer | dense queue/table plus details pane | authorization, counts, filter meaning and actions identical |
| dialogs | full-screen on narrow view with focus trap and visible close | bounded modal or page | focus return, Escape where safe, unsaved-change warning |
| charts | summary sentence and data table before/alongside chart | chart plus table/detail panel | no color-only encoding; zoom and screen-reader alternative |

## 4. State contract for all 45 screens

Every registered screen has an explicit record in `SCREEN_EXECUTION_EXTENSION.json` and CSV parity. At minimum each route must render and test:

- `loading`: titled skeleton or bounded progress; no spinner without context;
- `empty`: explain why empty and the permitted next action;
- `error`: stable error code, retry/back route and no private payload;
- `blocked`: gate/eligibility/permission reason that does not reveal another subject;
- `ready`: primary task, provenance/version where applicable and consistent navigation;
- `offline`: truthful capability statement; do not pretend a server mutation succeeded;
- `stale`: last-updated/version banner with refresh or safe continue rules;
- `forbidden`: generic not-found/unauthorized presentation appropriate to enumeration risk.

Mutations additionally test validating, submitting, idempotent retry, accepted/pending, success and rejected/conflict. Jobs additionally test queued, running, delayed, cancel requested, cancelled, failed-retryable and terminal-failed. Payments additionally test created, redirecting, pending, paid-unreconciled, entitled, failed, cancelled, refunded and disputed. Report screens additionally test draft, in review, published, corrected, withdrawn and export unavailable.

## 5. PWA and offline contract

Public shell/static educational assets may use versioned stale-while-revalidate or cache-first rules after content-owner approval. Authenticated API responses, report bodies, journals, identity data, payment pages, tokens and subject-specific HTML are network-only by default and must not be put in shared/service-worker caches. A private draft may be stored only after explicit product/privacy approval using origin storage, scoped encryption where supported, a visible device-local label, TTL, account separation, delete control and logout cleanup; no background sync until its conflict/idempotency design is approved.

Installability is progressive enhancement. The web journey must work without install. The app must expose online/offline state, update availability, reload timing and data-loss warning. A new service worker waits until the user can safely reload; forced takeover is reserved for an approved security incident path. Cache names include schema/build version; activation deletes only owned obsolete caches. `start_url` and explicit manifest scope remain inside the approved web surface.

Offline write rules:

1. deterministic guest calculation may run fully local and may be discarded on close;
2. authenticated forms may keep an explicitly permitted local draft but never display “saved to account” before a server receipt;
3. consent, sharing, deletion, payment, publication, review and admin actions are online-only;
4. queued mutation support, if later approved, requires an idempotency key, account/subject binding, conflict UI, expiry, manual discard and receipt reconciliation;
5. logout, account switch and deletion clear locally stored private drafts for that account and record only privacy-safe evidence.

## 6. Accessibility and responsive acceptance

For each critical journey test keyboard-only, VoiceOver/Safari and one additional agreed screen-reader/browser pair, 200% text spacing, 400% zoom/reflow, reduced motion, forced colors/high contrast where supported, portrait/landscape, touch and pointer. Automated checks are a floor. Focus order follows the visual/reading order; status and validation are announced; labels persist; password managers and paste are not blocked; drag interactions have a single-pointer alternative; timeout and session changes are warned.

Required receipts include build/SHA, route/screen ID, viewport, browser/OS/assistive technology versions, fixture ID, steps, expected/actual, screenshot or trace where safe, axe/manual results and reviewer. A screenshot alone is not conformance evidence.

## 7. Rollout slices

1. Shared shell, tokens, navigation, error/focus primitives and public UI-01–UI-06.
2. Adult/self onboarding, identity/privacy and profile UI-07–UI-14.
3. Goals, journal, analysis and jobs UI-15–UI-22.
4. Reports, payment, entitlement, support and privacy rights UI-23–UI-33.
5. Family/practice/academy/workspace/partner/admin UI-34–UI-45 only as their product gates open.

Each slice runs phone and desktop contracts in the same release. “Desktop complete, mobile later” is not an accepted state for an opened route.

