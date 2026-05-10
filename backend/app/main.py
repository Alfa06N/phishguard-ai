import json
import os
import re
from math import e
from asyncio import sleep
from app.schemas.ScanRequest import ScanRequest
from app.schemas.ScanResponse import ScanResponse
from app.services.ai_service import analyze_with_gemini
from app.services.vt_service import VTService
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from google.api_core import exceptions as google_exceptions
from google.genai import errors as genai_errors
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

load_dotenv()

app = FastAPI(title="Phishing Shield API")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "https://phishguard-ai-kappa.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

vt_service = VTService()


@app.exception_handler(Exception)
async def unified_proxy_handler(request: Request, exc: Exception):
  status_code = 500
  message = str(exc)
  error_type = exc.__class__.__name__

  if isinstance(
      exc, (genai_errors.ClientError,
            genai_errors.ServerError, genai_errors.APIError)
  ):
    status_code = getattr(exc, "code", getattr(exc, "status_code", 502))
    if "RESOURCE_EXHAUSTED" in str(exc):
      status_code = 429
      message = "Gemini API limit reached (20/day). Please try again later."

  elif isinstance(exc, HTTPException):
    status_code = exc.status_code
    message = exc.detail

  if not isinstance(status_code, int) or not (400 <= status_code < 600):
    status_code = 500

  if status_code == 500:
    print(f"CRITICAL SYSTEM ERROR: {exc}")

  return JSONResponse(
      status_code=status_code,
      content={"status": status_code, "message": message, "type": error_type},
  )


@app.get("/")
@limiter.limit("60/minute")
async def health_check(request: Request):
  return {"status": "online", "version": "1.0.0"}


@app.get("/favicon.ico", include_in_schema=False)
@limiter.limit("60/minute")
async def favicon(request: Request):
  return Response(status_code=204)


@app.post("/api/v1/scan", response_model=ScanResponse)
@limiter.limit("5/minute")
async def perform_scan(request: Request, scan_data: ScanRequest):
  content = scan_data.content
  if content.lower() == "test-phish":
    await sleep(2)
    return {
        "verdict": "Dangerous",
        "score": 98,
        "ai_analysis": {
            "risk_score": 0,
            "psychological_triggers": [
                "Urgency (Immediate action required)",
                "Fear (Account suspension threat)"
            ],
            "technical_red_flags": [
                "Suspicious Domain (.xyz TLD)",
                "Generic Greeting"
            ],
            "verdict": "Dangerous"
        },
        "vt_analysis": {
            "malicious": 3,
            "suspicious": 1,
            "harmless": 68,
            "status": "completed"
        },
        "domain_info": "http://secure-login-update.xyz",
        "threats": [
            "Suspicious Domain (.xyz TLD)",
            "Urgency (Immediate action required)",
            "Fear (Account suspension threat)",
            "Reported as Malicious by 3 VT Engines"
        ]
    }
  try:
    if not content:
      raise HTTPException(status_code=400, detail="No content provided")

    ai_raw_result = await analyze_with_gemini(content)
    if ai_raw_result is None:
      raise HTTPException(
          status_code=500, detail="Failed to retrieve AI analysis"
      )

    ai_data = json.loads(ai_raw_result)
    url_match = re.search(r'https?://[^\s<>"]+|www\.[^\s<>"]+', content)
    vt_data = {"status": "not_scanned", "malicious": 0}

    if url_match:
      extracted_url = url_match.group(0).rstrip(")")
      print(f"DEBUG: Scanning URL: {extracted_url}")
      vt_data = await vt_service.scan_url(extracted_url)

    final_verdict = ai_data.get("verdict", "Unknown")
    final_score = ai_data.get("risk_score", 0)

    if vt_data.get("malicious", 0) > 0:
      final_verdict = "Dangerous"
      final_score = max(final_score, 90)

    return {
        "verdict": final_verdict,
        "score": final_score,
        "ai_analysis": ai_data,
        "vt_analysis": vt_data
        if url_match
        else {"status": "skipped", "reason": "No URL found in content"},
        "domain_info": content if "." in content else None,
        "threats": ai_data.get("technical_red_flags", [])
        + ai_data.get("psychological_triggers", []),
    }
  except genai_errors.ClientError as e:
    if "RESOURCE_EXHAUSTED" in str(e):
      raise HTTPException(
          status_code=429,
          detail="Daily scan limit reached. Please try again tomorrow.",
      )
    raise HTTPException(status_code=502, detail=f"AI Service error: {str(e)}")
