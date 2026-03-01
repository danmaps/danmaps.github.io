from flask import Flask, render_template, abort, send_from_directory
import markdown
from pygments.formatters import HtmlFormatter
import os
import re
import unicodedata
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

# flask-frozen will try to freeze every route it discovers. Some routes exist only
# for runtime convenience or back-compat and should not be emitted as static files.
# Keeping these out of the freeze avoids noisy warnings during builds.
app.config['FREEZER_IGNORE_ENDPOINTS'] = [
    'drafts_redirect',  # /drafts -> /drafts.html redirect
    'beta_static',      # /beta/* dev/beta assets (not part of the main frozen site)
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to your markdown files
POSTS_DIR = os.path.join(BASE_DIR, 'posts')
BETA_BUILD_DIR = os.path.join(BASE_DIR, 'build', 'beta')

UNPUBLISHED_TAGS = {"Stub", "Draft", "Unlisted"}


def _normalize_tags(raw_tags) -> list[str]:
    # Make tags proper case, if the tag is not already all caps
    tags = [tag.title() if isinstance(tag, str) and not tag.isupper() else tag for tag in (raw_tags or [])]

    # a few canonical replacements
    tags = [t.replace("Arcgis Pro", "ArcGIS Pro") if isinstance(t, str) else t for t in tags]
    tags = [t.replace("Ai", "AI") if isinstance(t, str) else t for t in tags]
    tags = [t.replace("Gis", "GIS") if isinstance(t, str) else t for t in tags]

    # filter empties + coerce to strings
    return [str(t).strip() for t in tags if str(t).strip()]


def tag_slug(tag: str) -> str:
    """Convert a display tag into a stable URL slug."""
    if not tag:
        return ""

    # normalize unicode
    value = unicodedata.normalize("NFKD", str(tag))
    value = value.encode("ascii", "ignore").decode("ascii")

    value = value.lower().strip()
    value = value.replace("&", "and")
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value)
    value = re.sub(r"^-+|-+$", "", value)
    return value


def _parse_post_file(filename: str) -> dict | None:
    """Parse a markdown post and return metadata for lists (not full HTML)."""
    if not filename.endswith('.md'):
        return None

    with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    metadata = {}
    body = content

    # Try to parse YAML front matter
    try:
        if content.startswith('---'):
            _, front_matter, body = content.split('---\n', 2)
            metadata = yaml.safe_load(front_matter) or {}
    except (ValueError, IndexError, yaml.YAMLError):
        metadata = {}

    title = metadata.get('title', filename[:-3])
    date_str = metadata.get('date')

    if isinstance(date_str, str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    elif isinstance(date_str, datetime):
        date_obj = date_str
    elif isinstance(date_str, date):
        date_obj = datetime.combine(date_str, datetime.min.time())
    else:
        file_creation_time = os.path.getctime(os.path.join(POSTS_DIR, filename))
        date_obj = datetime.fromtimestamp(file_creation_time)

    tags = _normalize_tags(metadata.get('tags', []))
    tag_objs = [{"name": t, "slug": tag_slug(t)} for t in tags if t not in UNPUBLISHED_TAGS]

    return {
        'name': filename[:-3],
        'title': title,
        'date': date_obj,
        'tags': tags,
        'tag_objs': tag_objs,
    }


def _list_posts() -> list[dict]:
    posts = []
    for f in os.listdir(POSTS_DIR):
        parsed = _parse_post_file(f)
        if parsed:
            posts.append(parsed)

    # Stable ordering across OS/filesystems: break date ties by filename.
    posts.sort(key=lambda x: (x['date'], x['name']), reverse=True)
    return posts


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
    posts = _list_posts()
    return render_template('index.html', posts=posts, UNPUBLISHED_TAGS=UNPUBLISHED_TAGS)


@app.route('/drafts')
def drafts_redirect():
    """Back-compat redirect to the canonical drafts URL."""
    from flask import redirect
    return redirect('/drafts.html', code=302)


@app.route('/drafts.html')
def drafts():
    """List unpublished posts (Draft/Unlisted/Stub).

    Warning: this makes unpublished posts discoverable if you publish the frozen site.
    If you want truly private drafts, keep them out of the repo or serve behind auth.
    """
    posts = _list_posts()
    return render_template('drafts.html', posts=posts)


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
        date_str = metadata.get('date')

        tags = _normalize_tags(metadata.get('tags', []))
        tag_objs = [{"name": t, "slug": tag_slug(t)} for t in tags if t not in UNPUBLISHED_TAGS]

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
        return render_template(
            'post.html',
            content=html_content,
            title=title,
            pygments_css=pygments_css,
            tags=tags,
            tag_objs=tag_objs,
            date=date_obj,
        )
        
    
    except FileNotFoundError:
        abort(404)


@app.route('/tag/<tag_slug_value>.html')
def tag(tag_slug_value: str):
    posts = _list_posts()

    # Find canonical display tag for this slug
    canonical = None
    for p in posts:
        for t in p.get('tags', []):
            if tag_slug(t) == tag_slug_value:
                canonical = t
                break
        if canonical:
            break

    if not canonical:
        abort(404)

    # Filter posts by tag + hide unpublished
    filtered = []
    for p in posts:
        if any(t == canonical for t in p.get('tags', [])):
            if any(t in UNPUBLISHED_TAGS for t in p.get('tags', [])):
                continue
            filtered.append(p)

    return render_template('tag.html', tag_name=canonical, posts=filtered, UNPUBLISHED_TAGS=UNPUBLISHED_TAGS)


if __name__ == '__main__':
    # Get the port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 to make the server accessible externally
    app.run(host='0.0.0.0', port=port)

