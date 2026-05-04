from typing import List, Optional

from pydantic import BaseModel


class ScanResponse(BaseModel):
    verdict: str
    score: int
    ai_analysis: dict
    vt_analysis: dict
    domain_info: Optional[str]
    threats: List[str]
