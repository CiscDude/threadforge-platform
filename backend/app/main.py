from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.admin.routes import router as admin_router
from app.api.auth.routes import router as auth_router
from app.api.cart.routes import router as cart_router
from app.api.customization.routes import router as customization_router
from app.api.orders.routes import router as orders_router
from app.api.payments.routes import router as payments_router
from app.api.products.routes import router as products_router
from app.api.uploads_routes import router as uploads_router
from app.api.users.routes import router as users_router
from app.config.settings import settings
from app.middleware.error_handler import ErrorHandlerMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    description="Backend API for ThreadForge custom clothing e-commerce platform",
)


app.add_middleware(ErrorHandlerMiddleware)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(auth_router, prefix="/api/v1")
app.include_router(products_router, prefix="/api/v1")
app.include_router(cart_router, prefix="/api/v1")
app.include_router(orders_router, prefix="/api/v1")
app.include_router(payments_router, prefix="/api/v1")
app.include_router(customization_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")
app.include_router(uploads_router, prefix="/api/v1")
app.include_router(admin_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "ThreadForge API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
