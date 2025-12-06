from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.logger import logger  # <-- use logger

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.put("/{id}", response_model=schemas.BlogOut)
def update_blog(id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    logger.info(f"✏️ Attempting to update blog | id={id}")

    try:
        blog_data = db.query(models.Blog).filter(models.Blog.id == id).first()

        if not blog_data:
            logger.warning(f"⚠️ Blog not found for update | id={id}")
            raise HTTPException(status_code=404, detail="Blog not found")

        blog_data.title = blog.title
        blog_data.content = blog.content
        db.commit()
        db.refresh(blog_data)

        logger.info(f"✅ Blog updated successfully | id={id}")
        return blog_data

    except Exception as e:
        db.rollback()
        logger.exception(f"🔥 Failed to update blog | id={id} | error={e}")
        raise
