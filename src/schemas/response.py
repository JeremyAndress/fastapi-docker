from typing import Optional
from pydantic import BaseModel

class Response_SM(BaseModel):
    status: bool
    result: str