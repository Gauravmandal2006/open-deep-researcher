#  Open Deep Research Agent

An **Agentic AI-powered Research Automation System**  


---

##  Project Overview

**Open Deep Research Agent** is an intelligent research assistant that automates **topic-based** and **paper-based** research using a **multi-agent AI architecture**.

The system accepts:
- Any **research topic**, or  
- Any **academic paper / URL**

and generates:
-  **Concise summaries**
-  **Detailed, structured research reports**

This project demonstrates the **practical application of Agentic AI concepts** in real-world research automation.

---

## Objective

- Automate manual research workflows  
- Convert unstructured inputs into structured knowledge  
- Apply **multi-agent coordination** for intelligent decision-making  
- Build a scalable AI system with a clean UI

---

## Problem Statement

Manual research is often:
- Time-consuming  
- Unstructured  
- Difficult to scale  

Researchers and students spend excessive time collecting, organizing, and summarizing information.

### Solution
This project solves the problem by using **specialized AI agents**, where each agent handles a specific responsibility such as planning, searching, and writing.

---

## Software & Hardware Dependencies

###  Software Dependencies
- **Python** 3.9+
- **Streamlit** (UI Framework)
- **OpenAI / OpenRouter API** (LLM)
- **Tavily API** (Web Search)
- **dotenv** (Environment variables)
- **JSON** (Memory & history storage)

### Hardware Dependencies
- Minimum **4 GB RAM**
- No GPU required
- Stable internet connection

---

## System Architecture

<img width="632" height="620" alt="TASK_3_System_architecture" src="https://github.com/user-attachments/assets/e806e71a-b181-4829-903e-5039cd9c7a9d" />

## Workflow Explanation

1. User enters a **topic or research paper URL**
2. Planner Agent identifies:
   - Input type (topic / paper)
   - Research structure
3. Searcher Agent gathers relevant information from the web
4. Writer Agent:
   - Summarizes OR
   - Generates a detailed research report
5. Output is displayed in the UI and saved for future reference

---

##  Agent Roles

###  Planner Agent
- Determines research intent
- Designs the structure of the report
- Coordinates agent flow

###  Searcher Agent
- Fetches relevant web content
- Uses Tavily API for real-time search
- Filters noisy data

### Writer Agent
- Generates human-readable content
- Produces structured, academic-style output
- Ensures clarity and correctness

## Output Types

The system can generate:

Short summaries

Detailed research reports

Paper summaries from URLs

Structured academic-style content

Clean readable explanations


### 2. Sample Screenshots

 ### Dashboard
 
<img width="1919" height="883" alt="image" src="https://github.com/user-attachments/assets/1320472c-29e1-418a-8cdb-5b6991f71d51" />

### Generated Academic Report

<img width="1905" height="867" alt="image" src="https://github.com/user-attachments/assets/f2e25c64-7b6f-4ef7-8a80-c606a0279971" />

### Academic Papers
<img width="1918" height="843" alt="image" src="https://github.com/user-attachments/assets/c1e7486f-a452-4002-b2d8-da1fcdd44024" />
<img width="1913" height="694" alt="image" src="https://github.com/user-attachments/assets/6791bad5-0d66-4abe-97c9-bc9269b6b6b1" />
<img width="1566" height="321" alt="image" src="https://github.com/user-attachments/assets/85035866-d16e-4143-be44-16e20d2a7fca" />

## Limitations

- Depends on third-party APIs
- Very large topics may be token-limited
- Offline usage not supported
- Citation accuracy depends on source quality


##  Future Enhancements

- PDF / DOCX export
- Dark / Light mode toggle
- Multi-chat thread support (ChatGPT-style)
- Database-backed memory (MongoDB)
- Automatic citation formatting (APA / IEEE)
- User authentication

##  Conclusion
Open Deep Researcher successfully demonstrates how AI agents can automate and simplify the research process.
By combining planning, searching, and writing agents, the system is able to understand user queries, fetch relevant information, and generate meaningful summaries or detailed reports.

This project helped in:

Understanding agent-based AI architecture

Applying LLMs in real-world research tasks

Building an end-to-end AI-powered web application

Improving problem-solving and practical AI development skills

Overall, this project proves that AI can be effectively used to save time, reduce manual effort, and enhance research productivity, making it highly useful for students, researchers, and professionals.

## Live Project Deployment

🔗 **Streamlit App:**  
https://ankitkumar72767-open-deep-researcher-app-zyg9xh.streamlit.app/

---

## Local Setup Instructions

```bash
git clone https://github.com/ankitkumar72767/open-deep-researcher.git
cd open-deep-researcher

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
Developer Details
Ankit Kumar
B.Tech – Computer Science (AI & ML)


