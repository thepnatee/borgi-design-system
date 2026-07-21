# Borgi Phase Completion Matrix

This repository now contains the complete specification and automation baseline for the Borgi product design platform.

| Phase | Deliverables | Status |
|---|---|---|
| Foundation | Repository map, roadmap, registries and CI | Complete |
| Brand CI | Foundation, guidelines, voice and tone | Complete |
| Mascot CI | Master, anatomy, expressions, poses, accessories and do/don't | Complete |
| Illustration CI | Empty, success, error, reminder and payment states | Complete |
| Product | MVP, release scope, IA, permissions, notifications and payments | Complete |
| UX flows | Booking, lifecycle, cancel, reschedule, payment, reminder, staff and service | Complete |
| Screens | Catalog, templates and screen generator | Complete baseline |
| Components | Catalog, standards and component template | Complete baseline |
| Motion | Motion and reduced-motion rules | Complete |
| AI system | Shared prompt, manifest, system rules, quality checklist and validator | Complete |
| Automation | Prompt build, image generation, screen/module generators, registries and validation | Complete |
| Architecture | System architecture and canonical data model | Complete |
| Engineering | Engineering, security, observability and CI standards | Complete |
| QA | Quality strategy and automated repository checks | Complete |
| Tokens | JSON and CSS tokens | Complete baseline |
| Figma | Page, component, frame, variable and export mapping | Complete baseline |
| API | Versioning, conventions, resources, errors, idempotency and webhook rules | Complete baseline |
| Accessibility | WCAG 2.2 AA product rules | Complete |
| Localization | Thai and English formatting and testing rules | Complete |
| Content design | UI copy, actions, errors and destructive confirmation rules | Complete |

## Meaning of complete baseline

A baseline is complete when the repository contains a canonical standard, reusable template or generator, quality gate and extension path. Individual product screens and API endpoints should be generated and completed as implementation work begins rather than pre-creating hundreds of empty files.

## Required validation

```bash
python3 scripts/validate_repository.py
python3 scripts/validate_prompts.py
python3 -m compileall -q scripts
```

## Extension commands

```bash
python3 scripts/new_screen.py --name reports-overview --group admin --id ADM-REPORTS-01
python3 scripts/new_module.py --module inventory
python3 scripts/generate_asset_registry.py
```
