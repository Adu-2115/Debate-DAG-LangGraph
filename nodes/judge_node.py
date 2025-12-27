import time
from debate_state import DebateState
from llm_client import call_ollama
from nodes.logger import log_event

def judge_node(state: DebateState) -> DebateState:
    transcript = "\n".join(
        [f"{t['agent']}: {t['text']}" for t in state["memory"]["turns"]]
    )

    prompt = f"""
You are an impartial football debate judge.

Topic:
{state['topic']}

Transcript:
{transcript}

Return:
Summary:
Winner:
Reason:
"""

    response = call_ollama(prompt, seed=99)
    state["last_output"] = response

    print("\n========== JUDGE VERDICT ==========\n")
    print(response)
    print("==================================\n")

    log_event({
        "event": "final_verdict",
        "verdict": response,
        "timestamp": time.time()
    })

    return state
