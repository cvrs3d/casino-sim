"""Transaction Service Configuration"""
import os


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./transaction_service.db")
    RABBITMQ_URL: str = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")


settings = Settings()
