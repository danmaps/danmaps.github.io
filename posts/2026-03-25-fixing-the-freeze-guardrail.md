---
title: "Fixing the freeze guardrail by admitting generated files are part of the product"
date: 2026-03-25
tags:
  - Draft
  - blogging
  - systems
  - tooling
  - GitHub
layout: rich
---

A small but useful failure mode showed up in my blog workflow this week.

The repo has a guardrail in CI that runs `freeze.py` and fails if the generated site output under `docs/` is not committed.

That is a good rule.

The annoying part was that I had a publish flow that was still too manual.

So the setup looked like this:

- CI correctly checked whether generated output was up to date
- local publishing still relied on a hand-maintained `git add` list
- new generated files could appear without getting staged
- CI would catch the mismatch and fail

Which is exactly what happened.

## The bug was not the guardrail

The first instinct with this kind of thing is to blame the failing job.

But the guardrail was doing its job.

The actual problem was that the local publish process still assumed I knew exactly which generated files would change.

That assumption stops working the second the build becomes even slightly dynamic.

In this case, the culprit was tag pages.

A new tag appeared in a draft post.
`freeze.py` correctly generated new files like:

- `docs/tag/orchestration.html`
- `docs/tag/symphony.html`

But the publish step did not automatically stage them, because it was built around an explicit list of expected files.

That is fragile in a really boring way.

## The lesson: generated output is not â€œextraâ€

The real fix was not â€œremember to add those two files.â€

The real fix was to admit something more basic:

**if the frozen site in `docs/` is what gets deployed, then generated files are not incidental clutter â€” they are part of the product.**

Once that is true, the publish step should treat them that way.

Not as an afterthought.
Not as a special case.
Not as a list to keep updating by hand.

Just: freeze the site, then stage the generated output.

All of it.

## What I changed

I added a small repo-local helper:

```bash
./scripts/freeze_and_stage.sh
```

That is now the human-facing publish step.

It does three things:

1. runs the freeze build
2. ensures `docs/.nojekyll`
3. stages `posts/` and `docs/` together

That means new tag pages get picked up automatically.
It also means the local publish process now matches what the guardrail expects.

That is the important part.

A good guardrail should not just catch mistakes. It should push the workflow toward the shape where the mistake becomes less likely.

## The meta point

This is obviously a tiny blog-specific example, but I think the pattern is general.

A lot of workflow pain comes from pretending generated artifacts are somehow less real than source files.

But if those artifacts are what users actually get â€” deployed docs, compiled assets, reports, app bundles, generated plans, exported files â€” then they need to be handled as first-class outputs.

Otherwise you get a weird split-brain system where:

- the build knows what is real
- CI knows what is real
- but the human workflow still treats those outputs as optional debris

That is how boring process bugs keep happening.

## The better standard

The better rule is simple:

**if a file is generated as part of the canonical build, the workflow should make it hard to forget.**

That does not always mean committing build output. In many repos it should not.

But in a repo like this one, where `docs/` is the published GitHub Pages artifact, it absolutely does.

So the fix was not glamorous.

It was just making the workflow tell the truth:

- freeze
- stage the generated site
- review it
- commit it

Sometimes that is all a good systems improvement is.

Not a new capability.
Just one less place for reality and the process to drift apart.

