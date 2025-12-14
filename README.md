# Monitoring Access Control

Система управления доступом и мониторингом  проект создавался в целях изучения технологий
Это внутренняя система для контроля и мониторинга доступа пользователей и безопасностью.

## Технологии

- **Backend**: Python, FastAPI, MySQL
- **Frontend**: React, TypeScript, Tailwind CSS
- Monitoring Stack: Docker, Node Exporter, Prometheus, Grafana

# Структура проекта
```
auth-system/
├── backend/           # FastAPI приложение
├── frontend/          # React интерфейс
├── monitoring/                 # Docker-мониторинг
│   ├── docker-compose.yml
│   ├── prometheus.yml
│   ├── grafana/
│   │   └── provisioning/
│   │       └── datasources/
│   │           └── datasource.yml
├── alembic.ini        # конфиг миграций (НЕ коммитить!)
└── .env               # переменные окружения (НЕ коммитить!)
```

## Пример интерфейса

![авторизация](./screenshots/image.png)
![регистрация](./screenshots/imagecopy.png)

## 1. Клонирование и настройка

```bash
git clone <URL-репозитория>
cd monitoring_access_control
Создать виртуальное окружение
python -m venv .venv
```
![5330313070611467450](https://github.com/user-attachments/assets/f9538b0b-c7ad-41dd-a292-04a46b455549)
![5330313070611467683](https://github.com/user-attachments/assets/15a1184c-e486-4838-b1b8-febfaf932839)


# Windows
.venv\Scripts\Activate

# Linux/Mac
source .venv/bin/activate

Установить зависимости
```bash
pip install -r requirements.txt
Шаблоны конфигурации
.env.example → .env
```


Отредактируйте файлы с вашими данными:
alembic.example.ini → alembic.ini
.env – настройки приложения:

env
Копировать код
DATABASE_URL=mysql+pymysql://ваш_username:ваш_пароль@localhost:3306/monitoring_access_db
SECRET_KEY=ваш_длинный_секретный_ключ_не_менее_32_символов
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
alembic.ini – миграции базы данных:

ini
sqlalchemy.url = mysql+pymysql://ваш_username:ваш_пароль@localhost:3306/monitoring_access_db


2. Настройка базы данных
Применяем миграции:
alembic upgrade head


3. Запуск приложения
Backend
```bash
Копировать код
cd backend
uvicorn app.main:app --reload
```

Доступ к приложению:
Главная: http://localhost:8000
Документация API (Swagger): http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

4. Безопасность конфигурации
Файлы, которые НИКОГДА нельзя коммитить:
.env – содержит пароли БД и секретные ключи
alembic.ini – содержит строку подключения к БД

5. Управление базой данных
Создать новую миграцию:
```
alembic revision --autogenerate -m "Описание изменений"
Применить миграции:

alembic upgrade head
Проверить текущую миграцию:
alembic current
```

История миграций: alembic history

Важное примечание о безопасности
Проект использует переменные окружения для конфиденциальных данных.
НЕ КОММИТЬ файлы с паролями или секретными ключами.


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

## Запуск системы мониторинга
```
Перейти в папку мониторинга
cd monitoring

# Запустить Docker-контейнеры
docker-compose up -d
Доступ к мониторингу:

Node Exporter (метрики): http://localhost:9100/metrics

Prometheus (база метрик): http://localhost:9090

Grafana (дашборды): http://localhost:3000

Логин: admin

Пароль: admin

6. Автоматическая настройка Grafana
После запуска Grafana:

Откройте http://localhost:3000

Добавьте источник данных Prometheus:

URL: http://prometheus:9090

Импортируйте готовый дашборд:

ID: 1860 (Node Exporter Full)

Выберите источник данных Prometheus
```

Архитектура системы
```
Ваше приложение (Python/React)
      │
      ├───► MySQL Database
      │
      └───► Monitoring Stack
              ├───► Node Exporter (системные метрики)
              ├───► Prometheus (сбор и хранение)
              └───► Grafana (визуализация)
```

Запуск
cd monitoring
docker-compose up -d

Просмотр логов
docker-compose logs -f

Остановка
docker-compose down

Перезапуск
docker-compose restart

Проверка статуса
docker-compose ps


# Что реализовано
Регистрация и вход пользователей
JWT аутентификация (access + refresh токены)
Миграции базы данных через Alembic
Документированное API (Swagger/ReDoc)
Базовый фронтенд на React
мониторинг и докер компос

# Безопасность
Важно: Файлы .env и alembic.ini с чувствительными данными никогда не должны попадать в репозиторий. Используйте .env.example и alembic.example.ini как шаблоны.
