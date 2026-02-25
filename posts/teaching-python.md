---
date: 2024-09-11
tags:
  - Programming
  - Python
  - Education
  - AI

title: "Thinking like a programmer"
---

I teach python.

There’s a lot of gatekeeping in technical fields like software development. People talk themselves out of learning because they assume there’s some secret aptitude test they didn’t get the memo for. They tell themselves they lack the “brain for it.”

This has always been wrong, but it has never been more wrong than now.

In 2024, the biggest barrier to learning programming isn’t intelligence. It’s the feedback loop.

## Part I: Thinking like a programmer is shrinking the loop

When someone says “think like a programmer,” it can sound mystical. Like there’s a special mindset you’re supposed to download.

In practice it’s simpler and more human:

**Programming is making a guess, testing it, observing what happened, and updating your guess.**

That’s it.

Beginners don’t struggle because they can’t understand variables. They struggle because their loop is slow and punishing.

- They write code.
- It fails.
- The error message feels like an insult written in a foreign language.
- They don’t know what to try next.
- They either quit or they flail.

Thinking like a programmer means you learn to protect the loop.

### 1) Change one thing at a time
If you make three changes and it starts working, you didn’t learn anything. You got lucky.

Small moves make cause and effect visible.

### 2) Predict what you expect before you run it
This sounds goofy, but it’s the habit that creates a mental model.

Say it out loud:
- “This should print 10.”
- “This function should return a list of strings.”

Then run it and compare.

When your expectation is wrong, that’s the lesson.

### 3) Make the invisible visible
Most bugs are just hidden state.

Print things. Log things. Inspect small slices of data.

When you’re stuck, you don’t need more cleverness. You need more information.

### 4) Reduce the problem until it fits in your head
If your script is 400 lines and it’s failing, cut it down.

Make a tiny version that reproduces the bug.

The best debugging tool is embarrassment. Make the bug small enough that it feels a little stupid.

### 5) Treat errors as clues, not verdicts
A traceback is not a condemnation. It’s a breadcrumb trail.

Most of the time it’s telling you one of three things:
- you used the wrong type
- you used the wrong shape (list vs dict, row vs table)
- you’re calling something earlier than you think

If you keep this framing, you stop taking errors personally. You start interrogating them.

## Part II: Using ChatGPT as a coach (not a code vending machine)

ChatGPT knows a lot about programming and especially python. This isn’t magic. Python is popular, documented, and discussed everywhere, so LLMs tend to be unusually good at it.

That means you can get unstuck fast.

But there’s a fork in the road.

A lot of people meet ChatGPT as a **magic code dispenser**. They paste a problem in, get code out, paste it back, and call it done.

That works… until it doesn’t.

The real leverage is using it as a tutor while you ship real work.

### Choose your mode on purpose: Ship mode vs Learn mode
Before you ask, decide what you want:

- **Ship mode:** “Give me the fastest working solution. Minimal explanation.”
- **Learn mode:** “Coach me. Ask questions. Explain the reasoning. Make me do a piece of it.”

If you always choose ship mode, you’ll get work done until you hit a weird edge case. Then you’re stuck again.

If you mix in learn mode, the skill compounds. You start needing help less often.

A tiny habit that pays off: after you fix something, spend two minutes asking:
- “What was the root cause?”
- “How would I recognize this earlier next time?”
- “What’s the smallest test that would have caught it?”

### The AI tutor rules I give students

#### 1) Paste the exact error and the smallest reproduction
Don’t summarize. Copy the traceback.

Even better: cut your code down until it’s the smallest thing that still breaks.

#### 2) Ask for an explanation first, not a patch
Try this:

- “Explain this traceback like I’m new, then tell me the 3 most likely causes.”

You want the mental model, not just the bandaid.

#### 3) Ask for two solutions: quick fix and robust fix
- “Give me a quick fix to unblock me.”
- “Now give me the robust version I won’t regret later.”

This teaches you tradeoffs: correctness vs convenience, readability vs cleverness.

#### 4) Ask it to verify, not just propose
- “How do I confirm this is actually fixed?”
- “What should I print or assert?”

Most people skip this. It’s where bugs become reliable knowledge.

#### 5) Make it wait for you
If your goal is learning, don’t let it do everything.

- “Give me a hint, not the answer. Wait for my attempt, then critique it.”

This one move turns a code generator into a coach.

### My favorite prompts (copy/paste)

- “I want to learn. Don’t write the full code yet. Ask me 5 clarifying questions and then propose a plan.”
- “I’m in ship mode. Provide the smallest patch that fixes this, and a one sentence why.”
- “Explain what changed and why that change fixes it.”
- “Give me a minimal repro of this bug.”
- “Give me 3 test cases I should run right now.”

## Closing

Programming isn’t a talent. It’s a loop.

If you make the loop fast, kind, and repeatable, you will learn.

AI doesn’t replace the craft. It makes the craft easier to practice every day, while you’re playing, while you’re building, and while you’re getting real work done.
