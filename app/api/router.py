from fastapi import APIRouter

from app.api.v1 import dev
from app.api.v1 import post

api_router = APIRouter()

api_router.include_router(dev.router, prefix="/v1")
api_router.include_router(post.router, prefix="/v1")