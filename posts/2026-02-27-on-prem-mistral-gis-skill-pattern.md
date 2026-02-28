---
# IMPORTANT: Always quote title strings (YAML can break on colons)

title: "A practical GIS skill pattern for on-prem Mistral (and other local LLMs)"
date: 2026-02-27
tags:
  - GIS
  - LLM
  - On-Prem
  - RAG
  - ArcGIS
  - Draft
---

I’ve been poking at an on-prem LLM (Mistral-class) at work and wanted a pattern that stays practical.

Not "agents that do everything".

More like: small, reliable **GIS skills** that take a narrow input, pull the right context from internal docs, and return an artifact you can actually run or review.

This post is a structured draft of the pattern I want to explore.

## The "GIS skill" pattern

Think of each skill as a small product with four parts:

1) **Intent + inputs**
2) **Context pipeline (grounding)**
3) **Reasoning scaffold (structured output)**
4) **Guardrails + verification**

If you get those right, even a modest on-prem model becomes useful.

### 1) Intent + inputs

Start with a lightweight router that maps a user request to a skill.

This can be a tiny classifier, a ruleset, or the same LLM running in a constrained prompt.

Example intents for GIS:

- Explain or troubleshoot: "Why did my buffer tool fail?"
- Generate code: "Write arcpy to select poles within 100 ft of overhead lines"
- Plan an analysis: "How would you assess wildfire risk exposure for service drops?"
- Data QA: "This spreadsheet has duplicates and missing IDs, what should I do?"
- Translate business request → GIS steps: "We need targeted undergrounding candidates"

Inputs can be:

- User text
- Project context JSON (layer names, paths, spatial reference, selected layer, etc.)
- Optional snippets of schema, field lists, sample rows
- Optional error text and stack traces

My bias: **make project context a contract**.

If the skill depends on layer names, geometry types, fields, SR, and units, pass those in explicitly. Don’t make the model guess.

### 2) Context pipeline (grounding)

Before the model answers, give it the right context.

Usually that’s a simple retrieval step that pulls relevant snippets and includes them in the prompt.

Sources worth retrieving from in a GIS org:

- Internal GIS standards (naming, projections, publishing rules)
- Known-good code snippets (your "recipes")
- Runbooks (common ArcGIS Pro, Portal, service issues)
- Data dictionaries and authoritative dataset descriptions
- Safety/compliance rules (what not to do, what to redact)

This is where on-prem shines.

You can retrieve from internal docs without sending anything outside.

### 3) Reasoning scaffold (structured output)

Instead of free-form chat, force a predictable structure.

For GIS skills, I like outputs that look like this:

- Assumptions (short)
- Plan (3 to 7 steps)
- Actionable output (code, parameters, or a checklist)
- Validation (how to test it)
- Failure modes (what could break)

A key nuance:

You can keep deeper chain-of-thought private while still requiring a clean artifact. The artifact is what matters.

### 4) Guardrails + verification

This is what makes it enterprise-usable.

Even without fancy infra, you can add guardrails that keep the output honest.

Guardrails that work well:

- Allowlist actions: the skill can only do specific safe things (generate code, propose GP steps, suggest queries)
- Redaction rules: automatically remove customer PII from prompts and logs
- Citation requirement: when the model states a policy or standard, it must cite a retrieved snippet
- Static checks on code: lint basic arcpy patterns, ban destructive operations unless explicitly allowed
- Confidence gating: if context is missing, the skill asks for a field list or sample rows instead of hallucinating

GIS-specific guardrails that matter a lot:

- Spatial reference and units checks (the most common geospatial reasoning failure)
- Field existence checks
- Geometry type assumptions made explicit

## The “stoplight” I would add (small, huge trust win)

Every skill output should start with a simple readiness signal:

- **Green**: ready to run
- **Yellow**: answer 1 to 3 questions first
- **Red**: cannot proceed, missing key context

This is a cheap way to keep users from treating the model like an oracle.

## Example skill: ArcPy Assistant (code generation you can trust)

User request:

"Select service points within 200 ft of overhead primary, then export to a new feature class."

Skill flow:

1) Extract entities
- Target layer: service points
- Reference layer: overhead primary
- Distance: 200 ft
- Output: new feature class

2) Retrieve
- Projection guidance
- Known-good recipe for SelectLayerByLocation + CopyFeatures

3) Generate output
- arcpy script that includes:
  - environment workspace
  - projection and unit warning
  - selection count print
  - safe output naming

4) Verification
- run on a small AOI first
- confirm units: feet vs meters
- confirm layer is a feature layer

## Example skill: Spreadsheet Triage (don’t hallucinate provenance)

User request:

"This spreadsheet has duplicates, missing feeder IDs, and unknown provenance. What should I do?"

Skill output:

- Triage plan
  - profile uniqueness keys
  - identify duplicate patterns
  - infer likely source system from field patterns (clearly labeled as inference)
  - propose a canonical ID strategy

- Generates
  - pandas script to audit duplicates and missingness
  - a data contract checklist for the stakeholder

Guardrails:

- never invent authoritative sources
- mark every inference as inference
- require SME confirmation before anything gets published

## Example skill: Analysis Planner (reasoning-heavy, no execution)

User request:

"How do we rank undergrounding candidates by wildfire risk and customer impact?"

Skill produces:

- scoring framework with weights clearly labeled as a starting point
- required datasets list (authoritative only)
- steps to normalize, join, buffer, aggregate, validate
- pitfalls: MAUP, temporal mismatch, spatial resolution mismatch
- suggested MVP workflow

This is where a local model can absolutely hang, as long as you scaffold it.

## What I would build first (high leverage, low risk)

If I were prototyping this in a real GIS org, I’d start with:

1) **Troubleshooter skill**
- Reads ArcGIS errors
- Suggests fixes
- Cites internal runbooks

2) **ArcPy recipe skill**
- Generates code
- Must include unit and projection checks
- Must include validation steps

3) **Data QA skill**
- Spreadsheet profiling
- Hard guardrail against inventing provenance

But if I want to prove value quickly, I would start with just one: **Troubleshooter**.

## What I still need to answer

Before this becomes real, the environment matters:

- What exact on-prem model and runtime is available?
- Where will internal snippets live for retrieval (file share, wiki export, git)?
- What counts as authoritative standards in this org?

If those are fuzzy, the model will be fuzzy too.

---

If you’re exploring something similar, I’d love to compare notes: what’s your first skill, and what guardrail saved you from your first embarrassing demo?
