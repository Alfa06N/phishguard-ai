import os
import json
from google import genai
from google.genai import types
from fastapi import HTTPException


async def analyze_with_gemini(content: str):

  client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

  system_instruction = (
      "You are a Cyber-Security Analyst specialized in Social Engineering. "
      "Analyze the content for phishing or scam attempts. "
      "You MUST return ONLY a valid JSON object."
  )

  prompt = f"""
        Analyze the following URL or text for phishing/scam attempts:
        "{content}"
        
        Return ONLY a JSON object with:
        - risk_score (0-100)
        - psychological_triggers (list)
        - technical_red_flags (list)
        - verdict (Safe, Suspicious, or Dangerous)
        """

  response = client.models.generate_content(
      model="models/gemini-2.5-flash",
      config=types.GenerateContentConfig(
          system_instruction=system_instruction,
          response_mime_type="application/json"
      ),
      contents=prompt
  )

  return response.text
