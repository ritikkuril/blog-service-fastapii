from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.routers.auth.utils import hash_password, verify_password


def create_user(user: schemas.UserCreate, db: Session):
    try:
        print(f"[SERVICE] Checking if user exists: {user.email}")
        existing = db.query(models.User).filter(models.User.email == user.email).first()

        if existing:
            print("[SERVICE] User already exists!")
            raise HTTPException(status_code=400, detail="Email already registered")

        print("[SERVICE] Hashing user password...")
        hashed_pw = hash_password(user.password)

        print("[SERVICE] Creating new user in DB...")
        new_user = models.User(
            name=user.name,
            email=user.email,
            password=hashed_pw
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        print(f"[SERVICE] New User Created: {new_user.email}")
        return new_user

    except HTTPException:
        # re-raise HTTP exceptions so FastAPI handles them
        raise
    except Exception as e:
        print(f"[SERVICE ERROR] Failed to create user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


def authenticate_user(email: str, password: str, db: Session):
    try:
        print(f"[SERVICE] Authenticating user: {email}")
        user = db.query(models.User).filter(models.User.email == email).first()

        if not user:
            print("[SERVICE] User not found!")
            return None

        print("[SERVICE] Checking password...")
        if not verify_password(password, user.password):
            print("[SERVICE] Password mismatch!")
            return None

        print("[SERVICE] User authenticated successfully")
        return user

    except Exception as e:
        print(f"[SERVICE ERROR] Failed to authenticate user: {e}")
        return None  # safely return None if any error occurs
