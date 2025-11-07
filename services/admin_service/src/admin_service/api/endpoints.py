"""Admin Service API Endpoints"""
from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/flagged-players")
def get_flagged_players():
    """Get list of flagged players"""
    # This will be implemented with actual database queries
    return {"flagged_players": []}


@router.post("/players/{player_id}/flag")
def flag_player(player_id: int, reason: str):
    """Flag a player for suspicious activity"""
    return {"player_id": player_id, "flagged": True, "reason": reason}


@router.post("/players/{player_id}/suspend")
def suspend_player(player_id: int):
    """Suspend a player account"""
    return {"player_id": player_id, "suspended": True}
