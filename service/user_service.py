from crud import user_crud
from domain.user import CreateUser


def get_user_by_id(user_id: int):
    return user_crud.get_user_by_id(user_id)


def create_user(data: CreateUser):
    user_crud.create_user(data)
