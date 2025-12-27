import time
from debate_state import DebateState
from utils import hash_text
from nodes.logger import log_event

def memory_node(state: DebateState) -> DebateState:
    argument_text = state["last_output"]
    argument_hash = hash_text(argument_text)

    for t in state["memory"]["turns"]:
        if t["hash"] == argument_hash:
            raise RuntimeError("Duplicate argument detected")

    state["memory"]["turns"].append({
        "round": state["round"],
        "agent": state["current_agent"],
        "text": argument_text,
        "hash": argument_hash,
        "timestamp": time.time()
    })

    state["memory"]["summary"] = f"Total arguments: {len(state['memory']['turns'])}"

    log_event({
        "event": "memory_update",
        "round": state["round"],
        "agent": state["current_agent"],
        "text": argument_text
    })

    state["round"] += 1
    state["current_agent"] = (
        "AgentB" if state["current_agent"] == "AgentA" else "AgentA"
    )

    return state
