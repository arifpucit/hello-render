# Hello Render - A Groq-powered Gradio Chatbot

A minimal streaming chatbot built with Gradio and the Groq API, running the
open-source model `openai/gpt-oss-20b`. The same `app.py` runs locally and on Render.

## Run locally
```bash
pip install -r requirements.txt
echo "GROQ_API_KEY=gsk_your_key_here" > .env
python app.py
```

## Deploy on Render
1. Push this repo to GitHub.
2. render.com -> New -> Web Service -> connect this repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `python app.py`
5. Add environment variable `GROQ_API_KEY` in the Render dashboard.

Never commit `.env`.

## Note
`gpt-oss-20b` is a reasoning model: keep `max_tokens` generous (1024) and
`reasoning_effort="low"`, or replies arrive empty.
