from typing import Optional, List
from pydantic import BaseModel, EmailStr
from .response import Pagination


class UserBase(BaseModel):
    username: str


class Login(UserBase):
    password: str
    email: Optional[EmailStr]


class UserCreate(Login):
    rol_id: Optional[int]
    email: EmailStr


class UserUpdate(UserCreate):
    id: int
    password: Optional[str]

    class Config:
        orm_mode = True


class User(UserUpdate):
    password: str

    class Config:
        orm_mode = True


class UserListPag(Pagination):
    data: List[User]

    class Config:
        orm_mode = True
