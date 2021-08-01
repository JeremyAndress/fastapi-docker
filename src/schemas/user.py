from typing import Optional, List

from pydantic import BaseModel, EmailStr

from .response import Pagination


class Login(BaseModel):
    username: Optional[str]
    password: str
    email: Optional[EmailStr]


class UserInDBBase(BaseModel):
    username: str
    rol_id: Optional[int]
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserInDBBase):
    password: str


class UserUpdate(UserCreate):
    id: int
    password: Optional[str]


class User(UserInDBBase):
    id: int


class UserListPag(Pagination):
    data: List[User]

    class Config:
        orm_mode = True
