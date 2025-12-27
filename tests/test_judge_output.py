from nodes.judge_node import judge_node
from debate_state import DebateState

def test_judge_produces_output():
    state: DebateState = {
        "topic": "football test",
        "round": 9,
        "current_agent": "AgentA",
        "memory": {
            "turns": [
                {"round": 1, "agent": "AgentA", "text": "A1"},
                {"round": 2, "agent": "AgentB", "text": "B1"}
            ],
            "summary": ""
        },
        "last_output": ""
    }

    new_state = judge_node(state)
    assert isinstance(new_state["last_output"], str)
    assert len(new_state["last_output"]) > 0
