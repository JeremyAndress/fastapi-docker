import os
from typing import Dict, Optional, Any
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "fasatapi-auth"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    MYSQL_SERVER: str = os.getenv('MYSQL_SERVER', '30.40.0.10:3307')
    MYSQL_USER: str = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_DB: str = os.getenv('MYSQL_DB', 'fastapitest')
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql://{values['MYSQL_USER']}:{values['MYSQL_PASSWORD']}@{values['MYSQL_SERVER']}/{values['MYSQL_DB']}"

    class Config:
        case_sensitive = True


settings = Settings()
