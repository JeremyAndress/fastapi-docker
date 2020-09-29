from sqlalchemy.orm import Session
from schemas.user import UserCreate
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
    db_obj = User(
        username=obj_in.username,
        password=get_password_hash(obj_in.password),
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

