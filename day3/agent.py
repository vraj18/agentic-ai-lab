import os
from datetime import datetime

try:
    from . import llm_driver
    from . import tools
except ImportError:
    import llm_driver
    import tools


class AgentLogger:
    def __init__(self, log_file: str = "day3_agent.log"):
        self.log_file = log_file

    def log(self, user_input: str, tool_name: str, output: str) -> None:
        timestamp = datetime.now().isoformat()
        with open(self.log_file, "a", encoding="utf-8") as handle:
            handle.write(f"[{timestamp}] INPUT: {user_input} | TOOL: {tool_name} | OUTPUT: {output}\n")


class LLMToolAgent:
    def __init__(self):
        self.driver = llm_driver.LLMDriver()
        self.logger = AgentLogger(log_file=os.path.join(os.path.dirname(__file__), "day3_agent.log"))

    def respond(self, user_input: str) -> str:
        tool_name = self.driver.choose_tool(user_input)
        tool_output = self._execute_tool(tool_name, user_input)
        final_output = self.driver.generate_response(user_input, tool_name, tool_output)
        self.logger.log(user_input, tool_name, final_output)
        return final_output

    def _execute_tool(self, tool_name: str, user_input: str) -> str:
        if tool_name == "calculator":
            return tools.calculator(user_input)
        if tool_name == "weather":
            return tools.weather()
        if tool_name == "summarizer":
            return tools.summarizer(user_input)
        return (
            "I could not select a tool for your request. "
            "Try asking for a calculation, weather report, or a summary."
        )


def main():
    print("Day 3 - LLM-Based Agent")
    print("This agent uses an LLM agent driver to choose the correct tool.")
    print("Type 'exit' to quit.")

    agent = LLMToolAgent()
    while True:
        text = input("You: ").strip()
        if not text:
            continue
        if text.lower() in {"exit", "quit", "bye"}:
            print("Agent: Goodbye!")
            break
        answer = agent.respond(text)
        print(f"Agent: {answer}")


if __name__ == "__main__":
    main()
