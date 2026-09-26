---
title: "Graduated Engineering Rigor"
date: 2026-09-25
tags:
  - Draft
  - AI
  - Systems
  - Work
summary: "AI makes tiny bespoke apps cheap enough to be disposable. Engineering rigor should increase with consequence, dependence, and lifespan instead of treating every experiment like enterprise software."
layout: rich
---

<img src="/static/images/graduated-engineering-rigor-hero.jpg" alt="Futuristic abstract scene with colorful 3D icons, cards, spheres, and cubes streaming toward a sleek architectural structure against a dark background with glowing lines and geometric orbits" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

I think a lot of software governance starts from the wrong premise: if something is an app, it should be engineered like an app.

That made more sense when software was expensive to create.

If a team spent six months building an internal application, of course it needed ownership, tests, security review, deployment standards, documentation, monitoring, and a maintenance plan. The cost of building the thing already implied that it was meant to last.

Generative AI breaks that assumption.

Someone can now conjure a bespoke interface for a narrow task in an afternoon. Maybe it helps reconcile two exports. Maybe it lets a planner review a few hundred records. Maybe it wraps a tedious API call in three buttons. Maybe it exists for one project, does its job, and never needs to run again.

I think that is fine.

Throwaway vibe-coded apps are fine.

The mistake would be requiring every one of them to meet the standards of durable production software.

The better idea is **graduated engineering rigor**: the amount of engineering discipline around a tool should rise with the consequences of failure, the sensitivity of the data, the number of people depending on it, and how difficult its actions are to reverse.

Rigor should follow risk and dependence.

## We already tolerate disposable software

This future is less radical than it sounds.

Organizations are already full of bespoke, semi-disposable software. We just use names that make it sound less like software.

A spreadsheet with formulas is software.

A SQL query written to answer one question is software.

A Python script that reshapes a file is software.

A notebook used during an analysis is software.

A temporary dashboard is software.

We routinely allow these things to exist with much less ceremony than an application built by a software team. That is usually reasonable because their scope is small and their consequences are limited.

AI changes the form factor.

The analyst who once wrote a complicated workbook may now generate a small web app with a file picker, a map, a few controls, and an export button. The interface looks more like "real software," but the underlying job may still be temporary and narrow.

The fact that it has buttons should not automatically summon an enterprise architecture review.

The useful question is not, "Is this an app?"

It is, "What happens if this app is wrong?"

## A disposable app should be allowed to be disposable

Imagine I need to inspect a CSV, make a few decisions, and export a cleaned version.

The tool runs locally. It works on copies of the data. It does not write back to a production system. Nobody else depends on it. If it fails, I can delete it, regenerate it, or do the task manually.

That tool does not need a five-year architecture.

It may not need a database. It may not need observability. It may not need an elaborate test suite. It may not even deserve its own repository.

It still needs a basic floor of responsible behavior. I should not paste secrets into source code. I should know where the data is going. I should avoid sending sensitive information to an unapproved service. I should understand what the tool will do before I let it alter anything important.

But beyond that, messiness can be acceptable.

Temporary software can have temporary architecture.

There is a tendency among engineers to see every shortcut as technical debt. That metaphor assumes the thing will live long enough for the debt to come due.

Sometimes the correct maintenance plan is deletion.

## The problem starts when temporary software becomes infrastructure

The dangerous part is not that people can make tiny apps quickly.

The dangerous part is that a tiny app can quietly stop being tiny.

I build something for myself. A coworker sees it and asks for the link. Then three more people use it. Someone adds it to a monthly process. Another tool starts consuming its output. A manager begins treating one of its numbers as authoritative.

Nothing about the code changed at the moment the risk changed.

The dependency changed.

That is the point where the engineering posture needs to change too.

The little utility has graduated.

Now questions that previously did not matter very much start to matter. Who owns it? Where does its business logic come from? What happens when the creator leaves? Are dependencies pinned? Is there a test around the calculation everyone relies on? Who can access the data? Can a failed write be rolled back? Is anyone going to notice if the tool silently stops working?

This is where "shadow IT" becomes a useful concern, but I think the term is often applied too broadly.

A one-person throwaway tool is not automatically a governance crisis.

An unmanaged operational dependency is.

## Rigor should increase in steps

I do not think organizations need a binary choice between "vibe coding free-for-all" and "every script goes through central IT."

There is a large and useful space between those extremes.

A personal scratch tool can have almost no ceremony. Keep data inside approved boundaries. Do not expose credentials. Prefer read-only access. Make destructive actions obvious. Then use the thing and throw it away.

A shared utility deserves more. Put it in version control. Write down what it does. Make setup reproducible. Add a few tests around the behavior people actually care about. Give it an owner.

An operational tool that runs repeatedly or touches production systems deserves a stronger standard. Authentication, least-privilege permissions, logging, error handling, rollback, review, data lineage, dependency management, and some expectation of support begin to matter.

A system involved in safety, money, regulated decisions, authoritative records, or critical operations belongs in a different category entirely. At that point, the fact that an AI agent helped write it is almost beside the point. It needs serious engineering because the consequences are serious.

The categories do not need to be perfect.

The important part is that rigor can ratchet upward as dependence grows.

## The graduation triggers matter more than the coding method

The phrase "vibe coding" attracts a lot of attention because it makes the creation process sound reckless.

I care less about how the first version was created than what the tool becomes.

A carefully hand-written Python script that quietly turns into a business-critical process without tests or ownership is still a problem.

A vibe-coded prototype that gets reviewed, simplified, tested, secured, documented, and adopted deliberately can become perfectly respectable software.

The coding method is not the risk model.

The useful signals are things like persistence, reach, authority, and reversibility.

Is this still for one person, or is a team relying on it?

Is it answering an exploratory question, or is it producing an authoritative number?

Is it reading a copy of data, or writing into a system of record?

Can a mistake be undone in five minutes, or would it create a real incident?

Would anyone care if the app disappeared tomorrow?

Those questions tell me much more about the engineering rigor required than whether the code came from an AI agent, Stack Overflow, a contractor, or somebody typing it line by line.

## The goal is not to eliminate experimentation

There is a failure mode on the other side of this problem.

An organization gets nervous about AI-generated software and responds by applying production standards to everything.

Every experiment needs an intake form. Every little utility needs architecture review. Every prototype needs enterprise hosting. Every employee who wants to automate a two-hour task has to join a queue.

At that point we have recreated the bottleneck that AI was useful for removing.

People will still solve their problems. They will just retreat to spreadsheets, macros, copied scripts, browser tools, and other things that fit underneath the governance threshold.

Good governance should make the safe path easier, not make useful experimentation impossible.

I want people to be able to build a weird little tool on Tuesday, finish the job on Wednesday, and delete it on Thursday without feeling like they violated the software development lifecycle.

I also want us to notice when that weird little tool is still running six months later with twelve users and a production credential.

Both ideas can be true.

## Engineering judgment moves up the stack

This connects to something I have been thinking about more broadly as AI makes implementation cheaper.

The hard skill is shifting from simply producing code toward judging what kind of software we are dealing with.

Does this need to be durable?

Does this need tests?

Does this need an owner?

Does this need review?

Can this safely remain a disposable mess?

Those are engineering decisions.

And when software becomes cheap enough that almost anyone can make it, I think those decisions become more important, not less.

The future may contain vastly more software than the present. A lot of it will be personal, narrow, generated on demand, and short-lived.

That does not have to be a nightmare.

We just need to stop pretending every piece of software deserves the same amount of engineering.

Some things should be carefully designed, reviewed, monitored, and maintained for years.

Some things should solve today's problem and disappear.

The skill is knowing which one you are looking at, and noticing when one becomes the other.
