"""Player Service Main Application"""
from fastapi import FastAPI
from player_service.api.endpoints import router
from player_service.config import settings

app = FastAPI(title="Player Service", version="0.1.0")

app.include_router(router)


@app.get("/")
def read_root():
    return {"service": "Player Service", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
