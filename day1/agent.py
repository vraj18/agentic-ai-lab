from datetime import datetime

def get_intent(user_input):
    user_input = user_input.lower()

    if "calculate" in user_input:
        return "calculate"
    elif "date" in user_input:
        return "date"
    elif "hello" in user_input or "hi" in user_input:
        return "greeting"
    else:
        return "unknown"

def execute_action(intent, user_input):
    if intent == "calculate":
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            return f"Result: {result}"
        except:
            return "Invalid calculation."

    elif intent == "date":
        return str(datetime.now())

    elif intent == "greeting":
        return "Hello! How can I help you?"

    else:
        return "Sorry, I don't understand."

def main():
    print("Rule-Based Agent (type 'exit' to quit)")
    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        intent = get_intent(user_input)
        response = execute_action(intent, user_input)

        print(response)

if __name__ == "__main__":
    main()