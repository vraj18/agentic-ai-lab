from datetime import datetime

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Error in calculation"

def weather(city="Mumbai"):
    return f"Weather in {city}: Sunny (mock data)"

def summarize(text):
    return text[:50] + "..." if len(text) > 50 else text