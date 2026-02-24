---
title: "Agent vs Skill vs Deterministic Tool: a practical decision guide"
date: 2026-02-23
tags:
  - AI
  - Agents
  - Workflow
  - Draft
---

Most automation choices fail for a boring reason: you picked the wrong shape.

You can ship the same outcome three ways:

1. **An agent** (autonomous-ish, multi-step, context-heavy)
2. **An agent skill** (a reusable procedure that guides an agent)
3. **A deterministic tool** (a CLI/script/service that does the same thing every time)

They are not interchangeable. Pick the wrong one and you get either:
- a fragile “AI demo” that needs babysitting, or
- an overbuilt tool that should have been a one-page checklist.

Here’s how I decide.

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
- “figure out what the user meant”
- exploratory work

Examples:
- `arcgispro status --json --strict`
- “convert these 200 shapefiles to GeoParquet with a known schema”
- “pull PR metrics and write them to a CSV”

### 2) Agent skill
A skill is a **recipe**: structured instructions + prompts + checks that make an agent consistently useful in a domain.

Think of it like a standard operating procedure for an AI.

**Best at:**
- recurring workflows with variation
- decision trees and checklists
- teaching “how we do this here”
- bridging messy reality into tool calls

**Weak at:**
- jobs that should be one command
- anything where you need hard guarantees

Examples:
- “Audit an ArcGIS Pro project for common issues”
- “Search Living Atlas, vet candidates, pick 2 layers, record licenses and caveats”
- “Preflight checklist before publishing to AGOL”

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
- “Investigate why exports are failing on this machine”
- “Take a rough PRD and produce a coherent issue list + plan”
- “Triage incidents across a homelab and propose the smallest fix”

## The decision framework (use this first)

When a new task shows up, ask:

### 1) How repeatable is it?
- **Same steps every time** → deterministic tool
- **Same steps with branching** → skill
- **New puzzle every time** → agent

### 2) How expensive is a mistake?
- **High blast radius** (money, data loss, production) → deterministic tool + human review
- **Medium** → skill with strong checks
- **Low** → agent is fine

### 3) Is the input well-structured?
- **Clear inputs/outputs** → tool
- **Semi-structured** (documents, folders, “a project”) → skill
- **Unstructured** (goals, confusion, unknown unknowns) → agent

### 4) Does it need institutional knowledge?
- **Yes** (your standards, your environment, your weird edge cases) → skill
- **No** → tool or agent

### 5) Do you want it in CI?
If yes, you almost always want a deterministic tool. Agents can assist development, but CI should not be vibes-based.

## The “90% of the time” rule

If you can describe the task as:

> “Given X, do Y, produce Z”

…you probably want a deterministic tool.

If instead it sounds like:

> “Figure out what’s wrong / pick the best option / apply judgment”

…start with an agent, then extract a skill, then harden into a tool.

That progression matters.

## A healthy maturity path

### Stage 1: Agent does it manually
You’re exploring. Requirements are fuzzy. You don’t even know what the inputs should be.

Output: a working result and a trail of decisions.

### Stage 2: Turn the repeatable parts into a skill
Capture:
- steps that always happen
- the checklists you keep repeating
- the “gotchas”
- what “done” means

Output: a consistent playbook.

### Stage 3: Build a deterministic tool for the boring core
Anything that:
- is stable
- must be correct
- needs to run unattended
- should be testable

Output: a CLI/service with tests and predictable behavior.

This is the “agent-to-tool refinery”. Agents are great at discovery. Tools are great at production.

## Concrete examples

### Example A: “Export ArcGIS Pro project context for AI”
The agent can explain and troubleshoot, but the core should be deterministic.

Shape:
- **Tool:** `arcgispro_cli` exports + validates `.arcgispro/` snapshots (`status --strict --json`)
- **Skill:** “How to use arcgispro_cli in a real workflow” (install add-in, run snapshot, validate, paste context)
- **Agent:** helps when someone’s environment is broken or they need help interpreting the context

### Example B: “Find two good preschools to tour”
Lots of judgment, constraints, tradeoffs.

Shape:
- **Agent:** does the reasoning + asks clarifying questions
- **Skill:** eventually, a “school search” skill could standardize the rubric
- **Tool:** not worth it unless you’re doing this every week (please don’t)

### Example C: “Weekly repo activity report”
Same query pattern every time.

Shape:
- **Tool:** script that queries GitHub and prints a report
- **Agent:** only for “why is the report wrong?” investigations
- **Skill:** maybe, if multiple agents/users need to run it reliably with consistent interpretations

## A quick rubric you can paste into issues

Score each dimension 1–5:

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
- “it worked yesterday”
- you can’t test it
- you can’t diff it

Fix:
- isolate deterministic core
- add structured output (`--json`)
- add strict mode / exit codes
- write tests

### Failure: building a tool when you needed discovery
Symptoms:
- endless “requirements gathering”
- tool has 30 flags and still doesn’t work
- you’re encoding decisions you don’t understand yet

Fix:
- do it with an agent for a week
- write down the decisions you keep making
- then build the tool once the shape is obvious

### Failure: skills that are just vibes
Symptoms:
- “try to do X” with no checks
- no acceptance criteria
- no prompts or examples
- no failure handling

Fix:
- turn the skill into a checklist with a decision tree
- include expected outputs and “stop conditions”
- include “if this fails, do that”

## Practical recommendation
Default to:
1) agent for exploration
2) skill for repeatable human-in-the-loop workflows
3) deterministic tool for production, CI, and anything with consequences

If you do it in the opposite direction, you’ll waste time and build brittle junk.
