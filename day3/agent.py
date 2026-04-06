from tools import calculator, weather, summarize
from llm import decide_tool_with_llm

def run_tool(tool, user_input):
    if tool == "calculator":
        return calculator(user_input.replace("calculate", ""))

    elif tool == "weather":
        return weather()

    elif tool == "summarize":
        return summarize(user_input.replace("summarize", ""))

    else:
        return "No tool selected"

def main():
    print("LLM-Based Agent")

    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        tool = decide_tool_with_llm(user_input)
        result = run_tool(tool, user_input)

        print(f"[LOG] Tool Used: {tool}")
        print(f"[LOG] Output: {result}")

if __name__ == "__main__":
    main()