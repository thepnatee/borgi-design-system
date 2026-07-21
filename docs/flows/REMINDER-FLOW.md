# Reminder Delivery Flow

1. Resolve appointment, customer consent, channel preference, locale and timezone.
2. Calculate send time and respect quiet hours.
3. Render a versioned template with non-sensitive variables.
4. Create a delivery job with an idempotency key.
5. Send through the configured provider.
6. Record provider ID and status transitions.
7. Retry transient failures with bounded exponential backoff.
8. Stop retries for invalid recipient, opt-out or permanent provider rejection.

Appointment changes must invalidate obsolete reminder jobs. Delivery failure must not modify the appointment itself. Store enough metadata for support without storing unnecessary message content.
