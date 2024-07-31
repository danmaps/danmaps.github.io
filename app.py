from flask import Flask, render_template, abort
import markdown
from pygments.formatters import HtmlFormatter
import os
from markdown.extensions import Extension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.preprocessors import Preprocessor


class CodeHiliteWithLanguageExtension(Extension):
    def extendMarkdown(self, md):
        md.registerExtension(self)
        md.preprocessors.register(CodeHiliteWithLanguagePreprocessor(md), 'codehilite_with_language', 30)

class CodeHiliteWithLanguagePreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        in_code_block = False
        language = None
        
        for line in lines:
            if line.startswith('```'):
                if in_code_block:
                    # Closing code block
                    new_lines.append('</code></pre>')
                    in_code_block = False
                else:
                    # Opening code block
                    language = line.strip('`')
                    if not language:
                        language = 'text'  # Default to 'text' if no language is provided
                    new_lines.append(f'<pre><code class="language-{language}">')
                    in_code_block = True
            elif in_code_block:
                new_lines.append(line)
            else:
                new_lines.append(line)
        
        # If the code block wasn't closed, close it here
        if in_code_block:
            new_lines.append('</code></pre>')
        
        return new_lines

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

        # Convert markdown to HTML with syntax highlighting
        html_content = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
        # Convert markdown to HTML with syntax highlighting and language classes
        html_content = markdown.markdown(content, extensions=[
            'fenced_code',
            CodeHiliteWithLanguageExtension(),
            CodeHiliteExtension(pygments_style='monokai', noclasses=True)
        ])

        # Include the CSS for Pygments
        formatter = HtmlFormatter(style='monokai', full=True, cssclass='codehilite')
        pygments_css = formatter.get_style_defs()

        # Check if 'streamlit' is in the post_name to decide whether to embed the app
        embed_streamlit = 'streamlit' in post_name.lower()

        return render_template('post.html', content=html_content, title=post_name, pygments_css=pygments_css, embed_streamlit=embed_streamlit)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)

