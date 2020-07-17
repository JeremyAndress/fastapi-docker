from typing import Any, Dict, List, Optional, Union
from pydantic import (
    AnyHttpUrl, BaseSettings, EmailStr, HttpUrl
    , PostgresDsn, validator
) 

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FASTAPI-JWT"
    class Config:
        case_sensitive = True

settings = Settings()
