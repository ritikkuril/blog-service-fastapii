from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.logger import logger   # <-- add logger

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.post("/", response_model=schemas.BlogOut)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    logger.info(f"📝 Creating new blog | title={blog.title}")

    try:
        blog_model = models.Blog(
            title=blog.title,
            content=blog.content
        )

        db.add(blog_model)
        db.commit()
        db.refresh(blog_model)

        logger.info(f"✅ Blog created successfully | id={blog_model.id}")
        return blog_model

    except Exception as e:
        db.rollback()
        logger.exception(f"🔥 Failed to create blog | error={e}")
        raise
