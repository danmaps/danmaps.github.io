---
date: 2024-08-20
tags:
- programming
- python
- teamwork
- notebooks
title: Sharing Python Tools - Practical Solutions and Considerations
---

As a Python enthusiast, I've integrated automation into many of my daily GIS tasks over the past decade. However, I recognize that not everyone shares my passion for coding. At work, I'm always willing to answer questions and demonstrate programmatic solutions to everyday problems. But I also aim to avoid being preachy or condescending.

When I develop solutions that could benefit my team, I consider various methods for sharing them:

| Solution                             | Adoption Rate | Reason                                                    |
|--------------------------------------|---------------|-----------------------------------------------------------|
| **Jupyter Notebooks**                | Low           | People are generally reluctant to learn how to use them.  |
| **Python Script Geoprocessing Tools (ArcGIS Pro)** | High          | Team members are already familiar with these tools.       |
| **Python Scripts with UI (Tkinter)** | High          | Simple and easy to use, can be deployed with a .bat file. |
| **Streamlit Apps**                   | Low           | Cannot run them on their own, security concerns related to running them in the cloud.         |

Each of these solutions has its own pros and cons, but I have found ways to use each of them in different situations.

#### Important Constraints

| Constraint                          | Challenge                                              | Solution                                                              |
|-------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------|
| **Python Package Installation**     | Installing new Python packages is not easy.            | Constrain solutions to use only packages available by default in ArcGIS Pro. |
| **Running Python Code**             | Running Python code correctly can be difficult.        | Ensure solutions run within ArcGIS Pro or use simple deployment methods like .bat files. |
| **Jupyter Notebooks**               | Notebooks are difficult to use unless interested.      | Avoid using notebooks unless there is a strong push for their adoption. |
| **Hosting Web Apps**                | Not easy to host web apps on the intranet.             | Explore internal hosting options or justify the need for a dedicated server or cloud solution. |
| **External Python Code Execution**  | Cannot use `arcpy` outside of ArcGIS Pro (e.g., Streamlit). | Use alternatives like `geopandas` for geoprocessing and `folium` for mapping. |

#### Additional Suggestions

**Documentation and Training**
- Provide clear and concise documentation and training sessions.
- Create short tutorial videos to demonstrate tool usage effectively.

**User Feedback**
- Regularly solicit feedback to understand user pain points and improve tools.
- Incorporate user suggestions to enhance user-friendliness.

**Incremental Adoption**
- Start with small projects to demonstrate the value of automation.
- Gradually introduce more complex solutions as users become more comfortable.

**IT Collaboration**
- Work with the IT department to explore secure options for hosting web apps.
- Advocate for dedicated resources for automation and web app hosting.

**Hybrid Solutions**
- Use interfaces that users are familiar with and gradually introduce new ones with proper support.
- Consider hybrid solutions that combine simpler tasks automated within ArcGIS Pro with more complex external tools.

**Community Building**
- Foster a community of practice within the team for sharing scripts, tips, and tricks.
- Encourage collaboration and knowledge sharing to build a supportive learning environment.

By focusing on these areas, we can bridge the gap between technical and non-technical users, making Python-based automation more accessible and beneficial for everyone on the team.
