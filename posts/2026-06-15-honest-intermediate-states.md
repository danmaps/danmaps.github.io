---
title: Honest Intermediate States Make Better Systems
date: 2026-06-15
tags:
  - Draft
  - AI
  - systems
  - workflow
  - writing
summary: "A lot of the most useful work I did this week had the same shape: make the in-between state real. Drafts that can be shared without pretending they are finished, memory that can be revised instead of rediscovered, and mission systems that preserve intake and failure context instead of flattening everything into a fake success."
---

A lot of the useful work I did this week would look unimpressive in a launch thread.

No giant feature reveal.
No dramatic before-and-after demo.
No big claim about autonomous magic.

Mostly, I spent time making intermediate states more honest.

That sounds small. I think it is one of the more important design choices in any real system.

## The fake version of software wants to skip the middle

A lot of tools still behave as if the only states that matter are:

- not started
- done

Everything in between gets compressed into a vague progress bar, a reassuring status message, or a polished little bluff.

I do not trust that pattern much anymore.

In real work, the middle matters.

There is a big difference between:

- a draft that is coherent but still open to revision
- a frozen version that should stop changing structurally
- a published draft that is live by direct URL but intentionally not on the homepage
- a failed run that left enough evidence to debug
- a repair attempt that improved something but did not fully pass

Those are not cosmetic distinctions.
They are operational distinctions.

When software collapses them into one status, humans have to reconstruct the truth manually.

## This showed up in the blog workflow first

One concrete thing I tightened this week was the writing workflow for my site.

That was less about prose and more about state.

I added a clearer distinction between:

- drafting a post
- freezing a post
- publishing a draft
- publicly publishing a post

That matters because those are not the same action.

For `danmaps.github.io`, a post can stay tagged `Draft`, get frozen, be pushed live, and remain off the homepage while still having a real URL.

I like that a lot.

It means I do not have to choose between two bad options:

- keep ideas private until they feel overly polished
- throw half-formed writing onto the main feed

There is a better middle.

I can ship a real artifact.
I can preserve editorial caution.
I can keep momentum without pretending certainty.

That is a much healthier workflow than treating every post as either invisible or final.

## The same pattern showed up in memory

This week I also added a real long-term `MEMORY.md` layer on top of daily notes.

Again, that is not flashy work.
It is state design.

Without a durable middle layer, you get an annoying loop:

- daily notes become a pile
- useful lessons get buried
- the same context has to be rediscovered
- the system starts sounding forgetful even when the information exists somewhere on disk

The fix is not "more memory."
It is better memory states.

Raw daily notes are useful.
Curated long-term memory is useful.
Treating those as the same thing is not useful.

I keep noticing this across projects: a lot of systems get better when you stop asking one layer to do every job.

## Symphony keeps teaching me the same lesson

The Symphony work sitting behind a lot of my recent thinking still points in the same direction.

The part I trust is not the part that sounds most autonomous.
It is the part that keeps the system honest about what happened in the middle.

Recent Symphony changes preserved webhook intake metadata when a mission is created, exposed attachment references more clearly in mission detail, and kept recent mission runs on disk as inspectable records.

That is useful because a mission is not just a prompt.

It has provenance.
It has context.
It may have attachments.
It may have a repair attempt.
It may have failed after partially succeeding.

If the system throws all of that away and just reports a result, it turns real work into theater.

I want the opposite.

I want a mission system that can answer simple questions later:

- where did this work come from?
- what file came with it?
- what did the system try first?
- what repair happened after failure?
- what state is this in right now?

That is not bureaucracy.
That is the minimum needed for trust.

## Good systems should make partial truth visible

I think this is one reason so much AI tooling still feels slippery.

It is often optimized to avoid awkwardness.

If a run was incomplete, it wants to sound complete.
If an output was thin, it wants to sound helpful.
If a workflow is still evolving, it wants to present itself as a finished platform.

That instinct is understandable and usually wrong.

I would rather use a system that says:

- this is a draft
- this run failed validation
- this repair improved the output but did not finish the job
- this memory is curated and this other note is raw
- this artifact is live but intentionally unlisted

Those are much better boundaries.

They let the software be useful without forcing it to lie about its maturity.

## I trust systems more when they admit what they are

That is probably the broadest lesson I am taking from this week.

The boring-sounding work was not really about blog metadata or agent plumbing.
It was about building systems that admit what state they are actually in.

I trust that more than polish.

I trust a live draft more than a fake final.
I trust a visible failed run more than a smooth summary of imaginary success.
I trust curated memory more than a pile that calls itself knowledge.

The middle is where a lot of real work lives.

Software should stop pretending otherwise.

## The takeaway

If a system is going to be part of real work, its intermediate states need to be first-class.

Not hidden.
Not implied.
Not rounded up to success.

Draft.
Frozen.
Published-but-unlisted.
Pending.
Failed.
Repaired-but-still-incomplete.

Those states are not signs of weakness.
They are signs that the system is telling the truth.

And at this point, I think truthful state is more useful than impressive narration.
