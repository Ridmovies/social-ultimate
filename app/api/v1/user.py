import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.user import UserRead, UserCreate, UserPatch

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserRead, status_code=201)
async def create_user(
        user_in: UserCreate,
        db: AsyncSession = Depends(get_db),
):
    user = User(email=user_in.email, password_hash=user_in.password)
    db.add(user)

    await db.commit()
    return user


@router.patch(
    "/{user_id}",
    response_model=UserRead,
    status_code=200
)
async def patch_user(
        user_id: uuid.UUID,
        user_patch: UserPatch,
        db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")


    update_data = user_patch.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(user, key, value)

    user.updated_at = datetime.now(timezone.utc)

    await db.commit()

    return user




