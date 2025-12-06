from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app import schemas
from app.routers.auth.service import create_user, authenticate_user
from app.routers.auth.token import create_access_token
from app.logger import logger  # <-- use logger

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger.info("➡️ /auth/register endpoint called")
    logger.info(f"Register attempt | email={user.email}")

    try:
        created_user = create_user(user, db)

        logger.info(f"✅ User registered successfully | email={created_user.email}")

        return {"message": "User registered successfully"}

    except HTTPException as http_error:
        logger.warning(
            f"⚠️ HTTPException during registration | email={user.email} | detail={http_error.detail}"
        )
        raise

    except Exception as e:
        logger.exception(f"🔥 Unexpected error during registration | email={user.email} | error={e}")
        raise HTTPException(status_code=500, detail="Internal server error")
