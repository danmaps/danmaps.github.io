import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from app import app

SLUG = '2026-09-10-gis-from-scratch'

class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.scripts = []
        self.pre = False
        self.code = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'iframe': self.frames.append(attrs)
        if tag == 'script': self.scripts.append((attrs, self.pre))
        if tag == 'pre': self.pre = True
    def handle_endtag(self, tag):
        if tag == 'pre': self.pre = False
    def handle_data(self, data):
        if self.pre: self.code.append(data)

class ArticleTests(unittest.TestCase):
    def test_render_embeds_assets_and_safe_code(self):
        client = app.test_client()
        response = client.get(f'/post/{SLUG}.html')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Working draft · Interactive tutorial', response.text)
        parsed = Tags(); parsed.feed(response.text)
        self.assertEqual(len(parsed.frames), 8)
        self.assertEqual(len({f['title'] for f in parsed.frames}), 8)
        for frame in parsed.frames:
            with client.get(frame['src'].replace('../', '/')) as result:
                self.assertEqual(result.status_code, 200)
        # The tutorial's <script> is displayed inside <pre>, not executed.
        self.assertTrue(all(not inside_pre for script, inside_pre in parsed.scripts))
        source_blocks = re.findall(r'```(?:html|javascript)\n([\s\S]*?)\n```', Path(f'posts/{SLUG}.md').read_text())
        rendered_code = ''.join(parsed.code)
        for block in source_blocks:
            self.assertIn(block, rendered_code)
        for asset in ['article.css', 'embeds.js', 'tinygis.html']:
            with client.get('/static/gis-from-scratch/' + asset) as result:
                self.assertEqual(result.status_code, 200)

    def test_draft_is_listed_only_as_draft(self):
        client = app.test_client()
        for path in ['/', '/all-posts.html', '/tag/gis.html', '/tag/systems.html']:
            self.assertNotIn(SLUG, client.get(path).text)
        self.assertIn(SLUG, client.get('/drafts.html').text)

if __name__ == '__main__': unittest.main()
