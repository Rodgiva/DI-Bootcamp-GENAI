"""
lab2_rung4_hosted.py — LAB 2, Rung 4: the SAME shape, hosted (Groq).

Only the URL, an auth header, and the model name change vs the local version.

Setup:
    pip install requests python-dotenv
    free key at https://console.groq.com, then put it in a .env file next to this script:
        GROQ_API_KEY=your_key_here
Run:
    python lab2_rung4_hosted.py
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # reads GROQ_API_KEY from the .env file
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY not found. Add it to the .env file next to this script.")
    exit()


def ask_groq(prompt, model="openai/gpt-oss-20b", system=None,
             temperature=0.8, max_tokens=500):
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})

    r = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": model, "messages": msgs,
              "temperature": temperature, "max_tokens": max_tokens,
              "reasoning_effort": "low"},   # gpt-oss thinks first; keep it short
        timeout=60)

    data = r.json()
    # On failure Groq sends {"error": {...}} instead of "choices"
    if "error" in data:
        return "Groq error: " + data["error"]["message"]
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print(ask_groq("Why should our company consider open-source AI models?"))
    # Other ids: openai/gpt-oss-120b · qwen/qwen3.8-27b
    # Current list: https://console.groq.com/docs/models
