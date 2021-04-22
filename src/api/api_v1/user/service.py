from db.crud import CRUDBase
from models import User
from schemas.user import UserUpdate, UserCreate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


user_service = CRUDUser(model=User)
