# Day 1 - Rule-Based AI Agent

## Objective
Build a simple AI agent that uses rule-based logic to interpret user commands and perform actions.

## Implementation
- `agent.py` contains:
  - `InputHandler`: normalizes and preprocesses user text.
  - `DecisionLogic`: matches keywords to determine intent.
  - `ActionExecutor`: performs actions like greeting, returning the current date/time, and evaluating simple calculations.
  - `RuleBasedAgent`: connects the pipeline `Input -> Decision -> Action`.

## Usage
Run the agent from the `day1` folder:
```bash
python agent.py
```

Supported commands:
- `hello`, `hi`, `hey`
- `date`
- `time`
- `calculate 2 + 3`
- `what is 10 / 2`
- `exit`
