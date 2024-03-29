from domain.user import CreateUser
from config.models import User
from config.database import db


def get_user_by_id(user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(data: CreateUser):
    user = User(name=data.name, email=data.email, password=data.password,
                is_active=data.is_active)
    db.add(user)
    db.commit()
