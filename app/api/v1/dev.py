from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import AsyncSessionLocal

router = APIRouter(prefix="/dev", tags=["dev"])


@router.get("/hello")
def ping():
    return {"message": "pong"}


@router.get("/check")
async def check():
    async with AsyncSessionLocal() as session:
        return await session.execute(text("SELECT 1"))