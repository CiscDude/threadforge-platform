from fastapi import FastAPI

from app.api.auth.routes import router as auth_router
from app.api.products.routes import router as products_router
from app.config.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    description="Backend API for ThreadForge custom clothing e-commerce platform",
)


app.include_router(auth_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "ThreadForge API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
