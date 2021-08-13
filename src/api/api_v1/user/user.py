from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from db.session import get_db

from .service import user_service
from api.deps import get_admin_user
from schemas.user import UserCreate, UserUpdate, UserListPag, User

router = APIRouter()

# Document


@router.get('/user/{id}', response_model=User, tags=['user'])
def user_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.get(db, id)


@router.post('/user', response_model=User, status_code=201, tags=['user'])
def user_create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, obj_in=user)


@router.delete('/user/{id}', response_model=User, tags=['user'])
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.remove(db, id=id)


@router.put('/user', response_model=User, tags=['user'])
def update_user(
    upd_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.update(db, obj_in=upd_user)

# Collection


@router.get('/users', response_model=UserListPag, tags=['user'])
def get_all_user(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return user_service.get_paginate(db, page=page)
