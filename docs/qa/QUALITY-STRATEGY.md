# Quality Strategy

## Test layers
- Unit tests: availability, pricing, policy and state-transition rules.
- Integration tests: persistence, authorization, payment callbacks and notification outbox.
- Contract tests: API schemas and provider adapters.
- End-to-end tests: sign-in, create service, publish booking page, book, reschedule, cancel and export.
- Visual regression: shared components and critical responsive screens.
- Accessibility: automated checks plus keyboard and screen-reader review.

## Critical scenarios
- Two users attempt to reserve the same slot.
- Staff or resource becomes unavailable during checkout.
- Payment succeeds but callback is delivered more than once.
- Reminder retries after a temporary provider failure.
- Workspace timezone crosses daylight-saving boundaries.
- A user attempts cross-workspace access.
- Export contains only permitted fields and scope.

## Release severity
P0 blocks booking or exposes data. P1 breaks a critical flow without a safe workaround. P2 has a workaround. P3 is cosmetic or minor.

No release ships with open P0/P1 defects, failing critical-path tests or unresolved accessibility blockers.