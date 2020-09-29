from fastapi import APIRouter

router = APIRouter()

@router.get("/yyn/")
def firts(id: int):
    return {'id':id}
