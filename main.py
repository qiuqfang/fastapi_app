from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

from controller.index_controller import router
from middleware import cors_middleware
from redis import register_redis
from util import result
from controller.user_controller import userRouter

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(dict(request)["headers"])
    print(exc, exc.errors()[0]["msg"])
    return JSONResponse(content=result.failure(message=exc.errors()[0]["msg"]))


cors_middleware(app)

register_redis(app)

app.include_router(router=router)
app.include_router(userRouter, tags=["用户"])
