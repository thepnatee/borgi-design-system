#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "prompts" / "manifest.json"
OUTPUTS = ROOT / "outputs"

SIZE_MAP = {
    "16:9": "1536x1024",
    "9:16": "1024x1536",
    "4:5": "1024x1536",
    "1:1": "1024x1024",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate Borgi images from prompts/manifest.json")
    parser.add_argument("--group", action="append", help="Generate only selected group; repeatable")
    parser.add_argument("--id", dest="ids", action="append", help="Generate only selected ID; repeatable")
    parser.add_argument("--quality", choices=["low", "medium", "high", "auto"], default="low")
    parser.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-1"))
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--variants", type=int, default=1)
    parser.add_argument("--force", action="store_true", help="Overwrite existing images")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
    return parser.parse_args()


def load_manifest() -> tuple[str, list[dict[str, Any]]]:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    shared = (ROOT / data["shared_prompt"]).read_text(encoding="utf-8")
    return shared, data["items"]


def select_items(items: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected = items
    if args.group:
        groups = set(args.group)
        selected = [item for item in selected if item["group"] in groups]
    if args.ids:
        ids = set(args.ids)
        selected = [item for item in selected if item["id"] in ids]
    return selected


def output_path(item: dict[str, Any], variant: int) -> Path:
    suffix = f"-v{variant}" if variant > 1 else ""
    return OUTPUTS / item["group"] / f"{item['id']}-{item['name']}{suffix}.png"


def build_prompt(shared: str, item: dict[str, Any]) -> str:
    return (
        f"{shared}\n\n"
        f"Create the following specific asset.\n"
        f"Asset ID: {item['id']}\n"
        f"Asset group: {item['group']}\n"
        f"Requested composition: {item['prompt']}\n"
        f"Target aspect ratio: {item['aspect_ratio']}. "
        "Prioritize coherent product structure and mascot consistency over decorative detail."
    )


def generate_one(client: OpenAI, shared: str, item: dict[str, Any], variant: int, args: argparse.Namespace) -> dict[str, Any]:
    path = output_path(item, variant)
    if path.exists() and not args.force:
        return {"id": item["id"], "variant": variant, "status": "skipped", "path": str(path.relative_to(ROOT))}

    path.parent.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(shared, item)
    size = SIZE_MAP.get(item.get("aspect_ratio", "1:1"), "1024x1024")

    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = client.images.generate(
                model=args.model,
                prompt=prompt,
                size=size,
                quality=args.quality,
                background="opaque",
                output_format="png",
            )
            image_b64 = response.data[0].b64_json
            if not image_b64:
                raise RuntimeError("Image API returned no base64 payload")
            path.write_bytes(base64.b64decode(image_b64))
            return {
                "id": item["id"],
                "variant": variant,
                "status": "generated",
                "path": str(path.relative_to(ROOT)),
                "model": args.model,
                "size": size,
                "quality": args.quality,
                "request_id": getattr(response, "_request_id", None),
            }
        except Exception as exc:  # SDK exceptions vary by version
            last_error = exc
            if attempt < 3:
                time.sleep(2 ** attempt)

    return {"id": item["id"], "variant": variant, "status": "failed", "error": str(last_error)}


def main() -> int:
    args = parse_args()
    shared, items = load_manifest()
    items = select_items(items, args)
    jobs = [(item, variant) for item in items for variant in range(1, args.variants + 1)]

    if not jobs:
        print("No matching prompts.")
        return 1

    print(f"Model: {args.model}")
    print(f"Jobs: {len(jobs)}")
    for item, variant in jobs:
        print(f"- {item['id']} {item['name']} v{variant} -> {output_path(item, variant).relative_to(ROOT)}")

    if args.dry_run:
        return 0

    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is required.", file=sys.stderr)
        return 2

    if not args.yes:
        answer = input("Generate these images and incur API usage? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            return 0

    client = OpenAI()
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUTS / "generation-report.jsonl"

    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as executor:
        futures = [executor.submit(generate_one, client, shared, item, variant, args) for item, variant in jobs]
        with report_path.open("a", encoding="utf-8") as report:
            for future in as_completed(futures):
                result = future.result()
                report.write(json.dumps(result, ensure_ascii=False) + "\n")
                report.flush()
                print(json.dumps(result, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
