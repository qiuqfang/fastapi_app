# coding: utf-8
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(32))
    email = Column(VARCHAR(32), unique=True)
    password = Column(VARCHAR(32))
    is_active = Column(TINYINT(1))
