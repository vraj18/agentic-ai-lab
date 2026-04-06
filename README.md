# Agentic AI Lab

This repository contains a complete student lab implementation for `Software Lab: Introduction to Agentic AI Systems`.

## Structure
- `day1/` - Rule-based AI agent
- `day2/` - Tool-using agent with modular tools
- `day3/` - LLM-based agent that selects tools and logs decisions
- `day4/` - Multi-step planning agent with task decomposition

## How to run
From the repository root, run the desired assignment:

```bash
python day1/agent.py
python day2/agent.py
python day3/agent.py
python day4/agent.py
```

## Notes
- `day3` can use an actual OpenAI model if `openai` is installed and `OPENAI_API_KEY` is set.
- Otherwise, `day3` falls back to a simulated LLM decision driver.

## Assignment coverage
- Day 1: Rule-based intent detection and action execution
- Day 2: Tool abstraction and tool selection
- Day 3: LLM-driven decision-making with logging
- Day 4: Multi-step planning, intermediate outputs, and sequential execution
