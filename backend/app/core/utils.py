from fastapi import HTTPException


def validate_res(response):
  if not response.is_success:
    error_msg = response.json().get("error", "External Provider Error")
    raise HTTPException(status_code=response.status_code, detail=error_msg)

  return response.json()
