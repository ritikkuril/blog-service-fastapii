from pydantic import BaseModel

# ---------------- BLOG SCHEMAS ----------------
class BlogCreate(BaseModel):
    title: str
    content: str

class BlogOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True
#So FastAPI can convert SQLAlchemy objects → Pydantic objects.

# ---------------- USER SCHEMAS ----------------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True