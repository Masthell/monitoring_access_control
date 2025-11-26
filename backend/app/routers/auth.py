from fastapi import APIRouter, Depends, HTTPException  # ← все импорты
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User  # ← импорт модели
from app.schemas.user import UserLogin  # ← импорт схемы
from app.core.security import verify_password  # ← импорт безопасности

router = APIRouter()  # ← создаем router!

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"access_token": "token future"}