from sqlalchemy import Boolean, Column, Integer, String

from database import Base, engine


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(32), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)
