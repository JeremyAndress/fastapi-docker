from typing import Optional
from pydantic import BaseModel


class Response_SM(BaseModel):
    status: bool
    result: str


class Reponse_WITH_ID(Response_SM):
    id: int


class Pagination(BaseModel):
    previous_page: Optional[int]
    next_page: Optional[int]
    total: Optional[int]
    pages: Optional[int]
