# auth-system

Система аутентификации (frontend + backend).  
Изначально задумывался как система поддержки, но на текущем этапе реализована базовая аутентификация с возможностью расширения.

## Стек
- **Backend:** Python, FastAPI, JWT, MySQL
- **Frontend:** React, TypeScript, Tailwind CSS
- **Миграции:** Alembic

## Быстрый старт
```
# Клонирование
git clone <URL-репозитория>
cd auth-system

# Настройка окружения
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или .venv\Scripts\activate  # Windows

# Зависимости
pip install -r requirements.txt

# Настройка конфигов (скопировать и заполнить)
cp .env.example .env
cp alembic.example.ini alembic.ini

# Миграции БД
alembic upgrade head
```

# Запуск
cd backend
uvicorn app.main:app --reload
После запуска:

Приложение: http://localhost:8000
Документация API: http://localhost:8000/docs

# Структура проекта
```
auth-system/
├── backend/           # FastAPI приложение
├── frontend/          # React интерфейс
├── alembic.ini        # конфиг миграций (НЕ коммитить!)
└── .env               # переменные окружения (НЕ коммитить!)
```

# Что реализовано
Регистрация и вход пользователей
JWT аутентификация (access + refresh токены)
Миграции базы данных через Alembic
Документированное API (Swagger/ReDoc)
Базовый фронтенд на React

# Безопасность
Важно: Файлы .env и alembic.ini с чувствительными данными никогда не должны попадать в репозиторий. Используйте .env.example и alembic.example.ini как шаблоны.
