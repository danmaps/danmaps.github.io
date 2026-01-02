from flask import Flask, render_template, abort, send_from_directory
import markdown
from pygments.formatters import HtmlFormatter
import os
from markdown.extensions import Extension
from markdown.extensions import tables
from markdown.extensions import sane_lists
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.preprocessors import Preprocessor
import yaml
from datetime import datetime, date
import random

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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to your markdown files
POSTS_DIR = os.path.join(BASE_DIR, 'posts')
BETA_BUILD_DIR = os.path.join(BASE_DIR, 'build', 'beta')


def _resolve_beta_resource(resource: str) -> str | None:
    """Return the relative path to a beta asset if it exists."""
    if not os.path.isdir(BETA_BUILD_DIR):
        return None

    cleaned = (resource or '').strip()
    cleaned = cleaned.lstrip('/\\')
    cleaned = cleaned.rstrip('/\\')
    if not cleaned:
        cleaned = 'index.html'

    candidate = os.path.join(BETA_BUILD_DIR, cleaned)
    if os.path.isdir(candidate):
        cleaned = os.path.join(cleaned, 'index.html')
        candidate = os.path.join(BETA_BUILD_DIR, cleaned)

    if os.path.isfile(candidate):
        return cleaned.replace('\\', '/')

    return None

@app.route('/')
def index():
    posts = []
    for f in os.listdir(POSTS_DIR):
        # print file name for debugging
        print(f)
        if f.endswith('.md'):
            with open(os.path.join(POSTS_DIR, f), 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                metadata = {}
                body = content
                
                # Try to parse YAML front matter
                try:
                    if content.startswith('---'):
                        _, front_matter, body = content.split('---\n', 2)
                        metadata = yaml.safe_load(front_matter)
                except (ValueError, IndexError, yaml.YAMLError):
                    pass

                # Extract or default title and date
                title = metadata.get('title', f[:-3])
                date_str = metadata.get('date')
                
                if isinstance(date_str, str):
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                elif isinstance(date_str, datetime):
                    date_obj = date_str
                elif isinstance(date_str, date):
                    # Convert date to datetime for consistency
                    date_obj = datetime.combine(date_str, datetime.min.time())
                else:
                    # Fallback to the file's creation date
                    file_creation_time = os.path.getctime(os.path.join(POSTS_DIR, f))
                    date_obj = datetime.fromtimestamp(file_creation_time)

                               
                # Make tags proper case, if the tag is not already all caps
                tags = [tag.title() if not tag.isupper() else tag for tag in metadata.get('tags', [])]
                # if the tag is "Arcgis Pro", replace it with "ArcGIS Pro"
                if "Arcgis Pro" in tags:
                    tags = [tag.replace("Arcgis Pro", "ArcGIS Pro") for tag in tags]
                if "Ai" in tags:
                    tags = [tag.replace("Ai", "AI") for tag in tags]
                if "Gis" in tags:
                    tags = [tag.replace("Gis", "GIS") for tag in tags]


                posts.append({
                    'name': f[:-3],  # Remove the .md extension
                    'title': title,
                    'date': date_obj,
                    'tags': tags,
                })

    # Sort posts by date in descending order (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    # sort posts randomly
    # posts.sort(key=lambda x: random.random())

    return render_template('index.html', posts=posts)


@app.route('/beta', defaults={'resource': ''}, strict_slashes=False)
@app.route('/beta/<path:resource>')
def beta_static(resource: str):
    resolved = _resolve_beta_resource(resource)
    if not resolved:
        abort(404)
    return send_from_directory(BETA_BUILD_DIR, resolved)


@app.route('/post/<post_name>.html')
def post(post_name):
    try:
        with open(os.path.join(POSTS_DIR, f'{post_name}.md'), 'r', encoding='utf-8') as f:
            content = f.read()

        # Split the content to remove the YAML front matter
        try:
            _, front_matter, body = content.split('---', 2)
            metadata = yaml.safe_load(front_matter)
        except (ValueError, IndexError, yaml.YAMLError):
            metadata = {}
            body = content  # If there's no front matter, use the whole content

        # Extract title, tags, and date from metadata
        title = metadata.get('title', post_name)
        tags = metadata.get('tags', [])
        date_str = metadata.get('date')

        # Make tags proper case, if the tag is not already all caps
        tags = [tag.title() if not tag.isupper() else tag for tag in metadata.get('tags', [])]
        # if the tag is "Arcgis Pro", replace it with "ArcGIS Pro"
        if "Arcgis Pro" in tags:
            tags = [tag.replace("Arcgis Pro", "ArcGIS Pro") for tag in tags]

        # Handle date conversion if needed
        if isinstance(date_str, str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        elif isinstance(date_str, datetime):
            date_obj = date_str
        elif isinstance(date_str, date):
            # Convert date to datetime for consistency
            date_obj = datetime.combine(date_str, datetime.min.time())
        else:
            # Fallback to the file's creation date
            file_creation_time = os.path.getctime(os.path.join(POSTS_DIR, f'{post_name}.md'))
            date_obj = datetime.fromtimestamp(file_creation_time)

        # Convert markdown to HTML with syntax highlighting
        html_content = markdown.markdown(body, extensions=[
            'fenced_code',
            'codehilite',
            'tables',
            'nl2br',
            'sane_lists',
            CodeHiliteWithLanguageExtension(),
            CodeHiliteExtension(pygments_style='monokai', noclasses=True)
        ])

        # various replacements to clean up output from chatgpt
        # replace â€™ with ' in html_content to fix issue where '’' shows up in html as 'â€™'
        html_content = html_content.replace('â€™', '\'')
        html_content = html_content.replace('\\n---\\n', '\\n<hr>')
        html_content = html_content.replace('---', '—')
        html_content = html_content.replace('â€”', '—')
        html_content = html_content.replace('â€˜', '\'')

        # Include the CSS for Pygments
        formatter = HtmlFormatter(style='monokai', full=True, cssclass='codehilite')
        pygments_css = formatter.get_style_defs()

        # Render the template with all necessary data
        return render_template('post.html', content=html_content, title=title, pygments_css=pygments_css, tags=tags, date=date_obj)
        
    
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 to make the server accessible externally
    app.run(host='0.0.0.0', port=port)

