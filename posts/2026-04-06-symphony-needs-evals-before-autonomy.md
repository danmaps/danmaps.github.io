---
title: "Symphony needs evals before autonomy"
date: 2026-04-06
tags:
  - Draft
  - AI
  - systems
  - orchestration
  - Symphony
  - evaluation
---

This week on Symphony was less about shipping a flashy new feature and more about getting honest about what the next layer of work actually is.

Not more orchestration vocabulary.
Not more agent ambition.
Not some premature self-improving loop.

The next useful step is evaluation.

More specifically: a trustworthy, local, artifact-based eval setup that can tell me whether a Symphony agent or harness is actually getting better.

That may sound less exciting than adding another capability. I think it is more important.

## The temptation is obvious

Once you have a local orchestration system taking shape, the mind jumps ahead fast.

You start thinking about things like:

- benchmark-driven improvement
- multiple agent variants
- routing experiments
- automatic harness tuning
- systems that optimize themselves over time

All of that is interesting.
All of that is also a great way to optimize nonsense if the scoring layer is weak.

That is the part I have been trying to pin down more carefully.

## The real lesson: do not optimize what you cannot verify

I spent part of this week sketching what an evaluation layer for Symphony should actually look like.

The shape that feels right is pretty grounded:

- Symphony remains the orchestration layer
- local models do the work
- a thin adapter bridges tasks into the agent runtime
- an eval harness runs repeatable tasks
- outputs are saved as real files
- verifiers check those outputs directly
- run artifacts stick around for comparison

That is the key idea.

If I want to compare agent variants, prompt structures, tool policies, or routing behavior, I need something stronger than vibes.

I need tasks with explicit contracts.
I need outputs like:

- `summary.json`
- `report.md`
- `patched_script.py`
- `plan.json`

And I need verifiers that can say, with a straight face:

- the file exists
- the schema is valid
- the calculation is correct
- the output is incomplete
- the agent should have abstained here

Without that, "improvement" is mostly theater.

## This is where a lot of AI work goes sideways

I think a lot of agent work gets weird because people jump from:

- I can make the model do something interesting

straight to:

- now I should automate the improvement loop

That jump is too fast.

Before you let a system tune itself, you need to trust the thing doing the judging.

Otherwise you get all the usual failure modes:

- overfitting to a tiny visible task set
- benchmark gaming
- brittle prompt hacks
- apparent gains that do not transfer
- systems that look smarter on paper and less trustworthy in practice

That is not an abstract concern. It is the default failure mode.

## For Symphony, local and inspectable still feels right

What I like about the current direction is that it stays consistent with the rest of the project.

Symphony has been getting more useful as it gets more inspectable.
Not more magical.

That same rule applies here.

A good eval system for Symphony should be:

- local-first
- narrow at the start
- file-based where possible
- easy to rerun
- obvious to inspect after failure
- strict about output contracts

I do not want evaluation that depends on a heroic interpretation of a chatbot transcript.
I want evaluation that leaves receipts.

## The first tasks should be embarrassingly small

Another thing that became clearer this week: the first eval tasks should be almost boring.

Not full end-to-end multi-agent behavior.
Not desktop GIS automation.
Not some giant benchmark suite with ten layers of abstraction.

Just small, real tasks like:

- transform a CSV and GeoJSON into a `summary.json`
- inspect a dataset manifest and produce a schema summary
- patch a broken Python script
- generate a safe workflow plan with explicit constraints
- refuse a task that should be clarified instead of guessed

That sounds modest because it is modest.

Good.

If the small tasks are not trustworthy, the big ones will be fake confidence with better branding.

## The deeper point

I keep coming back to the same idea across these projects:

The value is not in sounding autonomous.
The value is in building systems where useful work can be inspected, compared, and trusted.

For Symphony, that means the next serious milestone is not "self-improving agents."
It is something more boring and more real:

- a repeatable local eval suite
- a few narrow tasks
- clear verifiers
- versioned agent variants
- stored run evidence
- comparisons that mean something

Once that exists, then it becomes reasonable to explore smarter mutation loops or benchmark-driven tuning.

Before that, it is mostly cosplay.

## What I think this week was really about

This was not a huge shipping week.
It was a boundary-setting week.

Those matter.

The useful constraint I am taking forward is simple:

**Symphony should earn the right to optimize itself by first proving it can evaluate itself honestly.**

That feels like the next real piece of work.
Not the loudest one. The real one.
