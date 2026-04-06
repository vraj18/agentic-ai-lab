from tools import calculator, weather, summarize

def decide_tool(user_input):
    user_input = user_input.lower()

    if "calculate" in user_input:
        return "calculator"
    elif "weather" in user_input:
        return "weather"
    elif "summarize" in user_input:
        return "summarize"
    else:
        return "unknown"

def run_tool(tool, user_input):
    if tool == "calculator":
        expression = user_input.replace("calculate", "")
        return calculator(expression)

    elif tool == "weather":
        return weather()

    elif tool == "summarize":
        text = user_input.replace("summarize", "")
        return summarize(text)

    else:
        return "No suitable tool found"

def main():
    print("Tool-Based Agent")
    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        tool = decide_tool(user_input)
        result = run_tool(tool, user_input)

        print(result)

if __name__ == "__main__":
    main()