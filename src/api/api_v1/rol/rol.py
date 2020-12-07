from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from api.deps import get_admin_user
from schemas.response import Response_SM
from schemas.rol import ListRol, RolBase, Rol
from .controller import (
    get_all_rol_cn, create_rol_cn,
    update_rol_cn, delete_rol_cn
)
router = APIRouter()


@router.get('/rol/get_all_rol/', response_model=ListRol)
def get_all_rol(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    rol = get_all_rol_cn(page, db)
    return rol


@router.post('/rol/create_rol/', response_model=Response_SM)
def create_rol(
    rol: RolBase,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = create_rol_cn(rol, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.put('/rol/update_rol/', response_model=Response_SM)
def update_rol(
    rol: Rol,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = update_rol_cn(rol, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.delete('/rol/delete_rol/', response_model=Response_SM)
def delete_rol(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = delete_rol_cn(id, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response
