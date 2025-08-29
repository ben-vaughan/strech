from database import get_db
from repositories.stretch_repository import StretchRepository
from services.stretch_service import StretchService
from sqlalchemy.orm import Session
from fastapi import Depends

def get_stretch_repository(db: Session = Depends(get_db)) -> StretchRepository:
    return StretchRepository(db)

def get_stretch_service(
    stretch_repo: StretchRepository = Depends(get_stretch_repository)
) -> StretchService:
    return StretchService(stretch_repo)