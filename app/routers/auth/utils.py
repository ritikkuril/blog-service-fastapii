import bcrypt
from app.logger import logger  # <-- add logger


def hash_password(password: str) -> str:
    try:
        if not password:
            logger.error("❌ Password is empty during hashing")
            raise ValueError("Password cannot be empty")

        logger.info("🔐 Hashing password...")
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        logger.info("✅ Password hashed successfully")
        return hashed.decode("utf-8")

    except Exception as e:
        logger.exception(f"🔥 Failed to hash password | error={e}")
        raise e  # re-raise for service layer to catch


def verify_password(plain: str, hashed: str) -> bool:
    try:
        if not plain or not hashed:
            logger.error("❌ Empty password or hash provided for verification")
            raise ValueError("Plain password or hashed password is empty")

        logger.info("🔍 Verifying password...")
        result = bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))

        logger.info(f"🔎 Password verification result | match={result}")
        return result

    except Exception as e:
        logger.exception(f"🔥 Failed to verify password | error={e}")
        return False  # safer fallback
