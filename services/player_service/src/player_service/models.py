"""Player Service Data Models"""
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class PlayerStatus(str, Enum):
    ACTIVE = "active"
    FLAGGED = "flagged"
    SUSPENDED = "suspended"


class PlayerCreate(BaseModel):
    name: str
    initial_balance: float = 0.0


class Player(BaseModel):
    id: int
    name: str
    balance: float
    status: PlayerStatus = PlayerStatus.ACTIVE

    class Config:
        from_attributes = True
