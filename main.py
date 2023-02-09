from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from controller.user import userRouter

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(str(request.get('query_string'), "utf-8"))

    return JSONResponse(content={})


app.include_router(userRouter)


@app.get("/")
def main():
    return "FastAPI-Demo"
