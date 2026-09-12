---
title: "Your Vibe-Coded GIS Scripts Need a Safety Harness"
date: 2026-09-12
tags:
  - Draft
  - AI
  - GIS
  - Python
summary: "AI can write ArcPy scripts quickly. A safety harness makes them easier to review, run, and trust."
layout: rich
---

<img src="/static/images/vibe-coded-gis-safety-harness-hero.jpg" alt="A serious retro-futuristic robot in a safety vest and helmet gives a thumbs up against a contour-map landscape" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

AI can write an ArcPy script in seconds.

That is the easy part.

> **Want the guardrails to already be there?** [ArcPy Safety Harness ->](https://dannymcvey.com/products/arcpy-safety-harness/) is a copyable, platform-agnostic starting point for safer AI-assisted ArcPy work.

The harder question is whether you should run that script against a real geodatabase.

A script can look completely reasonable and still do something you did not intend. It can point at production data instead of a copy. Update the wrong field. Overwrite an output. Delete something it thought was temporary. Finish with no errors and still leave you with a problem.

That is not really an AI problem. It is a software problem that AI makes easier to create.

When you write a script yourself, you usually build up a mental model as you go. You choose the workspace. You think about outputs. You pause before an update cursor or `Delete_management`.

When an AI assistant gives you 300 lines of code at once, the relationship changes. The bottleneck is no longer writing code.

It is trust.

## "Please be careful" is not a safety feature

Sure, you can prompt an AI assistant to validate inputs, use a dry run, log its work, and avoid overwriting data.

But will everyone on your team remember to ask?

Will they know which safeguards matter? Will they phrase the prompt well? Will the assistant actually implement them? Will somebody catch the missing confirmation step when the script is needed by Friday?

Probably not. Not consistently.

A prompt is a request.

A safety harness is an environment.

The important safeguards should already exist when the AI starts working. They should not depend on someone remembering to summon them into existence.

## What belongs in the harness

This does not need to be a giant framework. It can be a small, copyable project structure with a few strong opinions:

- Keep paths and settings in one obvious place.
- Confirm that inputs exist and have the expected fields.
- Default to a dry run for operations that edit or delete data.
- Require an explicit opt-in for destructive actions.
- Do not overwrite outputs by accident.
- Write logs and a simple run receipt.
- Fail early, before a half-finished workflow leaves confusing debris behind.

The exact implementation can vary. The principle should not.

Before a workflow runs, it should be able to say:

> Here is the dataset I am about to touch. Here is what I plan to change. Here is where outputs will go. Here is what will be overwritten, if anything.

Then the person running it gets to say yes or no.

That is a much better interface than double-clicking a Python file and hoping the paths are right.

## Better structure makes AI more useful

A safety harness is not about slowing down AI-generated work. It is about making it easier to use responsibly.

Without one, every script starts from zero. Every time, someone has to remember:

- Did we validate the input?
- Where are the outputs going?
- Does this overwrite anything?
- What happens if it fails?
- Can we tell what it did afterward?

With a harness, the assignment becomes much clearer:

> Add this workflow inside the existing project. Preserve the validation, dry-run behavior, output conventions, run receipt, and confirmation step for edits.

Now the AI has boundaries. The reviewer knows where to look. The domain expert has a predictable way to inspect what is about to happen.

The assistant still writes the implementation. You still own the judgment.

But the responsible path is no longer dependent on a perfect prompt.

## Scripts become software when failure is part of the design

A one-off script usually assumes everything will work.

A tool meant for real work has to account for reality:

- A dataset is locked.
- A field is missing.
- The workspace is wrong.
- The output already exists.
- Someone runs it twice.
- The workflow gets halfway through and fails.

That is when an ArcPy script starts becoming software. Not when it has more lines of code. When it has an opinion about what happens before, during, and after the geoprocessing call.

AI is going to help more people make more ArcPy scripts.

Good.

Now we need a better default than "copy this into a new `.py` file and be careful."

Your AI-generated ArcPy does not need to be perfect.

It needs a safety harness.

**If you want to start from that safer default, [get the ArcPy Safety Harness](https://dannymcvey.com/products/arcpy-safety-harness/). It gives you a practical foundation for building, reviewing, and running AI-assisted GIS automation with more confidence.**
