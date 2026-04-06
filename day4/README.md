# Day 4 - Multi-Step Planning Agent

## Objective
Design an agent that can decompose a user request into sequential steps and show intermediate outputs.

## Implementation
- `tools.py`: helper functions for number extraction, average calculation, and summarization.
- `planner.py`: builds a plan from the user query and executes each step.
- `agent.py`: interactive interface that prints the plan, intermediate outputs, and final result.

## Supported Scenario
Example request:
- `Find the average of 5, 10, 15 and summarize the result`

The agent performs:
1. Extract numbers
2. Compute average
3. Generate summary

## Usage
From the `day4` folder:
```bash
python agent.py
```
