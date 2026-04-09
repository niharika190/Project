# 🚀 AI Personal Growth OS (Agent-Based System)

---

## 📌 Business Problem

In today’s fast-paced world, individuals struggle with:

- ⏰ Time management  
- 📉 Unproductive behaviors (e.g., procrastination)  
- 🎯 Interview preparation  

Most users rely on **multiple disconnected tools**, forcing them to:
- Switch between apps  
- Make manual decisions  
- Lose efficiency and focus  

---

## 💡 Proposed Solution

An **AI-powered personal growth platform** that:

- 🧠 Understands user behavior  
- 🎯 Identifies user intent  
- 📊 Provides personalized guidance  

Using **Agentic AI**, the system assigns specialized roles:

- 🗓️ Planning Agent  
- 📈 Habit Analysis Agent  
- 🎤 Interview Preparation Agent  

---

## ⚙️ Solution Implemented

We developed an **AI Personal Growth OS** with:

- 🌐 Web-based user interface  
- 🧠 Smart Router Agent for intent classification  
- 🔄 Automatic routing to relevant agents  

### 🤖 Agents

- **Planning Agent** → Generates daily schedules  
- **Habit Agent** → Tracks habits & suggests improvements  
- **Interview Agent** → Generates Q&A for preparation  

---

## 🧰 Tech Stack

- 🐍 Python  
- 🎨 Streamlit (UI)  
- 🔗 LangChain (LLM orchestration)  
- 🧠 Ollama (local LLM runtime)  

### 🧠 Models Used

- `tinyllama`  
- `phi3`  

---

## 🖥️ Local Setup & Execution

### Step 1: Install Ollama  
Download from 👉 https://ollama.com  

### Step 2: Pull Model  
```bash
ollama pull tinyllama
