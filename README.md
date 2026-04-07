# Project
AI Personal Growth OS (Agent-Based System)
Business Problem
Today’s dynamic environment, people find it difficult to struggle with time management,
unproductive behaviours, including procrastination, and interview prep.
Most users have to manage different, disconnected, and manual tools, requiring them to switch between apps and make decisions.
Solution Options Create an AI-based platform that:
Comprehends the user
Identifies the user’s intent
Offers guidance on an individual level
With Agentic AI, the platform can assign roles to particular agents, such as:
Planning Agent
Habit Analysis Agent
Interview Preparation Agent
Solution Offered
We designed an AI Personal Growth OS that:
Accepts user input using a web interface
Employs a Smart Router Agent to classify user intent
Makes an automated call to the respective agent
Agents:
Planning Agent → Creates daily plans
Habit Agent → Monitors habits and presents solutions
Interview Agent → Creates and presents Q & A
Technology Stack
Python
Streamlit (UI)
LangChain (LLM Docs)
Ollama (local LLM runtime)
Local model: tinyllama / phi3
Local Execution
Step 1. Install Ollama
Download and install Ollama from: https://ollama.com
Step 2. Pull model
ollama pull tinyllama
Step 3. Start the server
ollama serve
Step 4. Install dependencies
pip install streamlit langchain langchain-ollama
Step 5. Launch the app
streamlit run app.py
Materials & Bibliography
Documentation for LangChain
Ollama web page
Course content (Agentic AI Training)
LLMs and Agents YouTube videos
Video
Include a demonstration video such as:
Instances of input
Agent selection
Generation of output
Snapshots
Present:
the User Interface
potential outputs
the routing of Agents
How to Organize and Align
Document with headings
Document with lists
Leave uniform blank spaces
Use Emojis for easier engagement
Challenges Faced & Their Resolution
Problem 1: Model is unresponsive
Reason: Ollama is not working
Fix: Used ollama serve
Problem 2: Device freezing
Reason: Heavy model (llama3 )
Fix: Changed to more lightweight models (tinyllama, phi3)
Problem 3: LangChain is throwing erros
Reason: Imports are outdated (LLMChain, PromptTemplate)
Fix: Used the llm.invoke() modern way
Problem 4: Agent selection is incorrect
Reason: Classification is weak

Fix: Implemented fallback logic based on keywords
