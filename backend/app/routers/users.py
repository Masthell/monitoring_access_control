from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession  
from sqlalchemy import select  
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password 
from app.core.dependencies import get_current_user
from app.core.exceptions import ( 
    EmailAlreadyExistsException,
    UserNotFoundException
)

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)): 
    # ПРОВЕРКА на существующего пользователя 
    result = await db.execute(select(User).where(User.email == user_data.email)) 
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise EmailAlreadyExistsException()  
    
    hashed_password = hash_password(user_data.password)  
    
    db_user = User(
        email=user_data.email,
        password=hashed_password,
        full_name=user_data.full_name,
        role=user_data.role or "user"
    )
    
    db.add(db_user)
    await db.commit()  
    await db.refresh(db_user)  
    return db_user

@router.get("/users/me", response_model=UserResponse)  
async def get_current_user_info(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)  
):  
    user_id = int(current_user["sub"])
    
    # Получаем полный объект пользователя из БД
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise UserNotFoundException()  
    
    return user  

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """Получить пользователя по ID"""
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise UserNotFoundException()
    
    return user