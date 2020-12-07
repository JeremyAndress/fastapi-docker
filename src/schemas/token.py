from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenUser(Token):
    rol_id: Optional[int]
    rol_name: Optional[str]


class TokenData(BaseModel):
    username: Optional[str] = None
