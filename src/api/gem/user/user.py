from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db.session import get_db
from schemas.user import UserCreate
from schemas.response import Response_SM
from schemas.token import Token
from core.security import create_access_token
from api.deps import get_current_active_user
from .controller import (
    get_by_email, create_user, authenticate
)
router = APIRouter()

@router.post("/user_create/",response_model=Response_SM)
def user_create(user:UserCreate, db:Session = Depends(get_db)):
    response = create_user(db,user)
    return response

@router.post("/login/",response_model=Token)
def login(db: Session = Depends(get_db),form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token(user.username),
        "token_type": "bearer",
    }

@router.get("/get_user_by_email/")
def user_get(db: Session = Depends(get_db),current_user: UserCreate = Depends(get_current_active_user)):
    user = get_by_email(db,'prueba')
    #get_current_user(db,'sdlkjsdfj')
    return {"user":user}