from flask_frozen import Freezer
from app import app  # Replace with your app's actual import

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
