from fastapi import APIRouter, Depends, HTTPException
from services.stretch_service import StretchService
from schemas.stretch import StretchCreate, StretchResponse
from dependencies import get_stretch_service

router = APIRouter(prefix="/stretches", tags=["stretches"])

@router.post("/", response_model=StretchResponse, status_code=201)
def create_stretch(
    stretch: StretchCreate,
    stretch_service: StretchService = Depends(get_stretch_service)
):
    """
    Create a new stretch.
    
    - name: Name of the stretch (required)
    - description: Brief description (required)
    - repetitions: Step-by-step instructions (required)
    - duration_seconds: How long to hold the stretch (required)
    - muscle_group: Main muscle group targeted (required)
    """
    return stretch_service.create_stretch(stretch)