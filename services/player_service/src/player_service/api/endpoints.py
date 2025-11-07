"""Player Service API Endpoints"""
from fastapi import APIRouter, HTTPException
from player_service.models import Player, PlayerCreate
from player_service.service import PlayerService

router = APIRouter(prefix="/players", tags=["players"])
player_service = PlayerService()


@router.post("/", response_model=Player)
def create_player(player: PlayerCreate):
    """Create a new player"""
    return player_service.create_player(player)


@router.get("/{player_id}", response_model=Player)
def get_player(player_id: int):
    """Get player by ID"""
    player = player_service.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.post("/{player_id}/deposit")
def deposit(player_id: int, amount: float):
    """Deposit funds to player account"""
    return player_service.deposit(player_id, amount)


@router.post("/{player_id}/withdraw")
def withdraw(player_id: int, amount: float):
    """Withdraw funds from player account"""
    return player_service.withdraw(player_id, amount)
