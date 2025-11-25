from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# СИНХРОННАЯ версия с pymysql
DATABASE_URL = "mysql+pymysql://root:#mila2008@localhost:3306/support_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()