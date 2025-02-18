from flask import Flask, render_template, abort
import markdown
from pygments.formatters import HtmlFormatter
import os
from markdown.extensions import Extension
from markdown.extensions import tables
from markdown.extensions import lists
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

# Path to your markdown files
POSTS_DIR = 'posts'
@app.route('/')
def index():
    posts = []
    for f in os.listdir(POSTS_DIR):
        # print file name for debugging
        print(f)
        if f.endswith('.md'):
            with open(os.path.join(POSTS_DIR, f), 'r', errors='ignore') as file:
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

@app.route('/post/<post_name>.html')
def post(post_name):
    try:
        with open(os.path.join(POSTS_DIR, f'{post_name}.md'), 'r') as f:
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
            'lists',
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

