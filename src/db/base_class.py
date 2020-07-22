import re
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        name = re.sub( '(?<!^)(?=[A-Z])', '_', cls.__name__ ).lower()
        return f'{name}s'