class AppBaseException(Exception):
  """Base class for all application errors"""

  def __init__(self, code: str, message: str, status_code: int = 400):
    self.code = code
    self.message = message
    self.status_code = status_code


class VirusTotalError(AppBaseException):
  """Errors specifically from the VT API"""
  pass


class AIAnalysisError(AppBaseException):
  """Errors from Gemini"""
  pass
