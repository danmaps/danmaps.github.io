---
title: "I Built a Map Where AI Chooses the Next Spatial Operation"
date: 2026-09-24
tags:
  - Draft
  - AI
  - GIS
  - Systems
summary: "JevMap tests a division of labor: Jev chooses from legal spatial actions, and application code validates and executes them."
layout: rich
---

A GIS operation can be deterministic even when deciding what to do next takes judgment.

If someone asks, “Find schools near major roads,” there are choices before a tool runs. Which layers should be involved? Does “near” suggest a buffer, a nearest-feature calculation, or an intersection? What distance would make sense? GIS analysts answer questions like these every day, often without naming them as separate decisions.

I wanted to see whether a model could help with that decision while ordinary application code stayed responsible for the spatial operation. That idea became JevMap.

## A decision and an operation are different jobs

I think of a spatial workflow as having two parts:

- **Decision:** Given the user's goal and the current map, which legal action should happen next?
- **Execution:** Check the selected action and run a known operation with defined inputs and parameters.

Choosing an operation can involve interpretation. A GIS operation should have a clear contract. Once the input layer and distance are set, a buffer should produce the same geometry every time.

JevMap gives Jev a small set of choices. It does not ask Jev to write JavaScript, SQL, or GIS code. The model can recommend an action; the application owns validation, geometry, and side effects.

## The map becomes structured context

JevMap sends Jev a description of the current task and GeoJSON-backed map state. That state includes information about the loaded layers and the work already done. The app generates legal candidates from that state: tools, eligible layers, and, for Buffer, a finite set of distances.

The current tool catalog includes Buffer, Intersect, Nearest, Filter, Select, and Export. Jev returns typed choices with confidence and probabilities. The application can inspect what it chose and how strongly the alternatives scored.

The workflow looks like this:

```text
GeoJSON map state + task
        ↓
legal tool, layer, and parameter candidates
        ↓
Jev's typed choices
        ↓
application policy and runtime validation
        ↓
deterministic spatial operation
        ↓
updated map result
```

The model's answer is still a recommendation. Before a Buffer call runs, JevMap checks that the selected layer exists and that the distance is a valid positive number. Turf.js performs the geometry operation. The result comes back as GeoJSON and is displayed on the map.

## Confidence belongs to application policy

A confidence score by itself should not decide what a GIS application does. JevMap has code-defined thresholds for the Buffer path:

- At 0.80 or above, the operation can run.
- From 0.55 to 0.80, the app asks for user approval.
- Below 0.55, it asks for more context and runs nothing.

The decision depends on operation, layer, and distance, so the Buffer path uses the lowest confidence across those choices. The thresholds are application policy, not a guarantee from the model.

A pending approval is also tied to the inputs that produced it. If the task or map data changes before approval, JevMap invalidates the old decision and asks for a fresh one. The operation should not run on state the model never evaluated.

For Buffer execution, a receipt records the decision, probabilities, confidence, validation outcome, and execution status. That makes it possible to inspect how the model-assisted action moved through the application.

## What I built, and what is still a demo

I started with the ideas in [webmap_ai](https://github.com/danmaps/webmap_ai), then narrowed the model's role around Jev's typed decision interface. The app is written in TypeScript and uses Vite, MapLibre GL JS, GeoJSON, and Turf.js. Jev requests go through a server-side proxy so an API key does not need to live in the browser.

The included Los Angeles points are synthetic examples, not real facilities. Buffer is the main confidence-gated analysis path, and Export is implemented in the workbench registry. The other operation choices run small deterministic previews against example data. Intersect, Nearest, Filter, and Select are still marked as planned in the reusable tool registry, so those previews should not be mistaken for general-purpose GIS implementations.

That distinction matters to me. I wanted to test the decision boundary in a working map: can a model choose a useful next action from a constrained set, and can the application keep execution inspectable and repeatable?

## The model may be a fad. The boundary is useful.

I know Jev is part of a silly internet hype train, and the current model or API may be a short-lived thing. I still wanted to build this demo because the engineering question lasts longer than the model name: what should an AI be allowed to decide, and which parts of the workflow should remain ordinary software?

If I replace Jev with another decision model, the rest of the design still makes sense. The map supplies state. Candidate generation defines legal choices. Application code validates the result. A spatial engine performs the operation.

For now, JevMap is a small experiment in making that division visible. The model chooses from a bounded set. The map shows the result. The code remains responsible for what actually runs.

The current implementation and its evolving limits are in the [JevMap repository](https://github.com/danmaps/jevmap).
