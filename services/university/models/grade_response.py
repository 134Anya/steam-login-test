from pydantic import BaseModel, ConfigDict, Field

from services.university.models.base_grade import BaseGrade, MIN_GRADE, MAX_GRADE


class GradeResponse(BaseGrade):
    id: int = Field(...)


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    count: int = Field(..., ge=0)
    min: int | None = Field(None, ge=MIN_GRADE, le=MAX_GRADE)
    max: int | None = Field(None, ge=MIN_GRADE, le=MAX_GRADE)
    avg: float | None = Field(None, ge=float(MIN_GRADE), le=float(MAX_GRADE))
