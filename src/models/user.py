from models import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(255))
    rol_id = Column(Integer, ForeignKey("rol.id",onupdate='CASCADE' ,ondelete='RESTRICT'), nullable=True)
    rol = relationship("Rol")
