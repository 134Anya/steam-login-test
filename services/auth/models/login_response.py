from typing import Literal

from pydantic import ConfigDict, BaseModel


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: str
    token_type: Literal["Bearer"]
