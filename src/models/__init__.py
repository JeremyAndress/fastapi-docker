from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .rol import Rol # noqa: F401 
from .user import User # noqa: F401 
 