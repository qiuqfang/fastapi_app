from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

from controller.index import router
from util import result
from controller.user import userRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(exc, exc.errors()[0]["msg"])
    return JSONResponse(content=result.failure(message=exc.errors()[0]["msg"]))


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router)
app.include_router(userRouter, tags=["用户"])
