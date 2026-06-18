---
date: 2026-02-24
tags:
  - Programming
  - Python
  - Education
  - AI

title: "Thinking like a programmer"
layout: rich
---

I teach python.

Thereâ€™s a lot of gatekeeping in technical fields like software development. People talk themselves out of learning because they assume thereâ€™s some secret aptitude test they didnâ€™t get the memo for. They tell themselves they lack the â€œbrain for it.â€

This has always been wrong, but it has never been more wrong than now.

In 2026, the biggest barrier to learning programming isnâ€™t intelligence. Itâ€™s the feedback loop.

## Part I: Thinking like a programmer is shrinking the loop

When someone says â€œthink like a programmer,â€ it can sound mystical. Like thereâ€™s a special mindset youâ€™re supposed to download.

In practice itâ€™s simpler and more human:

**Programming is making a guess, testing it, observing what happened, and updating your guess.**

Thatâ€™s it.

Beginners donâ€™t struggle because they canâ€™t understand variables. They struggle because their loop is slow and punishing.

- They write code.
- It fails.
- The error message feels like an insult written in a foreign language.
- They donâ€™t know what to try next.
- They either quit or they flail.

Thinking like a programmer means you learn to protect the loop.

### 1) Change one thing at a time
If you make three changes and it starts working, you didnâ€™t learn anything. You got lucky.

Small moves make cause and effect visible.

### 2) Predict what you expect before you run it
This sounds goofy, but itâ€™s the habit that creates a mental model.

Say it out loud:
- â€œThis should print 10.â€
- â€œThis function should return a list of strings.â€

Then run it and compare.

When your expectation is wrong, thatâ€™s the lesson.

### 3) Make the invisible visible
Most bugs are just hidden state.

Print things. Log things. Inspect small slices of data.

When youâ€™re stuck, you donâ€™t need more cleverness. You need more information.

### 4) Reduce the problem until it fits in your head
If your script is 400 lines and itâ€™s failing, cut it down.

Make a tiny version that reproduces the bug.

The best debugging tool is embarrassment. Make the bug small enough that it feels a little stupid.

### 5) Treat errors as clues, not verdicts
A traceback is not a condemnation. Itâ€™s a breadcrumb trail.

Most of the time itâ€™s telling you one of three things:
- you used the wrong type
- you used the wrong shape (list vs dict, row vs table)
- youâ€™re calling something earlier than you think

If you keep this framing, you stop taking errors personally. You start interrogating them.

## Part II: Using ChatGPT as a coach (not a code vending machine)

ChatGPT knows a lot about programming and especially python. This isnâ€™t magic. Python is popular, documented, and discussed everywhere, so LLMs tend to be unusually good at it.

That means you can get unstuck fast.

But thereâ€™s a fork in the road.

A lot of people meet ChatGPT as a **magic code dispenser**. They paste a problem in, get code out, paste it back, and call it done.

That worksâ€¦ until it doesnâ€™t.

The real leverage is using it as a tutor while you ship real work.

### Choose your mode on purpose: Ship mode vs Learn mode
Before you ask, decide what you want:

- **Ship mode:** â€œGive me the fastest working solution. Minimal explanation.â€
- **Learn mode:** â€œCoach me. Ask questions. Explain the reasoning. Make me do a piece of it.â€

If you always choose ship mode, youâ€™ll get work done until you hit a weird edge case. Then youâ€™re stuck again.

If you mix in learn mode, the skill compounds. You start needing help less often.

A tiny habit that pays off: after you fix something, spend two minutes asking:
- â€œWhat was the root cause?â€
- â€œHow would I recognize this earlier next time?â€
- â€œWhatâ€™s the smallest test that would have caught it?â€

### The AI tutor rules I give students

#### 1) Paste the exact error and the smallest reproduction
Donâ€™t summarize. Copy the traceback.

Even better: cut your code down until itâ€™s the smallest thing that still breaks.

#### 2) Ask for an explanation first, not a patch
Try this:

- â€œExplain this traceback like Iâ€™m new, then tell me the 3 most likely causes.â€

You want the mental model, not just the bandaid.

#### 3) Ask for two solutions: quick fix and robust fix
- â€œGive me a quick fix to unblock me.â€
- â€œNow give me the robust version I wonâ€™t regret later.â€

This teaches you tradeoffs: correctness vs convenience, readability vs cleverness.

#### 4) Ask it to verify, not just propose
- â€œHow do I confirm this is actually fixed?â€
- â€œWhat should I print or assert?â€

Most people skip this. Itâ€™s where bugs become reliable knowledge.

#### 5) Make it wait for you
If your goal is learning, donâ€™t let it do everything.

- â€œGive me a hint, not the answer. Wait for my attempt, then critique it.â€

This one move turns a code generator into a coach.

### My favorite prompts (copy/paste)

- â€œI want to learn. Donâ€™t write the full code yet. Ask me 5 clarifying questions and then propose a plan.â€
- â€œIâ€™m in ship mode. Provide the smallest patch that fixes this, and a one sentence why.â€
- â€œExplain what changed and why that change fixes it.â€
- â€œGive me a minimal repro of this bug.â€
- â€œGive me 3 test cases I should run right now.â€

## Closing

Programming isnâ€™t a talent. Itâ€™s a loop.

If you make the loop fast, kind, and repeatable, you will learn.

AI doesnâ€™t replace the craft. It makes the craft easier to practice every day, while youâ€™re playing, while youâ€™re building, and while youâ€™re getting real work done.

