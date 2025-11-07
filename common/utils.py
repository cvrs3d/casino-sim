"""Common Utility Functions"""


def format_currency(amount: float) -> str:
    """Format currency amount"""
    return f"${amount:.2f}"


def validate_positive_amount(amount: float) -> bool:
    """Validate that amount is positive"""
    return amount > 0
