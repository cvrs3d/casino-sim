"""Transaction Service Data Models"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Transaction(BaseModel):
    id: int
    player_id: int
    transaction_type: str  # deposit, withdraw, bet, result, flag
    amount: float
    game_id: Optional[str] = None
    timestamp: datetime

    class Config:
        from_attributes = True
