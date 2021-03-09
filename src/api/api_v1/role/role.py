from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.session import get_db
from api.deps import get_admin_user
from schemas.rol import ListRol, RolBase, Rol
from .service import role_service
from .controller import get_all_rol_cn

router = APIRouter()

# Document


@router.get('/role/{id}', response_model=Rol)
def get_rol(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return role_service.get(db, id)


@router.post('/role', response_model=Rol, status_code=201)
def create_role(
    rol: RolBase,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    try:
        return role_service.create(db, obj_in=rol)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')


@router.put('/role', response_model=Rol)
def update_role(
    rol: Rol,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    try:
        return role_service.update(db, obj_in=rol)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')


@router.delete('/role/{id}')
def delete_role(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    try:
        return role_service.remove(db, id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')


@router.get('/roles', response_model=ListRol)
def get_all_roles(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    rol = get_all_rol_cn(page, db)
    return rol
