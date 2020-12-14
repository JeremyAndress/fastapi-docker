from fastapi import APIRouter
from .api_v1.user import user
from .api_v1.rol import rol

router = APIRouter()
router.include_router(user.router)
router.include_router(rol.router, tags=["role"])
