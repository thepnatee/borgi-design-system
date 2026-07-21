# Claude Code Instructions for Borgi

Before planning or editing code:

1. Read `/AGENTS.md`.
2. Read `/.ai/context/product.md`.
3. Select the relevant reviewer under `/.ai/agents/`.
4. Follow the workflow under `/.ai/commands/`.

## Default behavior

- Keep scope focused on a production-ready Thai SME booking MVP.
- Prefer a modular monolith and explicit domain boundaries.
- Preserve no-payment and manual-payment operation.
- Treat Stripe Connect and other gateways as optional adapters.
- Include tenant authorization, validation, failure states, tests, auditability, observability and rollback considerations.
- Put unvalidated enterprise or automation ideas in the backlog instead of implementing them.

When asked to create a feature, use `/.ai/commands/new-feature.md`.
When asked to review a pull request, use `/.ai/commands/review-pr.md`.
Before approving a release, use `/.ai/commands/release-checklist.md`.