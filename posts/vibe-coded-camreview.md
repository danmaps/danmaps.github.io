---
date: 2026-01-30
tags:
- AI
- side-projects
- productivity
- gis
- javascript
title: Vibe coding CamReview: a trail cam app I actually use
---

I built a small app called **CamReview** to review trail camera photos and videos.

Not “fast” in the benchmark sense. Fast in the only way I care about: I can sit down with my phone, thumb through a couple hundred captures, keep the good ones, trash the junk, and move on with my life.

And yes, I vibe coded a lot of it.

This post is what it felt like when the target wasn’t a demo or a portfolio piece, but a tool I use on my own files.

## Trail cam review is a slog (and the tools don’t help)

Trail cameras produce a specific kind of annoyance:

- a ton of near-duplicates
- long stretches of nothing
- occasional gems you *really* want to keep
- files scattered across folders and SD cards

Most tools for dealing with this fall into a few buckets:

- **Too heavy:** cloud accounts, uploads, subscriptions
- **Too generic:** image viewers with no “decision engine”
- **Too risky:** deletes that feel permanent (or at least scary)

I wanted something simpler.

## My constraints (the whole point)

CamReview v0 has a few non‑negotiables, and the constraints basically *are* the product:

- **Local-only.** No cloud. No accounts. No Docker.
- **Runs on Windows.** That’s where the media lives.
- **Phone-first review loop.** The decisions happen on a couch, not at a desk.
- **Safe deletes.** Delete should mean “move into `Trash_YYYY-MM-DD/`”.
- **One-at-a-time decisions.** Keep / Delete / Favorite.
- **Undo.** Always.

It also has some explicit non-goals:

- no renaming
- no permanent deletes
- no albums, collections, or edits
- no cloud sync

If a feature didn’t help the core loop, it didn’t make the cut.

## The shape of the app (boring on purpose)

CamReview is intentionally boring:

- **Node + Express** backend
- a simple frontend
- a persistent JSON metadata file (`trailcam_review.json`)
- media served directly from disk

You point it at a `mediaRoot` folder, start the server, and open it on your phone over LAN (or Tailscale).

That’s it.

## Mobile vs desktop: same data, different vibe

I didn’t want “a mobile version” and “a desktop version.” I wanted *one* app with one set of state.

So the split is simple:

- **Desktop** is power-user mode: library drawer, search/filter, keyboard shortcuts, optional AI batch tools.
- **Mobile** is streamlined: big buttons + swipes, minimal chrome.

Both share the same queue, metadata, and safe-delete behavior.

## The part I’m proud of: safe deletes + trust

The most important thing in a personal media tool isn’t the UI.

It’s trust.

Delete in CamReview doesn’t delete. It moves files immediately into a dated folder under `mediaRoot`:

- `Trash_YYYY-MM-DD/`
- `Keep_YYYY-MM-DD/`
- `Favorites_YYYY-MM-DD/`

Once you trust the tool not to hurt you, you start moving faster.

That’s the whole game.

## Video on phones is weird (so I made a fallback)

A big surprise was how finicky video playback can be on mobile browsers.

So CamReview has a pragmatic fallback:

- Desktop tries to play the original MP4 with sound.
- If mobile playback is flaky, the server can generate a smaller H.264 MP4 (requires `ffmpeg`) and play that.
- For quick previews, it can generate low‑FPS preview frames.

It may look choppier, but it stays reliable.

## Optional AI: helpful, never required

CamReview has optional AI features (desktop-only) via OpenRouter:

- batch “critter detection” (move no‑animal photos to Trash)
- whimsical caption generation that’s always editable

But the key word is **optional**.

If AI is down, expensive, or annoying, the app still does the thing.

## What vibe coding felt like

Vibe coding shines when:

- the problem is small enough to keep in your head
- you can iterate in tight loops
- you’re willing to read what the model writes

CamReview fit that.

But it also punished sloppy thinking.

The easiest failure mode was “building UI instead of building product.” AI makes that dangerously easy: it removes friction that normally whispers, *this is not worth your time.*

So I tried to keep asking:

- Does this make review faster?
- Does this reduce risk?
- Does this reduce cognitive load?

If not, it’s bike shedding.

## What’s next

The next version is going to split into two pages:

- **Browse**: a GitHub-style capture heatmap + a fast way to jump around
- **Review**: the decision engine

If I can make “find the interesting day” as frictionless as “keep/delete,” the whole thing levels up.

---

If you want to check out the code, it’s on GitHub: https://github.com/danmaps/camreview
