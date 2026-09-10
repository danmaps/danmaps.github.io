"""Inject the browser-visible basemap key into the deployment artifact only."""
import json
import os
from pathlib import Path


def inject():
    key = os.environ.get("CARTO_BASEMAP_KEY", "").strip()
    if not key:
        raise SystemExit("CARTO_BASEMAP_KEY must be configured as an Actions secret.")
    target = Path("docs/static/gis-from-scratch/basemap-config.json")
    if not target.is_file():
        raise SystemExit("Freeze the site before injecting its basemap configuration.")
    target.write_text(json.dumps({"key": key}) + "\n", encoding="utf-8")


if __name__ == "__main__":
    inject()
