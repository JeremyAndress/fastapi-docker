from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db
from schemas.user import UserCreate, UserListPag,Login
from schemas.response import Response_SM
from schemas.token import TokenUser
from core.security import create_access_token
from api.deps import get_current_active_user,get_admin_user
from .controller import (
    get_by_email, create_user, authenticate,
    get_all_user_cn
)
router = APIRouter()

@router.post("/user_create/",response_model=Response_SM)
def user_create(user:UserCreate, db:Session = Depends(get_db)):
    response = create_user(db,user)
    return response

@router.post("/login/",response_model=TokenUser)
def login(user:Login,db: Session = Depends(get_db)):
    user = authenticate(db,user.username,user.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token(user.username),
        "token_type": "bearer",
        "rol_id": user.rol.id if user.rol else None,
        "rol_name": user.rol.name if user.rol else None
    }

@router.get("/get_all_user/",response_model=UserListPag)
def get_all_user(
    page:int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user),
):
    user = get_all_user_cn(page,db)
    return user