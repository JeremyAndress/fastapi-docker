from typing import Any
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import as_declarative, declared_attr
# Base = declarative_base()

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()