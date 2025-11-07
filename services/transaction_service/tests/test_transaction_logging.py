"""Tests for Transaction Service"""
import pytest
from fastapi.testclient import TestClient
from transaction_service.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "Transaction Service"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
