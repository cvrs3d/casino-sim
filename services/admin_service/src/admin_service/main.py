"""Admin Service Main Application"""
from fastapi import FastAPI
from admin_service.api.endpoints import router
from admin_service.config import settings

app = FastAPI(title="Admin Service", version="0.1.0")

app.include_router(router)


@app.get("/")
def read_root():
    return {"service": "Admin Service", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
