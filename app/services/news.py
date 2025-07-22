import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException

def fetch_sector_news(sector: str, max_results: int = 5):
    """Fetch recent news headlines for a sector using DuckDuckGo."""
    query = f"{sector} sector India market news"
    url = f"https://duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch news data.")
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for a in soup.select("a.result__a")[:max_results]:
        title = a.get_text()
        link = a.get("href")
        results.append({"title": title, "url": link})
    if not results:
        raise HTTPException(status_code=404, detail="No news found for this sector.")
    return results 