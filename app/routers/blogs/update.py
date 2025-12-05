from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.put("/{id}", response_model=schemas.BlogOut)
def update_blog(id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    try:
        blog_data = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog_data:
            print(f"[WARN] Blog with ID={id} not found for update")
            raise HTTPException(status_code=404, detail="Blog not found")

        blog_data.title = blog.title
        blog_data.content = blog.content
        db.commit()
        db.refresh(blog_data)

        print(f"[INFO] Updated blog with ID={id}")
        return blog_data
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Failed to update blog ID={id}: {e}")
        raise e
