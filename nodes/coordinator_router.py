from debate_state import DebateState

def coordinator_router(state: DebateState) -> str:
    if state["round"] > 8:
        return "judge"

    return "agent_a" if state["current_agent"] == "AgentA" else "agent_b"