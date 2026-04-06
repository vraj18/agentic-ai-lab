from typing import Any, Dict, List

try:
    from . import tools
except ImportError:
    import tools


class StepResult:
    def __init__(self, name: str, output: Any):
        self.name = name
        self.output = output

    def __repr__(self) -> str:
        return f"{self.name}: {self.output}"


class Planner:
    def create_plan(self, query: str) -> List[str]:
        normalized = query.lower()
        steps = []
        numbers = tools.extract_numbers(query)

        if "average" in normalized and numbers:
            steps.append("extract_numbers")
            steps.append("compute_average")
        elif numbers and any(word in normalized for word in ["sum", "total"]):
            steps.append("extract_numbers")
            steps.append("compute_sum")

        if any(word in normalized for word in ["summarize", "summary", "summarise"]):
            steps.append("summarize")

        if not steps:
            steps.append("fallback")

        return steps


class ExecutionEngine:
    def run(self, query: str, plan: List[str]) -> Dict[str, Any]:
        context = {"query": query, "numbers": [], "average": None, "sum": None, "summary": None}
        history: List[StepResult] = []

        for step in plan:
            if step == "extract_numbers":
                context["numbers"] = tools.extract_numbers(query)
                history.append(StepResult("extract_numbers", context["numbers"]))
            elif step == "compute_average":
                context["average"] = tools.calculate_average(context["numbers"])
                history.append(StepResult("compute_average", context["average"]))
            elif step == "compute_sum":
                context["sum"] = sum(context["numbers"])
                history.append(StepResult("compute_sum", context["sum"]))
            elif step == "summarize":
                target_text = self._build_summary_text(context)
                context["summary"] = tools.summarize_text(target_text)
                history.append(StepResult("summarize", context["summary"]))
            else:
                context["summary"] = (
                    "I could not identify a multi-step plan for this request. "
                    "Try asking for an average or a summary."
                )
                history.append(StepResult("fallback", context["summary"]))

        return {"context": context, "history": history}

    def _build_summary_text(self, context: Dict[str, Any]) -> str:
        if context.get("average") is not None:
            return f"The average is {context['average']}."
        if context.get("sum") is not None:
            return f"The sum is {context['sum']}."
        return context.get("query", "")
