from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from app.database import engine, Base
from app.routers.blogs.create import router as create_blog_router
from app.routers.blogs.read import router as read_blog_router
from app.routers.blogs.update import router as update_blog_router
from app.routers.blogs.delete import router as delete_blog_router
from app.routers.auth.register import router as register_router
from app.routers.auth.login import router as login_router

# JWT OAuth2 scheme for Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

app = FastAPI(title="Blog Service API")

# Include Auth routers
app.include_router(register_router)
app.include_router(login_router)

# Create tables
Base.metadata.create_all(bind=engine)

# Include Blog routers with JWT dependency 
app.include_router(create_blog_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(read_blog_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(update_blog_router, dependencies=[Depends(oauth2_scheme)])
app.include_router(delete_blog_router, dependencies=[Depends(oauth2_scheme)])

@app.get("/")
def root():
    return {"message": "Blog API is running"}
