# Payment Flow

## Flow
1. Create a payment intent using an idempotency key.
2. Show amount, currency, taxes, fees and cancellation terms.
3. Redirect to or embed the approved payment provider.
4. Treat the provider webhook as the source of truth.
5. Verify signature, amount, currency and merchant context.
6. Update payment and appointment in one consistent transaction or compensating workflow.
7. Issue receipt and enqueue confirmation.

## States
`pending`, `requires_action`, `processing`, `paid`, `failed`, `partially_refunded`, `refunded`, `cancelled`.

Never log credentials or full card data. Duplicate callbacks must be safe. A client success screen alone must never mark a payment as paid.
