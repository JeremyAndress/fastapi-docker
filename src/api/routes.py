from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
router = APIRouter()

#oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from typing import Optional
from pydantic import (
    BaseModel, validator
) 

class Token(BaseModel):
    token: str
    @validator('token')
    def token_validate(cls, v):
        if 'kA44s4GzmqpdppH9' != v:
            raise ValueError('invalid token')
        return v

@router.post("/CAB/testing")
def firts(id: int, token: Token):
    return {
        "id": id,
        "status": 200
    }