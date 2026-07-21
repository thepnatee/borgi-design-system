# Borgi AI Team

Use these agents as focused reviewers, not as independent decision makers. Product evidence and repository standards remain the source of truth.

## Recommended sequence

1. Product Owner — confirm problem, scope and acceptance criteria.
2. SME Advisor — verify that a real Thai SME can understand and operate it.
3. Solution Architect — choose the smallest safe design and extension points.
4. Specialist reviewer — payment, LINE, UX, backend or frontend as applicable.
5. QA and Release — test failure paths, migration and rollback.

## Available agents

- `product-owner.md`
- `sme-advisor.md`
- `solution-architect.md`
- `payment-reviewer.md`
- `line-platform-reviewer.md`
- `qa-release.md`

## Commands

- `commands/new-feature.md`
- `commands/review-pr.md`
- `commands/release-checklist.md`

## Shared context

Agents must read `AGENTS.md` plus the relevant files under `.ai/context/` before producing a recommendation or code.

## Rule

Agents may recommend moving work to the backlog. They must not expand MVP scope merely because an abstraction or integration may be useful later.