import re


def calculator(input_text: str) -> str:
    expression = _extract_calculation(input_text)
    if not expression:
        return "No calculation found. Try 'calculate 4 * 5'."

    expression = expression.replace("x", "*").replace("X", "*")
    if not _is_safe_expression(expression):
        return "Unsafe expression. Use only numbers and +, -, *, /, parentheses."

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"Calculation result: {result}"
    except Exception:
        return "Could not evaluate the expression. Please check the syntax."


def weather(location: str = "your city") -> str:
    return (
        f"Weather report for {location}:\n"
        "- Condition: Sunny with light clouds\n"
        "- Temperature: 25°C\n"
        "- Wind: 10 km/h east"
    )


def summarizer(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    if not sentences or sentences == [""]:
        return "Please provide text to summarize."

    if len(sentences) > 1:
        summary = sentences[0].strip()
        if len(sentences) > 1:
            summary = summary.rstrip('.') + '...'
        return "Summary: " + summary

    words = text.split()
    if len(words) <= 5:
        return "Summary: " + text
    limit = max(5, int(len(words) * 0.6))
    return "Summary: " + " ".join(words[:limit]) + "..."


def _extract_calculation(text: str) -> str:
    patterns = [r"calculate\s*(.*)", r"what is\s*(.*)", r"compute\s*(.*)"]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    return text.strip()


def _is_safe_expression(expr: str) -> bool:
    allowed_chars = set("0123456789+-*/. ()")
    return all(ch in allowed_chars for ch in expr)
