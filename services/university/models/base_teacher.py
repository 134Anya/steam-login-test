from pydantic import BaseModel, ConfigDict

from services.university.models.enums import SubjectEnum


class BaseTeacher(BaseModel):
    model_config = ConfigDict(extra="forbid")
    first_name: str
    last_name: str
    subject: SubjectEnum
