from pydantic import BaseModel, ConfigDict, Field


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int
    teacher_id: int
    grade: int = Field(ge=1, le=5, description="Оценка от 1 до 5")
