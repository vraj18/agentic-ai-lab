try:
    from . import tools
except ImportError:
    import tools


class InputHandler:
    def normalize(self, raw_input: str) -> str:
        return raw_input.strip().lower()


import re


def _contains_keyword(text: str, keywords: list[str]) -> bool:
    for word in keywords:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            return True
    return False


class ToolSelector:
    def choose(self, normalized_input: str) -> str:
        if _contains_keyword(normalized_input, ["calculate", "what is", "compute", "sum", "add", "subtract"]):
            return "calculator"
        if _contains_keyword(normalized_input, ["weather", "forecast", "temperature"]):
            return "weather"
        if _contains_keyword(normalized_input, ["summarize", "summary", "summariser"]):
            return "summarizer"
        return "unknown"


class ToolExecutor:
    def execute(self, tool_name: str, raw_input: str) -> str:
        if tool_name == "calculator":
            return tools.calculator(raw_input)
        if tool_name == "weather":
            return tools.weather()
        if tool_name == "summarizer":
            return tools.summarizer(raw_input)
        return "I could not choose a tool for your request. Try calculator, weather, or summarizer."


class ToolUsingAgent:
    def __init__(self):
        self.handler = InputHandler()
        self.selector = ToolSelector()
        self.executor = ToolExecutor()

    def respond(self, user_input: str) -> str:
        normalized = self.handler.normalize(user_input)
        tool = self.selector.choose(normalized)
        return self.executor.execute(tool, user_input)


def main():
    agent = ToolUsingAgent()
    print("Day 2 - Tool-Using Agent")
    print("Enter a request, or type 'exit' to stop.")
    while True:
        raw_input_value = input("You: ").strip()
        if not raw_input_value:
            continue
        if raw_input_value.lower() in {"exit", "quit", "bye"}:
            print("Agent: Goodbye!")
            break
        response = agent.respond(raw_input_value)
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()
