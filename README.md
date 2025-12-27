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
├── assets/
├── tests/
├── pytest.ini
├── requirements.txt


## Setup Instructions

Prerequisites:
- Python 3.10+
- Git
- Ollama (local LLM runtime)

Steps:
1. Clone the repository
   git clone https://github.com/Adu-2115/Debate-DAG-LangGraph.git
   cd Debate-DAG-LangGraph

2. Install Ollama
   Download from: https://ollama.com/

3. Pull the LLM model
   ollama pull llama3

4. Start the Ollama server
   ollama serve
   (Keep this running in the background)

5. Install Python dependencies
   pip install -r requirements.txt

6. Run the debate system
   python run_debate.py

7. (Optional) Run tests
   pytest tests/
