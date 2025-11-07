"""Fraud Detection Logic for Admin Service"""
from typing import Dict, List


class FraudDetector:
    """Detects fraudulent behavior patterns"""
    
    def __init__(self):
        self.player_history: Dict[int, List] = {}
        self.max_consecutive_wins = 3
        self.max_bet_spike_multiplier = 10.0
    
    def check_consecutive_wins(self, player_id: int, result: str) -> bool:
        """Check if player has too many consecutive wins"""
        if player_id not in self.player_history:
            self.player_history[player_id] = []
        
        history = self.player_history[player_id]
        history.append(result)
        
        # Keep only recent history
        if len(history) > 10:
            history.pop(0)
        
        # Count consecutive wins
        consecutive = 0
        for outcome in reversed(history):
            if outcome == "win":
                consecutive += 1
            else:
                break
        
        return consecutive >= self.max_consecutive_wins
    
    def check_bet_spike(self, player_id: int, current_bet: float, avg_bet: float) -> bool:
        """Check if bet amount is unusually high"""
        if avg_bet == 0:
            return False
        return current_bet > avg_bet * self.max_bet_spike_multiplier
    
    def evaluate_player(self, player_id: int, event_data: dict) -> dict:
        """Evaluate if player behavior is suspicious"""
        flags = []
        
        if "result" in event_data:
            if self.check_consecutive_wins(player_id, event_data["result"]):
                flags.append("consecutive_wins")
        
        return {
            "player_id": player_id,
            "is_suspicious": len(flags) > 0,
            "flags": flags
        }
