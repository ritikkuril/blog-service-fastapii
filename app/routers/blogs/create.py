from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.database import get_db

router = APIRouter()

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/", response_model=schemas.BlogOut)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    try:
        blog_model = models.Blog(title=blog.title, content=blog.content)
        db.add(blog_model)
        db.commit()
        db.refresh(blog_model)

        print(f"[INFO] Blog created successfully with ID={blog_model.id}")  # success print
        return blog_model

    except Exception as e:
        db.rollback()
        print(f"[ERROR] Failed to create blog: {e}")  # error print
        raise e  # re-raise to let FastAPI handle the exception
