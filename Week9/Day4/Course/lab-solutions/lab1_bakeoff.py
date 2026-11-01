"""
lab1_bakeoff.py — LAB 1 solution: same prompt, three models, measured.

Run the cross-model bake-off in code instead of clicking three tabs.
Uses the OpenAI SDK pointed at Groq (OpenAI-compatible). Free key: console.groq.com

Setup:
    pip install openai python-dotenv
    Put your key in a .env file next to this script:
        GROQ_API_KEY=your_key_here
Run:
    python lab1_bakeoff.py
"""
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads GROQ_API_KEY from the .env file
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY not found. Add it to the .env file next to this script.")
    exit()

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)

PROMPT = ("Explain how Mixture of Experts (MoE) works in exactly 3 bullets, "
          "plain English, no jargon, each bullet under 25 words.")

# Groq retires models often — current ids: https://console.groq.com/docs/models
MODELS = [
    "openai/gpt-oss-120b",  # OpenAI (open-weight)
    "qwen/qwen3.8-27b",     # Qwen
    "allam-2-7b",           # SDAIA (Arabic + English)
]


def run(model):
    # Some models "think" before answering. We hide the thinking so it doesn't
    # use up the token budget or get counted in the word count.
    extra = {}
    # if model.startswith("openai/gpt-oss"):
    #     extra = {"reasoning_effort": "low", "include_reasoning": False}
    # elif model.startswith("qwen/"):
    #     extra = {"reasoning_format": "hidden"}

    start = time.perf_counter()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        temperature=0.3,
        max_tokens=1024,
        extra_body=extra,  # Groq-only settings go here
    )
    secs = time.perf_counter() - start

    text = resp.choices[0].message.content or ""  # content can be None
    # Just in case a model still sends its thinking: keep only what comes after it
    # if "</think>" in text:
    #     text = text.split("</think>")[-1]
    return text.strip(), secs


if __name__ == "__main__":
    for model in MODELS:
        print("=" * 70)
        print("MODEL:", model)
        try:
            text, secs = run(model)
        except Exception as e:  # one broken model shouldn't stop the others
            print("Error:", e, "\n")
            continue
        if not text:
            text = "(empty response)"
        words = len(text.split())
        print(f"[{secs:.2f}s | {words} words]")
        print(text, "\n")
