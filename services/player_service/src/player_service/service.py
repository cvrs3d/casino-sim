"""Player Service Business Logic"""
from player_service.repository import PlayerRepository
from player_service.models import Player, PlayerCreate


class PlayerService:
    """Business logic for player operations"""
    
    def __init__(self):
        self.repository = PlayerRepository()
    
    def create_player(self, player_data: PlayerCreate):
        player = self.repository.create_player(
            name=player_data.name,
            balance=player_data.initial_balance
        )
        return Player.model_validate(player)
    
    def get_player(self, player_id: int):
        player = self.repository.get_player(player_id)
        if player:
            return Player.model_validate(player)
        return None
    
    def deposit(self, player_id: int, amount: float):
        player = self.repository.get_player(player_id)
        if not player:
            raise ValueError("Player not found")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        new_balance = player.balance + amount
        updated_player = self.repository.update_balance(player_id, new_balance)
        return Player.model_validate(updated_player)
    
    def withdraw(self, player_id: int, amount: float):
        player = self.repository.get_player(player_id)
        if not player:
            raise ValueError("Player not found")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if player.balance < amount:
            raise ValueError("Insufficient balance")
        
        new_balance = player.balance - amount
        updated_player = self.repository.update_balance(player_id, new_balance)
        return Player.model_validate(updated_player)
