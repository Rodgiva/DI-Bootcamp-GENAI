"""
lab2_solution.py — LAB 2 full ladder (raw requests · the OpenAI dialect, LOCAL).

Rungs 1, 2, 3, 5. (Rung 4 — hosted — is in lab2_rung4_hosted.py.)

Setup:
    pip install requests
    ollama pull qwen3:0.6b
    ollama pull mistral:7b        # for rung 5 (optional)
    (Ollama's server is usually already running; if not: ollama serve)
Run:
    python lab2_solution.py
"""
import json
import requests


def ask(prompt, model="qwen3:0.6b", system=None, temperature=0.8, max_tokens=800):
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})

    # qwen3 is a THINKING model: it can burn the whole budget on hidden reasoning
    # and return an EMPTY answer. reasoning_effort "none" turns thinking off.
    # (Ollama's own API calls this think=False.) Models that don't think ignore it.
    r = requests.post(
        "http://127.0.0.1:11434/v1/chat/completions",   # local, OpenAI-compatible
        json={"model": model, "messages": msgs,
              "temperature": temperature, "max_tokens": max_tokens,
              "reasoning_effort": "none"},
        timeout=120)
    return r.json()["choices"][0]["message"]["content"]


SYSTEM = """You are a senior tech writer.
Audience: a busy CFO who hates jargon.
Answer in exactly 3 bullets, each under 15 words.
Never invent statistics."""

SYSTEM_JSON = """You output ONLY valid JSON. No prose. No markdown fences.
Schema: {"sentiment": "pos"|"neg"|"neu", "confidence": number 0.0-1.0}
Example input: "Great pizza, slow service."
Example output: {"sentiment": "neu", "confidence": 0.7}"""


if __name__ == "__main__":
    # Rung 1 — first local reply
    print("— Rung 1: plain —")
    print(ask("Why should our company consider open-source AI models?"))

    # Rung 2 — add a SYSTEM message (the Day-1 six-ingredient frame)
    print("\n— Rung 2: with a system prompt —")
    print(ask("Why should our company consider open-source AI models?", system=SYSTEM))

    # Rung 3 — force JSON out
    print("\n— Rung 3: strict JSON —")
    raw = ask('Classify: "Loved the coffee, hated the wait."', system=SYSTEM_JSON)
    print(raw)
    # Small models often wrap JSON in ```json ... ``` fences even when told not to.
    # Remove them before parsing:
    raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```")
    print(json.loads(raw))        # parses cleanly when the schema holds

    # Rung 5 — swap the model, SAME code (needs: ollama pull mistral:7b)
    print("\n— Rung 5: same code, bigger model —")
    print(ask("Explain MoE in one sentence.", model="mistral:7b"))
