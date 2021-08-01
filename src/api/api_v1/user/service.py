from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from models import User
from db.crud import CRUDBase
from core.security import get_password_hash
from schemas.user import UserUpdate, UserCreate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data['password'] = get_password_hash(obj_in_data['password'])
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


user_service = CRUDUser(model=User)
