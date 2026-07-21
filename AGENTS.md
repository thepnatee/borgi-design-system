# Borgi AI Development Guide

This file is the source of truth for AI coding agents working on Borgi.

## Product objective

Build a production-ready booking and reminder product for Thai SMEs. The first goal is to help real businesses accept and manage bookings, not to build an enterprise platform.

## Non-negotiable principles

1. **SME first** — optimize for a business owner who has no technical administrator.
2. **MVP first** — implement only what is required to operate and sell the current product.
3. **Production ready** — include validation, permissions, auditability, errors, tests and operational visibility.
4. **Manual payment first** — Borgi must work without Stripe or any payment gateway.
5. **LINE friendly** — avoid forcing customers to install another application.
6. **Secure by default** — tenant isolation and server-side authorization are mandatory.
7. **No speculative complexity** — do not add marketplaces, settlement engines, workflow builders, plugin systems or AI customer features without validated demand.

## Current MVP domains

- Business and business settings
- Branch, staff and working hours
- Service and pricing
- Customer
- Booking, reschedule, cancellation, check-in, completion and no-show
- LINE reminder
- No-payment and manual-payment workflows
- Basic operational dashboard

## Payment order

1. No payment / pay at shop
2. Manual transfer or PromptPay with optional slip
3. Stripe Connect as an optional adapter
4. Additional gateways only after market validation

Borgi is not the merchant of record in the MVP. Customer funds must not be collected into Borgi's bank account for later settlement to SMEs.

## Required review questions

Before implementing a feature, answer:

- Which real SME problem does this solve?
- Is it required to acquire, activate or retain the first paying businesses?
- Can the product operate safely without it?
- What is the smallest production-ready implementation?
- What are the tenant, security, failure and recovery cases?
- What documentation, analytics and tests must change?

## Definition of done

A change is not complete until it has appropriate acceptance criteria, permissions, validation, empty/loading/error states, tests, audit/observability considerations, migration and rollback notes where relevant, and documentation updates.

Detailed roles and workflows are under `.ai/`.