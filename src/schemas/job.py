import os
from typing import Optional
from pydantic import BaseModel


class JobBase(BaseModel):
    access_token: Optional[str] = os.getenv('TRANSVIP_TOKEN','173b2181da40801736acc8ac14df23c4')

class JobUpdateStatus(JobBase):
    job_status: int
    job_id: str
    cancellation_reason: str
    cancellation_description: str
    cancellation_reason_id: int
    cancelled_by:int
