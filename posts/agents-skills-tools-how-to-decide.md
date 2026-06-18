---
title: "Agent vs Skill vs Deterministic Tool: a practical decision guide"
date: 2026-02-23
tags:
  - AI
  - Agents
  - Workflow
  - Draft
layout: rich
---

Most automation choices fail for a boring reason: you picked the wrong shape.

<img src="/static/images/agents-skills-tools-decision-guide-hero.png" alt="Illustration of three workflow shapes representing agents, skills, and deterministic tools" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

A lot of current AI tooling pressure nudges people toward agents first. That is usually backwards. In practice, many tasks that get framed as "agentic" are really one of two things:

- a known workflow with some branching
- a deterministic transformation wrapped in too much theater

You can ship the same outcome three ways:

1. **An agent** (autonomous-ish, multi-step, context-heavy)
2. **An agent skill** (a reusable procedure that guides an agent)
3. **A deterministic tool** (a CLI/script/service that does the same thing every time)

They are not interchangeable. Pick the wrong one and you get either:
- a fragile â€œAI demoâ€ that needs babysitting, or
- an overbuilt tool that should have been a one-page checklist.

Hereâ€™s how I decide.

## The three shapes

### 1) Deterministic tool
A deterministic tool is a command, script, or API that turns input into output with minimal ambiguity.

**Best at:**
- repeatable transformations
- stable interfaces
- high trust requirements
- anything you want in CI

**Weak at:**
- unclear tasks
- â€œfigure out what the user meantâ€
- exploratory work

Examples:
- `arcgispro status --json --strict`
- â€œconvert these 200 shapefiles to GeoParquet with a known schemaâ€
- â€œpull PR metrics and write them to a CSVâ€

### 2) Agent skill
A skill is a **recipe**: structured instructions + prompts + checks that make an agent consistently useful in a domain.

Think of it like a standard operating procedure for an AI.

**Best at:**
- recurring workflows with variation
- decision trees and checklists
- teaching â€œhow we do this hereâ€
- bridging messy reality into tool calls

**Weak at:**
- jobs that should be one command
- anything where you need hard guarantees

Examples:
- â€œAudit an ArcGIS Pro project for common issuesâ€
- â€œSearch Living Atlas, vet candidates, pick 2 layers, record licenses and caveatsâ€
- â€œPreflight checklist before publishing to AGOLâ€

### 3) Agent
An agent is a problem-solver that can plan and execute multi-step work, ask clarifying questions, and adapt.

**Best at:**
- ambiguous tasks
- multi-source synthesis
- troubleshooting
- workflows that require judgment

**Weak at:**
- strict repeatability
- anything where the cost of being wrong is high
- unattended execution without guardrails

Examples:
- â€œInvestigate why exports are failing on this machineâ€
- â€œTake a rough PRD and produce a coherent issue list + planâ€
- â€œTriage incidents across a homelab and propose the smallest fixâ€

## The decision framework (use this first)

When a new task shows up, ask:

### 1) How repeatable is it?
- **Same steps every time** â†’ deterministic tool
- **Same steps with branching** â†’ skill
- **New puzzle every time** â†’ agent

### 2) How expensive is a mistake?
- **High blast radius** (money, data loss, production) â†’ deterministic tool + human review
- **Medium** â†’ skill with strong checks
- **Low** â†’ agent is fine

### 3) Is the input well-structured?
- **Clear inputs/outputs** â†’ tool
- **Semi-structured** (documents, folders, â€œa projectâ€) â†’ skill
- **Unstructured** (goals, confusion, unknown unknowns) â†’ agent

### 4) Does it need institutional knowledge?
- **Yes** (your standards, your environment, your weird edge cases) â†’ skill
- **No** â†’ tool or agent

### 5) Do you want it in CI?
If yes, you almost always want a deterministic tool. Agents can assist development, but CI should not be vibes-based.

## The â€œ90% of the timeâ€ rule

If you can describe the task as:

> â€œGiven X, do Y, produce Zâ€

â€¦you probably want a deterministic tool.

If instead it sounds like:

> â€œFigure out whatâ€™s wrong / pick the best option / apply judgmentâ€

â€¦start with an agent, then extract a skill, then harden into a tool.

That progression matters.

## A healthy maturity path

### Stage 1: Agent does it manually
Youâ€™re exploring. Requirements are fuzzy. You donâ€™t even know what the inputs should be.

Output: a working result and a trail of decisions.

### Stage 2: Turn the repeatable parts into a skill
Capture:
- steps that always happen
- the checklists you keep repeating
- the â€œgotchasâ€
- what â€œdoneâ€ means

Output: a consistent playbook.

### Stage 3: Build a deterministic tool for the boring core
Anything that:
- is stable
- must be correct
- needs to run unattended
- should be testable

Output: a CLI/service with tests and predictable behavior.

This is the â€œagent-to-tool refineryâ€. Agents are great at discovery. Tools are great at production.

## Concrete examples

### Example A: â€œExport ArcGIS Pro project context for AIâ€
The agent can explain and troubleshoot, but the core should be deterministic.

Shape:
- **Tool:** `arcgispro_cli` exports + validates `.arcgispro/` snapshots (`status --strict --json`)
- **Skill:** â€œHow to use arcgispro_cli in a real workflowâ€ (install add-in, run snapshot, validate, paste context)
- **Agent:** helps when someoneâ€™s environment is broken or they need help interpreting the context

### Example B: â€œFind two good preschools to tourâ€
Lots of judgment, constraints, tradeoffs.

Shape:
- **Agent:** does the reasoning + asks clarifying questions
- **Skill:** eventually, a â€œschool searchâ€ skill could standardize the rubric
- **Tool:** not worth it unless youâ€™re doing this every week (please donâ€™t)

### Example C: â€œWeekly repo activity reportâ€
Same query pattern every time.

Shape:
- **Tool:** script that queries GitHub and prints a report
- **Agent:** only for â€œwhy is the report wrong?â€ investigations
- **Skill:** maybe, if multiple agents/users need to run it reliably with consistent interpretations

## A quick rubric you can paste into issues

Score each dimension 1â€“5:

- Repeatability
- Risk of mistakes
- Input ambiguity
- Need for judgment
- Need for institutional knowledge
- CI/unattended requirement

Then:
- High repeatability + high risk + CI = tool
- Medium repeatability + branching + institutional knowledge = skill
- High ambiguity + high judgment = agent

## Common failure modes (and how to avoid them)

### Failure: building an agent when you needed a tool
Symptoms:
- inconsistent output
- â€œit worked yesterdayâ€
- you canâ€™t test it
- you canâ€™t diff it

Fix:
- isolate deterministic core
- add structured output (`--json`)
- add strict mode / exit codes
- write tests

### Failure: building a tool when you needed discovery
Symptoms:
- endless â€œrequirements gatheringâ€
- tool has 30 flags and still doesnâ€™t work
- youâ€™re encoding decisions you donâ€™t understand yet

Fix:
- do it with an agent for a week
- write down the decisions you keep making
- then build the tool once the shape is obvious

### Failure: skills that are just vibes
Symptoms:
- â€œtry to do Xâ€ with no checks
- no acceptance criteria
- no prompts or examples
- no failure handling

Fix:
- turn the skill into a checklist with a decision tree
- include expected outputs and â€œstop conditionsâ€
- include â€œif this fails, do thatâ€

## Practical recommendation
Default to:
1) agent for exploration
2) skill for repeatable human-in-the-loop workflows
3) deterministic tool for production, CI, and anything with consequences

Or more bluntly:

> workflows first, agents second, deterministic tools for anything that has to keep working.

If you do it in the opposite direction, youâ€™ll waste time and build brittle junk.

