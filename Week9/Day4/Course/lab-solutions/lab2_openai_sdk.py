"""
lab2_openai_sdk.py — LAB 2, interface #2 of 4: the OpenAI SDK, pointed at local Ollama.

Same thing as lab2_solution.py, done with the official OpenAI SDK.
THE TRICK: change base_url + api_key and the OpenAI SDK talks to Ollama.

Setup:
    pip install openai
    ollama pull qwen3:0.6b
    (Ollama's server is usually already running; if not: ollama serve)
Run:
    python lab2_openai_sdk.py
"""
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="ollama")  # key ignored by Ollama


def ask(prompt, model="qwen3:0.6b", system=None, temperature=0.8, max_tokens=800):
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})

    resp = client.chat.completions.create(
        model=model,
        messages=msgs,
        temperature=temperature,
        max_tokens=max_tokens,
        # qwen3 thinks before answering — "none" turns it off so it answers directly.
        # (Ollama's own API calls this think=False.) Models that don't think ignore it.
        reasoning_effort="none",
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    print(ask("Why should our company consider open-source AI models?"))

# Hosted swap (2 lines):
#   import os
#   client = OpenAI(base_url="https://api.groq.com/openai/v1",
#                   api_key=os.environ["GROQ_API_KEY"])   ->  model="openai/gpt-oss-20b"
