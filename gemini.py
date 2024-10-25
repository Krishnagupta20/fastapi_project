import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

class GeminiClient:
    @staticmethod
    async def generate_content(query: str):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": query}
                    ]
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            async with client.stream("POST", API_URL, headers=headers, json=data) as response:
                if response.status_code != 200:
                    raise Exception(f"Failed to get response from Gemini API: {response.status_code}")
                
                async for chunk in response.aiter_text():
                    yield chunk
