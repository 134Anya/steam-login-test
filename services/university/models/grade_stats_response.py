from pydantic import BaseModel, ConfigDict, Field


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(..., ge=0)
    min: int = Field(..., ge=1, le=5)
    max: int = Field(..., ge=1, le=5)
    avg: float = Field(..., ge=1.0, le=5.0)
