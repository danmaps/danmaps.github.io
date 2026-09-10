const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const html = fs.readFileSync("static/gis-from-scratch/tinygis.html", "utf8");
const core = html.match(/<script id="gis-core">([\s\S]*?)<\/script>/)[1];
const G = vm.runInNewContext(core + "\nTinyGIS;");
const same = (value) => JSON.parse(JSON.stringify(value));
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-7, `${a} != ${b}`);

test("both transforms round trip and pointer-anchored zoom holds position", () => {
  const view = { cx: -117.2, cy: 34.05, scale: 2300 },
    p = [-117.19, 34.1];
  const screen = G.toScreen(p, view, 730, 310);
  G.toMap(screen, view, 730, 310).forEach((n, i) => near(n, p[i]));
  const next = G.zoomAt(view, [123, 87], 1.5, 730, 310);
  G.toMap([123, 87], next, 730, 310).forEach((n, i) =>
    near(n, G.toMap([123, 87], view, 730, 310)[i]),
  );
});
test("Mercator agrees with PROJ reference and clamps poles to finite values", () => {
  const projected = G.project([2, 49], true);
  assert.ok(Math.abs(projected[0] - 222638.98) < 0.01);
  assert.ok(Math.abs(projected[1] - 6274861.39) < 0.01);
  G.unproject(projected, true).forEach((n, i) => near(n, [2, 49][i]));
  assert.ok(G.project([0, 90], true).every(Number.isFinite));
});
test("sample demonstrates bbox false positives and explicit boundary policy", () => {
  const data = G.sampleData();
  G.validateGeoJSON(data);
  const rings = data.features[0].geometry.coordinates;
  const points = data.features.filter((f) => f.geometry.type === "Point");
  assert.deepEqual(
    same(
      points
        .filter((f) => G.inPolygon(f.geometry.coordinates, rings))
        .map((f) => f.id),
    ),
    ["A", "C", "F"],
  );
  assert.deepEqual(
    same(
      points
        .filter((f) => G.inBox(f.geometry.coordinates, G.bbox(rings.flat())))
        .map((f) => f.id),
    ),
    ["A", "B", "C", "E", "F"],
  );
  assert.equal(G.inPolygon([-117.19, 34.07], rings), false); // hole edge
  assert.equal(G.inPolygon(rings[0][0], rings), true); // exterior vertex
  assert.equal(G.inPolygon([-117.18, 34.065], rings), false);
});
test("grid returns exactly the scan IDs including negative cells and cell edges", () => {
  const points = [
    [-100, -100],
    [0, 0],
    [100, 100],
    [99, 101],
    ...G.randomPoints(50000),
  ];
  const grid = G.makeGrid(points, 100);
  for (const bounds of [
    [420, 420, 580, 580],
    [-100, -100, 100, 100],
    [0, 0, 1000, 1000],
    [2000, 2000, 2010, 2010],
  ]) {
    const scan = points.flatMap((p, i) => (G.inBox(p, bounds) ? [i] : []));
    const indexed = G.gridCandidates(grid, bounds)
      .filter((i) => G.inBox(points[i], bounds))
      .sort((a, b) => a - b);
    assert.deepEqual(same(indexed), scan);
  }
});
test("import validates all six types and rejects malformed, nonfinite and unsupported geometry", () => {
  const wrap = (type, coordinates) => ({
    type: "FeatureCollection",
    features: [
      { type: "Feature", properties: null, geometry: { type, coordinates } },
    ],
  });
  const ring = [
      [0, 0],
      [1, 0],
      [1, 1],
      [0, 0],
    ],
    line = [
      [0, 0],
      [1, 1],
    ];
  for (const [type, c] of [
    ["Point", [0, 0]],
    [
      "MultiPoint",
      [
        [0, 0],
        [1, 1],
      ],
    ],
    ["LineString", line],
    ["MultiLineString", [line, line]],
    ["Polygon", [ring]],
    ["MultiPolygon", [[ring], [ring]]],
  ])
    assert.doesNotThrow(() => G.validateGeoJSON(wrap(type, c)));
  for (const [type, c] of [
    ["Point", [NaN, 0]],
    ["Point", [181, 0]],
    ["LineString", [[1, 1]]],
    [
      "Polygon",
      [
        [
          [0, 0],
          [1, 0],
          [1, 1],
          [0, 1],
        ],
      ],
    ],
    [
      "LineString",
      [
        [179, 1],
        [-179, 1],
      ],
    ],
    ["GeometryCollection", []],
  ])
    assert.throws(() => G.validateGeoJSON(wrap(type, c)));
  assert.throws(() =>
    G.validateGeoJSON({ type: "FeatureCollection", features: [] }),
  );
});
test("zero-length line segments are handled", () => {
  near(G.segmentDistance([3, 4], [0, 0], [0, 0]), 5);
});
test("widget scripts and JavaScript article snippets parse", () => {
  const scripts = [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)];
  scripts.forEach((s) => {
    if (s[0].startsWith('<script id="basemap-config" type="application/json">')) JSON.parse(s[1]);
    else new vm.Script(s[1]);
  });
  const article = fs.readFileSync(
    "posts/2026-09-10-gis-from-scratch.md",
    "utf8",
  );
  for (const [, source] of article.matchAll(/```javascript\n([\s\S]*?)\n```/g))
    new vm.Script("(async()=>{" + source + "})");
});
