# AGENTS.md

Repo-specific instructions for agents working in this blog repository.

## What this repo is

This is Danny McVey's personal blog / GitHub Pages repo.

Primary content source:
- `posts/*.md`

Rendering/build system:
- `app.py`
- `templates/`
- `static/`
- generated site output in `docs/`

## Main rules

1. **Do not auto-publish.**
   - Drafting and editing are allowed.
   - Publishing requires explicit user intent.

2. **Prefer drafting over shipping.**
   - New posts should default to `Draft` in front matter unless the user clearly asks to publish.

3. **Do not invent experiences or outcomes.**
   - Posts should be grounded in real work, real experiments, real code, real notes, or real opinions.

4. **Match Danny's voice.**
   The voice should be:
   - practical
   - clear
   - direct
   - thoughtful
   - mildly opinionated
   - systems-minded
   - low on hype

5. **Keep structure simple.**
   Favor:
   - strong opening frame
   - a few clean sections
   - concrete examples
   - clear takeaway

## Front matter contract

Use YAML front matter like:

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

## Filename contract

Use:
- `YYYY-MM-DD-short-slug.md`

## Draft workflow

When asked to draft a post:
1. Create the file in `posts/`
2. Include `Draft` in tags
3. Keep claims honest and specific
4. Do not run publish steps unless explicitly requested

## Publish workflow

Only when explicitly asked:
1. Remove `Draft` / `Stub` / `Unlisted` tags
2. Run:
   ```bash
   python freeze.py
   ```
3. Review resulting changes in `docs/`
4. Commit and push if requested

## Good topics

High-fit topics include:
- GIS + AI
- geospatial tooling
- agent engineering
- workflow design
- practical software lessons
- product thinking
- career leverage grounded in technical work

## Avoid

- generic listicles
- fake confidence
- overuse of em dashes and slogan-y lines
- corporate assistant tone
- bloated introductions
- publishing without review
