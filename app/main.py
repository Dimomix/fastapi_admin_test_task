from fastapi import FastAPI
from .config import settings
from .db import engine, Base
from .routers import auth, settings as settings_router, users
from .admin import init_admin

app = FastAPI(title="MyApp with SQLAdmin", version="0.1.0")

@app.on_event("startup")
async def on_startup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router)
app.include_router(settings_router.router)
app.include_router(users.router)

# UI‑админка
init_admin(app)

@app.get("/healthz", include_in_schema=False)
async def healthz():
    return {"status": "ok"}
