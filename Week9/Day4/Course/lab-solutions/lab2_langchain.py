"""
lab2_langchain.py — LAB 2, interface #4 of 4: LangChain (what LangGraph / CrewAI build on).

Same local model, driven through LangChain message objects + the | pipe.

Setup:
    pip install langchain-ollama langchain-core
    ollama pull qwen3:0.6b
    (Ollama's server is usually already running; if not: ollama serve)
Run:
    python lab2_langchain.py
"""
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate


def ask(prompt, model="qwen3:0.6b", system=None, temperature=0.8, max_tokens=800):
    # reasoning=False is LangChain's name for Ollama's think=False:
    # the model (e.g. qwen3) skips its thinking step and answers directly.
    llm = ChatOllama(model=model, temperature=temperature, num_predict=max_tokens,
                     reasoning=False, base_url="http://127.0.0.1:11434")
    msgs = []
    if system:
        msgs.append(SystemMessage(content=system))
    msgs.append(HumanMessage(content=prompt))
    return llm.invoke(msgs).content


if __name__ == "__main__":
    print(ask("Why should our company consider open-source AI models?"))

    # Bonus — reusable template + the | pipe (the LCEL syntax from the agents week)
    template = ChatPromptTemplate.from_messages([
        ("system", "You are a {role}. Answer in one short sentence."),
        ("human", "{question}"),
    ])
    chain = template | ChatOllama(model="qwen3:0.6b", temperature=0.3, num_predict=800,
                                  reasoning=False, base_url="http://127.0.0.1:11434")
    for role in ("Python tutor", "chef", "startup founder"):
        answer = chain.invoke({"role": role, "question": "What is a list?"})
        print(f"[{role}]", answer.content.strip())
