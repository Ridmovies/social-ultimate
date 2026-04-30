from fastapi import APIRouter

from app.schemas.post import PostBase, PostResponse

router = APIRouter(prefix="/post", tags=["post"])

@router.get(
    "",
    #response_model=PostResponse
)
async def get_all_posts():
    pass