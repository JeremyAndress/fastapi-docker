from fastapi import APIRouter

from .api_v1.user import user
from .api_v1.role import role
from .api_v1.auth import auth

router = APIRouter()
router.include_router(auth.router)
router.include_router(user.router)
router.include_router(role.router, tags=['role'])
