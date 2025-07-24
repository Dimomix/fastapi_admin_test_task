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





git clone https://…/fastapi-admin-test-task.git
cd fastapi-admin-test-task
Создать и активировать виртуальное окружение

ь
python -m venv .venv

source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
Установить зависимости


pip install --upgrade pip
pip install -r requirements.txt
Создать файл .env (можно скопировать из .env.example) и указать:
REDIS_DSN = redis://:yourpassword@redis.example.com:6379/2



uvicorn app.main:app --reload
