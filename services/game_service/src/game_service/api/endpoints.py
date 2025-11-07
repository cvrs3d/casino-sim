"""Game Service API Endpoints"""
from fastapi import APIRouter
from game_service.models import BetRequest, BetResult

router = APIRouter(prefix="/games", tags=["games"])


@router.post("/{game_id}/bet", response_model=BetResult)
def place_bet(game_id: str, bet: BetRequest):
    """Place a bet on a game"""
    # This will be implemented with actual game logic
    return BetResult(
        player_id=bet.player_id,
        game_id=game_id,
        bet_amount=bet.amount,
        result="pending",
        win_amount=0.0
    )


@router.get("/")
def list_games():
    """List available games"""
    return {
        "games": [
            {"id": "lucky7", "name": "Lucky 7"},
            {"id": "megaspin", "name": "MegaSpin"},
            {"id": "diamondreel", "name": "Diamond Reel"}
        ]
    }
