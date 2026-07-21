#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "product.json",
    "assets/index.json",
    "tokens/tokens.json",
    "prompts/manifest.json",
    "prompts/shared-visual-prompt.md",
    "docs/brand/BRAND-FOUNDATION.md",
    "docs/mascot/MASTER.md",
    "docs/product/MVP-SCOPE.md",
    "docs/product/PERMISSIONS.md",
    "docs/flows/BOOKING-FLOW.md",
    "docs/components/COMPONENT-STANDARDS.md",
    "docs/architecture/SYSTEM-ARCHITECTURE.md",
    "docs/engineering/ENGINEERING-STANDARDS.md",
    "docs/ai/QUALITY-CHECKLIST.md",
]

JSON_FILES = [
    "product.json",
    "assets/index.json",
    "tokens/tokens.json",
    "prompts/manifest.json",
]


def validate_required_files() -> list[str]:
    return [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]


def validate_json() -> list[str]:
    errors: list[str] = []
    for relative in JSON_FILES:
        path = ROOT / relative
        if not path.is_file():
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{relative}: {exc}")
    return errors


def validate_manifest_paths() -> list[str]:
    path = ROOT / "prompts/manifest.json"
    if not path.is_file():
        return []

    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    shared = data.get("shared_prompt")
    if shared and not (ROOT / shared).is_file():
        errors.append(f"Missing shared prompt: {shared}")

    seen: set[str] = set()
    for item in data.get("items", []):
        item_id = item.get("id")
        if not item_id:
            errors.append("Manifest item is missing id")
        elif item_id in seen:
            errors.append(f"Duplicate manifest id: {item_id}")
        else:
            seen.add(item_id)

        for key in ("name", "group", "prompt", "aspect_ratio"):
            if not item.get(key):
                errors.append(f"Manifest item {item_id or '<unknown>'} is missing {key}")
    return errors


def main() -> int:
    errors: list[str] = []
    missing = validate_required_files()
    errors.extend(f"Missing required file: {path}" for path in missing)
    errors.extend(validate_json())
    errors.extend(validate_manifest_paths())

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
