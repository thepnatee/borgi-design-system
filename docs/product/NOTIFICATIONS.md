# Notifications

## Channels
Email is the default channel. LINE and SMS are provider adapters enabled per workspace and country. In-app notifications support operational events.

## Event types
Booking created, confirmed, rescheduled, cancelled, reminder, payment received, payment failed, staff assignment, customer follow-up and system alert.

## Reminder rules
Workspaces configure one or more offsets, such as 24 hours and 2 hours before an appointment. Rules evaluate in the appointment's workspace timezone and must not send after cancellation or completion.

## Delivery lifecycle
`queued`, `processing`, `sent`, `delivered`, `failed`, `suppressed`.

Every attempt stores channel, provider message ID, template version, locale, recipient reference, attempt count and failure category. Personal message content should not be copied into operational logs.

## Preferences and consent
Transactional messages required to operate a booking are separated from marketing messages. Marketing requires recorded consent and an unsubscribe path.

## Reliability
Use an outbox/event queue, idempotency key and bounded retries. Permanent failures are not retried indefinitely. Admins can inspect status and resend eligible messages.