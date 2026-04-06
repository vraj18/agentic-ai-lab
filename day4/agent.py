from tools import extract_numbers, compute_average, summarize_result

def plan_steps(user_input):
    return ["extract", "average", "summarize"]

def execute_plan(user_input):
    print("[Step 1] Extracting numbers...")
    numbers = extract_numbers(user_input)
    print("Numbers:", numbers)

    print("[Step 2] Computing average...")
    avg = compute_average(numbers)
    print("Average:", avg)

    print("[Step 3] Summarizing...")
    summary = summarize_result(avg)
    return summary

def main():
    print("Multi-Step Agent")

    while True:
        user_input = input(">> ")

        if user_input == "exit":
            break

        steps = plan_steps(user_input)
        result = execute_plan(user_input)

        print("Final Output:", result)

if __name__ == "__main__":
    main()