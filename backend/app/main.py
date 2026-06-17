from fastapi import FastAPI

from app.config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    description="Backend API for ThreadForge custom clothing e-commerce platform",
)


@app.get("/")
def root():
    return {"message": "ThreadForge API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
