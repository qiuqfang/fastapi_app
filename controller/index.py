from fastapi import APIRouter
from util import result

router = APIRouter()


@router.get("/")
def index():
    return result.ok(data={})
