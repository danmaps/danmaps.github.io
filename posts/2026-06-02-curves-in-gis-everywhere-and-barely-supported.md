---
title: "Curves in GIS: Everywhere and Barely Supported"
date: 2026-06-02
tags:
  - Draft
  - GIS
  - geometry
  - data
  - spatial
summary: "Curves in GIS feel exotic until you realize one of the most common operations in the field—buffering—creates them constantly, even as many common GIS formats barely support true curved geometry."
---

At first glance, curves in GIS seem exotic.

Something from CAD.
Something for surveyors.
Something hidden deep inside enterprise geodatabases.

Most GIS workflows appear overwhelmingly linear:

- points
- polylines
- polygons
- vertices
- segments

Straight lines everywhere.

Then you remember what a buffer actually is.

A buffer around a point is a circle.
A buffer around a line contains rounded end caps and curved offsets.
One of the most common operations in GIS quietly creates curves constantly.

That realization changes the framing entirely.

Curves are simultaneously everywhere in GIS and oddly unsupported by many GIS formats.

<!-- IMAGE SLOT: buffer examples / point buffer circle / line buffer rounded caps -->
<!-- Possible insert:
<img src="/static/images/curves-in-gis-buffer-hero.png" alt="..." style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />
-->

## Two Ways GIS Stores Curves

There are really only two approaches.

### True Curves

A true curve stores the mathematical definition of the curve itself.

Instead of storing dozens of tiny vertices, the geometry stores information like:

- start point
- end point
- center point
- radius
- direction

The software reconstructs the curve mathematically when rendering or analyzing it.

ArcGIS geodatabases support several true curve types, including circular arcs and Bézier curves. PostGIS also supports curved geometry types such as `CIRCULARSTRING` and `CURVEPOLYGON`.

<!-- INTERACTIVE SLOT: show true curve metadata or curved-geometry example -->

### Densified Curves

Many GIS formats cannot store true curves at all.

Instead, they approximate curves using many small straight segments.
This process is called **densification**.

A perfect circle becomes a polygon with dozens or hundreds of tiny edges.
Formats like Shapefile and GeoJSON work this way.

The curve is not truly stored.
It is approximated convincingly enough that most users never notice.

<!-- IMAGE SLOT: zoomed-in densified circle / polygon approximation -->

## The Strange Life of Buffers

Buffers are a perfect example of this contradiction.

Mathematically, a point buffer is a circle:

> all points at a fixed distance from a center point.

But whether that circle remains a true curve depends entirely on the geometry engine and output format.

A geodatabase may preserve it as curved geometry.
A shapefile export may flatten it into hundreds of vertices.
A GeoJSON export may simplify it even further.

The user still sees something that looks circular.
Underneath, the geometry may just be a carefully managed illusion.

<!-- INTERACTIVE SLOT: compare same buffer as true curve vs densified export -->

## Curves and the Difference Between Accuracy and Precision

Curves are also a great way to understand the difference between **accuracy** and **precision**.

A densified curve may appear perfectly smooth at normal map scales.
Visually, it feels accurate.
But mathematically, it is still only an approximation.

A “circle” made from 64 straight segments is not actually a true circle.
It is a 64-sided polygon pretending to be one.

Most of the time, this distinction barely matters.

At city scale, the approximation may be invisible.
At parcel scale, you may begin noticing vertices.
At engineering scale, the approximation may become unacceptable.

Geometry quality is contextual.

A generalized curve can be:

- visually accurate
- operationally useful
- analytically sufficient

while still being mathematically imprecise.

## The Zoom-In Test

One of the most interesting things about GIS curves is that many users never realize they are looking at approximations.

The illusion survives because rendering engines smooth over the underlying geometry.
But eventually every densified curve fails the zoom-in test.

Zoom in far enough and the vertices appear.
The smooth arc suddenly reveals itself as a sequence of tiny straight decisions.

This happens constantly in GIS:

- buffers
- vector tiles
- reprojection
- simplification
- shapefile exports
- web maps

The system continuously trades precision for practicality.

<!-- IMAGE SLOT: zoom progression from smooth-looking circle to visible vertices -->

## Why GIS Often Chooses Approximation

True curves are elegant.

But they also introduce complexity:

- more complicated geometry engines
- harder topology operations
- inconsistent software support
- interoperability problems

Linear approximations are simpler.
And simplicity scales extremely well.

That is one reason GIS ecosystems have historically leaned toward segmented geometry even while continuously generating curved concepts.

Not because curves are unimportant.
But because **accurate enough at the intended scale** is often more valuable than mathematical purity.

## The Hidden Philosophy of GIS Geometry

Curves expose something deeper about GIS itself.

GIS is full of carefully managed geometric illusions.

A smooth-looking curve may actually be:

- 24 segments
- 240 segments
- or a true mathematical arc

depending on the workflow and file format.

Most users never notice because the approximation is sufficient for the task at hand.

That phrase—**sufficient for the task at hand**—may be one of the defining philosophies of practical GIS.

<!-- OPTIONAL INTERACTIVE SLOT: demo true curve vs densified geometry at different zooms -->
