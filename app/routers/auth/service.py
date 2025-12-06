from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.routers.auth.utils import hash_password, verify_password
from app.logger import logger  # <-- use logger


def create_user(user: schemas.UserCreate, db: Session):
    logger.info(f"🔍 Checking if user exists | email={user.email}")

    try:
        existing = db.query(models.User).filter(models.User.email == user.email).first()

        if existing:
            logger.warning(f"⚠️ User already exists | email={user.email}")
            raise HTTPException(status_code=400, detail="Email already registered")

        logger.info("🔐 Hashing password...")
        hashed_pw = hash_password(user.password)

        logger.info("🧱 Creating new user in database...")
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=hashed_pw
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        logger.info(f"✅ User created successfully | email={new_user.email}")
        return new_user

    except HTTPException:
        raise  # FastAPI will handle it

    except Exception as e:
        logger.exception(f"🔥 Failed to create user | email={user.email} | error={e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def authenticate_user(email: str, password: str, db: Session):
    logger.info(f"🔍 Authenticating user | email={email}")

    try:
        user = db.query(models.User).filter(models.User.email == email).first()

        if not user:
            logger.warning(f"❌ User not found | email={email}")
            return None

        logger.info("🔐 Verifying password...")
        if not verify_password(password, user.password):
            logger.warning(f"❌ Password mismatch | email={email}")
            return None

        logger.info(f"✅ Authentication successful | email={email}")
        return user

    except Exception as e:
        logger.exception(f"🔥 Authentication error | email={email} | error={e}")
        return None
