import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from flask import render_template
from app import app


class ArticleLayoutTests(unittest.TestCase):
    def test_reading_features_do_not_depend_on_layout_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('app.POSTS_DIR', directory):
                for layout in ['', 'layout: default\n', 'layout: rich\n']:
                    with self.subTest(layout=layout):
                        Path(directory, 'example.md').write_text(
                            '---\ntitle: Example\ndate: 2026-10-29\n' + layout
                            + '---\n## First section\nText[^1]\n\n'
                            + '## Second section\nMore text.\n\n[^1]: A footnote.\n',
                            encoding='utf-8',
                        )
                        response = app.test_client().get('/post/example.html')
                        self.assertEqual(response.status_code, 200)
                        for feature in ['class="scroll-progress"', 'id="post-toc-list"',
                                        'post-reading.js', 'class="reading-time"',
                                        'datetime="2026-10-29"', 'map-embed.js',
                                        'leaflet.css', 'id="first-section"', 'class="footnote"']:
                            self.assertIn(feature, response.text)
                        self.assertNotIn('post-reading-legacy', response.text)

    def test_old_template_name_is_an_alias_of_the_shared_template(self):
        with app.test_request_context():
            data = dict(title='Example', content='<p>Example</p>', pygments_css='',
                        tag_objs=[], date=datetime(2026, 10, 29), reading_time=1)
            self.assertEqual(render_template('post.html', **data),
                             render_template('post_rich.html', **data))
