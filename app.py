from flask import Flask, render_template, abort
from markdown2 import markdown
import os

app = Flask(__name__)

# Path to your markdown files
POSTS_DIR = 'posts'



@app.route('/')
def index():
    # List all markdown files in the posts directory
    posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    return render_template('index.html', posts=posts)

@app.route('/post/<post_name>')
def post(post_name):
    try:
        # Load the markdown file
        with open(os.path.join(POSTS_DIR, f'{post_name}.md'), 'r') as f:
            content = f.read()

        # Convert markdown to HTML
        html_content = markdown(content)

        return render_template('post.html', content=html_content, title=post_name)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
