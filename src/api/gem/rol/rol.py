from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from api.deps import get_admin_user
from schemas.response import Response_SM
from schemas.rol import ListRol,RolBase,Rol
from .controller import (
    get_all_rol_cn,create_rol_cn,
    update_rol_cn
)
router = APIRouter()

@router.get('/get_all_rol/',response_model=ListRol)
def get_all_rol(
    page:int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    rol = get_all_rol_cn(page,db)
    return rol

@router.post('/create_rol/',response_model=Response_SM)
def create_rol(
    rol: RolBase,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = create_rol_cn(rol,db)
    return response

@router.put('/update_rol/',response_model=Response_SM)
def update_rol(
    rol: Rol,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    response = update_rol_cn(rol,db)
    return response