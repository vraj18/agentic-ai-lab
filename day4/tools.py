def extract_numbers(text):
    return [int(x) for x in text.split() if x.isdigit()]

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def summarize_result(avg):
    return f"The average is {avg}"