from typing import Optional,List
from pydantic import BaseModel
from .response import Pagination
# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

class UserList(UserCreate):
    id: int
    class Config:
        orm_mode = True

class UserListPag(Pagination):
    data: List[UserList]
    class Config:
        orm_mode = True