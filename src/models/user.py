from models import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    rol_id = Column(Integer, ForeignKey("rol.id", ondelete='cascade'), nullable=True)
    rol = relationship("Rol")
