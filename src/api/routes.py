from fastapi import APIRouter
from schemas.token import BasicToken
from .controller import get_booking_info
router = APIRouter()

@router.post("/CAB/testing")
def firts(id: int, token: BasicToken):
    r = get_booking_info(id)
    return r.json()
    