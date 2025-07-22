from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from app.core.config import ALLOWED_SECTORS
from app.core.rate_limit import rate_limiter
from app.core.session import get_and_update_session
from app.services.news import fetch_sector_news
from app.services.gemini import analyze_with_gemini
from app.utils.markdown import generate_markdown_report

router = APIRouter()

@router.get("/analyze/{sector}", response_class=PlainTextResponse)
def analyze_sector(sector: str, user: str = Depends(rate_limiter)):

    if sector.lower() not in ALLOWED_SECTORS:
        raise HTTPException(status_code=400, detail=f"Invalid sector. Allowed sectors: {', '.join(ALLOWED_SECTORS)}")

    session = get_and_update_session(user, sector)
    news = fetch_sector_news(sector)
    gemini_result = analyze_with_gemini(news)
    markdown_report = generate_markdown_report(sector, news, gemini_result)
    markdown_report += f"\n---\nSession info: {session}\n"
    return markdown_report 