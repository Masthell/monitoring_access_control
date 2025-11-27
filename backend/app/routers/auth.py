from fastapi import APIRouter, Depends, HTTPException  
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User  
from app.schemas.user import UserLogin, UserCreate, UserResponse
from app.core.security import verify_password, create_access_token, hash_password
from app.core.dependencies import get_current_user

router = APIRouter()  

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    
    if not user or not verify_password(user_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "email": user.email
    }

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
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

@router.get("/me", response_model=UserResponse)
def get_current_user_info(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    user_id = int(current_user["sub"]) # из токена айди пользователя получить
    user = db.query(User).filter(User.id == user.id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user