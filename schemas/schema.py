from pydantic import BaseModel

class URLCreate(BaseModel):
    long_url: str

class URL(BaseModel):
    short_code: str
    long_url: str
