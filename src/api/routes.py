from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def firts():
    return {"status": "ok"}