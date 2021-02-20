from fastapi import APIRouter, Depends, HTTPException
from core.security import create_access_token
from sqlalchemy.orm import Session
from schemas.token import TokenUser
from schemas.user import Login
from db.session import get_db
from .controller import authenticate

router = APIRouter()


@router.post('/login/', response_model=TokenUser, tags=['auth'])
def login(user: Login, db: Session = Depends(get_db)):
    user = authenticate(db, username=user.username, password=user.password, email=user.email)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')
    return {
        'access_token': create_access_token(user.username),
        'token_type': 'bearer',
        'rol_id': user.rol.id if user.rol else None,
        'rol_name': user.rol.name if user.rol else None
    }
