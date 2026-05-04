from pydantic import BaseModel, field_validator


class ScanRequest(BaseModel):
    content: str

    @field_validator("content", mode="before")
    @classmethod
    def handle_newlines(cls, v):
        if isinstance(v, str):
            return v.replace("\r\n", "\n").replace("\r", "\n")
        return v
