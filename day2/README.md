# Day 2 - Tool-Using AI Agent

## Objective
Extend the rule-based agent to use modular tools and decide which tool to call based on user input.

## Implementation
- `tools.py` includes:
  - `calculator(text)`: evaluates arithmetic expressions.
  - `weather(location)`: returns a mocked weather report.
  - `summarizer(text)`: generates a short summary from text.
- `agent.py` includes:
  - `InputHandler`: normalizes user input.
  - `ToolSelector`: chooses which tool to use based on keywords.
  - `ToolExecutor`: calls the selected tool and returns the result.

## Usage
Run from the `day2` folder:
```bash
python agent.py
```

Example inputs:
- `calculate 12 / 4`
- `what is 7 + 5`
- `weather today`
- `summarize This is a long text that needs a short summary.`
