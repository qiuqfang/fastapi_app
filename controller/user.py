from util import result
from fastapi import APIRouter


from service import user as userService

userRouter = APIRouter()


@userRouter.get("/getUserById")
def getUserById(userId: int):
    user = userService.getUserById(userId)
    return result.ok(user)
