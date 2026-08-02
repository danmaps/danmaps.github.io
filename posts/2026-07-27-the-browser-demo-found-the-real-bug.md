---
title: The Browser Demo Found the Real Bug
date: 2026-07-27
tags:
- Draft
- GIS
- Systems
- Product
summary: "Recent Spatial Workbench work reinforced a practical rule I trust more every week: a demo only counts if it exercises the real system path. The browser headless demo surfaced a live runtime dependency that tests and local setup had been quietly masking."
layout: rich
---

<img src="/static/images/the-browser-demo-found-the-real-bug-hero.png" alt="Editorial illustration of a browser-driven spatial workflow exposing a hidden fault line in a live system path" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

This week I spent a chunk of time making Spatial Workbench more callable.

Not more impressive in screenshots.
More callable in the boring sense that matters:

- a human should be able to run the workflow
- a script should be able to run the workflow
- an agent should be able to run the workflow
- they should all be touching the same real system

That work led to one of my favorite kinds of result:

**the demo found the real bug.**

I trust that kind of progress more than a clean architecture diagram every time.

## The useful milestone was not just "we have a demo"

The concrete step was a same-origin browser headless demo for Spatial Workbench.

It runs the canonical chain:

- `RandomPointsTool`
- `BufferTool`
- `ExportTool`

And it does that by calling the live `/api/run` surface directly from the browser.

That may sound small.
It is not.

There is a big difference between:

- a local script that succeeds in a controlled setup
- a test harness that proves the happy path
- a browser page hitting the live runtime the way a real user-facing surface would

The first two are useful.
The third is where hidden assumptions start dying.

That is exactly what happened here.

## The browser path exposed a dependency the local path was masking

While deploying the browser demo, I found a real production bug in the headless runtime.

Some live layer-state tools were implicitly depending on `global.turf` bootstrap that happened in tests and local demo setup.

That meant the system looked healthier than it really was.

The local path had been giving me partial truth:

- the tools looked callable
- the demo looked plausible
- the tests looked reassuring

But the live runtime had a dependency that was not honestly owned at the runtime layer.

The browser demo surfaced it because it was exercising the actual deployed path instead of a slightly padded development version of reality.

That is why I keep caring about proof surfaces.

A proof surface is not just marketing.
It is a way to force the system to show whether the real path works.

If the proof path is fake, the confidence is fake too.

## This is why I like browser demos more than polished "capability" pages

A lot of product work around AI and developer tooling still leans too hard on surfaces that imply power without proving much.

You get:

- a nice landing page
- a broad claim about what the system can do
- maybe an animation
- maybe an abstract architecture diagram

What you do not always get is a path that actually executes the real thing.

I care much more about a page that can prove:

- this endpoint is live
- this tool chain runs
- this artifact gets produced
- this output can be checked

That is why the Spatial Workbench landing work mattered too.

I moved the public root toward a clearer product story: callable spatial tools for agents, scripts, and humans.

But I do not think the story earns trust by itself.
It earns trust when the story sits next to a working proof path.

The headless demo does that better than a paragraph ever could.

## Hardening the proof path mattered as much as finding the bug

Once the browser path exposed the hidden dependency, the right next move was not to celebrate that "we found something."

The right move was to make that class of failure harder to hide next time.

So the recent Workbench work also tightened the validation loop:

- `npm run test:headless`
- `npm run demo:headless`
- headless artifact validation for the exported GeoJSON
- a GitHub Actions `Headless Smoke` workflow that runs the chain and uploads the artifact

I like this direction because it turns the demo from a one-off proof into an operational check.

The useful question is no longer just:

> can I run this once on my machine?

It becomes:

> does the system keep proving the same path under conditions closer to reality?

That is a much better standard.

## The MCP layer should be thin on purpose

Another recent step was adding the first-pass MCP layer on top of the Workbench runtime.

The important part was not "now it has MCP."

The important part was keeping the adapter thin.

`list_tools` wraps the existing API discovery.
`run_tool` wraps the existing execution surface.
Returned `state` stays opaque.
Execution receipts stay the audit surface.

That is the right shape for this stage.

I do not want an adapter that invents a second personality for the product.
I want one that exposes the existing capability boundary cleanly enough that agents can call it without hiding what is really happening.

Thin adapters are underrated.

If the underlying runtime is solid, a thin adapter preserves truth.
If the underlying runtime is weak, a thin adapter reveals that quickly.

Both outcomes are useful.

## The broader lesson is simple

If you want to make a system callable by humans, scripts, and agents, do not start by asking how clever the interface should feel.

Start by asking:

- what is the real execution path?
- which proof surface touches it directly?
- what assumptions are being masked by local setup?
- what artifact proves the run actually happened?

This is one reason I keep preferring practical, inspectable progress over grand claims about autonomy.

A browser demo hitting the live system taught me more than a lot of abstract orchestration talk would have.

It found the hidden dependency.
It clarified the runtime boundary.
It justified better smoke checks.
It strengthened the product story because the product story now has a working proof attached to it.

That is the kind of work I believe in.

Not "look what AI might do someday."

More like:

**here is the path, here is the run, here is the artifact, and here is the bug it forced into the open.**

That is a much better foundation for building tools that other systems can trust.
