# GIS from scratch experiments

Source article: `posts/2026-09-10-gis-from-scratch.md`.
Adapted from Danny's Google Drive draft, “GIS from scratch: Learning about web mapping by making a web GIS with only vanilla js.”:
https://docs.google.com/document/d/1KRPwmfW_iQcjBk8xFZQ1QxsLkuajblmAdhJ3gkJCvAU/edit

`tinygis.html` is the runnable source and the reader download. It contains its own CSS, sample GeoJSON, pure geometry functions, and UI. It has no runtime dependencies, tile requests, API keys, backend, or network requests. Open it directly in a browser. The named `gis-core` and `gis-ui` script blocks separate the math from the interface without requiring a build.

## Reusable article convention

Build on the numpad post's iframe pattern. Each experiment follows this sequence:

1. Explain a familiar GIS operation before introducing its JavaScript.
2. Ask the reader to predict a specific, observable change.
3. Embed a focused experiment with a unique descriptive title.
4. Explain the result, including an edge case where useful.
5. Link to complete runnable source and distinguish excerpts from standalone examples.

Use `layout: rich`, a `gis-experiment` figure, and an iframe with `data-tinygis`, `title`, `loading="lazy"`, and an initial `height`. Include `article.css` and `embeds.js` once in the article. The existing post template supplies copy buttons and a table of contents. Other posts do not load these assets.

`embeds.js` accepts resize messages only from a known iframe window on the same origin. Each iframe has independent data, view and selection state. The maps follow the device color scheme, offer keyboard navigation and labeled controls, and require explicit activation before capturing drag/wheel gestures. Feature tables provide an alternative to spatial picking. They display the first 50 records; all supported records remain available to the renderer and query.

Lesson values: `pixels`, `view`, `layers`, `identify`, `query`, `index`, `projection`, `lab`. No query parameter opens `lab`.

## Scope and deliberate policies

- Synthetic Redlands examples, not real assets or hazard data.
- GeoJSON FeatureCollection input: Point, MultiPoint, LineString, MultiLineString, Polygon and MultiPolygon. Basic validation only; no topology repair, antimeridian wrapping, GeometryCollection or null geometry.
- Maximum 2 MB / 50,000 positions; nonempty drawable collections on import. Empty selection exports are valid, but the loader rejects them with an explanation.
- Selections use array indices and clear on data replacement. Imported IDs and properties are preserved on export.
- Location query selects Point features in any Polygon/MultiPolygon, regardless of visibility or current extent. MultiPoint is not included in this teaching query.
- Outer boundary included; hole boundaries excluded. The segment boundary tolerance is 1e-10 input degrees. Intended for small, valid, planar teaching geometries.
- Working lab uses longitude/latitude directly. Web Mercator is isolated to the projection lesson, with source data unchanged.
- Index benchmark uses a deterministic Cartesian dataset; reports scan time, index build time and existing-index query time separately. Drawing is excluded.

## Verification

Run from the repository root with the site's Python requirements installed:

```sh
node --test tests/tinygis.test.cjs
python -m unittest discover -s tests -p 'test_*.py'
```

The checks cover inverse transforms, pointer-anchored zoom, a PROJ reference coordinate, hole/boundary selection, scan/grid equality, all supported geometry types, malformed input, excerpt syntax, article code escaping, iframe asset routes and unpublished filtering.

Manual review before publishing: try every lesson on desktop and a narrow touch device; open and close the data editor; check iframe height updates; navigate with the keyboard; import a local file; export A/C/F and reload it. No automated browser interaction or screenshot review was performed for this draft.

Keep the post's `Draft` tag until Danny asks to publish. Follow repository publishing instructions for generated output; do not maintain copies of the map code by hand under `docs/`.
