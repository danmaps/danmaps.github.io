import re
import unittest
from datetime import datetime
from html.parser import HTMLParser

from flask import render_template

from app import app, _list_posts, _published_posts


class TagLinks(HTMLParser):
    def __init__(self, css_class):
        super().__init__()
        self.css_class = css_class
        self.links = []
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and self.css_class in attrs.get('class', '').split():
            self.current = {'href': attrs.get('href'), 'name': ''}

    def handle_data(self, data):
        if self.current is not None:
            self.current['name'] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current)
            self.current = None


class TagDisplayTests(unittest.TestCase):
    def assert_tag_links(self, html, css_class, tags):
        parsed = TagLinks(css_class)
        parsed.feed(html)
        self.assertEqual(parsed.links, [
            {'href': f"/tag/{tag['slug']}.html", 'name': tag['name']}
            for tag in tags
        ])

    def test_homepage_cards_show_all_tags_and_hide_drafts(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        cards = re.findall(r'<article class="home-post-card">([\s\S]*?)</article>', response.text)
        all_posts = _list_posts()
        published = _published_posts(all_posts)
        posts = published[:6]
        self.assertEqual(len(cards), len(posts))
        for card, post in zip(cards, posts):
            with self.subTest(post=post['name']):
                self.assertIn(f"/post/{post['name']}.html", card)
                self.assert_tag_links(card, 'home-post-tag', post['tag_objs'])
        for post in all_posts:
            if post not in published:
                self.assertNotIn(f"/post/{post['name']}.html", response.text)

    def test_both_post_headers_handle_zero_one_and_four_tags(self):
        tags = [
            {'name': name, 'slug': slug}
            for name, slug in [('AI', 'ai'), ('Agents', 'agents'), ('Systems', 'systems'), ('GitHub', 'github')]
        ]
        with app.test_request_context():
            for template in ['post.html', 'post_rich.html']:
                for count in [0, 1, 4]:
                    with self.subTest(template=template, count=count):
                        html = render_template(
                            template, title='Tag display', content='<p>Example</p>',
                            pygments_css='', tag_objs=tags[:count],
                            date=datetime(2026, 9, 10), reading_time=1,
                        )
                        header = re.search(r'<header class="post-hero[^"]*"[\s\S]*?</header>', html).group()
                        self.assert_tag_links(header, 'post-kicker', tags[:count])
                        self.assertEqual('post-kicker-row' in header, count > 0)

    def test_post_routes_show_all_topical_tags_in_headers(self):
        client = app.test_client()
        for post in _list_posts():
            with self.subTest(post=post['name']):
                response = client.get(f"/post/{post['name']}.html")
                self.assertEqual(response.status_code, 200)
                header = re.search(r'<header class="post-hero[^"]*"[\s\S]*?</header>', response.text).group()
                self.assert_tag_links(header, 'post-kicker', post['tag_objs'])


if __name__ == '__main__':
    unittest.main()
