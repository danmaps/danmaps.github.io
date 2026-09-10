---
title: "GIS from Scratch: Reinventing Web GIS Without External Libraries"
date: 2026-09-10
layout: rich
tags:
  - GIS
  - Javascript
---

Most of my web maps begin with a pile of abstractions already in place. I create a map, add a layer, attach an event handler, and call a query method. A few lines later, I can pan, zoom, identify a feature, and inspect its attributes. That is exactly what I want from a good mapping library.

But I can use that library for years without explaining what happens between a geographic coordinate and the pixel I click.

This is an attempt to close that gap. We are going to build a small web GIS using HTML, CSS, vanilla JavaScript, Canvas, and GeoJSON. No ArcGIS Maps SDK, MapLibre, Leaflet, OpenLayers, Turf, React, or npm packages in the map. The constraint is simple: **if the browser does not already know how to do it, we have to write it.**

<link rel="stylesheet" href="../static/gis-from-scratch/article.css">
<script defer src="../static/gis-from-scratch/embeds.js"></script>

If you know GIS but are new to JavaScript, you have the right starting point. You already understand extents, features, selections, and coordinate systems. We will give those ideas names in code, then make them do something you can see.

Each experiment below stands on its own. Change a control, predict the result, and check what happened. You can also [open the finished tiny GIS](../static/gis-from-scratch/tinygis.html) or <a href="../static/gis-from-scratch/tinygis.html" download="tinygis.html">download the complete HTML file</a>. The download opens directly in a browser. No installation or development server is needed.

The sample features sit near Redlands, California, but they are invented teaching data. The study area is not a real hazard boundary. Its awkward shape and its hole are there to make our assumptions visible.

## 1. Start with a point and a blank canvas

A canvas is a rectangular drawing surface. It does not know about feature classes, spatial references, or layers. It knows how to paint pixels.

Create a file called `first-point.html`, paste this complete example into it, and open it in your browser:

```html
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<title>My first point</title>
<canvas id="map" width="600" height="300">
  A blue point at pixel 300, 120.
</canvas>
<script>
  const canvas = document.querySelector("#map");
  const ctx = canvas.getContext("2d");

  ctx.fillStyle = "#265fc0";
  ctx.beginPath();
  ctx.arc(300, 120, 6, 0, Math.PI * 2);
  ctx.fill();
</script>
</html>
```

There are three languages in play throughout this project. HTML supplies elements such as the canvas and buttons. CSS controls their appearance. JavaScript reads data and responds to actions. This first file only needs HTML and JavaScript.

`const` gives a value a name. Here, `canvas` refers to the element whose ID is `map`; `ctx` refers to its drawing context. A dot accesses a property or method: `ctx.fillStyle` is a setting, while `ctx.fill()` calls an operation. The parentheses contain arguments to that operation.

Read `arc(300, 120, 6, 0, Math.PI * 2)` as: draw a circular arc centered at x = 300, y = 120, with radius 6, from angle zero through one full turn. `beginPath()` starts a new path, and `fill()` paints its interior. Nothing in that instruction means “geographic point.”

**Try this:** move y toward 300. Which direction should the point move?

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 1: move a point in canvas pixel coordinates" src="../static/gis-from-scratch/tinygis.html?lesson=pixels" loading="lazy" height="470"></iframe>
<figcaption>The sliders use a logical 600 × 300 canvas. Its displayed size adapts to your screen.</figcaption>
</figure>

Down. The browser puts the origin in the upper-left corner. Increasing y moves toward the bottom. Remember that when we introduce northings.

The rest of the code samples are focused excerpts, not instructions to keep appending code to `first-point.html`. Use the complete download when you want to change the working application. Search it for the function names shown here. That keeps each explanation small without hiding the supporting code.

## 2. Invent a map view

In GIS, the map extent tells us what portion of the data we can see. We can describe the same view with a center and a scale:

```javascript
const view = {
  cx: -117.18,
  cy: 34.07,
  scale: 2000
};
```

The braces create an **object**, a collection of named properties. `cx` and `cy` locate the view center in map coordinates. `scale` is the number of CSS pixels per map unit. It is not a representative fraction such as 1:24,000.

For now, we treat longitude and latitude as ordinary x and y values. The map unit is a degree. That is an explicit simplification for drawing and interaction, not a suitable distance measurement system.

This interaction model is usually called a **slippy map**: you grab the map itself, drag it continuously, and zoom without replacing the whole page. Google Maps made that pattern feel normal on the web after its 2005 launch, and it helped make page-at-a-time maps from the MapQuest era feel dated.

ANYWAY... to draw a point, measure its offset from the view center, multiply by the scale, and add the screen center. Subtract the y offset because screen y runs downward:

```javascript
function toScreen([x, y], view, width, height) {
  return [
    width / 2 + (x - view.cx) * view.scale,
    height / 2 - (y - view.cy) * view.scale
  ];
}
```

A `function` defines an operation we can reuse. The parameters are its inputs; `return` supplies its result. Square brackets create an **array**, an ordered list. In the parameter list, `[x, y]` unpacks the incoming coordinate pair into two names. JavaScript calls that destructuring. It saves us from repeatedly writing `coordinate[0]` and `coordinate[1]`.

We use one scale for both axes. Scaling x and y independently would squeeze the geometry to fit the canvas. Instead, the download fits the data by choosing whichever axis needs more room and leaving space on the other axis. Equal degree spacing still does not mean equal ground distance.

The inverse transformation is just as useful:

```javascript
function toMap([px, py], view, width, height) {
  return [
    view.cx + (px - width / 2) / view.scale,
    view.cy - (py - height / 2) / view.scale
  ];
}
```

Now we can translate in both directions. Draw a feature: map to screen. Interpret a click: screen to map.

**Try this:** enable map dragging and move the features to the right. Watch the extent. Then click somewhere to read the coordinate conversion.

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 2: pan, zoom and inspect the map extent" src="../static/gis-from-scratch/tinygis.html?lesson=view" loading="lazy" height="610"></iframe>
<figcaption>Dragging is opt-in so the map does not capture your scrolling as you read. With the canvas focused, arrow keys pan, + and − zoom, and Home resets the extent.</figcaption>
</figure>

When the features move right, the view center moves west. Their stored coordinates do not change. The relationship between map coordinates and screen coordinates changes.

A drag gives us a displacement in pixels. Divide by the scale to get its displacement in map units:

```javascript
// dx and dy are the pointer's movement since the previous event.
view.cx -= dx / view.scale;
view.cy += dy / view.scale;
render();
```

`-=` means “subtract this amount from the current value.” `+=` adds to it. `render()` is our own function that clears the canvas and redraws the features using the updated view. Canvas does not redraw the map just because a JavaScript value changed.

Zooming changes `scale`. A pleasant zoom also keeps the location under the pointer in the same place. Convert the pointer to map coordinates before and after changing scale, then move the center by the difference:

```javascript
const before = toMap(pointer, view, width, height);
view.scale *= 1.5;
const after = toMap(pointer, view, width, height);
view.cx += before[0] - after[0];
view.cy += before[1] - after[1];
render();
```

The download packages that idea as `zoomAt()` and limits the scale to keep extreme zoom values manageable. It also uses pointer capture so an enabled drag can finish outside the canvas, and handles cancellation so a touch interruption does not leave the map stuck dragging. These details do not change the geometry, but they do change whether the map feels usable. [MDN’s pointer-event documentation](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_events) explains those browser behaviors.

## 3. Give the drawing some geography

A feature needs geometry and attributes. GeoJSON already expresses that combination in a format JavaScript can read:

```javascript
const site = {
  type: "Feature",
  id: "A",
  properties: {
    name: "Site A",
    status: "Needs inspection"
  },
  geometry: {
    type: "Point",
    coordinates: [-117.21, 34.06]
  }
};
```

You can read the object from the outside inward. `site.geometry.coordinates` reaches the coordinate array. `site.properties.status` reaches an attribute. Text has quotes; numeric coordinates do not.

GeoJSON’s position order is longitude, latitude, with optional altitude. The [GeoJSON specification](https://datatracker.ietf.org/doc/html/rfc7946) uses WGS 84 geographic coordinates. A file containing State Plane eastings and northings needs coordinate transformation before it fits this convention. Renaming its extension to `.geojson` does not do that work.

A `FeatureCollection` groups features in a `features` array. A small layer renderer can loop over them:

```javascript
for (const feature of data.features) {
  drawGeometry(feature.geometry);
}
```

`for...of` visits each value in an array. `feature` refers to a different feature on each trip through the loop. `drawGeometry()` is our function, not a hidden browser mapping API.

That function branches on the geometry type. Points become circles. Lines visit a sequence of vertices. Polygons close those paths and fill their interiors. Here is the path helper from the download:

```javascript
function pathLine(coords, close = false) {
  coords.forEach((p, i) => {
    const [x, y] = screen(p);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  if (close) ctx.closePath();
}
```

`forEach()` runs a function for every array item. The arrow `=>` introduces that short function, whose inputs are the coordinate `p` and its position `i` in the array. JavaScript starts counting at zero. `===` tests equality. So the first vertex moves the pen without drawing; the later vertices draw connected segments. `screen()` wraps our coordinate transformation.

A polygon can have a hole. Its first ring is the exterior; subsequent rings describe holes. We add all the rings to one path before filling:

```javascript
ctx.beginPath();
polygon.coordinates.forEach(ring => pathLine(ring, true));
ctx.fill("evenodd");
ctx.stroke();
```

The browser’s [even-odd fill rule](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/fill) leaves the interior ring unpainted for our valid simple polygon. Filling every ring independently would paint over the hole. That is a rendering error with a spatial consequence.

**Try this:** hide the polygon, then bring it back. Open the editor and change Site A’s longitude from `-117.21` to `-117.11`. Predict which way it moves before applying the data.

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 3: GeoJSON geometry, visibility and editable source data" src="../static/gis-from-scratch/tinygis.html?lesson=layers" loading="lazy" height="720"></iframe>
<figcaption>Restore sample data resets the experiment. Invalid input leaves the previous map in place and reports the problem.</figcaption>
</figure>

The download supports Point, LineString, Polygon, and their Multi variants. It validates coordinate ranges, basic nesting, ring closure, and input size. It does not repair invalid topology or support GeometryCollection, null geometries, or antimeridian-crossing rings. Those are useful places to stop a teaching project, provided we say so.

There is still no special layer object. There is an array of features, visibility settings, a symbol size, and a rendering function. A mature layer API adds a great deal of useful behavior to those basic ingredients.

## 4. Ask what is under the pointer

A canvas remembers painted pixels. It does not remember that a particular blue circle belongs to Site A. To identify a feature, we have to ask the data.

For points, the question is: how close is the click to the point’s **screen position**?

```javascript
const [sx, sy] = screen(site.geometry.coordinates);
const distance = Math.hypot(sx - clickX, sy - clickY);
const hit = distance <= pointSize + 5;
```

`Math.hypot()` calculates the length of those x and y differences together. We add a five-pixel allowance around the point symbol. That makes a small point easier to click.

The choice of units matters. A tolerance of five pixels stays usable as you zoom. A tolerance of 0.001 degrees changes its on-screen size with the map scale. The line test works similarly, using distance to each transformed segment and a six-pixel tolerance.

For polygons, convert the click back into map coordinates and ask whether that location falls inside the rings. Our test uses a ray-crossing idea: imagine a horizontal ray extending right from the point. Each crossing of a ring boundary toggles an inside/outside flag.

```javascript
function inRing([x, y], ring) {
  let inside = false;
  for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i];
    const [xj, yj] = ring[j];
    if ((yi > y) !== (yj > y) &&
        x < (xj - xi) * (y - yi) / (yj - yi) + xi) {
      inside = !inside;
    }
  }
  return inside;
}
```

This is the densest sample in the article. Read it geometrically first. The first condition asks whether the edge straddles the ray’s y coordinate. The second asks whether its crossing is to the right of the point. Only then do we flip the flag.

`let` allows us to assign a different value to a name. `!inside` means the opposite Boolean value. `&&` requires both conditions to be true, and skips the second when the first is false. That also keeps a horizontal edge out of the division. The loop keeps both endpoints of an edge available, including the closing edge.

A polygon test needs one more decision: the point must be in the exterior and outside every hole. Exact boundary behavior needs an explicit policy too. In this tiny GIS, the outer boundary is included and hole boundaries are excluded. `inPolygon()` handles those cases separately from `inRing()`, using a small numerical tolerance in the input coordinate units. This is a deliberately limited planar predicate, not a replacement for a robust GIS geometry engine.

**Try this:** click an empty part of the hole. Then select Site B, which sits inside that hole. A point can exist there even though the area excludes its location.

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 4: identify points, lines, polygon interiors and holes" src="../static/gis-from-scratch/tinygis.html?lesson=identify" loading="lazy" height="850"></iframe>
<figcaption>Features drawn later are tested first. Points can therefore be identified above the polygon beneath them. The table is an alternative way to inspect a feature.</figcaption>
</figure>

Once we have the feature, its attributes are ordinary text. The download inserts them with `textContent`, so an imported attribute containing HTML is displayed as text rather than interpreted as page content. Finding the right feature was the spatial part. Presenting its attributes is a separate interface task.

## 5. Make selection an ordinary value

A desktop GIS gives selection a lot of visual weight. Our selected state can be a `Set`: a collection of unique values.

```javascript
const selected = new Set();
selected.add(2);
selected.has(2); // true
selected.clear();
```

The download stores positions in the current feature array rather than trusting imported feature IDs to be present and unique. Reloading data clears the selection. That is sufficient for a read-only experiment; an editor that inserts and removes features would need a more durable identity policy.

During rendering, `selected.has(index)` decides whether a feature gets the orange selection symbol. Changing the symbol does not change the geometry. Changing the selection does not delete the unselected records.

An attribute query is a test on properties. A spatial query is a test on geometry. For our example, the useful question is: **which Point features are in the study area?**

```javascript
selected.clear();

data.features.forEach((feature, index) => {
  if (feature.geometry.type !== "Point") return;
  if (inPolygon(feature.geometry.coordinates, studyArea.geometry.coordinates)) {
    selected.add(index);
  }
});
```

Here, `!==` means “not equal.” The early `return` skips this callback for anything that is not a Point. It does not stop the entire loop. The download extends the same test to all Polygon and MultiPolygon query areas, selecting points that match any of them. MultiPoint features are rendered and identifiable, but this selection exercise deliberately queries individual Point features only.

Before writing a polygon test, we might be tempted to select by the polygon’s bounding box. That is useful for finding candidates. It is not the same spatial relationship.

**Try this:** run both queries. The bounding box returns A, B, C, E, and F. The polygon returns A, C, and F. What disqualifies B? What disqualifies E?

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 5: compare bounding-box and point-in-polygon selection" src="../static/gis-from-scratch/tinygis.html?lesson=query" loading="lazy" height="900"></iframe>
<figcaption>B is in the hole. E is beyond the sloping exterior edge. F sits on the included outer boundary. The dashed rectangle shows the bounding box when that query is active.</figcaption>
</figure>

These queries inspect the full dataset. Panning away from a point, or hiding a geometry type in the final lab, does not remove it from the query. A production interface should make choices like “visible features only” explicit rather than letting display state silently redefine the analysis.

## 6. Let the query earn an index

A loop over six points is easy to understand. A loop over fifty thousand points is still easy to understand; it just does more work. If we repeat the query against many areas, that work multiplies.

The question is where the wasted work lives. A point on the other side of the map cannot be inside this small query envelope. Why inspect it?

A uniform grid gives us a first spatial index. Divide the plane into cells and store a list of point indices in each occupied cell. These lines, inside `makeGrid()`, assign each point to a cell:

```javascript
const key = `${Math.floor(point[0] / cellSize)},${Math.floor(point[1] / cellSize)}`;
if (!cells.has(key)) cells.set(key, []);
cells.get(key).push(id);
```

`cells` is a JavaScript `Map`, a key/value collection. This particular capital-M Map has nothing inherently geographic about it. Our keys are cell addresses such as `4,5`, and the values are arrays of point indices. Backticks create a string that can insert expressions using `${...}`. `Math.floor()` rounds down to the cell’s integer coordinate, including for negative values.

A query finds the cells overlapped by its envelope, gathers their point indices, and performs the actual test on those candidates:

```javascript
const grid = makeGrid(points, 100);
const bounds = [420, 420, 580, 580];
const candidates = gridCandidates(grid, bounds);
const hits = candidates.filter(id => inBox(points[id], bounds));
```

`filter()` returns only the items that pass its test. The grid has reduced the search space; it has not answered the spatial question by itself. For a polygon query, we would follow candidate retrieval with the polygon predicate instead.

This experiment uses a rectangular query and deterministic synthetic points on a 1,000-unit square. That keeps the measured work easy to see without claiming a production benchmark.

**Try this:** compare 1,000 and 50,000 points. Look at candidate counts before looking at milliseconds. Then compare the cost of building the grid with the cost of just scanning once.

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 6: measure a full scan against a uniform-grid query" src="../static/gis-from-scratch/tinygis.html?lesson=index" loading="lazy" height="790"></iframe>
<figcaption>Both methods query the same points and check that their results agree. Timings come from your browser, exclude drawing, and separate index construction from querying.</figcaption>
</figure>

The grid can cost more than it saves for one small query. It becomes useful when we reuse it for enough queries over unchanged data. If points move, we have to update or rebuild it. Large query envelopes also reduce its advantage.

We have not built an R-tree. We have made the reason for spatial indexing observable: avoid detailed work on features that cannot qualify. That is a more useful starting point than adding an index merely because “GIS data should have one.”

## 7. Make the projection a function

So far, we have treated longitude and latitude as x and y. That was enough to expose the view transformation. It was never a claim that degrees were a uniform distance grid.

Now give the map a second coordinate transformation. Source coordinates remain longitude and latitude. Before drawing, project them to a working coordinate system. Then convert those projected coordinates into screen pixels.

For spherical Web Mercator, the forward transformation is compact:

```javascript
function project([lon, lat]) {
  const R = 6378137;
  const maxLat = 85.05112878;
  const clampedLat = Math.max(-maxLat, Math.min(maxLat, lat));
  const phi = clampedLat * Math.PI / 180;
  return [
    R * lon * Math.PI / 180,
    R * Math.log(Math.tan(Math.PI / 4 + phi / 2))
  ];
}
```

`R` is the sphere radius in metres. The trigonometric functions use radians, so we convert degrees first. Clamping keeps latitude away from the poles, where Mercator’s y value grows without bound. The limit here matches the familiar square Web Mercator world extent. The download’s `project()` accepts a second argument to switch this transformation on or off.

This is the spherical formula, not general-purpose projection support. [PROJ’s Web Mercator reference](https://proj.org/en/stable/operations/projections/webmerc.html) describes the same distinction from ellipsoidal Mercator.

**Try this:** switch the display. Compare the rectangle around the equator with the one at 60° north. Each spans 20° of longitude and 10° of latitude.

<figure class="gis-experiment">
<iframe data-tinygis title="Experiment 7: compare longitude-latitude drawing with Web Mercator" src="../static/gis-from-scratch/tinygis.html?lesson=projection" loading="lazy" height="550"></iframe>
<figcaption>The geographic grid changes shape because its coordinates are transformed. Projected metres are not automatically ground-distance metres.</figcaption>
</figure>

The higher-latitude rectangle gets taller in Mercator. That is a visible consequence of the nonlinear y transformation. It does not make the rectangle larger on Earth.

There are now three spaces to keep straight: source longitude/latitude, projected map coordinates, and screen pixels. Identification follows the transformations backward. Export should preserve the original geographic coordinates rather than accidentally writing projected metres into GeoJSON.

This is why a spatial reference is more than a label. It tells us how to interpret numbers, and a projection changes those numbers according to a defined relationship. Assigning a name to the canvas would accomplish neither.

## 8. Put the pieces together, then save something

The final lab combines the earlier pieces. Open data, choose visibility and point size, pan and zoom, identify a feature, make an attribute or spatial selection, and export it. It uses the direct longitude/latitude display from the early experiments; the projection comparison remains a separate lesson.

Reading a local file starts with browser APIs:

```javascript
const text = await file.text();
const nextData = JSON.parse(text);
validateGeoJSON(nextData);
data = nextData;
selected.clear();
fit();
```

`file` is the file chosen through the input control. `await` pauses this async handler until its text is available. `JSON.parse()` turns that text into objects and arrays. The validation happens before replacing the current data, so a bad file does not erase a working map. In the download, a `try...catch` reports parsing and validation failures next to the map.

**Try this:** select by polygon, export the three selected points, and open that exported file back in the lab. The result should contain A, C, and F. Its polygon has disappeared because it was the query area, not part of the selected result.

<figure class="gis-experiment">
<iframe data-tinygis title="Final lab: load, inspect, query and export GeoJSON with vanilla JavaScript" src="../static/gis-from-scratch/tinygis.html?lesson=lab" loading="lazy" height="1100"></iframe>
<figcaption>Files are read locally. Export includes the selected features and their original attributes and coordinates. Restore sample data brings back the complete example.</figcaption>
</figure>

Creating the result is mostly ordinary data handling:

```javascript
const result = {
  type: "FeatureCollection",
  features: data.features.filter((feature, index) => selected.has(index))
};

const blob = new Blob(
  [JSON.stringify(result, null, 2)],
  { type: "application/geo+json" }
);
const url = URL.createObjectURL(blob);
```

`JSON.stringify()` reverses parsing: it turns the selected objects into text. The final `2` asks for readable indentation. A `Blob` holds the output bytes. The object URL lets a download link refer to those bytes without uploading them to a server. The working `download()` function creates the link, clicks it, and releases the URL afterward.

If nothing is selected, the exported FeatureCollection is empty. That is a valid result, not a reason to silently export everything. The readout states how many features were exported. To keep the load exercise focused on drawable data, this demo rejects empty collections on import and explains why.

The file input, Canvas drawing surface, and download are enough to close a small GIS workflow. The important relationship is that the data, the view, and the selection are separate values. Moving the view does not move the data. Styling the selection does not change the query. Saving the result does not depend on which features happen to be on-screen.

## What I want this exercise to leave behind

I do not want to build a bad version of QGIS in my spare time. This stops well before rasters, editing, topology repair, labels, services, geodatabases, most projections, or serious symbology. Even this small version has boundary policies, malformed data, display scaling, pointer behavior, and performance tradeoffs to think about.

Those details are part of the value. Some capabilities that feel substantial in a desktop interface have a small core. Others become complicated as soon as we ask them to handle messy input or unusual geometry. Both outcomes tell us something about the tools we already use.

For your next experiment, change one thing you can predict. Move a coordinate in the GeoJSON. Change the point-picking tolerance. Make the index’s query envelope cover almost the entire dataset. Choose a different policy for a point on a hole boundary, and update the checks along with the code.

Then explain what changed in GIS terms and in JavaScript terms. If you can trace a point from its stored coordinate to its screen position, back through a click, into a selection, and out to a file, you have something more useful than a new mapping API recipe. You can explain the mechanisms that the recipe normally leaves out.
