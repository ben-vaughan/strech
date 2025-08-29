from sqlalchemy.orm import Session
from models.stretch import Stretch
from typing import List, Optional

class StretchRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, stretch_data: dict) -> Stretch:
        stretch = Stretch(**stretch_data)
        self.db.add(stretch)
        self.db.commit()
        self.db.refresh(stretch)
        return stretch

    def get_by_id(self, stretch_id: int) -> Optional[Stretch]:
        return self.db.query(Stretch).filter(Stretch.id == stretch_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Stretch]:
        return self.db.query(Stretch).offset(skip).limit(limit).all()