"""Admin Service Repository"""
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from admin_service.config import settings

Base = declarative_base()


class FlaggedPlayerModel(Base):
    __tablename__ = "flagged_players"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, index=True)
    reason = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="flagged")  # flagged, suspended


engine = create_engine(settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class AdminRepository:
    """Repository for admin data access"""
    
    def __init__(self):
        self.db = SessionLocal()
    
    def flag_player(self, player_id: int, reason: str):
        flagged = FlaggedPlayerModel(player_id=player_id, reason=reason)
        self.db.add(flagged)
        self.db.commit()
        self.db.refresh(flagged)
        return flagged
    
    def get_flagged_players(self):
        return self.db.query(FlaggedPlayerModel).all()
