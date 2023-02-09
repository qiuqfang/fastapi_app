from sqlalchemy.orm import Session

from model.user import User
from database import SessionLocal


def getUserById(user_id: int, db: Session = SessionLocal()):
    return db.query(User).filter(User.id == user_id).first()
