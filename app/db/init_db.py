# app/db/init_db.py

from app.db.session import engine
from app.models.base import Base
from app.models import post  # важно: импорт модели обязателен

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print(f"Base.metadata.drop_all")
        await conn.run_sync(Base.metadata.create_all)
        print(f"Base.metadata.create_all")