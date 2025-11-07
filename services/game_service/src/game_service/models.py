"""Game Service Data Models"""
from pydantic import BaseModel


class BetRequest(BaseModel):
    player_id: int
    amount: float


class BetResult(BaseModel):
    player_id: int
    game_id: str
    bet_amount: float
    result: str  # "win", "lose", or "pending"
    win_amount: float
