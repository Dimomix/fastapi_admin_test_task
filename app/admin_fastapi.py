import os
import redis.asyncio as aioredis
from fastapi import FastAPI
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from fastapi_admin.resources import Model
from fastapi_admin.widgets import filters, inputs, displays

from .config import settings
from .models_tortoise import AdminUser, Settings
from .security import verify_password  
from .config import settings
async def init_fastapi_admin(app: FastAPI):
    redis = aioredis.from_url(
        settings.redis_dsn,
        encoding="utf8",
        decode_responses=True,
        max_connections=10
        )

    await admin_app.init(
        app=app,
        redis=redis,
        login_provider=UsernamePasswordProvider(
            admin_model=AdminUser,
            username_field="username",
            password_field="password",
            verify_password=verify_password,  
        ),
        template_folders=[os.path.join(os.getcwd(), "templates")],
        title="Админка сервиса",
    )

    @admin_app.register
    class SettingsResource(Model):
        label = "Настройки пользователей"
        model = Settings

        filters = [
            filters.Search(name="support_email", label="Поиск по Email"),
        ]

        fields = {
            "user_id": displays.DisplayField(label="User ID"),
            "service_enabled": inputs.Switch(label="Сервис включён"),
            "support_email": inputs.Input(label="Email поддержки"),
        }
