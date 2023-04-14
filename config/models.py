# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    email = Column(String(32), unique=True)
    password = Column(String(32))
    is_active = Column(TINYINT(1))
