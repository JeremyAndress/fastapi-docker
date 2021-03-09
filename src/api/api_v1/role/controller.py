from sqlalchemy.orm import Session
from utils.pagination import paginate
from models import Rol


def get_all_rol_cn(page: int, db: Session):
    rol = paginate(db.query(Rol), page)
    return rol
