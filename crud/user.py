from fastapi import Depends
from sqlalchemy.orm import Session

from model.user import User
from database import get_db


def get_user_by_id(user_id: int, db: Session = get_db()):
    return db.query(User).filter(User.id == user_id).first()
