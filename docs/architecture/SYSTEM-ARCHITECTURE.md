# System Architecture

```mermaid
flowchart TB
WEB[Customer booking web] --> API[API gateway]
ADMIN[Admin web] --> API
API --> AUTH[Identity and access]
API --> BOOKING[Booking service]
API --> CATALOG[Service and resource catalog]
API --> CUSTOMER[Customer service]
API --> BILLING[Billing service]
BOOKING --> DB[(Operational database)]
CATALOG --> DB
CUSTOMER --> DB
BOOKING --> EVENTS[Event bus / outbox]
EVENTS --> NOTIFY[Notification worker]
EVENTS --> ANALYTICS[Analytics pipeline]
BILLING --> PAYMENT[Payment provider]
NOTIFY --> CHANNELS[Email / LINE / SMS adapters]
```

## Principles
- Modular monolith is acceptable for MVP; preserve domain boundaries.
- Workspace ID scopes every business record.
- Availability calculation has one canonical implementation.
- Writes use idempotency where retries are possible.
- Domain events use an outbox to avoid lost notifications.
- Secrets and provider credentials never enter the design repository.

## Domains
Identity, workspace, catalog, availability, booking, customer, notification, billing, reporting and audit.