---
title: "I Let an AI Write My GIS Workflow. Here's What Broke."
date: 2026-04-24
tags:
  - AI
  - GIS
  - ArcGIS
  - automation
  - guardrails
  - geoprocessing
summary: "AI can generate GIS workflow code, but the real story starts when that code meets projections, schemas, and production execution."
---

There’s a growing narrative that AI can write code for you.

That’s true.

What’s more interesting is what happens after the code is written.

I’ve been experimenting with integrating AI directly into ArcGIS Pro workflows. The idea is simple:

Describe what you want → get working geoprocessing code.

In practice, it looks like this:

- I type: “Select all points within 1 mile of schools and summarize by district”
- The system generates Python (ArcPy)
- The code runs inside a real project

And sometimes… it works perfectly.

Other times, it breaks in ways that are surprisingly consistent.

## Where things actually break

### 1. The “almost right” problem

AI is very good at generating code that looks correct.

It’s much worse at generating code that:

- uses the correct coordinate system
- handles edge cases in real datasets
- respects schema constraints

Example:

- It buffers in degrees instead of meters
- Or assumes a field exists that doesn’t

This is dangerous because:

The output looks valid, but the result is wrong.

### 2. Context is everything (and AI doesn’t have enough of it)

In a real GIS project:

- layers have naming conventions
- fields have meaning
- projections matter

Without that context, AI guesses.

Sometimes correctly. Often not.

This is where most “AI coding demos” fall apart. They work in isolation, not inside messy systems.

### 3. Execution is the real problem

Generating code is easy.

Running it safely is not.

In a production environment, you need:

- dry-run modes
- logging
- validation checks
- rollback strategies

Without that, you’re basically letting an AI modify your data blindly.

## What actually works

After a lot of trial and error, I’ve landed on a pattern:

AI should:

- generate code
- suggest approaches

Humans should:

- validate intent
- review execution
- own the result

## The key shift

The real value of AI isn’t:

“write code for me”

It’s:

“reduce the distance between intent and execution”

But there’s a gap between:

- generated code
- trustworthy systems

Most of my work lately has been about closing that gap.

## What I’m exploring next

- scoring AI-generated code quality
- comparing outputs against known-good datasets
- building guardrails into execution environments

Basically:

Not “can AI write code?”
But “can we trust what it produces?”

If you’re using AI in real workflows, I’d love to hear:

- where it breaks for you
- what guardrails you’ve built

Because that’s where the interesting work is happening.
