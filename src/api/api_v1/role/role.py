from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from api.deps import get_admin_user
from schemas.response import Response_SM
from schemas.rol import ListRol, RolBase, Rol
from .controller import (
    get_all_rol_cn, create_rol_cn,
    update_rol_cn, delete_rol_cn, get_rol_cn
)
router = APIRouter()

# Document


@router.get('/role/{id}', response_model=Rol)
def get_rol(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    role = get_rol_cn(id, db)
    return role


@router.post('/role', response_model=Response_SM, status_code=201)
def create_role(
    rol: RolBase,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = create_rol_cn(rol, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.put('/role', response_model=Response_SM)
def update_role(
    rol: Rol,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = update_rol_cn(rol, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.delete('/role/{id}', response_model=Response_SM)
def delete_role(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = delete_rol_cn(id, db)
    if not response.status:
        raise HTTPException(status_code=400, detail=response.result)
    return response


@router.get('/roles', response_model=ListRol)
def get_all_roles(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    rol = get_all_rol_cn(page, db)
    return rol
