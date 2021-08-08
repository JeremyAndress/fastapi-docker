from sqlalchemy.orm import Session
from typing import Union, Dict, Any
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

    def update(
        self, db: Session,
        *, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        db_obj = db.query(self.model).get(obj_in.id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data and field != 'password':
                setattr(db_obj, field, update_data[field])
            elif field in update_data and field == 'password':
                db_obj.password = get_password_hash(update_data['password'])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


user_service = CRUDUser(model=User)
