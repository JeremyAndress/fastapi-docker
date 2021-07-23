from sqlalchemy.orm import Session

from models import User
from utils.logging import logger
from schemas.response import Response_SM
from schemas.user import UserCreate, UserUpdate
from core.security import get_password_hash


def create_user(db: Session, obj_in: UserCreate):
    response = Response_SM(status=False, result='...')
    try:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            password=get_password_hash(obj_in.password),
            rol_id=obj_in.rol_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        response.status = True if db_obj.id else False
        response.result = 'success'
    except Exception as e:
        response.result = f'error {e}'
        logger.error(f'error {e}')
    return response


def update_user_cn(upd_user: UserUpdate, db: Session):
    response = Response_SM(status=False, result='...')
    try:
        user = db.query(User).filter(User.id == upd_user.id).update({
            User.rol_id: upd_user.rol_id,
            User.username: upd_user.username,
            User.email: upd_user.email
        })
        db.commit()
        db.flush()
        response.status = True if user else False
        response.result = 'success' if user else 'user does not exist'
        if upd_user.password and user:
            reset_password(user_id=upd_user.id, password=upd_user.password, db=db)
    except Exception as e:
        response.result = f'error {e}'
        logger.error(f'error {e}')
    return response


def reset_password(*, user_id: int, password: str, db: Session):
    try:
        db.query(User).filter(User.id == user_id).update({
            User.password: get_password_hash(password)
        })
        db.commit()
        db.flush()
    except Exception as e:
        logger.error(f'error {e}')
