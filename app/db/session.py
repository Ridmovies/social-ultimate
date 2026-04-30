# app/db/session.py

from sqlalchemy.ext.asyncio import (
    create_async_engine,      # создаёт "движок" подключения к БД (пул соединений + драйвер)
    async_sessionmaker,       # фабрика, которая создаёт сессии (контекст работы с БД)
    AsyncSession              # тип асинхронной сессии SQLAlchemy
)

from app.core.config import settings  # централизованная конфигурация (DATABASE_URL и др.)


# ENGINE — это уровень инфраструктуры
# Он НЕ выполняет SQL напрямую, а управляет подключениями к базе данных
engine = create_async_engine(
    settings.DATABASE_URL,  # строка подключения к PostgreSQL (asyncpg драйвер)
    echo=False,             # True = лог всех SQL запросов (используется только для отладки)
)


# SESSION FACTORY — создаёт сессии для работы с БД
# каждая сессия = один "контекст запроса" (unit of work)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,              # привязка к engine (использовать этот пул соединений)
    class_=AsyncSession,      # создаваемый объект будет AsyncSession
    expire_on_commit=False,   # после commit объекты не "протухают" (не делают reload из БД)
)