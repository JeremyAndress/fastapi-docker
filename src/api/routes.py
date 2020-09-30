from fastapi import APIRouter
from .gem.user import user

router = APIRouter()
router.include_router(user.router, tags=["user"])