# Market_Trade API

A FastAPI service that analyzes Indian market sectors and generates trade opportunity insights using Google Gemini AI.

## Features
- **GET /analyze/{sector}**: Analyze a specific Indian sector (e.g., pharmaceuticals, technology)
- **Data Collection**: Fetches recent market news per sector
- **AI Analysis**: Uses Gemini API for summarization and insights
- **Session Management**: Tracks user sessions in-memory
- **Authentication**: JWT-based login and protected endpoints
- **Rate Limiting**: Per user/session
- **Error Handling**: Handles API failures, invalid input, and rate limits

## Installation
1. Clone the repository or copy the project files.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the environment:
   - On Windows (PowerShell):
     ```
     .\venv\Scripts\Activate
     ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the API
```
uvicorn app.main:app --reload
```

## Authentication
- Obtain a JWT token via:
  ```
  POST /token
  Content-Type: application/x-www-form-urlencoded
  Body: username=testuser&password=testpass
  ```
- Use the returned `access_token` as a Bearer token in the Authorization header for requests.

## Example Usage
```
GET /analyze/pharmaceuticals
Authorization: Bearer <your_token>
```

## Allowed Sectors
pharmaceuticals, technology, finance, energy, fmcg, it, banking, auto, telecom, realty, metals, oil & gas, healthcare, infrastructure, consumer durables, power, capital goods, media, chemicals, insurance, retail

## Notes
- The Gemini AI integration is currently mocked. Replace the placeholder with real API calls as needed.
- All data is stored in-memory; restart will reset sessions and rate limits. 