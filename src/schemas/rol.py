from typing import List
from pydantic import BaseModel
from .response import Pagination


class RolBase(BaseModel):
    name: str


class Rol(RolBase):
    id: int

    class Config:
        orm_mode = True


class ListRol(Pagination):
    data: List[Rol]

    class Config:
        orm_mode = True
