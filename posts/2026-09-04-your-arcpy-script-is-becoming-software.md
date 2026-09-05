---
title: "Your ArcPy Script Is Becoming Software. Treat It Like Software."
date: 2026-09-04
tags:
- Draft
- GIS
- Python
- Product
summary: "ArcPy scripts have a habit of quietly becoming software. A practical guide to recognizing that transition and adding just enough structure: configuration, logging, testing boundaries, and a project layout that can grow with the work."
layout: rich
---

Most ArcPy projects don't start as software projects.

They start because you have a job to do.

Maybe you need to buffer several thousand features, intersect them with another layer, calculate a few fields, and write the result to a geodatabase. You open ArcGIS Pro, create a Python file, import `arcpy`, and start working.

```python
import arcpy

input_fc = r"C:\GIS\Projects\Vegetation\Data.gdb\Trees"
output_fc = r"C:\GIS\Projects\Vegetation\Data.gdb\Tree_Buffer"

arcpy.analysis.Buffer(input_fc, output_fc, "100 Feet")
```

It works.

Great.

Then somebody asks for one more thing.

You add it.

Then you need to run the workflow against a different geodatabase, so you add another path.

Then you need some logging.

Then somebody else needs to run it.

Then the output schema changes.

Then it needs to run every week.

Six months later, you open:

```text
vegetation_analysis_final_v2_WORKING.py
```

and discover that your 30-line ArcPy script has become 900 lines of software.

Nobody ever made a conscious decision to build software.

It just happened.

<!-- HERO_IMAGE: /static/images/your-arcpy-script-is-becoming-software-hero.png -->

## The awkward middle ground of GIS development

There's a huge amount of GIS code living in the space between a throwaway script and a professionally maintained application.

GIS analysts are especially likely to end up here.

ArcGIS makes it remarkably easy to start automating. You can copy a Python snippet from geoprocessing history, change a few parameters, and suddenly you've eliminated an hour of manual work.

That's a feature, not a problem.

The problem starts when successful scripts accumulate responsibilities without accumulating structure.

A single file starts handling:

- file paths
- configuration
- geoprocessing
- business logic
- logging
- validation
- error handling
- output naming
- environment settings
- notifications

Eventually, changing one thing means being afraid of three other things.

The script hasn't necessarily become bad.

It has simply outgrown the architecture it started with.

## The moment a script becomes software

There's no magic line count where this happens.

A 1,500-line script can occasionally be perfectly reasonable. A 100-line script can already be painful to maintain.

I think the better signal is **responsibility**.

Your script is becoming software when you start asking questions like:

- How does somebody configure this without editing the source code?
- How do I know what happened when it fails?
- How do I test this without running an expensive geoprocessing operation every time?
- How can another developer understand this six months from now?
- How do I run the same workflow in development and production?
- How do I change one piece without breaking everything else?

At that point, adding more functions to the same `.py` file doesn't really solve the problem.

The project needs structure.

## Start by getting configuration out of your code

Hard-coded paths are probably the most recognizable ArcPy example.

```python
workspace = r"\\server\department\production\Vegetation.gdb"
buffer_distance = "100 Feet"
output_name = "Tree_Buffer"
```

There's nothing inherently wrong with constants.

The problem is mixing things that describe **this particular execution environment** with the code that describes **what the workflow does**.

Instead, configuration can live somewhere explicit:

```yaml
workspace: "\\\\server\\department\\production\\Vegetation.gdb"
buffer_distance: "100 Feet"
output_name: "Tree_Buffer"
```

Now your Python code can ask for configuration instead of secretly containing it.

That matters when you want:

```text
local.yaml
test.yaml
production.yaml
```

It also means somebody can change an input path without modifying the program itself.

That's a small architectural decision with a surprisingly large payoff.

## `print()` eventually stops being enough

I love `print()`.

There is absolutely nothing wrong with this:

```python
print("Starting buffer...")
```

for a small script you're running interactively.

But once a workflow runs unattended, or somebody else needs to diagnose it, you start wanting more information.

```text
2026-09-04 08:03:12 INFO Starting vegetation workflow
2026-09-04 08:03:13 INFO Input features: 18,422
2026-09-04 08:03:13 INFO Buffer distance: 100 Feet
2026-09-04 08:04:51 INFO Buffer completed
2026-09-04 08:04:52 ERROR Failed writing output to production geodatabase
```

Python's standard `logging` module already solves this problem.

The important change isn't really `print()` to `logging`.

It's recognizing that **observability is part of the program**.

Once other people depend on your automation, knowing what happened matters almost as much as making it happen.

## Separate GIS operations from business logic

This is one of the biggest improvements I've made to how I structure ArcPy projects.

Consider logic like:

```python
def output_name(source_name, distance):
    return f"{source_name}_buffer_{distance}"
```

There is nothing GIS-specific about that function.

It doesn't need ArcGIS Pro.

It doesn't need a license.

It doesn't need `arcpy`.

It can be tested by ordinary Python:

```python
def test_output_name():
    assert output_name("poles", 100) == "poles_buffer_100"
```

Now compare that with:

```python
arcpy.analysis.Buffer(...)
```

That genuinely depends on ArcPy.

Keeping those concerns separate gives you a useful boundary:

```text
Pure Python
    |
    | configuration
    | validation
    | naming
    | transformations
    | business rules
    |
    v
ArcPy boundary
    |
    | Buffer
    | Intersect
    | Spatial Join
    | geodatabase I/O
    |
    v
GIS outputs
```

The goal isn't to abstract ArcPy away.

ArcPy is useful precisely because it gives us access to ArcGIS.

The goal is to avoid making **everything else** dependent on ArcPy unnecessarily.

That makes testing faster, reasoning easier, and maintenance much less painful.

## Give the project somewhere to grow

Eventually, I want the directory itself to communicate how the project works.

Something like:

```text
my-arcpy-project/
├── README.md
├── pyproject.toml
├── config/
│   ├── example.yaml
│   └── local.yaml
├── scripts/
│   └── run_workflow.py
├── src/
│   └── my_project/
│       ├── config.py
│       ├── logging_config.py
│       └── workflows/
│           └── buffer_features.py
└── tests/
    ├── test_config.py
    └── test_workflow_helpers.py
```

This may look like more complexity than:

```text
script.py
```

Technically, it is.

But it's **organized complexity**.

That's the trade.

As projects grow, complexity doesn't disappear because we refuse to create folders. It just gets compressed into increasingly difficult files.

A good project structure gives that complexity somewhere sensible to live.

## AI coding agents make this more important, not less

There's another reason I've been thinking about this lately.

I use AI coding tools increasingly often.

It's tempting to think these tools reduce the need for project structure because an AI model can understand messy code for us.

I've found almost the opposite.

Coding agents are much more useful when the repository communicates its expectations.

A file like:

```text
AGENTS.md
```

can tell an agent things a Python file can't.

For example:

- this project targets ArcGIS Pro on Windows
- ArcPy is only available in the ArcGIS Pro Python environment
- don't assume Linux-style paths
- keep pure Python logic outside ArcPy-dependent modules where practical
- don't modify production geodatabases in tests
- configuration belongs in YAML, not source code
- generated outputs shouldn't be committed
- run pure Python tests before ArcPy integration tests

That context helps both humans and machines.

The agent doesn't have to rediscover the architecture every time it touches the repository.

And neither do I.

## Don't overcorrect

There is an opposite failure mode here.

You can absolutely turn a 60-line ArcPy script into a ridiculous architecture involving dependency injection, abstract factories, twelve interfaces, Docker, Kubernetes, and an event bus.

Please don't.

If your script:

1. reads one feature class,
2. buffers it,
3. writes another feature class,

then maybe `buffer.py` is exactly the architecture you need.

The goal isn't to make GIS scripts look like enterprise software.

The goal is to notice when something **has already become software** and give it enough structure to remain understandable.

That's it.

## The starter I kept rebuilding

I noticed that I was repeatedly making the same decisions when starting ArcPy projects:

```text
src/
config/
scripts/
tests/
logging
.gitignore
pyproject.toml
AGENTS.md
```

None of these pieces is particularly exciting.

That's kind of the point.

They're the boring scaffolding I want in place before I start solving the interesting GIS problem.

So I packaged my preferred setup as **ArcPy Project Starter**.

It's a small, opinionated project template for ArcGIS Pro developers and GIS analysts who are moving from one-off Python scripts toward maintainable automation.

It includes:

- an ArcPy-friendly Python project structure
- YAML configuration
- centralized logging
- an example reusable workflow
- separation between pure Python tests and ArcPy-dependent execution
- ArcGIS Pro-aware Git configuration
- guidance for AI coding agents

It's **$15, one time**.

If that saves you even one round of creating `script_final_v2_WORKING.py`, I figure we're even.

[Get ArcPy Project Starter →](https://dannymcvey.com/products/arcpy-project-starter/)

## The larger lesson

GIS gives us unusually powerful building blocks.

A geoprocessing tool that represents years of engineering can be invoked with a single Python function call. That makes it possible to build genuinely useful automation very quickly.

But successful automation tends to grow.

That's a good problem.

The trick is recognizing when the thing you wrote to avoid clicking the same button 400 times has quietly become something people depend on.

At that point, don't throw it away and start over.

Give it a configuration file.

Give it logs.

Give it tests where tests make sense.

Give it a project structure.

Give the next developer some instructions.

Your ArcPy script became software.

Congratulations.
