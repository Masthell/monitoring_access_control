from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):

    # Обязательные настройки (будут искаться в .env файле)
    DATABASE_URL: str  # URL для подключения к базе данных
    SECRET_KEY: str    # Секретный ключ для JWT токенов
    
    # Настройки со значениями по умолчанию
    ALGORITHM: str = "HS256"                    # Алгоритм шифрования JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30       # Время жизни токена
    
    class Config:
        env_file = ".env"  # Указываем файл с переменными окружения
        case_sensitive = False  # Регистронезависимые переменные

# Создаём экземпляр настроек для импорта в других модулях
settings = Settings()