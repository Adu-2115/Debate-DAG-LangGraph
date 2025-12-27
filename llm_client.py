import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def call_ollama(prompt: str, seed: int = 42) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "seed": seed,
                "temperature": 0.7,
            },
        },
    )
    response.raise_for_status()
    return response.json()["response"].strip()
