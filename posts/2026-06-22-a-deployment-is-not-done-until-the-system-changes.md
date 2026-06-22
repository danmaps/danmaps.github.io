---
title: A Deployment Is Not Done Until the Running System Changes
date: 2026-06-22
tags:
  - Draft
  - systems
  - deployment
  - AI
  - work
summary: "The most useful technical lesson from this week was simple: a repo update, a successful build, and a restarted stack do not mean the running system actually changed. If the behavior matters, you need proof from the live runtime."
---

This week I spent some time getting `resume-tailor` into a more real state on my homelab.

That included Docker deployment work, wiring the web app to the API cleanly, getting assisted tailoring working with a server-side model key, and restoring `.docx` and PDF export behavior after it broke.

The technical details were specific.
The lesson was broader.

I keep running into the same rule:

**a deployment is not done until the running system changes.**

That sounds obvious.
It is amazing how easy it is to forget in practice.

## There are several fake definitions of "deployed"

A lot of us still use sloppy stand-ins for deployment success:

- the code was merged
- the repo was pulled on the server
- `docker compose up -d --build` finished
- the container restarted
- the logs looked mostly normal

Those things can all happen while the actual behavior stays old.

That is exactly what bit me.

In `resume-tailor`, the export buttons were visible in the UI.
The deploy checkout on disk had the newer code.
The stack had been rebuilt.
And yet the live API was still returning `404` for the export routes.

From a distance, that looks contradictory.
It is not.
It just means the system you think you updated is not always the system that is actually serving requests.

## Repo state is not runtime truth

One of the more useful debugging habits is separating three things that people casually collapse into one:

- repo state
- image state
- running container state

Those are related.
They are not interchangeable.

You can have the right repo checkout and the wrong image.
You can have the right image built and the wrong container still running.
You can have a container that restarted but is still serving behavior you did not expect because the rebuild boundary was wrong.

This week I had a version of all of that.

One problem was packaging.
`origin/main` was not actually cleanly Docker-deployable as merged because the web image build was missing files it needed, including shared package content and the master resume JSON.

That is already a useful reminder: if the deploy path is not reproducible from the main branch, then the branch is not really deploy-ready.

Then there was the second problem, which I think is even more interesting.

Later, after newer code had landed, the app still behaved like an older API was running even though the checkout on disk had moved forward.
The fix was not just "build again."
The reliable fix was to force the relevant service to rebuild without cache and recreate the running container so the new image actually became the active runtime.

That is the kind of issue that makes you suspicious in a healthy way.

## A successful build is still only a hypothesis

This is the part I want to remember.

A build step is not proof of live behavior.
It is a hypothesis about live behavior.

So is a deploy command.
So is a green container status.

If the feature that matters is "can this API export the file now?" then the only thing that really answers the question is checking the live API.

That might mean:

- hitting the real route
- inspecting the OpenAPI schema
- checking the running file inside the container
- making a known request and validating the response

In other words, you need runtime evidence.

That sounds a little boring.
Good.
Boring verification is better than confident fiction.

## The system should prove itself at the seam that matters

What I like about this lesson is that it scales beyond Docker.

The exact same pattern shows up in a lot of software work:

- a feature flag is enabled but the user path still fails
- a model integration is configured but the live endpoint is still using old behavior
- a migration ran but the app process did not pick up the expected schema state
- a static site froze correctly but the deployed output did not actually include the new artifact

The seam that matters is not "did some internal step succeed?"
It is "did the externally relevant behavior change in the place I care about?"

That is the seam worth checking first.

I think this is one reason I keep gravitating toward inspectable systems.

If a runtime is opaque, you are stuck negotiating with vibes:

- I think the right code is there
- I think the rebuild probably happened
- I think the service restarted
- I think this should work now

That is not a satisfying way to operate.

The better version is:

- here is the running container ID
- here is the active image
- here is the route definition in the live process
- here is the response from the real endpoint
- here is the artifact the user can now download

That is much closer to truth.

## This is not just ops advice

I do not really see this as a narrow DevOps lesson.

It feels connected to a broader rule that keeps showing up in my AI and systems work:

**do not confuse internal process with delivered reality.**

A mission system is not useful because it produced a plausible-looking summary.
It is useful because it left the right artifact, changed the right state, or completed the right task in a way that can be checked.

A writing workflow is not complete because a draft exists somewhere.
It is complete when the draft is in the right repo, frozen correctly, staged, reachable, and in the intended publish state.

A deployment is not done because a command ran.
It is done when the user-facing behavior changed and you can prove it.

That sounds stricter than a lot of modern software culture.
I think stricter is good here.

We already have enough layers that can make progress look more finished than it is.
The answer is not more narration.
It is better checks.

## What I want more systems to do

I want more of my tools to make this kind of proof easier by default.

Not in a giant enterprise dashboard sense.
Just in the practical sense of leaving behind the evidence that answers the obvious follow-up questions.

What version is actually running?
What changed?
What route is live?
What artifact was produced?
What command last recreated this service?

That is useful for homelab apps.
It is useful for internal tools.
It is useful for agent systems.

If an agent says it deployed something, I do not mainly want a polished summary.
I want a receipt that survives contact with reality.

## The takeaway

The most useful progress I made this week was not just getting `resume-tailor` more operational.
It was being reminded that "updated" has layers, and the only layer that really counts is the one the running system can prove.

Merged is not deployed.
Built is not deployed.
Restarted is not deployed.

Changed behavior, verified live, with evidence:
that is deployed.
