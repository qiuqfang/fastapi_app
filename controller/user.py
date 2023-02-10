from util import result
from fastapi import APIRouter

from service import user as user_service

userRouter = APIRouter()


@userRouter.get("/getUserById")
def get_user_by_id(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return result.ok(data=user, message='没有该用户')
    return result.ok(data=user)
