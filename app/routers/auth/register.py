from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.database import get_db
from app import schemas
from app.routers.auth.service import create_user, authenticate_user
from app.routers.auth.token import create_access_token


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("[ROUTE] /auth/register hit")
    created_user = create_user(user, db)
    print(f"[ROUTE] User registered: {created_user.email}")
    return {"message": "User registered successfully"}
