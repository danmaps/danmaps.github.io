---
date: 2024-09-09
tags:
- ai
- arcgis
- gis

title: AI enhanced GP tools in ArcGIS Pro
---

One of the biggest challenges with AI in the GIS world right now is its lack of situational awareness and the inability to provide actionable results without heavy user intervention.

Tools like Copilot are so promising, but they're blind to the specific environment the users operates in. Users have to do the heavy lifting, supplying all the context and guidance needed. It's like asking someone for help, and they respond with, "Sure, but you'll have to tell me where everything is first."

To help tackle this, I've been working on a set of "AI Assistant" geoprocessing tools for ArcGIS Pro. The main innovation here is attepmpting to feed the AI the necessary context through system prompts. I used python to bridge the gap between ArcGIS Pro and OpenAI's API.

One interesting technical note is that I avoided using the OpenAI python package in favor of directly interfacing with the API using the `requests` library. This avoids dependency on the OpenAI package and makes it easier for anyone to use these tools without cloning the default python environment.

The next step is to make this integration smarter—having the AI inspect the environment before and after actions, evaluate outcomes, and then make recommendations based on those evaluations. By doing so, the tool becomes more than just a code generator; it becomes an intelligent partner in decision-making.

This approach removes barriers like poor UI and lack of context, helping to bridge the gap between AI's limitations and what's truly needed in GIS. My end goal is to create a seamless, intuitive AI-GIS integration that enhances both user experience and productivity.

![AI Tools](/beta/static/images/ai_tools.jpg)

These tools, powered by the OpenAI API, are built to integrate smoothly with ArcGIS Pro. The results? Sometimes they're surprisingly spot-on, and other times they're hilariously off-base. Here's a taste of what the `Generate AI Python Code` tool came up with.

![Florida Code](/beta/static/images/florida_code.jpg)
![Florida Map](/beta/static/images/florida_map.jpg)
