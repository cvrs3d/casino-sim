"""Game Service Main Application"""
from fastapi import FastAPI
from game_service.api.endpoints import router
from game_service.config import settings

app = FastAPI(title="Game Service", version="0.1.0")

app.include_router(router)


@app.get("/")
def read_root():
    return {"service": "Game Service", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
