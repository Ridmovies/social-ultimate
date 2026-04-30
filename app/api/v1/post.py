from fastapi import APIRouter, Depends
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.dependencies import get_db
from app.models.post import Post
from app.schemas.post import PostResponse, PostCreate, PostPatch, PostPut

router = APIRouter(prefix="/posts", tags=["post"])

@router.get(
    "",
    response_model=list[PostResponse]
)
async def get_all_posts(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Post))
    return result.scalars().all()

@router.post(
    "",
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


@router.get(
    "/{post_id}",
    response_model=PostResponse,
)
async def get_post_by_id(
        post_id: int,
        db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Post).where(Post.id == post_id))
    return result.scalars().one_or_none()


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
        post_id: int,
        db: AsyncSession = Depends(get_db),
):
    stmt = delete(Post).where(Post.id == post_id)
    await db.execute(stmt)
    await db.commit()


@router.put("/{post_id}", response_model=PostResponse)
async def put_post(
        post_id: int,
        data: PostPut,
        db: AsyncSession = Depends(get_db),
) -> Post | None:

    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalars().one_or_none()

    if not post:
        return None

    update_data = data.model_dump(exclude_unset=False)

    for key, value in update_data.items():
        setattr(post, key, value)

    await db.commit()

    return post


@router.patch("/{post_id}", response_model=PostResponse)
async def patch_post(
        post_id: int,
        data: PostPatch,
        db: AsyncSession = Depends(get_db),
) -> Post | None:

    result = await db.execute(select(Post).where(Post.id == post_id))
    post = result.scalars().one_or_none()

    if not post:
        return None

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(post, key, value)

    await db.commit()

    return post
