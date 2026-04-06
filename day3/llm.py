def decide_tool_with_llm(user_input):
    user_input = user_input.lower()

    if "calculate" in user_input:
        return "calculator"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarize"
    else:
        return "unknown"