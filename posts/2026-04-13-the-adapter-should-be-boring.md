---
title: "The adapter should be boring"
date: 2026-04-13
tags:
  - Draft
  - AI
  - systems
  - orchestration
  - Symphony
  - evaluation
layout: rich
---

This weekâ€™s useful Symphony progress was not some new autonomous capability.

It was a clearer boundary.

I spent time tightening how I want the next layer of the project to work, especially around evaluation. The shape that keeps surviving contact with reality is pretty simple:

- Symphony is the orchestration and control layer
- local models do the actual generation work
- an eval harness runs narrow repeatable tasks
- a thin adapter bridges the task into the agent runtime
- outputs are written as real files
- verifiers score those files directly

The more I think about it, the more I think the adapter in that stack should be aggressively boring.

That is not an insult. It is a design goal.

## Boring is a feature

There is a temptation, once you start building agent systems, to make every layer "smart."

You do not just want an orchestrator. You want a clever orchestrator.
You do not just want evaluation. You want adaptive evaluation.
You do not just want an adapter. You want an adapter that enriches context, massages prompts, makes judgment calls, and maybe fixes things on the fly.

That is exactly how you create a system that becomes harder to trust with every improvement.

The adapter should not be where the magic lives.

Its job is much smaller:

- read the task input
- read the available files
- package the context cleanly
- call the Symphony-compatible agent runtime
- write outputs where the task expects them
- leave useful logs behind
- exit cleanly

That is enough.

If the adapter starts becoming clever, it muddies the experiment.
Then when a run improves, you do not know whether:

- the agent got better
- the prompt changed in a meaningful way
- the task got easier by accident
- the adapter quietly compensated for a weakness

That is bad science and bad engineering.

## I want the scoring layer to stay honest

This connects to the broader thing I have been circling with Symphony: I want improvement to mean something.

That requires a narrow contract.

A task should say what files exist, what output is required, what constraints apply, and what the verifier will check. Good first outputs are boring on purpose:

- `summary.json`
- `report.md`
- `plan.json`
- `patched_script.py`

Those are useful because they can be checked.

The file exists.
The schema parses.
The values are correct.
The required sections are present.
The agent refused when it should have refused.

That is a much better foundation than staring at a transcript and deciding that the model felt pretty smart.

## The more agentic the system sounds, the more important this gets

I think a lot of AI tooling goes sideways because the language gets ahead of the operating model.

People talk about self-improving agents, multi-agent collaboration, autonomous research loops, and dynamic routing before they have built a way to tell whether the system is actually producing better work.

So the project accumulates sophistication in all the least trustworthy places.

You get:

- more moving parts
- fuzzier accountability
- prettier demos
- weaker explanations for why something succeeded or failed

I am trying pretty hard not to do that with Symphony.

If the system gets more ambitious, I want it to also get more legible.
Not less.

## This is the same lesson as artifact-first orchestration

Some of this clicked because of how Symphony already evolved earlier.

The project got more real when outputs stopped being treated like undifferentiated text and started becoming first-class artifacts.

A brief should become `brief.md`.
A plan should become `plan.md`.
A tiny app should produce actual files.
A failed run should leave behind prompts, outputs, validation state, and evidence that can be inspected later.

That shift made the system more useful because it made it easier to tell what actually happened.

The adapter question is really the same question.

Do I want a layer that performs intelligence, or a layer that preserves clarity?

For this stage of Symphony, clarity wins.

## What I think the real decision was this week

I do not think this was a huge shipping week in the usual sense.

It was more of an architectural honesty week.

The useful decision was to keep the eval path narrow:

- file-based tasks first
- small verifiers first
- one stable baseline model first
- explicit agent versions later
- optimization loops only after the benchmark is trustworthy

And inside that, keep the adapter boring.

That sounds modest, but modest is underrated.
A boring adapter means cleaner experiments.
Cleaner experiments mean better comparisons.
Better comparisons mean I can eventually change the system with less self-deception.

That feels like real progress.

Not because it is flashy.
Because it is the kind of constraint that makes later work more believable.

