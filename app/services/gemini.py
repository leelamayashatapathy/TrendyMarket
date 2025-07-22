import os
import requests
from fastapi import HTTPException

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = 'AIzaSyD444K4Vk_6rmcTLSK94USoh2Gzlns1bw0'

def analyze_with_gemini(news_items):
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API key not set in environment variable GEMINI_API_KEY.")
    prompt = "Summarize and analyze the following news headlines for market insights:\n" + "\n".join([item['title'] for item in news_items])
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
    # Extract the generated text from the response
    try:
        text = result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        text = str(result)
    return {"summary": text, "insights": text} 