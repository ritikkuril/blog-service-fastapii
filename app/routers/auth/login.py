from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.auth.service import authenticate_user
from app.routers.auth.token import create_access_token
from app.logger import logger

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    logger.info("➡️ /auth/login endpoint called")
    logger.info(f"Login attempt | username={form_data.username}")

    try:
        user = authenticate_user(form_data.username, form_data.password, db)

        if not user:
            logger.warning(
                f"❌ Authentication failed | username={form_data.username}"
            )
            raise HTTPException(status_code=400, detail="Invalid email or password")

        token = create_access_token({"sub": user.email})
        logger.info(f"✅ JWT generated | user={user.email}")

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except HTTPException as http_error:
        logger.error(f"HTTPException during login | detail={http_error.detail}")
        raise

    except Exception as e:
        logger.exception(f"🔥 Unexpected error in login: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
