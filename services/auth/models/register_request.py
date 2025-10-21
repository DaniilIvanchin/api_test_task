from pydantic import BaseModel, ConfigDict

class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)
    email: str
    password: str
    password_repeat: str
    username: str
