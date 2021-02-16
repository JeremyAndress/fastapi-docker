from uuid import uuid4 as v4
from sqlalchemy import Column
from .uuid import UUIDType


class MixinGetById(object):
    id = Column(UUIDType(binary=False), primary_key=True, default=v4)

    @classmethod
    def get_by_id(cls, id: v4):
        return cls.session.query(cls).filter(cls.id == id).first()
