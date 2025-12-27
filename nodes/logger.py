import os
import json

os.makedirs("logs", exist_ok=True)

def log_event(event: dict):
    with open("logs/debate_log.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")
