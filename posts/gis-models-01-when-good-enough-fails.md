---
title: "When \"Good Enough\" Fails"
series: "Choosing the Right AI Model for the Right GIS Job"
series_index: 1
date: 2026-02-22
tags:
  - Unlisted
  - AI
  - GIS
  - ArcGIS Pro
  - Automation
  - Models
---

A lot of people treat LLMs like fancy autocomplete.

That mindset works… right up until you ask the model to produce a runnable GIS workflow from vague human intent.

This post is about that moment.

## Core question

Can a model reliably turn vague human intent into a correct, runnable GIS workflow?

More bluntly: can it translate English into *safe, correct geoprocessing steps*?

## Case study

### Prompt

> Select parcels within 500 ft of transmission lines, dissolve by circuit, export to GeoJSON.

This is a realistic request.

It is also a perfect trap because it contains four failure points:

1) what “within 500 ft” means (units, projection, geodesic vs planar)
2) what “transmission lines” are (feature layer? multiple circuits? multipart?)
3) what “dissolve by circuit” implies (which field is “circuit” and is it clean?)
4) exporting GeoJSON (ArcGIS Pro vs ArcPy vs GDAL, and field name constraints)

## Models tested

I’m intentionally not making this a brand fight. Think in classes:

- **Small fast model**: cheap, quick, good at plausible text
- **Mid-tier reasoning model**: can keep more state, notices contradictions
- **High-end reasoning model**: tends to ask clarifying questions and avoid unsafe assumptions

## What I’ll show

### 1) Generated steps (side-by-side)

For each model:

- what tools it suggests
- the order of operations
- where it asks questions vs assumes

### 2) Where each model breaks

Common breakpoints to look for:

- **Tool confusion**: Buffer vs Select By Location vs Near, and when to project
- **Unit handling**: feet vs meters vs dataset units
- **Dissolve logic**: dissolve field selection, multipart handling, nulls
- **Export reality**: GeoJSON export path in ArcGIS Pro, field/schema gotchas

### 3) Actual runtime results in ArcGIS Pro

Not “it sounds right”.

- did it run?
- did it produce the right parcels?
- did it dissolve correctly?
- did it export usable GeoJSON?

## Early pattern (draft observation)

Cheap models are fine for brainstorming.

But in production GIS automation, the cost of a quiet mistake is usually higher than the cost of a better model.

The difference is not prose quality. It’s whether the model:

- notices missing inputs
- refuses to guess on high-impact choices
- checks units and projections
- verifies the meaning of “circuit” instead of inventing it

## Key takeaway

**Cheap models are fine for suggestions. Production GIS automation needs reasoning, not autocomplete.**

## Next steps

I’m going to fill this in with:

- the exact side-by-side outputs
- screenshots / logs from ArcGIS Pro
- a “minimum safe checklist” you can use regardless of model choice
