from sqlalchemy.orm import Session

from models import User
from utils.logging import logger
from schemas.response import Response_SM
from schemas.user import UserUpdate
from core.security import get_password_hash


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
