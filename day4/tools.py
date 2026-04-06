import re
from typing import List


def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("No numbers provided for average calculation.")
    return sum(numbers) / len(numbers)


def summarize_text(text: str) -> str:
    sentences = re.split(r"(?<=[.!?])\\s+", text.strip())
    if not sentences or sentences == [""]:
        return "No text available to summarize."
    return "Summary: " + " ".join(sentences[:2])


def extract_numbers(text: str) -> List[float]:
    found = re.findall(r"[-+]?[0-9]*\.?[0-9]+", text)
    return [float(num) for num in found]
