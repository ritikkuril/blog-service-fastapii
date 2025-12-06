from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.logger import logger  # <-- add logger

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    logger.info(f"🗑️ Attempting to delete blog | id={id}")

    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()

        if not blog:
            logger.warning(f"⚠️ Blog not found for deletion | id={id}")
            raise HTTPException(status_code=404, detail="Blog not found")

        db.delete(blog)
        db.commit()

        logger.info(f"✅ Blog deleted successfully | id={id}")
        return {"message": "Blog deleted successfully"}

    except Exception as e:
        db.rollback()
        logger.exception(f"🔥 Failed to delete blog | id={id} | error={e}")
        raise
