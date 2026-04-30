# Минимум для поста:
#
# id
# author_id (FK)
# content
# created_at
# updated_at
# возможно: is_deleted / visibility
#
# Сразу закладываются:
#
# индексы (author_id, created_at)
# связи (relationship с User)
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String)
