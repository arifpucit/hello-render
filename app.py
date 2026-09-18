"""A minimal streaming chatbot: Gradio + Groq + openai/gpt-oss-20b.

Runs unchanged on your laptop and on Render.
"""
import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "openai/gpt-oss-20b"
SYSTEM_PROMPT = "You are a helpful, friendly teaching assistant. Answer clearly and concisely."

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY is not set.\n"
        "  Locally : put GROQ_API_KEY=gsk_... in a .env file next to app.py\n"
        "  Render  : add it under Environment -> Environment Variables"
    )

client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")


def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for turn in history:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
        max_tokens=1024,
        reasoning_effort="low",
    )

    partial = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            partial += delta
            yield partial


demo = gr.ChatInterface(
    fn=chat,
    title="🤖 Hello Render - Groq Chatbot",
    description=f"Streaming chat powered by `{MODEL}` on Groq.",
    examples=["What is a large language model?", "Explain Groq in one line."],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ["PORT"]) if os.environ.get("PORT") else None,
    )
