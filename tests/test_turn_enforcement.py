import pytest
from nodes.agent_nodes import agent_a_node
from debate_state import DebateState

def test_agent_a_out_of_turn():
    state: DebateState = {
        "topic": "football test",
        "round": 2,
        "current_agent": "AgentB",
        "memory": {"turns": [], "summary": ""},
        "last_output": ""
    }

    with pytest.raises(RuntimeError):
        agent_a_node(state)