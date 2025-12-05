from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.get("/", response_model=list[schemas.BlogOut])
def get_blogs(db: Session = Depends(get_db)):
    try:
        blogs = db.query(models.Blog).all()
        print(f"[INFO] Retrieved {len(blogs)} blogs")
        return blogs
    except Exception as e:
        print(f"[ERROR] Failed to fetch blogs: {e}")
        raise e

@router.get("/{id}", response_model=schemas.BlogOut)
def get_blog(id: int, db: Session = Depends(get_db)):
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            print(f"[WARN] Blog with ID={id} not found")
            raise HTTPException(status_code=404, detail="Blog not found")
        print(f"[INFO] Retrieved blog with ID={id}")
        return blog
    except Exception as e:
        print(f"[ERROR] Failed to fetch blog ID={id}: {e}")
        raise e
