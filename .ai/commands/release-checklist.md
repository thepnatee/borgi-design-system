# Release Checklist

## Product

- Scope matches accepted user story and out-of-scope list.
- A real SME can complete setup and daily operation.
- Manual/no-payment usage remains available where applicable.

## Engineering

- Tenant authorization and validation are enforced server-side.
- Migrations are backward compatible or have a documented maintenance plan.
- Idempotency, concurrency and retry behavior are covered.
- Secrets and personal data are protected and excluded from logs.
- Error states are recoverable and customer-safe.

## Quality

- Automated tests cover primary and critical failure paths.
- Regression scenarios are documented.
- Accessibility and responsive behavior are verified.
- Analytics, audit events, logs and alerts are ready.

## Operations

- Rollout strategy and owner are identified.
- Rollback steps are executable.
- Support notes and known limitations are documented.
- Release notes and affected documentation are updated.

Do not approve release while a blocker remains unresolved.