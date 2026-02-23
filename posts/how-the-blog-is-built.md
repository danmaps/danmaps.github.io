---
title: How the Blog Is Built
date: 2025-05-15
tags:
  - Meta
  - Workflow
---

I wanted a space where I could draft ideas fast and publish them without negotiating with a heavyweight CMS or JavaScript framework. The solution is this tiny Flask app: it reads Markdown files from `posts/`, extracts front-matter metadata with YAML, and renders everything with Jinja templates.

There’s no database, no admin console, and no notion of components that need compiling. Writing is nothing more than dropping a `.md` file into the repository. The Python code walks the directory, sorts the posts by date, and injects each file into a simple layout. The retro styling and new animated background come from hand-written CSS and a WebGL snippet that only runs on the homepage.

Keeping it lightweight means I can swap laptops, edit in any text editor, and still publish by pushing Markdown. I get syntax-highlighted code blocks through Markdown extensions, Prism for inline snippets, and zero build step beyond `flask run`. This workflow keeps the focus on the words, not on wrestling with a “real” block framework just to ship a post.

## Drafts and unlisted posts

I keep WIP posts in the repo but hide them from the homepage.

- Add `stub` or `draft` to the YAML front matter `tags:` list.
- The homepage template filters out posts tagged **Stub** or **Draft**.
- The post still renders if you know the URL (`/post/<filename>.html`), so it is effectively unlisted.

## Publishing

When I’m ready to publish:

1. Remove `stub` / `draft` from the tags
2. Run the freeze step to generate the static site into `docs/`:
   ```bash
   python freeze.py
   ```
3. Commit and push
