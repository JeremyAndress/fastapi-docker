from typing import Optional
from pydantic import BaseModel

# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

