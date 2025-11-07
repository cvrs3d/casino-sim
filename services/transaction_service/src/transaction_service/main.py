"""Transaction Service Main Application"""
from fastapi import FastAPI
from transaction_service.api.endpoints import router
from transaction_service.config import settings

app = FastAPI(title="Transaction Service", version="0.1.0")

app.include_router(router)


@app.get("/")
def read_root():
    return {"service": "Transaction Service", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
