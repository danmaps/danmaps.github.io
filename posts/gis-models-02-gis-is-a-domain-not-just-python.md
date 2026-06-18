---
title: "GIS Is a Domain, Not Just Python"
series: "Choosing the Right AI Model for the Right GIS Job"
series_index: 2
date: 2026-02-22
tags:
  - Unlisted
  - AI
  - GIS
  - Data
  - Automation
  - Models
layout: rich
---

A lot of AI tooling assumes the world is â€œjust data framesâ€.

GIS looks like data frames until you make a decision that depends on meaning.

Then you learn the difference between:

- *a field* and *a stable identifier*
- *a category* and *a code list*
- *a timestamp* and *an operational truth*

## Core question

Which models actually understand what GIS data **means**, not just how itâ€™s shaped?

## Case study

### Input

A feature class schema plus basic stats.

Not the full dataset. Not a map.

Just enough to force the model to reason about:

- field purpose
- field hygiene
- operational semantics

### Task

> Which fields are safe to group outages by, and why?

This sounds simple.

It is not.

Grouping by the wrong field gives you charts that look clean and are quietly wrong.

## What Iâ€™ll compare

### Field selection logic

Does it:

- pick stable, intentioned identifiers (like circuit IDs) over human labels
- notice null rates, mixed types, free-text landmines
- ask what the downstream use is (reporting, dispatch, billing, etc.)

### Awareness of utility domain concepts

Even without being â€œutility-tunedâ€, a good model should recognize:

- feeder vs circuit vs device vs work order
- the difference between â€œcauseâ€ and â€œstatusâ€
- why you donâ€™t group by a field that is updated mid-incident

### Explanation quality

Would a real analyst trust it?

Not â€œdoes it sound smartâ€, but:

- does it explain tradeoffs
- does it propose validation steps
- does it call out uncertainty

## What Iâ€™ll show

- Incorrect but plausible answers
- Subtle mistakes that could cause real-world issues
- The difference between:
  - â€œconfident narrativeâ€
  - â€œsafe recommendation with verification stepsâ€

## Key takeaway

**GIS automation fails quietly when models lack domain intuition.**

That is why GIS is not â€œjust Pythonâ€.

It is judgment about data that represents the world.

## Next steps

Iâ€™ll fill this with:

- a concrete schema example
- model outputs annotated with failure modes
- a short rubric you can use to evaluate model recommendations on GIS fields

