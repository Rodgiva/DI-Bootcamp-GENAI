"""
lab2_ollama_native.py — LAB 2, interface #3 of 4: Ollama's own Python library.

Same thing as lab2_solution.py, done with the official `ollama` package.
No URL, no OpenAI dialect — it talks to Ollama's native API directly,
so you get Ollama-only features like think=False and format=<schema>.

Setup:
    pip install ollama
    ollama pull qwen3:0.6b
    (Ollama's server is usually already running; if not: ollama serve)
Run:
    python lab2_ollama_native.py
"""
import json
import ollama


def ask(prompt, model="qwen3:0.6b", system=None, temperature=0.8, max_tokens=800):
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})

    resp = ollama.chat(
        model=model,
        messages=msgs,
        think=False,   # skip the thinking step and answer directly
        options={"temperature": temperature, "num_predict": max_tokens},
    )
    return resp.message.content


if __name__ == "__main__":
    print(ask("Why should our company consider open-source AI models?"))

    # Bonus 1 — turn thinking ON and see it separately from the answer
    print("\n— Thinking ON —")
    resp = ollama.chat(
        model="qwen3:0.6b",
        messages=[{"role": "user", "content": "Is 17 a prime number? Answer yes or no."}],
        think=True,
    )
    print("THINKING:", resp.message.thinking)
    print("ANSWER:  ", resp.message.content)

    # Bonus 2 — force valid JSON with a schema (no "please output JSON" prompt tricks)
    print("\n— Strict JSON with format= —")
    schema = {
        "type": "object",
        "properties": {
            "sentiment": {"type": "string", "enum": ["pos", "neg", "neu"]},
            "confidence": {"type": "number"},
        },
        "required": ["sentiment", "confidence"],
    }
    resp = ollama.chat(
        model="qwen3:0.6b",
        messages=[{"role": "user", "content": 'Classify: "Loved the coffee, hated the wait."'}],
        think=False,
        format=schema,   # Ollama makes the model follow this shape
    )
    print(resp.message.content)
    print(json.loads(resp.message.content))   # parses reliably — no fences to strip
