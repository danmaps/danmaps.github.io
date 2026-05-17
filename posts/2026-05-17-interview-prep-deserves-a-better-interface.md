---
title: Interview Prep Deserves a Better Interface
date: 2026-05-17
tags:
  - Draft
  - AI
  - work
  - systems
  - product
---

I have spent plenty of time using AI in the now-familiar ways:

- ask a question
- get a response
- refine the prompt
- maybe copy something into a note
- maybe forget half of it later

That is still useful.

<img src="/static/images/interview-prep-better-interface-hero.png" alt="Illustration of a focused interview prep desk with a custom HTML study page and notes" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

But this week I ended up doing something that felt like a step up from my usual AI interactions.

I had an internal interview coming up for a **Data Engineering Senior Specialist** role at Southern California Edison. Instead of just chatting with a model, collecting scattered notes, and hoping I would remember the good parts later, I turned the whole prep process into a small, purpose-built website.

Not a product. Not a startup. Not a full application in the grand sense.

Just a sharp little HTML site built from my resume, the job description, the likely panel, mock interview runs, and the follow-up reflections that came out of those conversations.

It ended up being one of the more useful examples I have seen lately of what AI is actually good for when it is paired with a real interface.

## The job was not "get better answers"

The obvious use of AI for interview prep is to ask it for:

- likely questions
- suggested answers
- salary advice
- talking points
- encouragement

That is fine as far as it goes.

But the real problem was not a lack of generated content.

The problem was overload.

Once you do a few mock interviews with a chatbot, ask follow-up questions, refine answers, and collect some research on the hiring manager and the role, you end up with a pile of decent material and no especially good place to hold it.

A chat transcript is not a study surface.

A note dump is not a study surface either.

What I actually needed was something more like:

- a quick-glance alignment between the job description and my experience
- a few strongest stories to lean on
- a tighter intro
- mock interview lessons turned into visible reminders
- a one-page cheat sheet I could open during the interview without digging through paragraphs of context

That is a UI problem, not a language problem.

## So I made the prep material into a site

I built a small static prep site in its own repo.

It included things like:

- a concise role overview
- panel deep-dive notes
- a JD ↔ resume alignment table
- an intro script
- behavioral question prompts
- a story bank
- practical tips
- questions to ask them

Then I kept iterating it as the prep got better.

When a mock interview exposed a weakness, I did not just tell myself to remember it. I updated the page.

When a conversation surfaced a better framing, I did not leave it trapped in chat history. I folded it into the prep site.

When the full page got too long for interview pressure, I created a separate **one-page cheat sheet** with only the most important at-a-glance material:

- the opening spine
- the themes to repeat
- answer structure
- best story prompts
- gap answers
- questions to ask
- final reminders

That was the real upgrade.

The AI did not become more magical.

The interface became more useful.

## The best insight was structural, not verbal

The strongest thing that came out of the mock interview work was not a perfect canned answer.

It was a pattern.

My raw answers were usually pretty solid in substance, but I kept compressing them too early. I would jump straight to the gist, the lesson, or the outcome before fully explaining:

- what was actually happening
- why it was difficult
- what decision I made
- what changed as a result

That turned into a better answer structure for me:

1. **Situation**
2. **Tension**
3. **Judgment**
4. **Outcome**

That is close to STAR, but it puts more emphasis on the part that makes an answer sound senior: judgment.

That one insight was more valuable than another 20 generated sample answers.

And once it was on the page, I could actually use it.

## This is what I mean by better AI use

The point is not that every interview prep process deserves a custom site.

The point is that the best AI workflows increasingly look like this:

- use the model to help generate, critique, and refine material
- convert the useful parts into structured artifacts
- build a surface that fits the real use case
- keep the output inspectable and editable
- optimize for retrieval and application, not just production

That is a lot closer to how I want to use AI in general.

Not as an oracle.
Not as a vibe machine.
Not as a pile of disposable chat sessions.

More like a collaborator that helps produce components, which then get arranged into a durable interface for a real task.

In this case the interface was simple HTML.

But the principle is bigger than interview prep.

## A bespoke site is sometimes the right answer

There is a tendency to think custom interfaces are overkill for small personal workflows.

Sometimes they are.

But sometimes a bespoke little website is exactly the right place for a pile of semi-structured thinking to settle into something usable.

That was true here.

A static site gave me things that a chat window did not:

- hierarchy
- quick scanning
- mobile usability
- stable sections
- linkable views
- a dedicated cheat sheet mode
- a place for the best insights to accumulate instead of evaporate

And because it was just HTML, I could keep changing it quickly without pretending I was building a platform.

That matters too.

The right interface for a workflow does not always have to be ambitious. It just has to be fit for purpose.

## This felt different from ordinary prompting

What made this feel like a step up was not the technology. It was the loop.

Instead of:

- ask AI
- read answer
- move on

it became:

- ask AI
- pressure-test the answer
- notice what is actually useful
- distill it
- place it into a real study surface
- improve that surface based on the next round

That is closer to product work than prompt work.

And honestly, that is where a lot of the value seems to live.

Not in accumulating generated text, but in shaping the environment where the good parts of that text can actually help you do something better.

## My takeaway

The lesson from this week was simple:

**AI got more useful the moment it stopped being the place where the work lived, and started helping me build the place where the work could be used.**

That is true for interview prep.

I think it is also true for a lot of other workflows that still get trapped in chat windows when they really want a purpose-built surface instead.
