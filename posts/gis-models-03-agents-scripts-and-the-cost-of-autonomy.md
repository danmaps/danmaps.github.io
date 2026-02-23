---
title: "Agents, Scripts, and the Cost of Autonomy"
series: "Choosing the Right AI Model for the Right GIS Job"
series_index: 3
date: 2026-02-22
tags:
  - Unlisted
  - AI
  - GIS
  - Agents
  - Automation
  - Models
  - Reliability
---

Agents are the natural next step after “LLM writes a script”.

Instead of generating code once, you let the model decide what to do next.

That is powerful.

It is also where model choice stops being “quality” and starts being **governance**.

## Core question

When does it make sense to let a model decide what to do next?

And what does “the right model” look like when autonomy is on the table?

## Case study

Same task, two approaches:

### Approach A: Fixed Python script

- deterministic
- testable
- boring
- reliable

### Approach B: Agent-driven workflow

- adaptive
- can recover from surprises
- can also confidently do the wrong thing faster

Same data, same environment.

Different models powering the agent.

## What I’ll compare

### Recovery from data changes

- field renamed
- layer missing
- projection mismatch
- geometry invalid

Does it:

- stop and ask
- search for alternatives
- keep going and invent things

### Risky actions avoided (or not)

GIS has actions that are easy to do and hard to undo:

- overwrite outputs
- delete intermediates
- dissolve away detail
- publish wrong data

A good agent should treat these like a loaded weapon.

### Logging and explainability

If the agent did something, can a human:

- reconstruct what happened
- reproduce it
- identify the decision point where it went sideways

### Human intervention required

The real measure isn’t “did it finish”.

It’s “how many times did a human have to rescue it” and “how bad would it have been if nobody noticed”.

## What I’ll show

- One small model making confident bad decisions
- One larger model stopping and asking
- Why “asking” is often the correct behavior in GIS

## Key takeaway

**Autonomy is not free. Model choice is governance.**

You are selecting not just capability, but behavior under uncertainty.

## Next steps

I’ll fill this with:

- one concrete end-to-end workflow
- the logs from an agent run
- the guardrails that turned “agent” into “safe tool”
