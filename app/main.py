from fastapi import FastAPI
from app.database import engine, Base
from app.routers.blogs.create import router as create_blog_router # import the router object
from app.routers.blogs.read import router as read_blog_router #immport for the get all /id blog
from app.routers.blogs.update import router as update_blog_router #import for update api blog
from app.routers.blogs.delete import router as delete_blog_router #import for update api blog


app = FastAPI(title="Blog Service API")

# Create tables
Base.metadata.create_all(bind=engine)

# Include the Blogs router
app.include_router(create_blog_router)
app.include_router(read_blog_router)
app.include_router(update_blog_router)
app.include_router(delete_blog_router)

@app.get("/")
def root():
    return {"message": "Blog API is running"}
