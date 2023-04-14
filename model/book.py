from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base, engine


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(32), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)
