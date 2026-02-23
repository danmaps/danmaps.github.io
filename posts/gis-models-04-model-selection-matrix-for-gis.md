---
title: "A Practical Model Selection Matrix for GIS"
series: "Choosing the Right AI Model for the Right GIS Job"
series_index: 4
date: 2026-02-22
tags:
  - Unlisted
  - AI
  - GIS
  - Automation
  - Models
  - Resilience
---

If you do GIS automation in the real world, you do not need a “best model”.

You need a *default choice* that is safe, and a *cheap choice* that is fast, and a *high-end choice* for when the cost of being wrong is high.

This is a draft of a practical selection matrix.

## The model selection matrix (draft)

| Task type | Risk level | Recommended model class | Why |
|---|---:|---|---|
| Brainstorming steps | Low | Small / fast | Speed matters, mistakes are cheap |
| Writing first-pass docs | Low | Small / fast | You will edit, correctness is human-verified |
| ArcGIS Pro geoprocessing workflow design | Medium | Mid-tier reasoning | Needs tool selection, ordering, and sanity checks |
| Unit/projection-sensitive spatial analysis | High | High-end reasoning | Needs to ask questions and verify assumptions |
| Editing production datasets / publishing | High | High-end reasoning + guardrails | You want refusal/pauses and explicit confirmation |
| Agent autonomy (multi-step decisions) | High | High-end reasoning | Model behavior under uncertainty is the product |

## A boring rule that saves you

When the task can silently produce *plausible wrong output*, treat it as high risk.

That’s most GIS.

## The resilience angle

This is not just about picking a model.

It’s about building an automation practice where:

- you can ship value repeatedly
- you don’t get wiped out by one quiet mistake
- you can adapt as models and tooling change

The durable skill is: **turn compute into outcomes safely**.

## Next steps

I’ll evolve this into:

- a printable one-pager
- a checklist for “when to upgrade the model class”
- real examples from the case study posts
