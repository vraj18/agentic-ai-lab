import os
import re

try:
    import openai
except ImportError:
    openai = None


class LLMDriver:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if openai and self.api_key:
            openai.api_key = self.api_key

    def choose_tool(self, user_input: str) -> str:
        if self._can_use_openai():
            return self._choose_tool_with_openai(user_input)
        return self._mock_choose_tool(user_input)

    def _can_use_openai(self) -> bool:
        return openai is not None and bool(self.api_key)

    def _choose_tool_with_openai(self, user_input: str) -> str:
        prompt = (
            "You are a tool-selection assistant. Choose one of: calculator, weather, summarizer, or unknown. "
            "Only return the tool name.\n"
            f"User request: {user_input}\n"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt}],
                temperature=0,
                max_tokens=10,
            )
            text = response.choices[0].message.content.strip().lower()
            tool = self._extract_tool_name(text)
            if tool == "unknown":
                return self._mock_choose_tool(user_input)
            return tool
        except Exception:
            return self._mock_choose_tool(user_input)

    def generate_response(self, user_input: str, tool_name: str, tool_output: str) -> str:
        if not self._can_use_openai():
            return tool_output

        prompt = (
            "You are a helpful assistant. The user asked: \"" + user_input + "\". "
            "The chosen tool is: " + tool_name + ".\n"
            "The tool output is:\n" + tool_output + "\n"
            "Respond to the user with a concise, friendly answer that includes the tool result."
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You create a natural final answer based on tool output."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
                max_tokens=150,
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return tool_output

    def _contains_keyword(self, text: str, keywords: list[str]) -> bool:
        for word in keywords:
            if re.search(r"\b" + re.escape(word) + r"\b", text):
                return True
        return False

    def _mock_choose_tool(self, user_input: str) -> str:
        text = user_input.lower()
        if self._contains_keyword(text, ["calculate", "what is", "compute", "sum", "add", "subtract", "multiply", "divide"]):
            return "calculator"
        if self._contains_keyword(text, ["weather", "forecast", "temperature"]):
            return "weather"
        if self._contains_keyword(text, ["summarize", "summary", "summariser"]):
            return "summarizer"
        return "unknown"

    def _extract_tool_name(self, text: str) -> str:
        match = re.search(r"calculator|weather|summarizer|unknown", text)
        return match.group(0) if match else "unknown"
