from sqlalchemy.orm import Session
from utils.logging import logger
from utils.pagination import paginate
from models import Rol

def get_all_rol_cn(page:int,db:Session):
    rol  = paginate(db.query(Rol),page,10)
    return rol