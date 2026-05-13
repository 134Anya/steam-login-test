from pydantic import BaseModel, ConfigDict, Field

MIN_GRADE = 1
MAX_GRADE = 5


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    student_id: int
    teacher_id: int
    grade: int = Field(
        ge=MIN_GRADE, le=MAX_GRADE, description=f"Оценка от {MIN_GRADE} до {MAX_GRADE}"
    )
