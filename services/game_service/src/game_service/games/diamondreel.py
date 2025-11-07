"""Diamond Reel Slot Game"""
from game_service.games.slot_base import SlotBase


class DiamondReel(SlotBase):
    """Diamond Reel slot game with 5x payout"""
    
    def __init__(self):
        super().__init__(
            name="Diamond Reel",
            min_bet=10.0,
            max_bet=1000.0,
            win_probability=0.25
        )
    
    def calculate_payout(self, bet_amount: float) -> float:
        """Returns 5x the bet amount"""
        return bet_amount * 5.0
