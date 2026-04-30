from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.dependencies import get_db
from app.models.post import Post
from app.schemas.post import PostBase, PostResponse, PostCreate

router = APIRouter(prefix="/post", tags=["post"])

@router.get(
    "",
    #response_model=PostResponse
)
async def get_all_posts(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Post))
    return result.scalars().all()

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PostResponse,
)
async def create_post(
        data: PostCreate,
        db: AsyncSession = Depends(get_db),
):
    post = Post(**data.model_dump())
    db.add(post)
    await db.commit()
    return post