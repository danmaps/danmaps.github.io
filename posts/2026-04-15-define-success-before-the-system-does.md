---
title: "Define Success Before the System Does"
date: 2026-04-15
tags:
  - Draft
  - AI
  - evaluation
  - systems
  - agents
  - governance
---

![Define Success Before the System Does](/static/images/define-success-route-hero.jpg)

We often talk about evals as if they are just measurement tools.

Did the model pass?
Did the agent complete the task?
Did the benchmark score go up?

That framing is too small.

Evals do more than measure performance. They define what performance is. They turn values, tradeoffs, and institutional preferences into something a system can optimize.

That matters much more than people think.

While humans are still in the loop, we still have a chance to define success carefully. Once that loop thins out, the system will keep pursuing whatever objective we gave it — whether or not it still serves us.

## We already know this from traditional ML

This is not a brand new agent-era problem.

Traditional machine learning already taught us the lesson.

Pick the wrong metric and you get the wrong system:

- optimize for clicks and you get clickbait
- optimize for engagement and you get compulsion
- optimize for a narrow benchmark and you get systems that look good in testing but fail in the real world
- optimize for a proxy and eventually the proxy becomes the real objective

None of this required malicious intent.

It just required a system that got very good at pursuing the thing we told it to pursue.

That is the basic pattern.

First we choose the metric.
Then the model optimizes it.
Then the team organizes around it.
Then the organization starts treating it as reality.

What started as a measurement becomes a steering function.

## Evals are not neutral

That is why evals are more important than they look.

An eval answers questions like:

- What counts as success?
- What tradeoffs are acceptable?
- What kinds of failure are tolerated?
- What gets rewarded?
- What gets ignored?
- What gets optimized away?

Those are not just technical questions.

They are product questions.
They are organizational questions.
Eventually, they become governance questions.

The eval is where an abstraction becomes an incentive.

## This gets more serious with agents

With classic ML systems, the model often predicts, ranks, or classifies.

With agentic systems, the model can do much more than that.

It can:

- plan
- act
- call tools
- generate artifacts
- decide what to look at next
- coordinate across multiple steps
- optimize iteratively over time

That means a bad eval does not just create a system that is wrong in one place.

It creates a system that can become coherently wrong.
Strategically wrong.
High-performing against the wrong target.

That is a different level of risk.

## The eval scopes the whole thing

This is why I keep coming back to a simple idea:

> **How we define evals doesn’t just measure the system. It scopes the future the system will optimize for.**

That sounds dramatic, but I think it is just true.

From relatively small traditional ML tools all the way up to systems like Karpathy’s AutoResearch, the shape of the eval determines the shape of the project.

If the eval rewards surface polish, the system will learn surface polish.
If the eval rewards shallow confidence, the system will learn shallow confidence.
If the eval confuses completion with understanding, the system will optimize for completion.

That does not stay local.

It changes what gets built, what gets trusted, and what gets deployed.

## AutoResearch makes the stakes easier to see

A system like AutoResearch makes the issue obvious because it is supposed to do more than answer one question.

It is supposed to:

- search
- synthesize
- iterate
- judge progress
- improve outputs over time

But all of that depends on what counts as progress.

What gets rewarded as better research?
What gets scored as a useful next step?
What gets treated as success?

If those answers are shallow, the whole system becomes a machine for industrializing shallow success.

You do not get truth.
You get optimized appearances of truth.

You do not get understanding.
You get benchmark-shaped confidence.

You do not get aligned autonomy.
You get a system that is very good at performing well against the wrong objective.

## Human-in-the-loop is the window to define the objective

This is the part I think people are underestimating.

While humans are still in the loop, they can still say things like:

- this output is technically correct but operationally bad
- this answer sounds good but hides uncertainty
- this summary is polished but misses the point
- this action is efficient but not trustworthy
- this tradeoff is unacceptable even if the score improves

That human layer is not just there to rubber-stamp the machine.

It is there to surface the parts of success that are hard to compress into a simple benchmark.

That is why the current moment matters.

Right now, we still have a chance to decide what these systems should actually be optimizing for before more autonomy gets layered on top.

## If we do this badly, the system inherits someone else’s values

If we do not define success carefully, someone else will define it for us.

Sometimes that someone else is:

- the easiest measurable proxy
- the benchmark author
- the product deadline
- the vendor default
- the growth team
- the optimization loop itself

And those definitions are often not the same as:

- human flourishing
- trust
- judgment
- resilience
- reversibility
- long-term usefulness

That is the real danger.

Not that the system becomes evil.

That it becomes relentlessly effective at serving a shallow, partial, or misaligned definition of success.

## What better evals should include

If we are serious about building systems that continue to serve us, evals need to measure more than “did the task complete?”

They need to capture things like:

- correctness
- restraint
- uncertainty handling
- explainability
- reversibility
- human ownership
- usefulness under changing conditions
- the ability to surface tradeoffs instead of hiding them

Those are harder to measure.

That is not a reason to ignore them.
It is a reason to take eval design more seriously.

## Eval work is governance work

I think this is the uncomfortable but necessary conclusion.

We still tend to talk about evals as if they are mostly a technical layer:

- tests
- scorecards
- benchmarks
- regression checks

But once systems start acting in the world, eval design becomes upstream governance.

It determines what gets rewarded.
What gets deployed.
What gets trusted.
What gets scaled.

That makes eval work a lot more important than many people are treating it.

Not because it is glamorous.
Because it is where values become optimization targets.

## Define success before the system does

The point of evals is not just to tell us whether a system works.

It is to force us to answer what working is for.

That question matters in every era of machine learning.
But it matters even more when systems stop being narrow tools and start becoming collaborators, operators, and optimizers.

If we get the eval wrong, we do not just get a bad score.
We get a system that becomes better and better at the wrong thing.

And if those systems become important enough, that stops being a product problem and starts becoming a future problem.

So yes, model quality matters.
System design matters.
Tooling matters.

But before all of that, we need to answer a simpler question:

> **What exactly are we asking the system to optimize for?**

If we cannot answer that clearly, the system eventually will.
