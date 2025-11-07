"""Tests for Game Service"""
import pytest
from fastapi.testclient import TestClient
from game_service.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "Game Service"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_games():
    response = client.get("/games/")
    assert response.status_code == 200
    assert "games" in response.json()
