#!/usr/bin/env python3
"""Validate Borgi prompt coverage and required brand guardrails."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "prompts" / "manifest.json"
REQUIRED_TERMS = ("Borgi", "booking", "not", "pet")


def main() -> int:
    failures: list[str] = []
    shared = ROOT / "prompts" / "shared-visual-prompt.md"
    if not shared.exists():
        failures.append("missing prompts/shared-visual-prompt.md")
    else:
        text = shared.read_text(encoding="utf-8")
        for term in REQUIRED_TERMS:
            if term.lower() not in text.lower():
                failures.append(f"shared prompt missing guardrail term: {term}")

    if not MANIFEST.exists():
        failures.append("missing prompts/manifest.json")
    else:
        try:
            payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid manifest JSON: {exc}")
        else:
            if not isinstance(payload, (dict, list)):
                failures.append("manifest must be an object or array")

    for path in sorted((ROOT / "prompts").rglob("*.md")):
        if path.stat().st_size < 40:
            failures.append(f"prompt is too short: {path.relative_to(ROOT)}")

    if failures:
        print("Prompt validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Prompt validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
