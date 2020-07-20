from fastapi import APIRouter
router = APIRouter()

@router.get("/CAB/testing")
def firts(id: int):
    return {
        "id": id,
        "status": 200
    }