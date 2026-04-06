import re


def calculator(input_text: str) -> str:
    expression = _extract_calculation(input_text)
    if not expression:
        return "No valid calculation identified. Use 'calculate 5 + 3'."

    expression = expression.replace("x", "*").replace("X", "*")
    if not _is_safe_expression(expression):
        return "Unsafe expression. Use only digits and +, -, *, /, parentheses."

    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"Tool output -> {result}"
    except Exception:
        return "Failed to evaluate the expression. Please try a simpler arithmetic statement."


def weather(location: str = "your location") -> str:
    return (
        f"Weather tool output for {location}:\n"
        "- Condition: Light breeze and partly sunny\n"
        "- Temperature: 24°C\n"
        "- Humidity: 55%\n"
        "- Note: This is a mocked weather report."
    )


def summarizer(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    if not sentences or sentences == [""]:
        return "No text found to summarize."

    if len(sentences) > 1:
        summary = sentences[0].strip()
        if len(sentences) > 1:
            summary = summary.rstrip('.') + '...'
        return "Summary tool output -> " + summary

    words = text.split()
    if len(words) <= 5:
        return "Summary tool output -> " + text
    limit = max(5, int(len(words) * 0.6))
    return "Summary tool output -> " + " ".join(words[:limit]) + "..."


def _extract_calculation(text: str) -> str:
    patterns = [r"calculate\s*(.*)", r"what is\s*(.*)", r"compute\s*(.*)"]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    return text.strip()


def _is_safe_expression(expr: str) -> bool:
    allowed = set("0123456789+-*/. ()")
    return all(ch in allowed for ch in expr)
