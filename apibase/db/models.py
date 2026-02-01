import datetime
from oslo_db.sqlalchemy import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

class _Base(models.ModelBase):
    def to_dict(self):
        """Simple model to dict conversion."""
        res = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, datetime.datetime):
                value = value.isoformat()
            res[column.name] = value
        return res

Base = declarative_base(cls=_Base)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
