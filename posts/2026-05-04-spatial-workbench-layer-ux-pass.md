---
date: 2026-05-04
tags:
  - Draft
  - GIS
  - AI
  - product
  - work
title: Spatial Workbench Needed a Layer UX Pass Before Anything Smarter
layout: rich
---

This past week I did a concentrated UX pass on Spatial Workbench.

Not the flashy kind. Not "we added agent magic" or "AI now does everything." The opposite, really.

I spent the week making layers behave more like real objects in the system and less like temporary side effects of tools.

That meant a few concrete things:

- defining a canonical layer model
- documenting the table-of-contents action model
- normalizing multi-feature imports into single layers
- improving layer naming, badges, removal, and summaries
- separating mobile tools and data views
- adding a responsive attribute inspector
- fixing mobile top bar overlap
- fixing a desktop attribute drawer layout regression

On paper, that sounds like a grab bag of UI chores. In practice, it felt like foundational product work.

## The temptation is always to skip this part

Spatial Workbench is interesting because it sits in a useful middle zone:

- lighter than a full desktop GIS
- more inspectable than most map demos
- more spatially concrete than generic AI playgrounds

That makes it very easy to start dreaming about the "smart" parts.

More tools. More automation. Better AI feature generation. Agent-driven workflows. Provenance. Replay. Scoring. Guidance.

All of that is still interesting.

But if the layer model is fuzzy, the contents pane is awkward, mobile navigation is clumsy, and results from tools donâ€™t land in a predictable structure, then every higher-level feature is built on mush.

Iâ€™ve been noticing this pattern a lot lately: the real bottleneck often isnâ€™t missing intelligence. Itâ€™s missing shape.

## Layers had to become first-class

A lot of GIS software treats layers as obvious because decades of convention already did the hard work. You inherit a whole mental model for free.

When you build a small spatial tool from scratch, you do not get that for free.

You have to decide things like:

- what exactly counts as a layer
- when a tool result becomes a new layer versus updating an existing one
- how imported data should group
- what metadata belongs to the layer
- what actions should be available from the layer row
- how much detail the UI should expose by default

That is not glamorous work, but it determines whether the app feels coherent.

One concrete improvement this week was normalizing multi-feature results into single layers. That sounds tiny, but it matters. If one import or tool execution explodes into a messy pile of pseudo-layers, the app stops feeling inspectable and starts feeling accidental.

The same goes for naming, badges, summaries, zoom actions, and properties. Those details are not decoration. They are how the system explains itself.

## Inspectability is the product

I keep coming back to this idea.

For a project like Spatial Workbench, the product is not just "map stuff on a screen." It is the ability to see what happened and why.

That is why I care about things like:

- clear layer identity
- visible geometry state
- readable metadata
- understandable tool outputs
- predictable UI behavior across desktop and mobile

If AI is involved, this matters even more.

I do not think the interesting future of spatial AI is a black box that emits impressive shapes. I think it is a system where generated geometry can be inspected, edited, traced, combined with other data, and treated like any other object in the workspace.

That only works if the "boring" substrate is solid.

## Mobile was a good reality check

Some of the work this week was specifically about mobile: splitting tools and data into separate views, measuring the mobile bar correctly, and fixing layout overlap.

Mobile has a way of exposing whether your structure is real or just barely holding together on a large screen.

If a UI only works when there is infinite horizontal space, then a lot of its clarity was fake.

The responsive attribute inspector was part of the same lesson. I did not just need data to exist. I needed it to remain reachable and understandable when the screen got smaller and the layout got tighter.

That kind of constraint is annoying in the moment, but useful. It forces decisions.

## This is the kind of work AI does not save you from

AI can absolutely help generate code for this sort of pass. It can suggest layouts, tests, event handlers, and refactors.

But it does not remove the need to decide what the app should actually be.

This week felt like a good example of where product thinking still earns its keep.

The hard part was not writing a resize listener or a drawer component. The hard part was deciding that Spatial Workbench needed a layer UX pass more than it needed another clever feature.

That is the judgment call.

And honestly, I think it was the right one.

Because now the project feels a little less like a pile of promising spatial tools and a little more like a coherent environment.

That is usually the real prerequisite for smarter things later.

## Draft takeaway

I am trying to get better at respecting this phase of a project.

Not every useful week produces a headline feature. Sometimes the meaningful progress is that the system got more legible, more predictable, and more honest about its own structure.

For a tool meant to support spatial thinking, that seems like real progress.

