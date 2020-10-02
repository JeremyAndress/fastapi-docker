from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .rol import Rol
from .user import User
