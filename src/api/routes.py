from fastapi import APIRouter
from .api_v1.user import user
from .api_v1.role import role

router = APIRouter()
router.include_router(user.router)
router.include_router(role.router, tags=["role"])
