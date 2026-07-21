# API Specification

Borgi APIs are versioned under `/v1`, tenant-scoped and documented with OpenAPI.

## Conventions

- JSON request and response bodies
- ISO 8601 UTC timestamps
- Stable resource IDs and cursor pagination
- Idempotency keys for booking, payment, refund and notification creation
- Optimistic concurrency for mutable scheduling resources
- Consistent error envelope containing `code`, `message`, `field`, `requestId` and optional details
- Authentication and authorization enforced server-side for every tenant resource

## Core resources

`businesses`, `branches`, `staff`, `services`, `availability`, `customers`, `appointments`, `payments`, `refunds`, `notifications`, `templates`, `integrations` and `audit-events`.

Every endpoint specification must include permission, validation, success schema, error codes, idempotency behavior, rate limits, audit behavior and example payloads. Webhooks require signature verification, replay protection and documented retry semantics.
