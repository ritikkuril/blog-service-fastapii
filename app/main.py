from fastapi import FastAPI
from app.database import engine, Base
from app.routers.blogs.create import router as create_blog_router  # import the router object

app = FastAPI(title="Blog Service API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include the Blogs router
app.include_router(create_blog_router)

@app.get("/")
def root():
    return {"message": "Blog API is running"}
