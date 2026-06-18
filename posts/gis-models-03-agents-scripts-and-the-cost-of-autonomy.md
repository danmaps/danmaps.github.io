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
layout: rich
---

Agents are the natural next step after â€œLLM writes a scriptâ€.

Instead of generating code once, you let the model decide what to do next.

That is powerful.

It is also where model choice stops being â€œqualityâ€ and starts being **governance**.

## Core question

When does it make sense to let a model decide what to do next?

And what does â€œthe right modelâ€ look like when autonomy is on the table?

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

## What Iâ€™ll compare

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

The real measure isnâ€™t â€œdid it finishâ€.

Itâ€™s â€œhow many times did a human have to rescue itâ€ and â€œhow bad would it have been if nobody noticedâ€.

## What Iâ€™ll show

- One small model making confident bad decisions
- One larger model stopping and asking
- Why â€œaskingâ€ is often the correct behavior in GIS

## Key takeaway

**Autonomy is not free. Model choice is governance.**

You are selecting not just capability, but behavior under uncertainty.

## Next steps

Iâ€™ll fill this with:

- one concrete end-to-end workflow
- the logs from an agent run
- the guardrails that turned â€œagentâ€ into â€œsafe toolâ€

