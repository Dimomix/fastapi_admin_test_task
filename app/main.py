import asyncio
from fastapi import FastAPI
from .db import engine, Base
from .routers import auth, settings, users
from .admin import init_admin  # если используешь админку

app = FastAPI(title="Test Task API", version="0.1.0")

# Подключаем роутеры
app.include_router(auth.router)
app.include_router(settings.router)
app.include_router(users.router)

# Инициализация sqladmin UI (опционально)
init_admin(app)

@app.on_event("startup")
async def on_startup():
    # создаём таблицы (для теста без alembic)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
