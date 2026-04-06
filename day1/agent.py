import datetime
import re


class InputHandler:
    def parse(self, raw_input: str) -> str:
        return raw_input.strip().lower()


class DecisionLogic:
    def decide(self, normalized_input: str) -> str:
        if normalized_input in {"exit", "quit", "bye"}:
            return "exit"
        if any(word in normalized_input for word in ["hello", "hi", "hey"]):
            return "greeting"
        if any(word in normalized_input for word in ["date", "today"]):
            return "date"
        if any(word in normalized_input for word in ["time"]):
            return "time"
        if any(word in normalized_input for word in ["calculate", "what is", "sum", "add", "subtract", "multiply", "divide", "average"]):
            return "calculate"
        return "unknown"


class ActionExecutor:
    def execute(self, action: str, raw_input: str) -> str:
        if action == "exit":
            return "Goodbye!"
        if action == "greeting":
            return "Hello! I am your simple rule-based agent. How can I help you today?"
        if action == "date":
            return f"Today's date is {datetime.date.today().isoformat()}"
        if action == "time":
            now = datetime.datetime.now().strftime('%H:%M:%S')
            return f"The current time is {now}"
        if action == "calculate":
            result = self._calculate(raw_input)
            return result
        return "Sorry, I did not understand that. Try a command like 'calculate 2 + 3', 'date', or 'hello'."

    def _calculate(self, raw_input: str) -> str:
        expression = self._extract_expression(raw_input)
        if not expression:
            return "I could not find a calculation to perform. Try 'calculate 2 + 3'."

        expression = expression.replace("x", "*").replace("X", "*")
        if not self._is_safe_expression(expression):
            return "That expression is not allowed. Please use only numbers and +, -, *, / operators."

        try:
            value = eval(expression, {"__builtins__": None}, {})
            return f"Result: {value}"
        except Exception:
            return "Failed to evaluate the expression. Please check the syntax."

    def _extract_expression(self, raw_input: str) -> str:
        match = re.search(r"calculate\s*(.*)", raw_input, re.IGNORECASE)
        if match:
            return match.group(1)
        match = re.search(r"what is\s*(.*)", raw_input, re.IGNORECASE)
        if match:
            return match.group(1)
        return raw_input

    def _is_safe_expression(self, expression: str) -> bool:
        allowed_chars = set("0123456789+-*/. ()")
        return all(char in allowed_chars for char in expression)


class RuleBasedAgent:
    def __init__(self):
        self.handler = InputHandler()
        self.decision = DecisionLogic()
        self.executor = ActionExecutor()

    def respond(self, user_input: str) -> str:
        normalized = self.handler.parse(user_input)
        action = self.decision.decide(normalized)
        return self.executor.execute(action, user_input)


def main():
    agent = RuleBasedAgent()
    print("Day 1 - Rule-Based Agent")
    print("Type a command, or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        response = agent.respond(user_input)
        print(f"Agent: {response}")
        if response == "Goodbye!":
            break


if __name__ == "__main__":
    main()
