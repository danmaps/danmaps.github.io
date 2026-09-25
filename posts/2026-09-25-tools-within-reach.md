---
title: "Tools Within Reach"
date: 2026-09-25
tags:
  - Draft
  - AI
  - Systems
  - Career
summary: "Domain experts already know real problems. With curiosity, frameworks, and a few traditionally gatekept tools, they can increasingly turn that knowledge into useful software."
layout: rich
---

I have spent a lot of time making software without ever fully matching the traditional profile of a software developer.

I do not have a computer science degree. My job title has never been Software Engineer. My formal career grew out of GIS. At the same time, I write Python, build web applications, use APIs, design automated workflows, deploy code, work in GitHub, use CI/CD, and think constantly about how software should behave when other people depend on it.

For a long time, I saw the mismatch between my title and my work mostly as a career problem. It still is sometimes. Formal software roles often ask for a degree, a sequence of previous engineering titles, or years spent doing nothing but production software development.

Lately I have started to see another side of it.

I learned many software-development tools from outside the traditional pipeline. I remember what GitHub looked like before it felt ordinary. I remember when a repository, a branch, a pull request, a package manager, a deployment pipeline, or a terminal command all seemed like things that belonged to another profession.

That perspective has become useful because a lot of people I work with are standing near the same boundary.

They are highly technical in their own domains. They understand maps, infrastructure, operations, planning, engineering, science, data, policy, or field work. They know where the friction is. They know what a bad result looks like. They know which edge cases matter because they live with them.

They may never have been shown how much software-making capability is already within reach.

## The boundary around software has always been partly cultural

Software development has real depth. Good engineering requires judgment about architecture, security, testing, maintainability, failure, performance, and consequences. Those skills matter more as software becomes important, shared, or difficult to reverse.

The tools around software development also grew up inside a profession with its own vocabulary and assumptions.

A developer can say, "Open a PR, add a test, pin the dependency, and let CI run," and every part of that sentence may feel routine.

To someone outside that culture, it can sound like a foreign language.

The surprising thing is how often the individual concepts become understandable once somebody explains why they exist.

A repository is a place where the work and its history live together.

A branch gives you a safe place to change something.

A pull request creates a moment to inspect that change before it becomes part of the main system.

A test records behavior you want to preserve.

A deployment process moves software from your workspace to somewhere other people can use it.

None of those explanations require a computer science degree to understand. They require an introduction.

That distinction matters.

A lot of people have spent years assuming these tools were farther away than they really were.

## Domain experts already possess something valuable

When someone opens a blank code editor for the first time, the screen may look empty. Their understanding of the problem is not empty.

A GIS analyst may know exactly why a spatial workflow breaks on multipart features.

An engineer may know which measurements are trustworthy and which ones need context.

A planner may understand the political and operational constraints behind a seemingly simple map.

An operations specialist may know the manual process everyone hates, the weird exceptions nobody documented, and the exact moment where a spreadsheet stops being enough.

That knowledge is difficult to manufacture.

It is also a strong foundation for software.

When people talk about learning to code, the conversation often starts with syntax. Syntax matters, but syntax is only one piece of the work. Useful software starts with understanding what should happen, what should never happen, what information matters, and how a person will actually use the result.

Domain experts often arrive with those answers already forming in their heads.

The blank editor is less blank than it looks.

## GitHub is one of the doors I want to show people

GitHub is a good example of a tool that can feel strangely gatekept even when nobody is actively guarding it.

For developers, it is infrastructure. For many people outside software development, it is a website full of source code, unfamiliar terminology, and people who seem to know rules that were never explained.

Once someone gets a useful introduction, GitHub can become much more concrete.

It is where an idea can have a history.

It is where a script can stop living as `final_v2_really_final.py` on a shared drive.

It is where an issue can capture a problem before the solution is obvious.

It is where an AI coding agent can work against a real project instead of an isolated chat.

It is where automated checks can run every time something changes.

It is where a small personal tool can gradually become a maintained piece of software.

I do not expect everyone I show GitHub to become enthusiastic about Git internals. That is not the goal.

The goal is to make the tool legible enough that they can decide whether it helps them.

## AI shortened the distance between curiosity and a working result

Generative AI has changed this boundary quickly.

A curious domain expert can now ask questions in the middle of the work instead of stopping to search for a course that might explain the right concept three chapters later.

They can ask:

- What does this Git error mean?
- How should I organize this small Python project?
- Turn this repeated workflow into a function.
- Write a test for this behavior.
- Explain this API response.
- Help me make this script safer before it edits production data.
- What would I need to deploy this so someone else can use it?

That feedback loop is powerful.

The person still needs judgment. They still need to recognize when the stakes are high, when a generated answer is suspicious, when they need review, and when they are operating outside their depth.

AI makes experimentation cheaper. It also makes guardrails more important.

That is why I keep becoming interested in frameworks.

## Frameworks let people start with better defaults

A newcomer should not have to invent software architecture before they can automate a useful task.

They should be able to start inside a structure that already contains some hard-earned lessons.

That might mean:

- an opinionated project starter
- a safe folder structure
- version control from the beginning
- tests around destructive operations
- reusable agent instructions
- explicit validation before a tool runs
- clear separation between choosing an action and executing it
- a small set of supported patterns instead of infinite freedom

I think of these as rails for software-making.

They do not remove the need for engineering. They package some engineering knowledge into defaults, constraints, and reusable patterns.

A woodworking beginner can make something useful much sooner with a square, a jig, and a good set of plans. They still need to respect the saw.

Software can work the same way.

A good framework lets someone focus first on the problem they understand while inheriting safer ways to structure the solution.

## Making software is becoming a larger category than being a software developer

This is the idea I keep coming back to.

The profession of software engineering remains real and demanding. At the same time, the population of people who can make useful software is expanding.

Those two groups do not have to be identical.

A scientist who builds a reliable data-processing tool has made software.

A GIS analyst who turns a repeated spatial workflow into a tested application has made software.

An operations employee who creates a small internal tool around a painful process has made software.

Some of those people may eventually want a software engineering career. Some will have no interest in that at all.

Both outcomes are fine.

Someone may learn enough Python to remove three hours of repetitive work every Friday and stop there.

Someone else may build a web app for their team.

Another person may discover that they love repositories, tests, APIs, and systems design, then decide to go much deeper.

Access creates options.

That is the part I care about.

## Curiosity is the prerequisite I care about most

I am increasingly less interested in asking whether someone is "technical."

That label hides too much.

I am more interested in whether they are curious enough to keep pulling on a thread.

Could this be automated?

Why do we do this manually?

What is an API, exactly?

What happens if I clone this repository?

Could these two systems talk to each other?

Could I build a tiny version of this idea myself?

What would make this safe enough for someone else to use?

Those questions can travel surprisingly far now.

My role, as I see it, is not to tell every domain expert that they should become a programmer.

I want to shine a light on the tools that are already nearby. I want to explain some of the vocabulary. I want to provide frameworks that make the first steps safer. I want to show what I have learned from using these tools on real problems.

Then people can take what is useful and leave the rest.

Some will automate one task. Some will make applications. Some will contribute to repositories. Some will decide they would rather keep using software than make it.

All of those are reasonable choices.

The important thing is that the choice becomes visible.

If you know a problem deeply and you are curious enough to keep asking how things work, you may already have more of what you need to make software than you think.

The rest is increasingly within reach.
