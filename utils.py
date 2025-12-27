import hashlib
from typing import List
from debate_state import DebateState


def hash_text(text: str) -> str:
    return hashlib.sha256(text.lower().strip().encode()).hexdigest()


def get_agent_memory_slice(state: DebateState, agent: str):
    """
    Returns only opponent arguments for the given agent.
    """
    return [
        t for t in state["memory"]["turns"]
        if t["agent"] != agent
    ]


def load_persona(path: str) -> str:
    """
    Loads persona prompt from a text file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()