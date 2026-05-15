---
title: Inspectable Tools Still Need Clear Modes
date: 2026-05-11
tags:
  - Draft
  - GIS
  - AI
  - product
  - work
---

I spent some time this week tightening up **Spatial Workbench**, and the work was a useful reminder that "inspectable" is not the same thing as "self-explanatory."

I have been circling a bigger idea with a lot of my projects lately: if geometry, tools, and state are visible, humans and AI agents can reason about them together instead of treating GIS like a black box. I still think that is the right direction.

But visible systems can still be awkward.

This week’s work was less about adding flashy capability and more about reducing ambiguity in the product.

## The product got clearer in three ways

First, I fixed some spec drift in the repo and pushed a better docs flow for tools. Spatial Workbench now generates a static per-tool documentation site from the tool specs, links to those docs from the selected tool panel, and includes a workflow to keep the generated specs and docs in sync on relevant pushes.

That is not a glamorous feature, but it matters. If the tool system is declarative, the docs should fall out of the same source of truth. Otherwise the project starts making promises in three places at once: the code, the UI, and the README. That gets sloppy fast.

Second, I made the map interaction model more explicit by separating **Select** and **Inspect** modes while leaving Draw, Edit, and Delete alone.

That sounds small, but I think it is important. A lot of map tools blur "I am selecting features" and "I am poking around for details" into one mushy click behavior. That kind of ambiguity is survivable in a personal prototype, but it becomes friction as soon as the app wants to teach anyone else how to use it, including future-me.

Now the behaviors are clearer:

- **Select** is for selection only
- **Inspect** is for opening details and updating the active context

That is a better mental model than one click trying to do everything.

Third, I opened up the next layer conceptually by sketching an **MCP server direction** above Workbench's headless API. The idea is not to turn the project into "AI GIS" marketing fluff. The idea is to make the spatial tools callable in a way that lets agents build useful, opinionated micro-apps on top of deterministic geometry operations.

That distinction matters to me.

I do not want magic map demos. I want inspectable systems with enough structure that automation can be useful without becoming opaque.

## The lesson was product, not just implementation

The interesting part of this week was not any single feature. It was the pattern.

When a project starts as a sandbox, you can get away with a lot of fuzzy edges because the person using it is also the person who built it. Context fills the gaps.

As soon as you start thinking about broader use, those gaps become the work.

Not because the underlying geometry operations are hard. In many cases they are already straightforward. The hard part is making the system legible:

- what tool is available
- what it expects
- what clicking means right now
- where the output went
- whether a human or an agent could repeat the same operation on purpose

That is the kind of product work I increasingly care about.

A lot of software energy still goes into either heavyweight enterprise surfaces or clever demos. I am more interested in the middle layer: tools that are lightweight enough to experiment with, but structured enough to trust.

## Why I think this matters for AI too

I keep coming back to the same opinion: AI becomes more useful when it operates inside systems with visible state and constrained actions.

If a spatial tool is inspectable, documented, and mode-driven, an agent has a better chance of using it well. More importantly, a human has a better chance of seeing what happened and correcting it when needed.

That is a much healthier direction than pretending the model should just "do GIS."

For now, the practical takeaway is simple: making a tool inspectable is a good start, but it is not the finish line. If the interaction model is muddy or the docs drift from the source of truth, the system is still harder to trust than it should be.

This week was a good reminder that clarity is a feature.
