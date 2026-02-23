from flask_frozen import Freezer
from app import app, POSTS_DIR, UNPUBLISHED_TAGS, tag_slug
import os

# Publish the static site into /docs so GitHub Pages can serve it from the master branch.
# (User/Org Pages work best from the default branch + /docs.)
app.config["FREEZER_DESTINATION"] = "docs"

freezer = Freezer(app)


@freezer.register_generator
def post():
    """Freeze all /post/<name>.html pages, including unlisted drafts.

    Frozen-Flask will crawl links it can see (eg, homepage), but unlisted posts
    won't be discovered. This generator ensures every markdown file in /posts
    gets an HTML page.
    """
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            yield {"post_name": filename[:-3]}


@freezer.register_generator
def tag():
    """Freeze all tag pages."""
    slugs = {}
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue

        # Parse front matter cheaply
        path = os.path.join(POSTS_DIR, filename)
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except OSError:
            continue

        tags = []
        if content.startswith("---"):
            try:
                # tolerate CRLF/LF
                normalized = content.replace("\r\n", "\n")
                _, front_matter, _ = normalized.split("---\n", 2)
                import yaml

                meta = yaml.safe_load(front_matter) or {}
                raw_tags = meta.get("tags", [])
                # mirror app normalization behavior as close as possible
                for t in raw_tags or []:
                    if not isinstance(t, str):
                        continue
                    tt = t.title() if not t.isupper() else t
                    tt = tt.replace("Arcgis Pro", "ArcGIS Pro").replace("Ai", "AI").replace("Gis", "GIS")
                    tt = tt.strip()
                    if tt:
                        tags.append(tt)
            except Exception:
                tags = []

        if any(t in UNPUBLISHED_TAGS for t in tags):
            # unlisted posts don't get to create discoverable tag pages
            continue

        for t in tags:
            if t in UNPUBLISHED_TAGS:
                continue
            slugs[tag_slug(t)] = True

    # never publish tag pages for unpublished tags
    for t in UNPUBLISHED_TAGS:
        slugs.pop(tag_slug(t), None)

    for s in sorted(slugs.keys()):
        if s:
            yield {"tag_slug_value": s}


if __name__ == "__main__":
    freezer.freeze()

