from repositories.stretch import StretchRepository
from schemas.stretch import StretchCreate, StretchResponse
from fastapi import HTTPException

class StretchService:
    def __init__(self, stretch_repo: StretchRepository):
        self.stretch_repo = stretch_repo

    def create_stretch(self, stretch_data: StretchCreate) -> StretchResponse:
        stretch = self.stretch_repo.create(stretch_data.dict())
        return StretchResponse.from_orm(stretch)