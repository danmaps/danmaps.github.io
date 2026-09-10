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
    html = target.with_name("tinygis.html")
    source = html.read_text(encoding="utf-8")
    marker = '<script id="basemap-config" type="application/json">{"key": ""}</script>'
    if source.count(marker) != 1:
        raise SystemExit("Expected one empty inline basemap configuration after freezing.")
    payload = json.dumps({"key": key}).replace("<", "\\u003c")
    html.write_text(source.replace(marker, '<script id="basemap-config" type="application/json">' + payload + '</script>'), encoding="utf-8")
    target.write_text(json.dumps({"key": key}) + "\n", encoding="utf-8")


if __name__ == "__main__":
    inject()
