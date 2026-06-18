---
title: "From Prompt to Production: Making AI-Generated Code Actually Usable"
date: 2026-04-24
tags:
  - AI
  - automation
  - GIS
  - systems
  - guardrails
  - software
summary: "AI-generated code becomes genuinely useful only when it is wrapped in context, validation, guardrails, and human review."
layout: rich
---

Thereâ€™s a big gap between:

â€œAI can generate codeâ€

and

â€œAI can help you ship something realâ€

Iâ€™ve been working on tools that bring AI directly into production workflows, specifically inside ArcGIS Pro.

The goal isnâ€™t novelty.

Itâ€™s usability.

## The dream

You type:

â€œFind all parcels within 500 feet of a fault line and summarize by countyâ€

And you get:

- correct code
- correct output
- something you can trust

## The reality

What you actually get is:

- mostly correct code
- missing assumptions
- subtle errors

The output might run, but:

- it might use the wrong projection
- it might ignore null values
- it might silently fail

## So how do you make it usable?

You donâ€™t just generate code.

You build a system around it.

## Pattern 1: Constrained generation

Donâ€™t let AI generate anything.

Give it structure:

- known layers
- known fields
- known operations

This reduces hallucination dramatically.

## Pattern 2: Execution guardrails

Before running anything:

- validate inputs
- check schema
- simulate execution

Iâ€™ve been using:

- dry-run modes
- logging outputs
- explicit validation steps

This turns â€œrisky automationâ€ into something usable.

## Pattern 3: Human-in-the-loop

The best workflows arenâ€™t:

- fully manual
- fully automated

Theyâ€™re hybrid.

AI accelerates:

- setup
- boilerplate
- exploration

Humans handle:

- correctness
- judgment
- edge cases

## The mental model shift

Stop thinking of AI as:

â€œa coderâ€

Think of it as:

â€œa fast but unreliable junior developerâ€

You wouldnâ€™t:

- blindly run their code
- skip review

Same rules apply.

## Where this gets interesting

Once you have guardrails, you can start doing more:

- chaining multi-step workflows
- evaluating outputs automatically
- iterating on results

This is where â€œagentic workflowsâ€ actually start to mean something.

## What Iâ€™m working on now

- CLI tools that make workflows reproducible
- evaluation systems for AI-generated outputs
- better ways to inject context into prompts

## Final thought

The question isnâ€™t:

â€œCan AI write code?â€

It can.

The real question is:

â€œCan we build systems where that code is safe, correct, and useful?â€

Thatâ€™s the problem worth solving.

