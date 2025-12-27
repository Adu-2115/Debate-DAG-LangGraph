from debate_state import DebateState

def user_input_node(state: DebateState) -> DebateState:
    print("UserInputNode reached")

    topic = input("Enter debate topic: ").strip()

    if len(topic) < 10:
        raise ValueError("Topic too short")

    FOOTBALL_KEYWORDS = [
        "football", "soccer", "player", "team", "coach",
        "tactics", "match", "league", "club", "goal"
    ]

    if not any(k in topic.lower() for k in FOOTBALL_KEYWORDS):
        raise ValueError("Topic not compatible with football personas")

    state["topic"] = topic
    state["round"] = 1
    state["current_agent"] = "AgentA"
    state["memory"] = {"turns": [], "summary": ""}
    state["last_output"] = ""

    return state