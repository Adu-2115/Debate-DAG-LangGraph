from nodes.memory_node import memory_node
from debate_state import DebateState

def test_memory_updates():
    state: DebateState = {
        "topic": "football test",
        "round": 1,
        "current_agent": "AgentA",
        "memory": {"turns": [], "summary": ""},
        "last_output": "Test argument"
    }

    new_state = memory_node(state)

    assert len(new_state["memory"]["turns"]) == 1
    assert new_state["round"] == 2
