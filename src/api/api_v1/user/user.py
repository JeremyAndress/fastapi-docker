from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from db.session import get_db

from .service import user_service
from api.deps import get_admin_user
from schemas.response import Response_SM
from .controller import create_user, update_user_cn
from schemas.user import UserCreate, UserUpdate, UserListPag, UserInDBBase

router = APIRouter()

# Document


@router.get('/user/{id}', response_model=UserInDBBase, tags=['user'])
def user_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.get(db, id)


@router.post('/user', response_model=Response_SM, status_code=201, tags=['user'])
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.delete('/user/{id}', response_model=UserInDBBase, tags=['user'])
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.remove(db, id=id)


@router.put('/user', response_model=Response_SM, tags=['user'])
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


@router.get('/users', response_model=UserListPag, tags=['user'])
def get_all_user(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.get_paginate(db, page=page)
