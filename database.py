from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

DATABASE_URL = settings.DATABASE_URL

# ✅ PostgreSQL uchun connection pool sozlamalari qo'shildi
engine = create_engine(
    DATABASE_URL,
    pool_size=5,        # Bir vaqtda max 5 ta ulanish
    max_overflow=10,    # Qo'shimcha 10 ta ulanish ruxsat
    pool_timeout=30,    # 30 soniyadan keyin timeout
    pool_recycle=1800,  # 30 daqiqada ulanishni yangilaydi (PostgreSQL uzib qo'ymasligi uchun)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
