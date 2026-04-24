Title: From Prompt to Production: Making AI-Generated Code Actually Usable
Date: 2026-04-24
Tags: [AI, Automation, GIS, Systems]
Summary: AI-generated code becomes genuinely useful only when it is wrapped in context, validation, guardrails, and human review.

There’s a big gap between:

“AI can generate code”

and

“AI can help you ship something real”

I’ve been working on tools that bring AI directly into production workflows, specifically inside ArcGIS Pro.

The goal isn’t novelty.

It’s usability.

## The dream

You type:

“Find all parcels within 500 feet of a fault line and summarize by county”

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

You don’t just generate code.

You build a system around it.

## Pattern 1: Constrained generation

Don’t let AI generate anything.

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

I’ve been using:

- dry-run modes
- logging outputs
- explicit validation steps

This turns “risky automation” into something usable.

## Pattern 3: Human-in-the-loop

The best workflows aren’t:

- fully manual
- fully automated

They’re hybrid.

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

“a coder”

Think of it as:

“a fast but unreliable junior developer”

You wouldn’t:

- blindly run their code
- skip review

Same rules apply.

## Where this gets interesting

Once you have guardrails, you can start doing more:

- chaining multi-step workflows
- evaluating outputs automatically
- iterating on results

This is where “agentic workflows” actually start to mean something.

## What I’m working on now

- CLI tools that make workflows reproducible
- evaluation systems for AI-generated outputs
- better ways to inject context into prompts

## Final thought

The question isn’t:

“Can AI write code?”

It can.

The real question is:

“Can we build systems where that code is safe, correct, and useful?”

That’s the problem worth solving.
