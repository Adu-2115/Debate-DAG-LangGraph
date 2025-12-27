from debate_state import DebateState
from llm_client import call_ollama
from utils import get_agent_memory_slice, load_persona

def agent_a_node(state: DebateState) -> DebateState:
    if state["current_agent"] != "AgentA":
        raise RuntimeError("Turn violation")

    memory_slice = get_agent_memory_slice(state, "AgentA")
    persona = load_persona("personas/football_tactician.txt")

    prompt = f"""
{persona}

Debate topic:
{state['topic']}

Opponent arguments:
{[t['text'] for t in memory_slice]}
"""

    response = call_ollama(prompt, seed=42)
    state["last_output"] = response
    print(f"Agent A (Tactician): {response}")
    return state


def agent_b_node(state: DebateState) -> DebateState:
    if state["current_agent"] != "AgentB":
        raise RuntimeError("Turn violation")

    memory_slice = get_agent_memory_slice(state, "AgentB")
    persona = load_persona("personas/football_traditionalist.txt")

    prompt = f"""
{persona}

Debate topic:
{state['topic']}

Opponent arguments:
{[t['text'] for t in memory_slice]}
"""

    response = call_ollama(prompt, seed=42)
    state["last_output"] = response
    print(f"Agent B (Traditionalist): {response}")
    return state
