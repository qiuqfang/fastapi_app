from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from controller.index_controller import router
from config.middleware import cors_middleware
from config.redis import register_redis
from util import result
from controller.user_controller import userRouter

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content=result.failure(message=exc.errors()[0]["msg"]))


cors_middleware(app)

register_redis(app)

app.include_router(router=router)
app.include_router(userRouter, tags=["用户"])
