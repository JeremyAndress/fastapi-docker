from db.crud import CRUDBase
from models.rol import Rol
from schemas.rol import Rol as RolUpdate, RolBase


class CRUDRole(CRUDBase[Rol, RolBase, RolUpdate]):
    pass


role_service = CRUDRole(model=Rol)
