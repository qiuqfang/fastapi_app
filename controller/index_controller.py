from fastapi import APIRouter, Request

from util import result

router = APIRouter()


@router.get("/", summary="FastAPI")
async def index(request: Request):
    await request.app.state.redis.set("111", 222)
    return result.ok(data={})
