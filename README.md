# Borgi Design System

Complete brand identity, mascot guidelines, product UX specification, screen inventory, design tokens, and image-generation prompts for **Borgi** — a booking and reminder SaaS platform.

## Product position

Borgi helps clinics, salons, consultants, education providers, event teams, meeting rooms, workshops, and service businesses manage bookings, schedules, reminders, follow-ups, and no-shows.

Borgi must feel like a modern general-purpose SaaS product. It must **not** look like a pet-care, veterinary, or grooming application.

## Mascot

Borgi is a short, round orange-and-cream corgi with a lovable derpy expression, asymmetric goofy eyes, rosy cheeks, a tiny tongue-out smile, floppy ear tips, a teal scarf, a gold bell tag, and a crooked teal-and-orange propeller beanie.

## Repository map

- `docs/brand/` — CI, mascot, logo, color, typography, illustration, voice
- `docs/product/` — information architecture, user flows, roles, responsive rules
- `docs/screens/` — page requirements from landing through admin
- `docs/components/` — foundations and component specifications
- `prompts/` — shared and page-level image prompts
- `tokens/` — design tokens in JSON
- `src/styles/` — CSS custom properties
- `scripts/` — prompt builder and batch image generator
- `.github/workflows/` — validation and optional image generation workflow

## Quick start

```bash
python3 scripts/build_prompts.py
python3 scripts/generate_images.py --dry-run
```

See `docs/IMPLEMENTATION-ROADMAP.md` for the recommended delivery sequence.
