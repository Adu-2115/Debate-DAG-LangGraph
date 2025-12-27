# Multi-Agent Debate DAG using LangGraph

This project implements a structured **multi-agent debate system** using **LangGraph**.
Two AI agents with distinct personas debate a topic over a fixed number of rounds,
with strict turn enforcement, memory tracking, duplication prevention, and an
LLM-powered judge that produces a summary and declares a winner.

The system uses a **local LLM via Ollama**, enabling offline, deterministic, and cost-free execution.

---

## Features

- LangGraph-based debate DAG
- Strict turn alternation between agents
- Persona-driven arguments (external prompt files)
- Agent-specific memory slicing
- Duplicate argument detection
- LLM-powered judge with explainable verdict
- CLI-based topic input
- Automated tests for control-flow rules

---

## Project Structure

```text
debate_dag/
├── run_debate.py
├── debate_state.py
├── utils.py
├── llm_client.py
├── nodes/
├── personas/
├── tests/
├── pytest.ini
├── requirements.txt


Setup Instructions

1. Install Ollama

Download and install from: https://ollama.com/
Pull the model:
  ollama pull llama3
Start the server:
  ollama serve

2. Install Python Dependencies

pip install -r requirements.txt

3. Run the Debate

python run_debate.py


Testing

Run automated tests with:
  pytest tests/
