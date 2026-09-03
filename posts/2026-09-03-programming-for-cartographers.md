---
title: "Programming for Cartographers"
date: 2026-09-03
tags:
- Draft
- GIS
- Python
- Cartography
summary: "You do not need to learn how to think like a programmer from scratch. If you work in GIS, you have probably been programming already—you just learned the concepts through maps and geoprocessing."
layout: rich
---

There is a particular kind of anxiety that shows up when a cartographer decides to learn programming.

They open a Python tutorial and meet variables, types, functions, loops, and objects as if these are entirely new ideas. The tutorial assumes a blank slate. But the cartographer's mind is not blank. It is already full of parameters, inputs, transformations, dependencies, geometry, and output rules.

The problem is usually not a lack of programming intuition.

It is a translation problem.

If you have built a ModelBuilder workflow, written a field calculation, chained geoprocessing tools, or repeatedly repaired a broken layer by changing one parameter at a time, you have already practiced a large part of programming. You learned the concepts through a map interface instead of a text editor.

You do not need to learn how to think like a programmer from scratch. You need to translate concepts you already understand.

Consider a familiar chain:

```text
Select → Buffer → Intersect → Calculate Field → Export
```

It has inputs, operations, intermediate results, and an output. Programming gives us a language for expressing that workflow, generalizing it, repeating it, and testing it.

## You were programming already

ModelBuilder makes the connection easy to see. A model has inputs, operations, dependencies, and outputs. One tool runs only after another tool has produced the data it needs. A parameter changes the result. A broken connection stops the workflow.

That is a program, even if the interface lets you draw it.

Field calculations are programs too. A condition such as “if this field is null, use this other value” is a conditional. A calculation that combines two fields is an expression. Applying it to every row is iteration.

The graphical interface does not remove the logic. It hides some of the syntax.

This is useful because syntax is often the least important part of learning to program. The durable skill is understanding what state exists, what transformation should happen next, and how to tell whether the result is trustworthy.

## Variables are the things you name so the workflow can continue

In GIS, you already work with named things:

- a source feature class
- a selected layer
- a workspace path
- a buffer distance
- a date range
- an output table

In Python, these become variables:

```python
roads = "data/roads.gpkg"
distance = 500
output = "outputs/roads_buffered.gpkg"
```

The variable is not the data itself. It is a name that lets you refer to a value later. That is exactly what an output connection in a geoprocessing model does: it gives a later step a reliable handle on the result of an earlier step.

The important habit is the same in both environments: name things according to their role. `roads_buffered_for_schools` tells you more than `layer3`. Good names make a workflow inspectable before you run it.

## Types are the shape of your assumptions

GIS users encounter types constantly, although software does not always explain them clearly. A text field is not interchangeable with a numeric field. A date is not the same thing as a string that happens to look like a date. A geometry is not a table, and a layer is not necessarily the same thing as the dataset behind it.

Programming makes these distinctions explicit.

```python
district_name = "North"       # string
buffer_distance = 1000        # integer
include_parks = True          # boolean
```

Many frustrating errors are type errors in disguise. A distance stored as text cannot behave reliably like a number. A missing geometry cannot be treated like a valid polygon. A list of features is not one feature.

Learning types is not memorizing an abstract taxonomy. It is learning to ask a GIS question earlier: what kind of thing is this, and what operations make sense for it?

## A geoprocessing tool is basically a function

A function takes inputs, does something defined, and returns a result. That description could appear in the documentation for almost any geoprocessing tool.

```python
buffered_roads = buffer(roads, distance=500)
```

The exact syntax varies by library, but the mental model is familiar. The tool has parameters. Some are required. Some have defaults. The output can become the input to another operation.

Once you see tools as functions, a script becomes less mysterious. It is a written workflow in which the connections are visible in the code.

That visibility is valuable. A model can show the broad shape of a process. Code can show the small decisions inside each step: how a path is constructed, how nulls are handled, what gets logged, and what happens when an output already exists.

## Assignment is capturing the result

Running a tool is only half the operation. The next question is: where does its result go?

In a graphical workflow, the answer is an output node. In code, it is assignment:

```python
selected = select_by_attribute(parcels, "status = 'active'")
buffered = buffer(selected, distance=250)
```

The right-hand side runs the operation. The left-hand side gives the result a name.

This is the basic rhythm of a script:

1. get a value
2. transform it
3. assign the result
4. pass it downstream

It is the same chain you have built many times in GIS. Code simply makes the chain portable and easier to repeat.

## Conditionals are the decisions inside the workflow

GIS workflows are full of branching logic:

- if a field is null, calculate a fallback
- if a layer exists, update it; otherwise create it
- if a feature is inside the study area, include it
- if a district has no records, report that explicitly

In Python:

```python
if parcel["owner_name"] is None:
    parcel["owner_name"] = "Unknown"
```

The syntax is new. The decision is not.

The useful shift is to stop thinking of conditionals as programming ceremony. They are simply places where your workflow has more than one valid path. Writing those paths down makes hidden assumptions visible.

## Loops are iteration with a name

When someone says “loop,” a GIS professional can reasonably ask: loop over what?

That is exactly the right question. You might iterate over:

- features in a feature class
- files in a folder
- layers in a map
- dates in a reporting period
- districts in a region

```python
for district in districts:
    create_report(district)
```

Batch tools and iterators have always provided this capability through a user interface. Code gives you control over the iteration: filtering items first, collecting results, handling an individual failure, or stopping when a validation rule is violated.

The loop is not the clever part. Choosing the correct collection and deciding what should happen for every item is the real GIS judgment.

ModelBuilder's iterators are graphical loops. “Iterate Feature Classes,” “Iterate Rows,” and “Iterate Field Values” all express the same basic idea as a `for` loop: get one item, apply an operation, and continue until the collection is exhausted.

## Lists and dictionaries turn repetition into structure

A list is an ordered collection. A dictionary maps names to values. Both are useful when a workflow starts repeating itself.

```python
districts = ["North", "South", "Central"]

settings = {
    "distance": 500,
    "unit": "meters",
    "include_inactive": False,
}
```

Instead of writing three nearly identical operations, you can represent the things that vary as data. That makes the workflow easier to change and easier to test.

This is one of the first moments when scripting feels substantially different from clicking. You stop encoding every operation separately and start describing a pattern that applies across many inputs.

## Objects are features, geometries, layers, and maps with behavior

Object-oriented programming can sound especially distant from cartography. It becomes less distant if you start with the things you already manipulate.

A feature has geometry and attributes. A layer has data, a name, a renderer, and visibility properties. A map contains layers and an extent. These are not just bags of values. They have relationships and operations.

That is the intuition behind objects: data and the behavior associated with that data can travel together.

You do not need to master every object-oriented pattern to write useful GIS software. You do need to recognize when a recurring thing in your workflow deserves a clear representation instead of a loose collection of variables.

## Errors are the unhappy paths you already know exist

Every GIS analyst has seen the happy path fail:

- the input path is wrong
- the schema is not what you expected
- a lock prevents an overwrite
- a projection is missing
- a geometry is invalid
- an output already exists

Programming calls these errors and exceptions, but the underlying reality is familiar. A robust workflow does not pretend that inputs are perfect. It decides how to detect failure, explain it, and recover where recovery makes sense.

The goal is not to catch every error and continue blindly. Sometimes the correct behavior is to stop with a useful message. “The process failed” is not useful. “The parcels layer has no `parcel_id` field, so the report cannot be generated” is useful.

## Abstraction is how a one-off workflow becomes a tool

The progression usually looks something like this:

**Manual GIS → ModelBuilder → scripts → libraries and applications**

Each step moves a little more of the workflow out of your immediate attention.

Manual work is flexible but repetitive. A model captures the sequence. A script adds control, testing, logging, and reuse. A library or application gives the workflow a stable interface for other people and other systems.

Abstraction is not about making a workflow impressive. It is about deciding which details should remain configurable and which should become reliable defaults.

If you have run the same ten-step process twenty times, you probably do not need to become a software engineer before improving it. You need to identify the repeated structure and give it a name.

That name might eventually look like this:

```python
find_affected_parcels(roads, parcels, distance)
```

The five underlying operations still exist. They are simply packaged behind an interface that can be reused. This is how a script becomes a library, and how a library becomes software.

## The translation is the advantage

Cartographers already think in relationships. They ask what belongs inside what, what connects to what, what is visible at a given scale, and what changes when the reference system changes. Those are powerful programming instincts.

The move into code does not discard that way of thinking. It gives it another medium.

The next time a programming tutorial introduces a variable, think of a named layer or output. When it introduces a function, think of a geoprocessing tool. When it introduces a loop, think of an iterator over features or files. When it introduces an exception, think of the last time a workflow failed because the real data did not match the assumed data.

The syntax will still take practice. That part is unavoidable.

But the reasoning is already familiar. You have been programming through maps for years.
