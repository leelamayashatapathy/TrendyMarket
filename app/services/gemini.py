import os
from dotenv  import load_dotenv
import requests
from fastapi import HTTPException

load_dotenv()

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_with_gemini(news_items):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API key not set in environment variable GEMINI_API_KEY.")
    prompt = "Summarize and analyze the following news items for market insights:\n"
    for item in news_items:
        prompt += f"- {item['title']}: {item.get('description', '')}\n"
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail=f"Gemini API error: {response.text}")
    result = response.json()
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        text = str(result)
    return {"summary": text, "insights": text} 