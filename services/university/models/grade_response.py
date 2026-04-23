from typing import List
from pydantic import BaseModel, ConfigDict, Field
from services.university.models.base_grade import BaseGrade


class GradeResponse(BaseGrade):
    id: int


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    avg: float = Field(..., ge=1.0, le=5.0)
    count: int = Field(..., ge=0)
    min: int = Field(..., ge=1, le=5)
    max: int = Field(..., ge=1, le=5)

    grades: List[GradeResponse] = []
