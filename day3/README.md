# Day 3 - LLM-Based AI Agent

## Objective
Use a language model to improve tool selection and decision-making.

## Implementation
- `llm_driver.py` defines `LLMDriver`:
  - Uses OpenAI if `OPENAI_API_KEY` is configured and the `openai` package is installed.
  - Otherwise falls back to a simulated LLM that still decides between tools.
- `tools.py` provides the same modular tools as Day 2.
- `agent.py` executes the selected tool and logs each request.
- `day3_agent.log` records input, selected tool, and output.

## Usage
From the repository root or the `day3` folder:
```bash
python day3/agent.py
```

Optional OpenAI usage:
- install `openai`
- set `OPENAI_API_KEY`

Example queries:
- `calculate 15 * 2`
- `weather forecast`
- `summarize This paragraph explains how the agent works.`
