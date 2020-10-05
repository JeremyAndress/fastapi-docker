from sqlalchemy.orm import Session
from utils.logging import logger
from utils.pagination import paginate
from models.user import User
# from models.rol import Rol
from schemas.user import UserCreate
from schemas.response import Response_SM
from core.security import verify_password,get_password_hash

def get_by_email(db: Session,username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate(db: Session,username: str, password: str):
    user = get_by_email(db, username=username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

def create_user(db: Session,obj_in: UserCreate):
    arsene =  Response_SM(status=False,result= '...')
    try:
        db_obj = User(
            username=obj_in.username,
            password=get_password_hash(obj_in.password),
            rol_id=obj_in.rol_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        arsene.status = True if db_obj.id else False
        arsene.result = 'success'
    except Exception as e:
        arsene.result = f'error {e}'
        logger.error(f'error {e}')
    return arsene

def get_all_user_cn(page,db: Session):
    user  = paginate(db.query(User),page,2)
    return user

def delete_user_cn(id:int,db:Session):
    arsene =  Response_SM(status=False,result= '...')
    try:
        user = db.query(User).filter(User.id == id).delete()
        arsene.status = True if user else False
        arsene.result = 'success' if user else 'user does not exist'
    except Exception as e:
        arsene.result = f'error {e}'
        logger.error(f'error {e}')
    return arsene
