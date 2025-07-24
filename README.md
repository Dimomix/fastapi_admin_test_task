FastAPI Admin Test Task
Проект демонстрирует асинхронный REST API на FastAPI с JWT-авторизацией, CRUD-эндпоинтами для пользовательских настроек и встроенной админкой на SQLAdmin.

⚙️ Функциональность
Регистрация и аутентификация
– /auth/register (POST)
– /auth/login (POST, OAuth2PasswordRequestForm)

Параметры пользователя
– GET /settings/ — получить текущие настройки (service_enabled, support_email)
– PUT /settings/ — изменить настройки

Пользовательские данные
– GET /users/me — информация о текущем юзере

Swagger-UI
– http://localhost:8000/docs
– кнопка Authorize → OAuth2 Password Flow

SQLAdmin
– UI-админка CRUD для моделей User и UserSettings
– http://localhost:8000/admin/

Healthcheck
– GET /healthz возвращает {"status":"ok"}

🧰 Технологии
Python 3.11+

FastAPI

SQLAlchemy 2.x (asyncio) + SQLite / PostgreSQL

Pydantic v2

JWT via python-jose

Passlib (bcrypt)

SQLAdmin (админ-панель)

Docker & docker-compose (опционально)

📋 Предварительные требования
Python 3.11+ или Docker

Если работаете без Docker:

Установить зависимости из requirements.txt

Для работы с Postgres в .env:

ini
Копировать
Редактировать
DB_URL=postgresql+asyncpg://appuser:apppass@db:5432/appdb
Для SQLite (по умолчанию):

ini
Копировать
Редактировать
DB_URL=sqlite+aiosqlite:///./app.db
🚀 Установка (локально)
Клонировать репозиторий

bash
Копировать
Редактировать
git clone https://…/fastapi-admin-test-task.git
cd fastapi-admin-test-task
Создать и активировать виртуальное окружение

bash
Копировать
Редактировать
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
Установить зависимости

bash
Копировать
Редактировать
pip install --upgrade pip
pip install -r requirements.txt
Создать файл .env (можно скопировать из .env.example) и указать:

ini
Копировать
Редактировать
DB_URL=sqlite+aiosqlite:///./app.db
JWT_SECRET=ВАШ_СЕКРЕТ
JWT_ALG=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
Запустить приложение

bash
Копировать
Редактировать
uvicorn app.main:app --reload