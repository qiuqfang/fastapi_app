from domain.user import CreateUser
from util import result
from fastapi import APIRouter, Query

from service import user_service

userRouter = APIRouter()


@userRouter.get("/get_user", summary="通过用户id获取用户")
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return result.ok(data=user, message='没有该用户')
    return result.ok(data=user)


@userRouter.post("/create_user", summary="创建用户")
def create_user(user: CreateUser):
    user_service.create_user(user)
    return result.ok(data=user, message="添加成功")
