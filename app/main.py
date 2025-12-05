from fastapi import FastAPI



app = FastAPI(title="Blog Service API")



@app.get("/")
def root():
    return {"message": "Blog API is running"}