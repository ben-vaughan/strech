from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator
from models.stretch import DifficultyLevel, MuscleGroup

class StretchCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Name of the stretch")
    description: str = Field(..., min_length=1, max_length=100, description="Description of the stretch")
    repetitions: int = Field(..., gt=0, le=32, description="Number of repetitions to perform (max. 32)")
    duration_seconds: int = Field(..., gt=0, le=300, description="Hold time in seconds (max. 5 minutes)")
    muscle_group: MuscleGroup

    @validator('name'):
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty or only whitespace")
        return v.strip().title()

class StretchResponse(BaseModel):
    id: int
    name: str
    description: str
    repetitions: int
    duration_seconds: int
    muscle_group: MuscleGroup
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True