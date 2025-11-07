"""MegaSpin Slot Game"""
from game_service.games.slot_base import SlotBase


class MegaSpin(SlotBase):
    """MegaSpin slot game with 3x payout"""
    
    def __init__(self):
        super().__init__(
            name="MegaSpin",
            min_bet=5.0,
            max_bet=500.0,
            win_probability=0.35
        )
    
    def calculate_payout(self, bet_amount: float) -> float:
        """Returns 3x the bet amount"""
        return bet_amount * 3.0
