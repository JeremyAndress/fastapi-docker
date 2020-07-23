from fastapi import APIRouter
from schemas.token import BasicToken
from schemas.job import JobUpdateStatus
from .controller import get_booking_info, change_job_status_admin
router = APIRouter()

@router.post("/CAB/testing")
def firts(id: int, token: BasicToken):
    r = get_booking_info(id)
    return r.json()
    
@router.post("/CAB/testing/job")
def second(job: JobUpdateStatus, token: BasicToken):
    r = change_job_status_admin(job)
    return r.json()