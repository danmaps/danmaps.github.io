---
title: The Human Stays Sequential
date: 2026-09-10
tags:
- Draft
- AI
- Agents
- Systems
summary: "Parallel coding agents change the shape of software development, not just its speed. Implementation can happen concurrently, but defining work, reviewing it, and deciding what belongs still depend on my attention."
layout: rich
---

I can only define one task at a time.

That sounds like a limitation. But I think it describes something important about how software development changes when coding agents can work in parallel.

The familiar development loop is mostly sequential: define a task, implement it, review it, repeat. I decide what needs to happen, write the code, check the result, and move on.

A coding agent changes who does the implementation. Several coding agents change what I can do while implementation is happening.

While an agent works on Task 1, I can define Task 2. While those two agents are working, I can define Task 3. I am still doing one thing at a time, but several pieces of work can move forward without waiting for my next turn.

**The human is still sequential. The work isn't.**

## Worktrees make this practical

Git worktrees are a surprisingly important piece of this.

One coding agent gets its own worktree and branch. Another gets another. They can work on the same repository without sharing a working directory or overwriting each other's uncommitted changes.

The worktree-based sessions in the GitHub Copilot app make that separation useful: each session has somewhere to work, and its changes can come back for review independently.

That does not make the changes independent in an architectural sense. Two agents can still make incompatible decisions in separate directories. Worktrees isolate the editing, not the assumptions.

But they remove a practical obstacle. I do not have to wait for one agent to finish before another can safely start editing.

The interesting part is not simply that four agents can write code at once. It is what I do while they are writing it.

I define the next task.

## Review is the other end of the pipeline

Eventually, completed work starts coming back.

Now I have another activity that needs focused attention: review. I need to understand what changed, whether it solves the intended problem, and whether it fits the rest of the system.

Agents can help inspect code, run tests, and respond to feedback. But I still have to decide what I am willing to integrate. I cannot meaningfully make four of those decisions at once.

The workflow starts to look like a pipeline:

- **Definition is sequential.** I frame and dispatch one task at a time.
- **Implementation is parallel.** Agents work on separate tasks concurrently.
- **Review is sequential.** I examine the results and decide what belongs.

These are not three clean phases. I might stop defining a new task to review a finished one, then send it back for changes while I look at another. Later tasks can keep running throughout.

That feels like a more useful mental model than "AI writes code faster." It explains both the leverage and the constraint.

If work comes back faster than I can review it, adding another agent mostly gives me a longer queue.

## The bottleneck moves

For a long time, implementation was expensive enough to dominate the workflow. I could have ten ideas for improvements, but somebody still had to write all that code.

Parallel coding agents can make implementation capacity much less scarce. That does not eliminate the work. It changes which work deserves more of my attention.

What should we build? Can this task be separated from the others? What constraints does the agent need to know? What does "done" mean, and how will I verify it?

Then there is the question that a passing test suite cannot settle on its own: does this change belong in the system we are building?

Those are software engineering questions. They were always part of the job. Now they can occupy a much larger percentage of it.

## Issues become units of work

This changes how I think about writing GitHub issues.

"Add retries" might be enough to remind me of a conversation. It is not enough context for an agent working independently.

A dispatchable version would specify which operation to retry, which failures are eligible, how attempts are bounded, and what should happen when retries are exhausted. It would also say which behavior must not change and how to demonstrate that the result is correct.

For example, a task might call for bounded retries on a read-only request after a transient server error, while leaving authentication failures alone. That gives an agent a boundary to implement and gives me something concrete to review.

The issue is no longer just a reminder. It carries enough intent for work to proceed while my attention is elsewhere.

That is why specification quality matters so much here. Vague tasks do not become clearer when I dispatch more of them. They create more simultaneous opportunities for agents to fill in the blanks differently.

## The skill is decomposition

There is a temptation to call all of this prompt engineering. I do not think that gets at the difficult part.

The hard part is recognizing boundaries.

Which changes are genuinely independent? Which share assumptions? Which need to wait for an interface or a data model to settle?

Two agents might each build a reasonable abstraction for the same problem. Both changes could pass their own tests and still leave me with two competing designs to reconcile.

Running four agents against four poorly separated tasks could create more work than running one. Separate branches do not change that.

Sometimes the useful move is to establish the shared contract first, then parallelize the work around it. Sometimes it is to keep a tightly coupled change together. The goal is not to keep every available agent busy. It is to get coherent work through review.

## A technical lead on a team of one

This starts to resemble technical leadership: defining work, providing context, delegating implementation, reviewing results, and deciding what gets integrated.

The strange part is that this structure can now exist for a team of one.

I do not suddenly have four brains. My attention remains stubbornly sequential, and the responsibility for the result does not disappear because several agents contributed to it.

But implementation no longer has to wait for my attention at every step.

That is the leverage I care about: not how many agents I can launch, but how well I can define work that moves independently and comes back in a form I can understand.

The human stays sequential. The software development process does not have to.
