from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.logger import logger  # <-- add logger

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.get("/", response_model=list[schemas.BlogOut])
def get_blogs(db: Session = Depends(get_db)):
    logger.info("📄 Fetching all blogs...")

    try:
        blogs = db.query(models.Blog).all()
        logger.info(f"✅ Retrieved {len(blogs)} blogs")
        return blogs

    except Exception as e:
        logger.exception(f"🔥 Failed to fetch blogs | error={e}")
        raise


@router.get("/{id}", response_model=schemas.BlogOut)
def get_blog(id: int, db: Session = Depends(get_db)):
    logger.info(f"🔍 Fetching blog by ID | id={id}")

    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()

        if not blog:
            logger.warning(f"⚠️ Blog not found | id={id}")
            raise HTTPException(status_code=404, detail="Blog not found")

        logger.info(f"✅ Retrieved blog successfully | id={id}")
        return blog

    except Exception as e:
        logger.exception(f"🔥 Failed to fetch blog | id={id} | error={e}")
        raise
