---
title: Rich Formatting Demo
date: 2026-06-11
tags:
  - Draft
  - Meta
layout: rich
---

This post is a kitchen-sink demo of every formatting element the blog renders. Use it to verify new styles, spot regressions, or just see what is available when writing a post.

---

## Headings

# H1 — post title level (use sparingly inside body)
## H2 — main section
### H3 — subsection
#### H4 — rarely needed

---

## Paragraphs and inline formatting

Plain prose with **bold**, *italic*, `inline code`, and a [link to the homepage](/).

You can also mix **bold and `code`** in the same sentence without things falling apart.

---

## Blockquotes

> The real bottleneck often isn't missing intelligence. It's missing shape.

Multi-line blockquote:

> Keeping it lightweight means I can swap laptops, edit in any text editor,
> and still publish by pushing Markdown.
> The workflow keeps the focus on the words.

---

## Lists

Unordered:

- define a canonical layer model
- document the table-of-contents action model
- normalize multi-feature imports into single layers
- improve naming, badges, removal, and summaries

Ordered:

1. Create the post file in `posts/`
2. Include `Draft` in tags
3. Push to the repo
4. Remove the tag when ready to publish

Nested:

- Tools
  - GIS tools
    - Buffer
    - Clip
  - Dev tools
    - git
    - rg
- Models
  - Small / fast
  - High-end reasoning

---

## Code blocks

Python — with syntax highlighting and the copy button:

```python
import geopandas as gpd

gdf = gpd.read_file("input.geojson")
buffered = gdf.to_crs(epsg=3857).buffer(100)
print(buffered.head())
```

JavaScript:

```javascript
document.querySelectorAll('pre code').forEach((block) => {
  const lang = block.className.replace('language-', '') || 'text';
  const btn = document.createElement('button');
  btn.textContent = 'Copy';
  block.parentElement.prepend(btn);
});
```

Bash:

```bash
./scripts/freeze_and_stage.sh
git status
git add -p
git commit -m "publish: remove Draft tag"
```

YAML front matter example:

```yaml
---
title: Example Title
date: 2026-06-11
tags:
  - Draft
  - GIS
  - AI
---
```

Plain text / no language:

```
No language specified — falls back to plain pre/code block.
Line 2.
Line 3.
```

---

## Tables

Simple comparison table:

| Format element | Markdown syntax | Notes |
|---|---|---|
| Bold | `**text**` | Also `__text__` |
| Italic | `*text*` | Also `_text_` |
| Inline code | `` `code` `` | Backtick-wrapped |
| Blockquote | `> text` | Styled with blue left border |
| Fenced code | ` ```lang ` | Gets language label + copy button |
| Table | `| col |` | Full-width, dark-header |

Right-aligned numbers column:

| Model class | Latency | Typical use |
|---|---:|---|
| Small / fast | ~200 ms | Brainstorming, first drafts |
| Mid-tier reasoning | ~1.5 s | Workflow design, code generation |
| High-end reasoning | ~5 s | High-stakes spatial analysis |

---

## Horizontal rules

Three hyphens produce a styled `<hr>`:

---

---

## Retro text

The `.retro-text` CSS class produces a CRT-style terminal look. Drop raw HTML into the post to use it:

<p class="retro-text">SYSTEM ONLINE — spatial data loaded</p>

---

## Mixed content section

A realistic snippet with all elements together:

The task was to buffer every parcel by 50 m and flag those that overlap a flood zone.

```python
parcels = gpd.read_file("parcels.geojson").to_crs(epsg=3857)
flood   = gpd.read_file("flood_zones.geojson").to_crs(epsg=3857)

buffered = parcels.copy()
buffered["geometry"] = parcels.buffer(50)

at_risk = gpd.sjoin(buffered, flood, how="inner", predicate="intersects")
print(f"{len(at_risk)} parcels within 50 m of a flood zone")
```

> The dangerous case is when plausible-looking output masks a unit error. Always verify CRS before any distance operation.

Results:

| Parcel count | At-risk | Pct |
|---|---|---|
| 4,821 | 312 | 6.5% |

Takeaway: the join is fast but the CRS check is the real guard.

---

## End

That covers everything the blog currently renders. If a new formatting feature is added — callouts, diagrams, math — add a section here.

