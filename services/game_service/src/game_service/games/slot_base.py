"""Base Slot Game Implementation"""
import random
from abc import ABC, abstractmethod


class SlotBase(ABC):
    """Base class for slot games"""
    
    def __init__(self, name: str, min_bet: float, max_bet: float, win_probability: float):
        self.name = name
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.win_probability = win_probability
    
    @abstractmethod
    def calculate_payout(self, bet_amount: float) -> float:
        """Calculate payout for a winning bet"""
        pass
    
    def play(self, bet_amount: float) -> tuple[bool, float]:
        """
        Play the game with the given bet amount
        Returns: (is_win, payout_amount)
        """
        if bet_amount < self.min_bet or bet_amount > self.max_bet:
            raise ValueError(f"Bet must be between {self.min_bet} and {self.max_bet}")
        
        is_win = random.random() < self.win_probability
        payout = self.calculate_payout(bet_amount) if is_win else 0.0
        
        return is_win, payout
