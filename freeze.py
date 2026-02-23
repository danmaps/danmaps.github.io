from flask_frozen import Freezer
from app import app, POSTS_DIR
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


if __name__ == "__main__":
    freezer.freeze()

