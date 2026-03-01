from flask_frozen import Freezer
from app import app, POSTS_DIR, UNPUBLISHED_TAGS, tag_slug, BETA_BUILD_DIR
import os

# Publish the static site into /docs so GitHub Pages can serve it from the master branch.
# (User/Org Pages work best from the default branch + /docs.)
app.config["FREEZER_DESTINATION"] = "docs"

# Silence noisy warnings by explicitly excluding endpoints that are not meant to be
# part of the frozen static output.
# Avoid noisy warnings:
# - /drafts is an HTML page without a .html extension (mimetype mismatch warning)
# - /beta/* requires an explicit generator or Freezer warns
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True

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
def drafts():
    """Freeze the /drafts.html page.

    Note: this page lists unpublished posts and is intentionally not linked from the homepage.
    """
    yield {}


@freezer.register_generator
def beta_static():
    """Freeze /beta/* assets if they exist.

    This avoids MissingURLGeneratorWarning and keeps /beta working on GitHub Pages.
    """
    if not os.path.isdir(BETA_BUILD_DIR):
        return

    for root, _, files in os.walk(BETA_BUILD_DIR):
        for fn in files:
            abs_path = os.path.join(root, fn)
            rel = os.path.relpath(abs_path, BETA_BUILD_DIR).replace('\\', '/')
            yield {"resource": rel}


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


def _ensure_nojekyll():
    """GitHub Pages uses Jekyll by default, which ignores directories starting with underscores.

    This site depends on serving paths under /docs, so we force a .nojekyll file
    to exist after freezing (the freeze step may wipe the destination).

    Also cleans up legacy freeze artifacts that can cause guardrail failures.
    """
    dest = app.config.get("FREEZER_DESTINATION") or "docs"
    try:
        os.makedirs(dest, exist_ok=True)
        with open(os.path.join(dest, ".nojekyll"), "w", encoding="utf-8") as f:
            f.write("")

        # Legacy artifact: older /drafts route froze to docs/drafts (no extension).
        # We now serve drafts at /drafts.html. Remove the old file if it exists.
        legacy = os.path.join(dest, "drafts")
        if os.path.isfile(legacy):
            os.remove(legacy)
    except OSError:
        # Non-fatal; freezing succeeded but Pages might behave oddly.
        pass


if __name__ == "__main__":
    freezer.freeze()
    _ensure_nojekyll()

