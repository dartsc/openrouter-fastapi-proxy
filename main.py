from fastapi import FastAPI, Request
import uvicorn
import requests
import os

app = FastAPI()
API_KEY = os.getenv("API_KEY")  # Read from env var

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
