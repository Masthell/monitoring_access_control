from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:  # ← исправлено pasword → password
    """Хеширует пароль"""
    return pwd_context.hash(password)  # ← теперь password определена

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяет пароль хешем"""
    return pwd_context.verify(plain_password, hashed_password)