# POSTING.md

This repo is Danny McVey's blog and GitHub Pages site.

## Purpose

Use this repo to draft, edit, build, and publish blog posts for `https://danmaps.github.io/`.

## Authoring model

Posts live in:
- `posts/`

Each post is a Markdown file with YAML front matter:

```yaml
---
title: Example Title
date: 2026-03-16
tags:
  - Draft
  - AI
  - GIS
---
```

Then the body is plain Markdown.

## File naming

Use:
- `YYYY-MM-DD-short-slug.md`

Examples:
- `2026-03-16-building-trustworthy-agents.md`
- `2026-03-16-what-i-learned-from-rebuilding-my-stack.md`

## Drafts

Draft posts must include at least one of these tags:
- `Draft`
- `Stub`
- `Unlisted`

The site hides these from the homepage, but they may still exist in the generated site if someone knows the URL.

## Publishing workflow

### Draft a post
1. Create a Markdown file in `posts/`
2. Include `Draft` in tags
3. Match Danny's style:
   - practical
   - clear
   - opinionated
   - systems-minded
   - not hypey
4. Base claims on real work, real experiments, or real observations

### Prepare to publish
1. Remove `Draft` / `Stub` / `Unlisted` tags
2. Verify title, date, and tags
3. Build the static site:
   ```bash
   python freeze.py
   ```
4. Review changes in `docs/`
5. Commit and push

## Style guidance

Good post types for this repo:
- GIS + AI workflows
- practical agent engineering
- software/tooling lessons
- productivity and leverage
- systems and career reflections grounded in real work

Avoid:
- empty hype
- invented wins
- vague AI futurism with no operational insight
- filler intros that take too long to get to the point

## Images and assets

Use `static/` for assets when needed.
Reference them with site-root paths like:
- `/static/images/example.png`

## Useful local commands

Run the dev server:
```bash
python app.py
```

Freeze the static site:
```bash
python freeze.py
```

## Safety rule

Do not publish automatically unless Danny explicitly asks.
Drafting is fine. Publishing is a separate decision.
