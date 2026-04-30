# app/models/base.py

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    # Базовый класс для всех ORM моделей SQLAlchemy

    # DeclarativeBase включает:
    # - систему регистрации моделей
    # - metadata (описание всех таблиц)
    # - связь Python классов с таблицами БД

    pass