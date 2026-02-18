---
title: Demystifying Agent Jargon So You Can Actually Use This Stuff
date: 2026-02-17
tags:
  - AI
  - Agents
  - Workflow
---

<img src="/static/images/demystifying-agent-jargon-header.jpeg" alt="Demystifying agent jargon" style="width:100%; display:block; margin: 12px 0 18px 0; border-radius: 12px;" />

Lately I’ve felt myself getting a little lost in new AI jargon. Agents. Agent-first. Tools. Skills. Commands. Hooks. System prompts. Protect layers. None of these ideas are bad. Most of them are useful. But the vocabulary explosion is real, and it’s easy to feel like you’re behind if you can’t instantly map the words to something concrete. This post is my attempt to slow things down and rebuild a clean mental model. These concepts are completely LLM- and platform-agnostic. Not for research papers or hype decks. For real work.

## Most of the jargon points to the same few ideas
When you strip things down, almost everything in agent land boils down to three questions:
- What does the system know?
- What can it do?
- When is it allowed to act?

If you keep those questions in mind, the terminology starts to fall into place.

## Prompts and prompt libraries
A prompt library is just text you reuse. Instructions. Examples. Guidelines. Tone. That’s it. They are static. They do not act. They do not decide. They are closer to boilerplate than intelligence.

In GIS terms, this is a folder of snippets you paste into tickets or tools because you already know what good instructions look like. Useful. Necessary. But not autonomous.

## Agents are loops, not magic
An agent is not a personality or a chatbot. It’s a loop. Observe. Decide. Act. Repeat.

An agent can keep working without you typing the next sentence. That’s the defining feature. If it can’t do that, it’s not really an agent. It’s just a fancy prompt runner.

## Tools are the hands
Agent tools are the things that actually do work. They are callable functions with clear inputs and predictable outputs. No UI assumptions. No hidden state. Buffer a layer. Select features. Export a map. Run a script.

In modern agent systems there’s also a distinction between local tools and externally exposed tools. Standards like the Model Context Protocol (MCP) let you expose tools over a structured boundary with clear schemas and predictable inputs and outputs. MCP isn’t magic. It’s just a well-defined way for agents to call functions safely and discover what’s available without embedding everything in the prompt. This helps readers bridge from “tools exist” to “here’s how tools are actually surfaced in real systems.”

If an autonomous system did not exist, tools would still need to exist. That’s how you know they’re fundamental.

Tools do the work. Skills tell the agent how to use those tools well. A skill is a reusable capability definition, not just a single API call, and it may bundle multiple tools plus procedural instructions that help an agent decide when and how to apply them. This aligns with broader usage where skills are treated as composable capability bundles rather than synonyms for tools.

## Skills are behavior, not capability
This one gets overloaded fast. An agent skill is not a tool. It’s a bundle of behavior. Tone. Judgment style. Risk tolerance. Preferred depth. A QA skill behaves differently than a cartography skill, even if both have access to the same tools.

Think roles, not features.

## Commands are UX, not power
Slash commands feel important because they’re visible. They’re not. A command is just a human-friendly shortcut that says “do this now.” Behind the scenes, the agent still decides what tools to use and how cautious to be.

If a system could run unattended, it would not need slash commands at all. That’s the giveaway that commands are UX sugar.

## Hooks are how agents notice the world
Hooks answer the when question. When a layer is added. When a tool fails. When new data appears. On a schedule.

Hooks are what turn agents from chat participants into coworkers.

## MCP and predictable external interactions
In real deployments, agents don’t just have internal helpers. They interact with external systems too — databases, internal APIs, GIS servers, cloud services, and more. MCP standardizes how an agent calls these external capabilities, what inputs it expects, and what outputs it gets back.

This separation matters because it keeps:
- execution semantics deterministic
- large schemas out of token context
- authorization and credentials controlled outside the model

Define and separate that from skill logic and agent reasoning.

## The hierarchy matters more than the terms
The most important concept I’ve internalized is not another noun. It’s hierarchy.

Some instructions must never be overridden. Some rules exist to slow things down when risk appears. Some preferences shape behavior. Some requests are just requests.

A clean mental stack looks like this:
- System level
- Protect level
- Skill level
- Task or command level

Higher levels constrain lower ones. Never the other way around. This is how you stop autonomy from becoming chaos.

There can also be access semantics layered into tools. For example, some tools or endpoints return a payment required response (HTTP 402 or x402) to indicate that the action isn’t free or allowed by default. Agents need a clear way to interpret that, decide whether to proceed, and retry with authorization or an approved budget. That belongs at the layer that constrains tool use, not at the behavioral skill layer.

## How I’m actually learning this
Not by memorizing definitions. I’m learning by building vocabulary and playing with the tools at the same time. Every time I implement something, I ask:
- Is this knowledge, capability, or timing?
- Does this belong at the system level or the task level?
- Would this still exist if no human were watching?

The act of naming things correctly while using them is where understanding clicks.

## A final thought
This space is moving fast, and the jargon will keep changing. That’s fine. New labels will keep appearing — MCP, skills, payment semantics, hooks, sub-agents, supervisor agents. The underlying axis really stays the same: knowledge, capability, and control.

If you can clearly separate:
- what an agent knows
- what it can do
- when it is allowed to act

you’ll be able to adapt to whatever new labels show up next. When you train yourself to see through the names and focus on those axes, the vocabulary ceases to be noise. Vocabulary plus practice beats theory every time.
