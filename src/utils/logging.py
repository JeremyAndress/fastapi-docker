import os
import uuid
import logging
from logging.handlers import RotatingFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILENAME_INFO = BASE_DIR+'/logs/info.log'

logging.basicConfig(
    handlers=[
        logging.StreamHandler(),
        RotatingFileHandler(LOG_FILENAME_INFO, maxBytes=20000, backupCount=10)
    ],
    level=logging.INFO, 
    format= '[%(asctime)s] [%(pathname)s:%(lineno)d] [%(levelname)s] - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logger = logging.getLogger("launchpad")

def gene_extra(ms):
    return {
        'id':str(uuid.uuid4()),
        'msisdn': ms
    }