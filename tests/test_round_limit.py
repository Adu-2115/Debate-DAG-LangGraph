from nodes.coordinator_router import coordinator_router
from debate_state import DebateState

def test_round_limit_goes_to_judge():
    state: DebateState = {
        "topic": "football test",
        "round": 9,
        "current_agent": "AgentA",
        "memory": {"turns": [], "summary": ""},
        "last_output": ""
    }

    next_node = coordinator_router(state)
    assert next_node == "judge"