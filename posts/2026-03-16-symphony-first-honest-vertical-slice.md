---
date: 2026-03-16
tags:
  - Draft
  - AI
  - Agents
  - side-projects
  - systems
  - homelab
title: "Symphony and the first honest vertical slice"
---

Over the last few days I finally got Symphony into a shape that feels real.

Not finished. Not impressive in the "autonomous agents are coming" sense. Real in the much less glamorous sense that I can point at the repo and say: this now has a coherent boundary, a small API surface, a documented layout, and a clearer idea of what belongs in the system versus what is still hand-wavy ambition.

That matters more than the demo.

## The main decision: keep Symphony narrow

The most important progress was not adding code. It was deciding what Symphony is **not**.

I do not want it to become a vague "AI operating system" or a replacement for OpenClaw. That path leads straight into architecture cosplay.

The useful version is narrower:

- a **mission / validation / delegation layer**
- running locally
- inspectable on disk
- opinionated about structure
- willing to escalate only when needed

That framing immediately made the project easier to reason about.

## What changed

The repo started as a scaffold. Today it looks more like an actual product skeleton.

A few concrete changes got it there:

### 1. I replaced the hardcoded demo with a generic mission API

This was the biggest shift.

Instead of treating the app like a one-off proof of concept, Symphony now exposes a basic mission flow:

- `POST /missions`
- `GET /missions/{mission_id}`

That sounds small because it is small. Good.

You can submit a score payload, write a mission run to disk, and retrieve the stored request / score / validation state later. That is not "agent orchestration" in the flashy sense, but it is the first version of a system that can be inspected, replayed, and debugged.

That is the kind of boring I trust.

### 2. I added model exercise endpoints

I also added:

- `GET /models`
- `POST /models/exercise`

This is one of those things that looks secondary until you actually build local AI tooling.

If your routing story depends on local models, you need a dead-simple way to answer basic questions:

- What models are visible?
- Which alias maps to what?
- Can this thing answer a prompt right now?

Without that, every failure turns into a ghost story. With it, the system gets a little more legible.

## 3. I separated reusable specs from runtime runs

This may be the most important structural change in the repo.

I split mission definitions into:

- `missions/specs/` for reusable mission templates
- `missions/runs/` for runtime-created mission instances

And I did the same kind of cleanup for reports.

That sounds obvious in retrospect, which is usually a sign it was the right move.

Before that split, the repo was already drifting toward the classic prototype problem: examples, generated artifacts, and reusable definitions all living too close together. That is how projects get confusing faster than they get useful.

The new layout makes a simple distinction:

- what the system knows how to do
- what happened during a specific run

If I want Symphony to be inspectable and eventually replayable, that distinction is not optional.

## 4. I wrote the docs early enough to matter

I also added and updated the boring documents that tend to get postponed:

- `README.md`
- `API.md`
- `DEVELOPMENT.md`
- `ARCHITECTURE.md`
- `ROADMAP.md`

I am increasingly convinced that writing docs early is not a ceremony problem. It is a design pressure problem.

If you cannot explain the shape of the system in a few files, the shape is probably not real yet.

In this case, the docs forced some useful honesty:

- the current endpoints are small
- the model defaults are practical, not magical
- the next steps are obvious
- the non-goals matter as much as the goals

That last part is doing a lot of work.

## The deeper lesson: architecture should earn the right to exist

I have a strong tendency, like a lot of technical people, to enjoy naming things a little too early.

Conductor. Melody. Composition. Performance. Resonance.

Those names are fun. They are also dangerous.

It is very easy to build a vocabulary for a system before you have built the system itself. Once that happens, you can trick yourself into feeling more progress than you have actually made.

What made this week feel different is that some of the architecture started earning its keep.

The names are no longer floating abstractions. They are attached to a repo with:

- a real API
- actual test coverage
- local model checks
- on-disk mission state
- clearer separation between definitions and execution

Still early. Still incomplete. But at least now the words are attached to something.

## What is next

The roadmap is still pretty simple:

- worker dispatch
- actual step execution
- run / replay flows
- better validation
- reporting

In other words: the part where Symphony actually starts doing work instead of just describing how work should be done.

That is fine. The point of this pass was not to pretend the orchestration layer is mature. The point was to get to a first honest vertical slice.

I think it is there now.

And honestly, that is the part of building I trust most: when a project stops sounding clever and starts becoming inspectable.
