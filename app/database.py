from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.logger import logger

DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = None
    try:
        logger.info("Creating new database session...")
        db = SessionLocal()
        yield db
    except Exception as e:
        logger.error(f"Failed to create database session: {e}")
        raise
    finally:
        if db:
            db.close()
            logger.info("Database session closed.")
