import os
import requests
from schemas.job import JobUpdateStatus
url_transvip = os.getenv('TRANSVIP_URL','http://staging-api.transvip.cl/')
token_transvip = os.getenv('TRANSVIP_TOKEN','173b2181da40801736acc8ac14df23c4')

def get_booking_info(job_id:int):
    endpoint = 'get_booking_info'
    url = f'{url_transvip}{endpoint}?access_token={token_transvip}&job_id={job_id}'
    response = requests.get(url)
    return response

def change_job_status_admin(job:JobUpdateStatus):
    print(job)
    endpoint = 'change_job_status_admin'
    url = f'{url_transvip}{endpoint}'
    response = requests.post(url)
    return response