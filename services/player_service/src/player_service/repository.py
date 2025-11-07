"""Player Repository for Database Operations"""
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from player_service.config import settings

Base = declarative_base()


class PlayerModel(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    balance = Column(Float, default=0.0)
    status = Column(String, default="active")


engine = create_engine(settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class PlayerRepository:
    """Repository for player data access"""
    
    def __init__(self):
        self.db = SessionLocal()
    
    def create_player(self, name: str, balance: float):
        player = PlayerModel(name=name, balance=balance)
        self.db.add(player)
        self.db.commit()
        self.db.refresh(player)
        return player
    
    def get_player(self, player_id: int):
        return self.db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
    
    def update_balance(self, player_id: int, new_balance: float):
        player = self.get_player(player_id)
        if player:
            player.balance = new_balance
            self.db.commit()
            self.db.refresh(player)
        return player
