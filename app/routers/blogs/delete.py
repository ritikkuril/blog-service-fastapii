from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter()


router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            print(f"[WARN] Blog with ID={id} not found for deletion")
            raise HTTPException(status_code=404, detail="Blog not found")

        db.delete(blog)
        db.commit()
        print(f"[INFO] Deleted blog with ID={id}")
        return {"message": "Blog deleted successfully"}
    except Exception as e:
        db.rollback()
        print(f"[ERROR] Failed to delete blog ID={id}: {e}")
        raise e
