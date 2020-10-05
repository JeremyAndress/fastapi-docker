from sqlalchemy.orm import Session
from utils.logging import logger
from utils.pagination import paginate
from schemas.rol import RolBase, Rol as Rol_Update
from schemas.response import Response_SM
from models import Rol

def get_all_rol_cn(page:int,db:Session):
    rol  = paginate(db.query(Rol),page,10)
    return rol

def create_rol_cn(rol:RolBase,db:Session):
    arsene =  Response_SM(status=False,result= '...')
    try:
        rol_data = Rol(name=rol.name)
        db.add(rol_data)
        db.commit()
        db.refresh(rol_data)
        arsene.status = True if rol_data.id else False
        arsene.result = 'success'
    except Exception as e:
        arsene.result = f'error {e}'
        logger.error(f'error {e}')
    return arsene

def update_rol_cn(rol:Rol_Update,db:Session):
    arsene =  Response_SM(status=False,result= '...')
    try:
        rol_data = db.query(Rol).filter(Rol.id == rol.id).update({
            Rol.name : rol.name
        })
        db.commit()
        db.flush()
        arsene.status = True if rol_data else False
        arsene.result = 'success' if rol_data else 'rol does not exist'
    except Exception as e:
        arsene.result = f'error {e}'
        logger.error(f'error {e}')
    return arsene