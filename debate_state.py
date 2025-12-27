from typing import TypedDict, Dict, Any


class DebateState(TypedDict):
    topic: str
    round: int
    current_agent: str
    memory: Dict[str, Any]
    last_output: str
