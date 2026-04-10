# TASKSENSE

## Business Problem

In today’s fast-paced environment, individuals struggle with:

* Time management
* Unproductive behaviors (e.g., procrastination)
* Interview preparation

Most users rely on multiple disconnected tools, leading to:

* Context switching
* Poor decision-making
* Lack of personalization

---

## Solution Overview

We propose an **AI-powered Personal Growth OS** that:

* Understands user input
* Identifies user intent
* Provides personalized guidance

Using **Agentic AI**, the system assigns tasks to specialized agents.

---

## Agent Architecture

### Smart Router Agent

* Classifies user intent
* Routes request to the appropriate agent
<img width="433" height="611" alt="Screenshot 2026-04-09 200210" src="https://github.com/user-attachments/assets/d6b02012-3f10-4744-8785-566685adbb2a" />

---

### Core Agents

#### Planning Agent

* Generates daily schedules
* Prioritizes tasks
* Helps with time management

#### Habit Analysis Agent

* Identifies unproductive habits
* Suggests improvements
* Provides actionable solutions

#### Interview Preparation Agent

* Generates interview questions
* Provides sample answers
* Helps in practice sessions

---

## Technology Stack

* Python
* Streamlit (User Interface)
* LangChain (LLM Integration)
* Ollama (Local LLM Runtime)
* Models: `tinyllama`, `phi3`

---

## Local Setup & Execution

### Install Ollama

Download from: https://ollama.com

---

### Pull Model

```bash
ollama pull tinyllama
```

---

### Start Ollama Server

```bash
ollama serve
```

---

### Install Dependencies

```bash
pip install streamlit langchain langchain-ollama
```

---

### Run Application

```bash
streamlit run app.py
```

---

## Features

* Intelligent intent detection
* Multi-agent workflow
* Fast local execution (no API needed)
* Personalized outputs
* Simple and interactive UI

---

## Snapshots (Add Screenshots Here)

Include:
<img width="950" height="879" alt="Screenshot 2026-04-09 223936" src="https://github.com/user-attachments/assets/d3b3eac5-32f1-4810-a812-822dec47eb27" />
<img width="934" height="841" alt="Screenshot 2026-04-09 224121" src="https://github.com/user-attachments/assets/81e84258-e4ca-4a11-9020-664e406fdce2" />

---

## Demo Video

Include a demo showing:

* User input scenarios
* Generated outputs
https://drive.google.com/drive/folders/15zR86o7XkR9MbKR_-P86P3AneffGJcfW

---

## Materials & References

* LangChain Documentation
* Ollama Official Website
* Agentic AI Course Content
* LLMs & Agents YouTube Tutorials

---

## Challenges & Solutions

### Problem 1: Model Not Responding

**Reason:** Ollama not running
**Solution:** Run

```bash
ollama serve
```

---

### Problem 2: System Freezing

**Reason:** Heavy model (e.g., llama3)
**Solution:** Use lightweight models (`tinyllama`, `phi3`)

---

### Problem 3: LangChain Errors

**Reason:** Deprecated imports (`LLMChain`, `PromptTemplate`)
**Solution:** Use modern method:

```python
llm.invoke()
```

---

## Future Improvements

* Add user progress tracking dashboard
* Improve intent classification (ML-based)
* Add memory (vector database)
* Mobile-friendly UI

---

## Conclusion

The **AI Personal Growth OS** demonstrates how Agentic AI can:

* Simplify decision-making
* Improve productivity
* Provide personalized guidance

 A powerful step toward intelligent personal assistants 
