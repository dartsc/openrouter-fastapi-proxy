# filename: openrouter_proxy.py
from fastapi import FastAPI, Request
import uvicorn
import requests

app = FastAPI()
API_KEY = "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"

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    user_msg = body.get("message", "")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://yourgame.com",
        "X-Title": "Roblox Chat"
    }

    data = {
        "model": "openrouter/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": user_msg}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return response.json()

# To run: uvicorn openrouter_proxy:app --reload
