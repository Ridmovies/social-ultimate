import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserPatch(BaseModel):
    email: EmailStr | None = None



class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime