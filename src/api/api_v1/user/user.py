from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db
from schemas.user import UserCreate, UserUpdate, UserListPag
from schemas.response import Response_SM
from api.deps import get_admin_user
from .controller import (
    create_user, get_user_cn,
    get_all_user_cn, delete_user_cn, update_user_cn
)
router = APIRouter()

# Document


@router.get("/user/{id}", response_model=UserUpdate, tags=["user"])
def user_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    user = get_user_cn(db, id)
    return user


@router.post("/user", response_model=Response_SM, status_code=201, tags=["user"])
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.delete("/user/{id}", response_model=Response_SM, tags=["user"])
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = delete_user_cn(id, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.put("/user", response_model=Response_SM, tags=["user"])
def update_user(
    upd_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = update_user_cn(upd_user, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response

# Collection


@router.get("/users", response_model=UserListPag, tags=["user"])
def get_all_user(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    user = get_all_user_cn(page, db)
    return user
