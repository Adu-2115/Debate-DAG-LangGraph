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


## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Ollama (for local LLM inference)

---

### 1. Clone the Repository

```bash
git clone https://github.com/Adu-2115/Debate-DAG-LangGraph.git
cd Debate-DAG-LangGraph

### 2. Install Ollama

Download and install Ollama from the official website:  
https://ollama.com/

After installation, pull the required model:

```bash
ollama pull llama3
ollama serve

### 3. Install Python Dependencies
pip install -r requirements.txt

### 4. Run the Debate
python run_debate.py
