from flask_frozen import Freezer
from app import app

# Publish the static site into /docs so GitHub Pages can serve it from the master branch.
# (User/Org Pages work best from the default branch + /docs.)
app.config["FREEZER_DESTINATION"] = "docs"

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

