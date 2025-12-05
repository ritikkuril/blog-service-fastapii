from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.routers.auth.service import create_user, authenticate_user
from app.routers.auth.token import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    try:
        print("[ROUTE] /auth/login hit")
        print(f"[ROUTE] Form data received username={form_data.username}")

        user = authenticate_user(form_data.username, form_data.password, db)
        if not user:
            print("[ROUTE] Authentication failed")
            raise HTTPException(status_code=400, detail="Invalid email or password")

        token = create_access_token({"sub": user.email})
        print(f"[ROUTE] Token generated for {user.email}")

        return {"access_token": token, "token_type": "bearer"}

    except HTTPException:
        # re-raise HTTP exceptions so FastAPI handles them
        raise
    except Exception as e:
        print(f"[ROUTE ERROR] Failed to login user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
