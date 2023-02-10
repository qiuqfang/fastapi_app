from domain.user import CreateUser
from util import result
from fastapi import APIRouter

from service import user as user_service

userRouter = APIRouter()


@userRouter.get("/get_user", description="通过用户id获取用户")
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return result.ok(data=user, message='没有该用户')
    return result.ok(data=user)


@userRouter.post("/create_user")
def create_user(user: CreateUser):
    return result.ok(data=user)
