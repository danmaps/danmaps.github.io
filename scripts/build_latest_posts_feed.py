from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
OUTPUT_PATH = ROOT / "docs" / "latest-posts.json"
UNPUBLISHED_TAGS = {"draft", "stub", "unlisted"}
MAX_POSTS = 8


def parse_front_matter(text: str) -> tuple[dict, str]:
    normalized = text.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        return {}, normalized

    try:
        _, front_matter, body = normalized.split("---\n", 2)
    except ValueError:
        return {}, normalized

    try:
        metadata = yaml.safe_load(front_matter) or {}
    except yaml.YAMLError:
        metadata = {}

    return metadata, body


def normalize_date(value, fallback: date) -> str:
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
        except ValueError:
            pass
    return fallback.isoformat()


def is_published(metadata: dict) -> bool:
    tags = metadata.get("tags", []) or []
    normalized = {str(tag).strip().lower() for tag in tags}
    return not bool(normalized & UNPUBLISHED_TAGS)


def build_feed() -> dict:
    posts = []

    for path in POSTS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        metadata, _ = parse_front_matter(text)
        if not is_published(metadata):
            continue

        fallback_date = datetime.fromtimestamp(path.stat().st_mtime).date()
        post_date = normalize_date(metadata.get("date"), fallback_date)
        title = str(metadata.get("title") or path.stem).strip()
        summary = str(metadata.get("summary") or "").strip()

        posts.append(
            {
                "title": title,
                "date": post_date,
                "summary": summary,
                "url": f"https://danmaps.github.io/post/{path.stem}.html",
            }
        )

    posts.sort(key=lambda post: (post["date"], post["url"]), reverse=True)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "posts": posts[:MAX_POSTS],
    }


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(build_feed(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
