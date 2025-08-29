from sqlalchemy import Column, Integer, String, Text, Enum, Datetime
from sqlalchemy.sql import func
from database import Base
import enum

class MuscleGroup(enum.Enum):
    

class Stretch(Base):
    __tablename__ = "stretches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=False)
    repetitions = Column(Integer, nullable=False)
    duration_seconds = Column(Integer, nullable=False)
    muscle_group = Column(Enum(MuscleGroup), nullable=False)