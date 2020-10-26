from fastapi import APIRouter
from .gem.user import user
from .gem.rol import rol

router = APIRouter()
router.include_router(user.router)
router.include_router(rol.router,tags=["rol"])