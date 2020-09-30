from jose import JWTError, jwt
from sqlalchemy.orm import Session
from fastapi import HTTPException, status,Depends
from fastapi.security import OAuth2PasswordBearer
from db.session import get_db
from core.config import settings
from schemas.user import UserCreate
from schemas.token import TokenData
from .gem.user.controller import get_by_email

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/"
)

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as e:
        print(f'error {e}')
        raise credentials_exception
    user = get_by_email(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user: UserCreate = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user