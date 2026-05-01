from fastapi import APIRouter

from app.api.v1 import post, user
from app.api.v1 import dev

api_router = APIRouter()

api_router.include_router(user.router, prefix="/v1")
api_router.include_router(post.router, prefix="/v1")
api_router.include_router(dev.router, prefix="/v1")