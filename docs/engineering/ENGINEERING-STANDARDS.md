# Engineering Standards

## Repository rules
Use conventional commits, short-lived branches and reviewed pull requests. Generated assets must not contain secrets or customer data.

## API rules
Version public contracts, use UTC timestamps with explicit workspace timezone for display and policy evaluation, return stable error codes, support idempotency for booking/payment writes and document pagination/filtering.

## Quality gates
- Format and lint pass.
- Unit tests cover domain rules.
- Integration tests cover booking conflicts and permissions.
- Critical user journeys have end-to-end tests.
- Dependency and secret scanning pass.
- Accessibility checks pass for changed UI.
- Migration and rollback are documented.

## Observability
Structured logs include request ID and workspace ID but exclude sensitive personal data. Track latency, error rate, availability conflicts, notification failures and payment reconciliation failures.

## Security
Least privilege, encrypted transport/storage, audited role changes, secure cookie/session handling, rate limits and retention/deletion policies are required.