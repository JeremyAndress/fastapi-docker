from models import Base
from sqlalchemy import Column, Integer, String


class Rol(Base):
    __tablename__ = 'rol'
    id = Column(Integer, primary_key=True)
    name = Column(String)
