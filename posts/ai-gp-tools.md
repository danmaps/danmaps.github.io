---
date: 2024-09-09
tags:
- AI
- ArcGIS Pro
- Geoprocessing

title: AI enhanced GP tools in ArcGIS Pro
---

From my perspective, the current challenge with AI in the GIS workplace is its lack of contextual awareness and actionable capabilities.

AI tools like Copilot are generic and unable to see or understand the specific environment they're operating in.

To address this, I've developed an "AI Assistant" tool in ArcGIS Pro, which feeds the AI context through system prompts and enables it
to perform actions by executing the generated code within the software.

Looking ahead, I aim to enhance this integration by allowing the AI to inspect
the current state of the environment before and after actions are performed, 
allowing it to evaluate the results, and make recommendations based on these evaluations.

This approach removes friction caused by ignorance, skepticism, and bad UI, ultimately bridging the gap between AI limitations and practical applications in GIS. My goal is to create a seamless and efficient AI-GIS integration that improves user experience and workflow efficiency.

![AI Tools](..\static\images\ai_tools.jpg)

These tools are designed to work in conjunction with ArcGIS Pro and rely on the OpenAI API. The results can be equal parts funny and terrible.

![Florida Code](..\static\images\florida_code.jpg)
![Florida Map](..\static\images\florida_map.jpg)