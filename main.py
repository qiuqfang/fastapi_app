from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from util import result
from controller.user import userRouter

app = FastAPI()

app.include_router(userRouter)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content=result.failure(message="请求参数有误！"))


@app.get("/")
def main():
    return "FastAPI-App"
