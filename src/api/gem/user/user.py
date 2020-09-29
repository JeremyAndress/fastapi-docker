from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from db.session import get_db
from schemas.user import UserCreate
from .controller import create_user, authenticate

router = APIRouter()

@router.post("/user_create/")
def user_create(user:UserCreate, db:Session = Depends(get_db)):
    user = create_user(db,user)
    return {"user":user}

@app.post("/login/")
def login(db: Session = Depends(get_db),form_data: OAuth2PasswordRequestForm = Depends()):
    print(f'form {form_data}')
    user = authenticate(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return {
        "access_token": create_access_token(user.username),
        "token_type": "bearer",
    }