#!/usr/bin/env python3
"""Create a Borgi screen specification and prompt stub."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("name must contain letters or numbers")
    return slug


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--group", required=True)
    parser.add_argument("--id")
    args = parser.parse_args()

    name = slugify(args.name)
    group = slugify(args.group)
    screen_id = args.id or name.upper().replace("-", "_")

    doc = ROOT / "docs" / "screens" / group / f"{name}.md"
    prompt = ROOT / "prompts" / "screens" / group / f"{name}.md"
    for path in (doc, prompt):
        if path.exists():
            raise SystemExit(f"refusing to overwrite {path.relative_to(ROOT)}")
        path.parent.mkdir(parents=True, exist_ok=True)

    title = args.name.strip().title()
    doc.write_text(f"""# {title}\n\n- ID: `{screen_id}`\n- Group: `{group}`\n\n## Goal\n\n## Actors and permissions\n\n## Layout and components\n\n## Data and API\n\n## States\n\nLoading, empty, success, error, disabled and permission-denied.\n\n## Responsive behavior\n\n## Accessibility\n\n## Analytics\n\n## Acceptance criteria\n""", encoding="utf-8")
    prompt.write_text(f"""# {screen_id} — {name}\n\nCreate the Borgi `{title}` screen. Follow `prompts/shared-visual-prompt.md`, the matching screen specification and canonical mascot references. Do not embed unreadable text or imply pet-care usage.\n""", encoding="utf-8")
    print(doc.relative_to(ROOT))
    print(prompt.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
