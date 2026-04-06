import os

try:
    from .planner import Planner, ExecutionEngine
    from . import tools
except ImportError:
    from planner import Planner, ExecutionEngine
    import tools


class MultiStepAgent:
    def __init__(self):
        self.planner = Planner()
        self.engine = ExecutionEngine()

    def run(self, user_query: str) -> str:
        plan = self.planner.create_plan(user_query)
        execution = self.engine.run(user_query, plan)
        history = execution["history"]
        context = execution["context"]

        output_lines = ["Plan:"]
        for step in plan:
            output_lines.append(f"- {step}")

        output_lines.append("\nIntermediate outputs:")
        for item in history:
            output_lines.append(f"- {item.name}: {item.output}")

        final_output = context.get("summary") or context.get("average") or context.get("sum")
        output_lines.append("\nFinal result:")
        output_lines.append(str(final_output))
        return "\n".join(output_lines)


def main():
    print("Day 4 - Multi-Step Planning Agent")
    print("This agent decomposes complex commands and shows intermediate outputs.")
    print("Type 'exit' to quit.")

    agent = MultiStepAgent()
    while True:
        raw_input_value = input("You: ").strip()
        if not raw_input_value:
            continue
        if raw_input_value.lower() in {"exit", "quit", "bye"}:
            print("Agent: Goodbye!")
            break
        response = agent.run(raw_input_value)
        print(response)


if __name__ == "__main__":
    main()
