"""Transaction Repository for Database Operations"""
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from transaction_service.config import settings

Base = declarative_base()


class TransactionModel(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, index=True)
    transaction_type = Column(String)
    amount = Column(Float)
    game_id = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


engine = create_engine(settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class TransactionRepository:
    """Repository for transaction data access"""
    
    def __init__(self):
        self.db = SessionLocal()
    
    def create_transaction(self, player_id: int, transaction_type: str, amount: float, game_id: str = None):
        transaction = TransactionModel(
            player_id=player_id,
            transaction_type=transaction_type,
            amount=amount,
            game_id=game_id
        )
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def get_transactions(self, player_id: int = None, limit: int = 100):
        query = self.db.query(TransactionModel)
        if player_id:
            query = query.filter(TransactionModel.player_id == player_id)
        return query.order_by(TransactionModel.timestamp.desc()).limit(limit).all()
