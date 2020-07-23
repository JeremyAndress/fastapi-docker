import os
from typing import Optional
from pydantic import BaseModel, validator

basic_token = os.getenv('BASIC_TOKEN','kA44s4GzmqpdppH9')

class BasicToken(BaseModel):
    token: str
    @validator('token')
    def token_validate(cls, v):
        if basic_token != v:
            raise ValueError('invalid token')
        return v