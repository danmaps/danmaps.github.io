---
date: 2026-01-30
tags:
- AI
- javascript
- side-projects
- productivity
title: Vibe coding CamReview: a trail cam app I actually use
---

I built a small app called **CamReview** to review trail camera photos and videos fast.

Not "fast" in the benchmark sense. Fast in the *real* sense: I can sit down with my phone, thumb through a couple hundred captures, keep the good ones, trash the junk, and move on with my life.

And yes, I vibe coded a lot of it.

This post is about what that felt like when the target wasn't a demo, but a tool I use on my own files.

## The problem: trail cam review is a slog

Trail cameras produce a specific kind of annoyance:

- a ton of near-duplicates
- long stretches of nothing
- occasional gems you *really* want to keep
- files scattered across folders and SD cards

Most tools for dealing with this are either:

- too heavy (cloud accounts, uploads, subscriptions)
- too fragile (random image viewers with no "decision engine")
- too risky (delete operations that feel irreversible)

I wanted something simpler.

## My constraints (the whole point)

CamReview had a few non-negotiables:

- **Local-only.** No cloud. No accounts.
- **Runs on Windows.** That's where the media lives.
- **Phone-first UI.** The review action happens on a couch, not at a desk.
- **Safe deletes.** Deleting should mean "move to Trash_YYYY-MM-DD".
- **One-at-a-time decisions.** Keep / Delete / Favorite.
- **Undo.** Always.

If a feature didn't help the core loop, it didn't make the cut.

## The shape of the app

The current version is intentionally boring:

- **Node + Express** backend
- a single-page frontend
- a JSON metadata file (flat rows)
- media served directly from disk

You point it at a `mediaRoot` folder, start the server, and open it on your phone via LAN (or Tailscale).

## Why vibe coding worked here (and where it didn't)

Vibe coding shines when:

- the problem is small enough to keep in your head
- you can iterate in tight loops
- you're willing to read what the model writes

CamReview fit that.

But it also punished sloppy thinking.

The easiest failure mode was **building UI instead of building product**. I could have spent a week arguing with CSS about "perfect" layout. AI makes that dangerously easy.

So I forced myself to stay honest:

- Does this change make review faster?
- Does this reduce risk?
- Does this reduce cognitive load?

If not, it was bike shedding.

## The part I'm proud of: safe deletes + trust

The most important thing in a personal media tool isn't the UI.

It's trust.

Delete in CamReview doesn't delete. It moves files immediately into a dated folder:

- `Trash_YYYY-MM-DD/`
- `Keep_YYYY-MM-DD/`
- `Favorites_YYYY-MM-DD/`

That made the tool feel safe enough to use at speed.

## Optional AI: useful, but never required

I added optional "AI batch" features (desktop-only) that can:

- detect whether an image likely contains an animal
- generate a short whimsical caption

The key word is **optional**. The review loop never depends on AI.

If you don't set an API key, the app still works.

## What I learned

A few lessons from this project:

1. **Vibe coding is leverage, not a substitute for taste.**
2. **A real tool needs constraints.** Otherwise you build a demo.
3. **Mobile UX is where bad decisions show up immediately.**
4. **Safety beats cleverness.** People move faster when they're not afraid.

## What's next

The next version is going to split into two pages:

- **Browse**: a GitHub-style capture heatmap + a fast way to jump around
- **Review**: the decision engine

If I can make the "find the interesting day" part as frictionless as the "keep/delete" part, the whole experience levels up.

---

If you want to check out the code, it's on GitHub: https://github.com/danmaps/camreview
