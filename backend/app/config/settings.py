from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "ThreadForge"
    API_VERSION: str = "v1"

    DATABASE_URL: str = "postgresql://threadforge:threadforge_password@localhost:5432/threadforge_db"

    SECRET_KEY: str = "change_this_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "backend/.env"


settings = Settings()
