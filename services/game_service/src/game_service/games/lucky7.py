"""Lucky 7 Slot Game"""
from game_service.games.slot_base import SlotBase


class Lucky7(SlotBase):
    """Lucky 7 slot game with 2x payout"""
    
    def __init__(self):
        super().__init__(
            name="Lucky 7",
            min_bet=1.0,
            max_bet=100.0,
            win_probability=0.45
        )
    
    def calculate_payout(self, bet_amount: float) -> float:
        """Returns 2x the bet amount"""
        return bet_amount * 2.0
