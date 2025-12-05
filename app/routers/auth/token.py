from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "n4Qk8dY2vE+0R7pFx9uT1lWs3BqH5oZg2VbX4cMd7sKqP0rEj6TfGhWwY8pLa9Zm"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict):
    print("[TOKEN] Creating access token...")
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire

    print(f"[TOKEN] Payload before encode: {to_encode}")
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(f"[TOKEN] Generated Token: {token}")

    return token


def get_current_user(token: str = Depends(oauth2_scheme)):
    print("[TOKEN] Verifying token...")
    print(f"[TOKEN] Received Token: {token}")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"[TOKEN] Decoded payload: {payload}")

        email: str = payload.get("sub")

        if email is None:
            print("[TOKEN] Email missing from token payload")
            raise HTTPException(status_code=401, detail="Invalid token")

        print(f"[TOKEN] Authenticated User: {email}")
        return email

    except JWTError as e:
        print(f"[TOKEN] JWT decode error: {e}")
        raise HTTPException(status_code=401, detail="Invalid token")
