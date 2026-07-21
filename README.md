# Borgi Design System

Complete brand identity, mascot guidelines, product UX specification, screen inventory, design tokens, architecture, engineering standards, quality strategy, and image-generation prompts for **Borgi** — a booking and reminder SaaS platform.

## Product position

Borgi helps clinics, salons, consultants, education providers, event teams, meeting rooms, workshops, and service businesses manage bookings, schedules, reminders, follow-ups, and no-shows.

Borgi must feel like a modern general-purpose SaaS product. It must **not** look like a pet-care, veterinary, or grooming application.

## Mascot

Borgi is a short, round orange-and-cream corgi with a lovable derpy expression, asymmetric goofy eyes, rosy cheeks, a tiny tongue-out smile, floppy ear tips, a teal scarf, a gold bell tag, and a crooked teal-and-orange propeller beanie.

## Repository map

- `docs/brand/` — brand foundation, identity, voice and usage rules
- `docs/mascot/` — canonical mascot anatomy, expression and consistency rules
- `docs/product/` — MVP, releases, permissions, notifications and payments
- `docs/flows/` — booking and appointment lifecycle definitions
- `docs/screens/` — page requirements from landing through admin
- `docs/components/` — component standards and specification templates
- `docs/motion/` — interaction and reduced-motion guidance
- `docs/architecture/` — system architecture and canonical data model
- `docs/engineering/` — API, security, observability and delivery standards
- `docs/qa/` — quality strategy and critical scenarios
- `docs/ai/` — AI generation rules and acceptance checklist
- `prompts/` — shared and page-level image prompts
- `references/` — canonical mascot and optional UI style references
- `assets/` — approved asset registry
- `tokens/` — design tokens in JSON
- `src/styles/` — CSS custom properties
- `scripts/` — prompt builder, validation and batch image generator
- `.github/workflows/` — automated repository validation

## Source-of-truth reading order

1. `docs/brand/BRAND-FOUNDATION.md`
2. `docs/mascot/MASTER.md`
3. `docs/product/MVP-SCOPE.md`
4. `docs/product/RELEASE-SCOPE.md`
5. `docs/flows/BOOKING-FLOW.md`
6. `docs/components/COMPONENT-STANDARDS.md`
7. `docs/architecture/SYSTEM-ARCHITECTURE.md`
8. `docs/engineering/ENGINEERING-STANDARDS.md`
9. `docs/qa/QUALITY-STRATEGY.md`
10. `docs/ai/QUALITY-CHECKLIST.md`

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set the API key only when generating images:

```bash
export OPENAI_API_KEY="sk-..."
```

## Validate the repository

```bash
python3 scripts/validate_repository.py
```

The GitHub Actions workflow runs the same validation on pushes and pull requests.

## Build prompts

```bash
python3 scripts/build_prompts.py
```

## Reference image setup

Choose the best canonical Borgi image and copy it to:

```text
references/borgi-master.png
```

The generator automatically uses this file when it exists. Additional references can be supplied with repeated `--reference` options. Use no more than three references in one generation.

Recommended roles:

```text
references/borgi-master.png       mascot identity
references/borgi-ui-style.png     product UI direction
references/borgi-brand-board.png  color and material direction
```

## Dry run

```bash
python3 scripts/generate_images.py --dry-run
```

The output should show:

```text
Mode: reference edit
Reference: references/borgi-master.png
```

## Recommended first generation

```bash
python3 scripts/generate_images.py \
  --id CI-01 \
  --quality high \
  --input-fidelity high \
  --variants 3 \
  --force \
  --yes
```

## Generate with explicit references

```bash
python3 scripts/generate_images.py \
  --id MKT-01 \
  --reference references/borgi-master.png \
  --reference references/borgi-ui-style.png \
  --quality high \
  --input-fidelity high \
  --variants 3 \
  --force \
  --yes
```

## Generate a group

```bash
python3 scripts/generate_images.py \
  --group admin \
  --reference references/borgi-master.png \
  --reference references/borgi-ui-style.png \
  --quality high \
  --input-fidelity high \
  --concurrency 2 \
  --yes
```

## Text-to-image without references

```bash
python3 scripts/generate_images.py \
  --id CI-01 \
  --no-reference \
  --quality high \
  --force \
  --yes
```

## Important behavior

- If `references/borgi-master.png` exists, reference-edit mode is enabled automatically.
- `--reference` is repeatable and accepts relative or absolute paths.
- The script rejects more than three references to reduce conflicting visual direction.
- `--input-fidelity high` is the default for reference editing.
- `--quality high` is the default.
- Existing outputs are skipped unless `--force` is supplied.
- Generation metadata is appended to `outputs/generation-report.jsonl`.

See `docs/IMPLEMENTATION-ROADMAP.md` for the delivery sequence and `product.json` for the machine-readable product registry.