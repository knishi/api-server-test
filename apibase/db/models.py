from oslo_db.sqlalchemy import models
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

class _Base(models.ModelBase):
    pass

Base = declarative_base(cls=_Base)

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
