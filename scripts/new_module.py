#!/usr/bin/env python3
"""Create documentation, flow, prompt and asset folders for a Borgi module."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not value:
        raise ValueError("module must contain letters or numbers")
    return value


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise SystemExit(f"refusing to overwrite {path.relative_to(ROOT)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", required=True)
    args = parser.parse_args()
    module = slugify(args.module)
    title = args.module.strip().title()

    write_new(ROOT / "docs" / "product" / "modules" / f"{module}.md", f"# {title} Module\n\n## Goal\n\n## Actors\n\n## Capabilities\n\n## Permissions\n\n## Data\n\n## API\n\n## States and edge cases\n\n## Metrics\n")
    write_new(ROOT / "docs" / "flows" / f"{module.upper().replace('-', '_')}-FLOW.md", f"# {title} Flow\n\n## Preconditions\n\n## Main flow\n\n## Errors\n\n## Edge cases\n\n## Audit events\n")
    write_new(ROOT / "prompts" / "modules" / f"{module}.md", f"# {title} visual prompt\n\nCreate Borgi product visuals for the {title} module. Follow the shared visual prompt, product scope, accessibility rules and canonical mascot reference.\n")
    (ROOT / "assets" / "modules" / module).mkdir(parents=True, exist_ok=True)
    (ROOT / "outputs" / module).mkdir(parents=True, exist_ok=True)
    print(f"created module scaffold: {module}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
