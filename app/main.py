from fastapi import FastAPI

from app.api.router import api_router

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # LIFESPAN MANAGER (жизненный цикл приложения FastAPI)

    # Этот декоратор создаёт контекст, который управляет:
    # 1. запуском приложения (startup phase)
    # 2. завершением приложения (shutdown phase)

    # ----------------------------
    # STARTUP PHASE (до yield)
    # ----------------------------

    # Здесь выполняется код один раз при запуске сервера:
    # - подключение к БД
    # - инициализация кеша (Redis)
    # - загрузка конфигураций
    # - запуск фоновых сервисов

    print("🚀 Starting application...")

    # yield = точка, где приложение "живёт"
    # FastAPI начинает обрабатывать HTTP запросы

    await init_db()

    yield

    # ----------------------------
    # SHUTDOWN PHASE (после yield)
    # ----------------------------

    # Этот код выполняется при остановке приложения:
    # - закрытие соединений с БД
    # - остановка фоновых задач
    # - освобождение ресурсов

    print("🛑 Shutting down application...")


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix="/api")