from pydantic import BaseModel


class PostBase(BaseModel):
    content: str


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int