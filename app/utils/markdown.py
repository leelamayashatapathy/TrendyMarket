def generate_markdown_report(sector: str, news, gemini):
    md = f"""# Market Analysis Report: {sector.title()}\n\n## News Headlines\n"""
    for item in news:
        md += f"- [{item['title']}]({item['url']})\n"
    md += f"\n## Gemini Summary\n{gemini['summary']}\n"
    md += f"\n## Gemini Insights\n{gemini['insights']}\n"
    return md 