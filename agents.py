from langchain_ollama import OllamaLLM

# Load local model
llm = OllamaLLM(model="tinyllama")


# Common function
def call_llm(prompt):
    return llm.invoke(prompt)


# -------- Planner Agent --------
def planner_agent(user_input):
    prompt = f"""
    Create a simple daily plan for:
    {user_input}

    Include:
    - Tasks
    - Time
    - Priority
    """
    return call_llm(prompt)


# -------- Habit Agent --------
def habit_agent(user_input):
    prompt = f"""
    Analyze this habit problem:
    {user_input}

    Give:
    - Cause
    - Why it happens
    - 3 solutions
    """
    return call_llm(prompt)


# -------- Interview Agent --------
def interview_agent(user_input):
    prompt = f"""
    Act as an interviewer.

    Ask 2 interview questions for:
    {user_input}

    Also give sample answers.
    """
    return call_llm(prompt)


# -------- Router (IMPORTANT 🔥) --------
def smart_router(user_input):
    # Step 1: LLM classification
    prompt = f"""
    Classify the user input into one:
    planner, habit, interview

    Only return one word.

    Input: {user_input}
    """

    decision = call_llm(prompt).lower()

    # Step 2: fallback (important)
    if "plan" in user_input.lower():
        return planner_agent(user_input)

    elif "habit" in user_input.lower() or "delay" in user_input.lower():
        return habit_agent(user_input)

    elif "interview" in user_input.lower():
        return interview_agent(user_input)

    # Step 3: LLM decision
    elif "plan" in decision:
        return planner_agent(user_input)

    elif "habit" in decision:
        return habit_agent(user_input)

    elif "interview" in decision:
        return interview_agent(user_input)

    else:
        return "Sorry, I couldn't understand."