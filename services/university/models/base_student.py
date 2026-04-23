from pydantic import BaseModel, ConfigDict, EmailStr

from services.university.models.enums import DegreeEnum


class BaseStudent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: EmailStr
    degree: DegreeEnum
    phone: str
    group_id: int
