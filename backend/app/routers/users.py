from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password 

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):  # ← user_data определена!
    hashed_password = hash_password(user_data.password)  
    
    db_user = User(
        email=user_data.email,
        password=hashed_password,
        full_name=user_data.full_name,
        role=user_data.role or "user"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from app.core.dependencies import get_current_user

@router.get("/users/me")
def get_current_user_info(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Это защищенный эндпоинт!",
        "user_data": current_user
    }