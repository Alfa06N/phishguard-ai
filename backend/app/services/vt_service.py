import httpx
import os
from app.core.utils import validate_res


class VTService:
  def __init__(self):
    self.api_key = os.getenv("VIRUSTOTAL_API_KEY")
    self.base_url = "https://www.virustotal.com/api/v3"

  async def scan_url(self, target_url: str):
    headers = {"x-apikey": self.api_key}

    async with httpx.AsyncClient() as client:
      payload = {"url": target_url}

      response = await client.post(f"{self.base_url}/urls", data=payload, headers=headers)
      res = validate_res(response)

      analysis_id = res["data"]["id"]
      report = await client.get(f"{self.base_url}/analyses/{analysis_id}", headers=headers)
      report_res = validate_res(report)

      stats = report_res["data"]["attributes"]["stats"]
      return {
          "malicious": stats["malicious"],
          "suspicious": stats["suspicious"],
          "harmless": stats["harmless"],
      }
