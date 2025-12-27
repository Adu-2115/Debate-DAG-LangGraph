from langgraph.graph import StateGraph, END

from debate_state import DebateState

# Import nodes
from nodes.user_input_node import user_input_node
from nodes.agent_nodes import agent_a_node, agent_b_node
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node
from nodes.coordinator_router import coordinator_router


# -------------------------
# Build LangGraph DAG
# -------------------------
def build_graph():
    graph = StateGraph(DebateState)

    # Register nodes
    graph.add_node("user_input", user_input_node)
    graph.add_node("agent_a", agent_a_node)
    graph.add_node("agent_b", agent_b_node)
    graph.add_node("memory", memory_node)
    graph.add_node("judge", judge_node)

    # Entry point
    graph.set_entry_point("user_input")

    # Routing from user input
    graph.add_conditional_edges(
        "user_input",
        coordinator_router,
        {
            "agent_a": "agent_a",
            "agent_b": "agent_b",
            "judge": "judge",
        },
    )

    # Routing after each memory update
    graph.add_conditional_edges(
        "memory",
        coordinator_router,
        {
            "agent_a": "agent_a",
            "agent_b": "agent_b",
            "judge": "judge",
        },
    )

    # Linear edges
    graph.add_edge("agent_a", "memory")
    graph.add_edge("agent_b", "memory")
    graph.add_edge("judge", END)

    return graph.compile()


# -------------------------
# Run Debate
# -------------------------
if __name__ == "__main__":
    app = build_graph()

    # Initial empty state
    initial_state: DebateState = {
        "topic": "",
        "round": 0,
        "current_agent": "",
        "memory": {},
        "last_output": "",
    }

    app.invoke(initial_state)
    print("\nExecution finished.")