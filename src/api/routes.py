from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/CAB/testing")
def firts(id: int,token: str = Depends(oauth2_scheme)):
    return {
        "id": id,
        "status": 200
    }