"""Event Schema Definitions"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PlayerCreatedEvent(BaseModel):
    """Event emitted when a player is created"""
    type: str = "player_created"
    player_id: int
    name: str
    timestamp: datetime


class DepositEvent(BaseModel):
    """Event emitted when a player deposits funds"""
    type: str = "deposit"
    player_id: int
    amount: float
    timestamp: datetime


class WithdrawEvent(BaseModel):
    """Event emitted when a player withdraws funds"""
    type: str = "withdraw"
    player_id: int
    amount: float
    timestamp: datetime


class BetPlacedEvent(BaseModel):
    """Event emitted when a bet is placed"""
    type: str = "bet_placed"
    player_id: int
    game_id: str
    bet_amount: float
    timestamp: datetime


class BetResolvedEvent(BaseModel):
    """Event emitted when a bet is resolved"""
    type: str = "bet_resolved"
    player_id: int
    game_id: str
    bet_amount: float
    result: str  # "win" or "lose"
    win_amount: float
    timestamp: datetime


class PlayerFlaggedEvent(BaseModel):
    """Event emitted when a player is flagged"""
    type: str = "player_flagged"
    player_id: int
    reason: str
    timestamp: datetime


class PlayerSuspendedEvent(BaseModel):
    """Event emitted when a player is suspended"""
    type: str = "player_suspended"
    player_id: int
    reason: Optional[str] = None
    timestamp: datetime
