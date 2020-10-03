from typing import Optional,List
from pydantic import BaseModel
from .response import Pagination
# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None

# Properties to receive via API on creation
class Login(UserBase):
    password: str

class UserCreate(Login):
    rol_id: Optional[int]

class UserList(UserCreate):
    id: int
    class Config:
        orm_mode = True

class UserListPag(Pagination):
    data: List[UserList]
    class Config:
        orm_mode = True