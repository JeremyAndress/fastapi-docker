from .response import Pagination
from typing import Optional, List
from pydantic import BaseModel

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
