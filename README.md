# Open Deep Research Agent

An Agentic AI-Powered Research Automation System

---

## Project Overview

Open Deep Research Agent is an intelligent research assistant that automates topic-based and paper-based research using a multi-agent AI architecture.

The system accepts:

* Any research topic
* Any academic paper or URL

and generates:

* Concise summaries
* Detailed structured research reports
* Research insights
* Academic-style content

This project demonstrates the practical application of Agentic AI concepts in real-world research automation.

---

## Objective

* Automate manual research workflows
* Convert unstructured inputs into structured knowledge
* Apply multi-agent coordination for intelligent decision-making
* Build a scalable AI system with a clean user interface

---

## Problem Statement

Manual research is often:

* Time-consuming
* Unstructured
* Difficult to scale

Researchers and students spend excessive time collecting, organizing, and summarizing information from multiple sources.

---

## Solution

This project solves the problem by using specialized AI agents where each agent performs a specific responsibility such as planning, searching, and report generation.

---

## Software & Hardware Dependencies

### Software Dependencies

* Python 3.9+
* Streamlit
* Gemini API
* Tavily Search API
* LangChain
* LangGraph
* Python-dotenv
* PyPDF
* Pillow
* JSON

### Hardware Dependencies

* Minimum 4 GB RAM
* No GPU required
* Stable Internet Connection

---

## System Architecture

---

## Workflow Explanation

1. User enters a research topic.
2. User may optionally upload:

   * PDF documents
   * Images
3. Planner Agent creates a research plan.
4. Searcher Agent gathers information using Tavily Search.
5. Writer Agent generates structured reports.
6. Final report is displayed and stored in history.

---

## Agent Roles

### Planner Agent

* Determines research intent
* Creates research strategy
* Coordinates workflow

### Searcher Agent

* Searches relevant web content
* Retrieves research sources
* Filters irrelevant information

### Writer Agent

* Generates research reports
* Produces summaries
* Creates structured academic-style content

---

## Current Features

### Research Features

* General Web Research
* Academic Research
* Multi-Agent Workflow
* Research History
* Chat-Based Interface

### Document Processing

* PDF Upload
* PDF Text Extraction
* PDF Context Integration

### Image Processing

* Image Upload
* Image Understanding
* Research Context Enhancement

### AI Capabilities

* Gemini AI Integration
* Tavily Search Integration
* LangGraph Workflow
* LangChain Agents

---

## Output Types

The system can generate:

* Short Summaries
* Detailed Research Reports
* Academic Content
* Structured Explanations
* Research Insights

---

## Sample Screenshots

### Dashboard

### Generated Academic Report

### Academic Papers

---

## Limitations

* Depends on third-party APIs
* Large topics may be token-limited
* Offline mode not supported
* Citation quality depends on source quality

---

## Future Enhancements

* PDF Export
* DOCX Export
* Citation Generation (APA, IEEE, MLA)
* Knowledge Graph Visualization
* RAG-Based PDF Chat
* Semantic Scholar Integration
* ArXiv Integration
* User Authentication
* Research Quality Scoring

---

## Conclusion

Open Deep Research Agent demonstrates how AI agents can automate and simplify research workflows.

By combining planning, searching, and writing agents, the system can understand user queries, collect relevant information, and generate meaningful reports with minimal manual effort.

This project helped in:

* Understanding Agentic AI Architecture
* Applying LLMs in Real-World Applications
* Building End-to-End AI Systems
* Developing Practical AI Engineering Skills

---

## Live Project Deployment

Streamlit App:

https://ankitkumar72767-open-deep-researcher-app-zyg9xh.streamlit.app/

---

## Local Setup Instructions

```bash
git clone https://github.com/Gauravmandal2006/open-deep-researcher.git
cd open-deep-researcher

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

## Original Developer

Ankit Kumar
B.Tech – Computer Science (AI & ML)

GitHub: https://github.com/ankitkumar72767

Original Repository: https://github.com/ankitkumar72767/open-deep-researcher

---

## Customized & Enhanced By

Gaurav Mandal
B.Tech – Computer Science & Engineering (CSE)
Guru Ghasidas Vishwavidyalaya (GGV)

GitHub: https://github.com/Gauravmandal2006

### Contributions of Ankit Kumar and Gaurav Mandal

* PDF Upload & Analysis
* Image Upload & Understanding
* Gemini AI Integration
* Streamlit UI Enhancements
* Multi-Agent Workflow Improvements
* Testing and Deployment

---

## Project Maintainer

This repository is currently maintained and enhanced by Gaurav Mandal.

---

## Acknowledgement

This project is based on the original Open Deep Research Agent developed by Ankit Kumar (https://github.com/ankitkumar72767/open-deep-researcher) and has been further customized and enhanced with additional features and improvements.




