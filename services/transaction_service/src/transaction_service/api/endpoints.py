"""Transaction Service API Endpoints"""
from fastapi import APIRouter
from typing import List, Optional
from transaction_service.models import Transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/", response_model=List[Transaction])
def get_transactions(player_id: Optional[int] = None, limit: int = 100):
    """Get transaction logs"""
    # This will be implemented with actual database queries
    return []


@router.get("/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: int):
    """Get a specific transaction"""
    # This will be implemented with actual database queries
    return None
