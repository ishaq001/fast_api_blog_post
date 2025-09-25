from fastapi import FastAPI
from routes import router as blog_router

app = FastAPI(title="Blog API")
app.include_router(blog_router)
