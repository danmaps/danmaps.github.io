---
date: 2025-12-12
tags:
- AI
- productivity
- strategy
- work
title: Vibe Coding, Bike Shedding, and the Real Work
---

I recently got GitHub Enterprise access from someone I met at a vibe coding hackathon. Overnight my Copilot usage limit quadrupled, so between that and my own projects I have been vibe coding constantly: at work, after work, and while building Advent of Code visualizations at night.

I still hit those limits, which pushed me to try GPT-5 Codex through my $20/month ChatGPT plan. It works just as well, if not better. The VS Code extension feels familiar, the workflows rhyme, and the only downside is that I still need better muscle memory for undo.

The net effect is simple: I now have an abundance of coding capacity. That abundance forced me to notice something uncomfortable.

It is impossible to talk about vibe coding right now without acknowledging the controversy around it. There is a real risk of generating AI slop, including this very blog post if I am not careful. Using these tools thoughtlessly can turn code into something opaque, brittle, and unearned. Because of that, I try to be deliberate. I read as much code as I write. I step through it. I question it. I enjoy learning from what the model produces as much as I enjoy the end result. This does not feel lazy to me. It feels awkward because the tools are new, and we are still figuring out what good taste looks like when assistance is cheap.

### When Friction Disappears, Mistakes Get Subtle

On a recent project I built a small frontend whose only real purpose was to surface a Python script. The script was the product. The frontend was just the delivery mechanism.

And yet, with AI help, I found myself decorating the page with reckless abandon. I wrote and rewrote CSS like an amateur graffiti artist: colors, spacing, layout tweaks. Hundreds, then thousands, of barely structured styles.

The problem was not that CSS is hard. The problem was that it was easy. AI removed the friction that normally whispers, "This is not worth your time." I did not have the taste, experience, or constraints to make good frontend decisions, but I had infinite suggestions and infinite patience from a machine.

Eventually I stepped back and asked a basic question: why am I doing this at all? The answer was obvious. I was not building a design system. I was building a Python tool. So I migrated the whole thing to Streamlit. No bike shedding. No taste decisions. No pretending I cared about polish. Streamlit already built those defaults. The value lives in the Python logic underneath, and that is the tool. That decision felt less like giving up and more like leveling up.

### A Puzzle That Rewarded Paying Attention

This reminded me of Advent of Code 2025, Day 12. For the final puzzle, Eric Wastl teased an NP-hard problem--the kind that makes you brace for exponential time and clever heuristics. On paper it looked scary.

In reality, the input structure made the problem trivial. If you stopped thinking about the theoretical worst case and instead focused on the actual puzzle in front of you, it was arguably the easiest problem of the entire event.

The people who struggled were not bad programmers. They were solving a different problem than the one they were given. The lesson was not about algorithms. It was about attention.

### Product Thinking Is a Defense Mechanism

Technical people have a natural tendency to dive into the weeds. Implementation feels productive. It is measurable. It scratches the itch. AI amplifies that tendency. When every micro-decision is cheap, it becomes dangerously easy to spend all of your energy on low-leverage work that looks like progress.

Product thinking is how you fight that.

Product thinking asks:

- What is the actual goal?
- What decisions matter?
- What can I safely delegate to tools, frameworks, or defaults?
- What would success look like if I stripped this down to its essence?

This is not about doing less work. It is about choosing better work.

### This Shows Up Outside of Code Too

I have started noticing this pattern everywhere. Emily is shopping for a new stroller for when Willow can sit up, which will be soon. There are overlapping criteria: trunk fit, weight, handling, and a standing spot for Rowan. The options are endless. Facebook Marketplace alone is a doom scroll of near-duplicates.

This is a multidimensional data problem. The hard part is not finding options. It is assigning the right weights to each variable so the solution space collapses into something manageable. That is the same problem as software. The same problem as Advent of Code. The same problem as product management.

### The Real Work

It is not just how hard you work. Depending on the situation, aiming the laser matters more than how bright it is.

AI makes this unavoidable. When execution is cheap, judgment becomes everything: clarity about goals, willingness to ignore shiny distractions, and comfort with letting other people's good decisions stand in for your own.

I have been circling this idea for a while. Lately it feels like it is coalescing across work, side projects, puzzles, and life. Maybe that is just how I see the world.
