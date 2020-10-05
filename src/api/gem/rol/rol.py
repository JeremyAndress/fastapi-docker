from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from api.deps import get_admin_user
from .controller import (
    get_all_rol_cn
)
router = APIRouter()

@router.get('/get_all_rol/')
def get_all_rol(
    page:int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    rol = get_all_rol_cn(page,db)
    return rol