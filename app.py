import os
from flask import Flask, render_template, abort
from markdown2 import markdown

app = Flask(__name__)

# Path to your markdown files
POSTS_DIR = 'posts'

@app.route('/')
def index():
    posts = [f[:-3] for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    return render_template('index.html', posts=posts)

@app.route('/post/<post_name>.html')
def post(post_name):
    try:
        with open(os.path.join(POSTS_DIR, f'{post_name}.md'), 'r') as f:
            content = f.read()

        html_content = markdown(content)

        # Check if 'streamlit' is in the post_name to decide whether to embed the app
        embed_streamlit = 'streamlit' in post_name

        return render_template('post.html', content=html_content, title=post_name, embed_streamlit=embed_streamlit)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 to make the server accessible externally
    app.run(host='0.0.0.0', port=port)
