from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./blog.db"

# connect_args needed for SQLite
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = None
    try:
        print("[INFO] Creating new database session...")
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"[ERROR] Failed to create database session: {e}")
        raise e
    finally:
        if db:
            db.close()
            print("[INFO] Database session closed.")
