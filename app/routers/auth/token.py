from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.logger import logger  # <-- logger added

SECRET_KEY = "n4Qk8dY2vE+0R7pFx9uT1lWs3BqH5oZg2VbX4cMd7sKqP0rEj6TfGhWwY8pLa9Zm"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login", scheme_name="JWT")


def create_access_token(data: dict):
    logger.info("🔐 Creating access token...")

    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode["exp"] = expire

        logger.info(f"📝 Token payload before encoding | payload={to_encode}")

        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        logger.info("✅ Token generated successfully")
        return token

    except Exception as e:
        logger.exception(f"🔥 Failed to create access token | error={e}")
        raise HTTPException(status_code=500, detail="Failed to create token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    logger.info("🔍 Verifying JWT token...")

    try:
        logger.info(f"📥 Received token | token={token}")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        logger.info(f"📤 Decoded payload | payload={payload}")

        email: str = payload.get("sub")

        if email is None:
            logger.warning("⚠️ Token payload missing email (sub)")
            raise HTTPException(status_code=401, detail="Invalid token")

        logger.info(f"✅ Authenticated user | email={email}")
        return email

    except JWTError as e:
        logger.warning(f"❌ Invalid JWT token | error={e}")
        raise HTTPException(status_code=401, detail="Invalid token")

    except Exception as e:
        logger.exception(f"🔥 Unexpected error verifying token | error={e}")
        raise HTTPException(status_code=500, detail="Internal server error")
