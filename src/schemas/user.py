from typing import Optional, List
from pydantic import BaseModel
from .response import Pagination


class UserBase(BaseModel):
    username: str


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
