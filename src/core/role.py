import os
from enum import Enum


class ROLE(Enum):
    ADMIN: str = os.getenv('ADMIN')
