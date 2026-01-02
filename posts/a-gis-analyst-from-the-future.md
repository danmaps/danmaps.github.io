---
date: 2025-12-16
tags:
- AI
- GIS
- workflows
- automation
title: A GIS Analyst From the Future

---

Imagine opening a GIS project you have never seen before.

Not a demo. A real one. Messy. Half-documented. Layers named by someone who left three years ago. Fields that almost make sense.

Today, the first thing you do is triage. You click around. You scan attribute tables. You try to reconstruct intent from leftovers.

In the future, you ask the map to explain itself.

This post is about what that future looks like, and how we get there without replacing analysts, breaking workflows, or pretending AI is magic.

Along the way, you will see interactive maps and tables. They are not screenshots. They are live examples of the same ideas, running in the browser, driven by the same system prompts I use in ArcGIS Pro.

---

## Step 1: Let the map speak first

Before doing analysis, a good analyst builds context.

What layers are here?
What coordinate system are we in?
Which fields look authoritative and which look improvised?

This information exists, but it is scattered across dialogs, panels, and institutional memory.

In the future, context is extracted once and reused everywhere.

**Interactive example:**
*A live map with several layers. Click "Explain this map."*

What the system does is simple:

* Reads the map state
* Extracts layers, fields, symbology, extents
* Produces structured context, not prose

Nothing intelligent has happened yet. This is just compression. But compression matters.

Once context is explicit, everything downstream improves.

---

## Step 2: Attributes that explain themselves

Most GIS attributes answer the wrong question.

They tell you *what* something is coded as, not *why it matters*.

Look at this table.

**Interactive example:**
*A table of features. Toggle a column called "AI summary."*

Each row now has a short explanation written in plain language. Not documentation. Interpretation.

This is not meant to replace metadata. It complements it.

The key idea is locality.
The explanation lives with the feature it describes.

You do not have to leave the map to understand the data.

---

## Step 3: Cleaning data without leaving the thought

Every analyst recognizes this moment.

You notice a field that is almost numeric:

* "~30 ft"
* "115kV"
* "approx. 12"

You know what to do, but doing it breaks flow.

Open a notebook.
Write a regex.
Test edge cases.
Hope you did not miss one.

In the future, you state intent.

**Interactive example:**
*Select a column. Click "Convert to numeric."*

The system infers units, strips text, preserves uncertainty where needed.

The important thing is not that AI cleaned the data.
It is that the analyst never left the problem they were thinking about.

---

## Step 4: Asking for what is missing

Now we do something different.

Instead of analyzing what exists, we ask what *should* exist.

**Interactive example:**
*A button labeled "Create hypothesis layer."*

Prompt:

> Create a layer representing likely inspection gaps based on distance from substations and asset age.

The result is explicitly marked as hypothetical.
It behaves like any other layer, but it does not pretend to be truth.

This is one of the most important shifts.

AI in GIS should propose, not assert.

---

## Step 5: Code as a translation layer, not a test

Eventually, you need code.

Select features within a buffer.
Join attributes.
Summarize by category.

Today, this is where momentum often dies.

In the future, code is generated from intent and local context.

**Interactive example:**
*A panel shows Python code generated for the current map state.*

Layer names match.
Fields are correct.
The code is readable.

The analyst still owns it.
But they are no longer fighting syntax to express a spatial idea.

---

## Step 6: The map documents itself

At the end of the session, something subtle happens.

The map now contains:

* Cleaner fields
* New layers
* Embedded explanations

**Interactive example:**
*Click "Summarize changes."*

The system produces a short narrative of what changed and why.

This is not for management.
It is for the next analyst. Or future you.

---

## What this is really about

This is not about replacing GIS analysts.

It is about removing the tax of translation:

* Between thought and tool
* Between data and meaning
* Between analysis and explanation

The analyst from the future still thinks spatially.
They just spend less time fighting software.

---

## Try it yourself

The browser examples in this post are powered by the same system prompts I use inside ArcGIS Pro.

If you want this workflow in your own projects:

* Download the ArcGIS Pro AI Toolbox
* Bring your own model
* Stay in control of your data

I am also writing more like this.
About geospatial AI adoption, change management, and how we evolve workflows without breaking trust.

If that interests you, subscribe for email updates.

The future of GIS is not flashy.
It is calmer, clearer, and easier to think in.

And it is already here.

