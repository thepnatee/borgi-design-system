#!/usr/bin/env python3
"""Regenerate assets/index.json from repository asset files."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUTPUT = ASSETS / "index.json"
EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".mp4"}


def main() -> int:
    existing: dict = {}
    if OUTPUT.exists():
        try:
            existing = json.loads(OUTPUT.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}

    previous = {item.get("path"): item for item in existing.get("assets", []) if isinstance(item, dict)}
    assets = []
    for path in sorted(ASSETS.rglob("*")):
        if not path.is_file() or path == OUTPUT or path.suffix.lower() not in EXTENSIONS:
            continue
        relative = path.relative_to(ROOT).as_posix()
        old = previous.get(relative, {})
        assets.append({
            "id": old.get("id") or path.stem.lower().replace("_", "-"),
            "path": relative,
            "type": old.get("type") or path.parent.name,
            "status": old.get("status") or "active",
            "alt": old.get("alt") or "",
        })

    payload = {"schemaVersion": 1, "generated": True, "assets": assets}
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"registered {len(assets)} assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
