from fastapi import APIRouter

from app.api.v1 import dev

api_router = APIRouter()

api_router.include_router(dev.router, prefix="/v1")