#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "prompts" / "manifest.json"
DIST = ROOT / "dist" / "prompts"


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    shared = (ROOT / data["shared_prompt"]).read_text(encoding="utf-8")
    DIST.mkdir(parents=True, exist_ok=True)

    for item in data["items"]:
        body = (
            f"{shared}\n\n"
            f"# Page specification\n\n"
            f"- ID: {item['id']}\n"
            f"- Group: {item['group']}\n"
            f"- Aspect ratio: {item['aspect_ratio']}\n\n"
            f"{item['prompt']}\n"
        )
        path = DIST / f"{item['id']}-{item['name']}.md"
        path.write_text(body, encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
