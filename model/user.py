from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base, engine


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    email = Column(String(32), unique=True)
    password = Column(String(32))
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)
