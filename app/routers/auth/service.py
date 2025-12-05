from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas
from app.routers.auth.utils import hash_password, verify_password


def create_user(user: schemas.UserCreate, db: Session):
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



