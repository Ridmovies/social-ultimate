from fastapi import APIRouter

router = APIRouter(prefix="/dev", tags=["dev"])


@router.get("/hello")
def ping():
    return {"message": "pong"}