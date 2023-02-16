from fastapi import APIRouter
from util import result

router = APIRouter()


@router.get("/", summary="FastAPI")
def index():
    return result.ok(data={})
