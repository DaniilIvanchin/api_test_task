from pydantic import BaseModel, ConfigDict

class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    email: str
    password: str
    password_repeat: str
    username: str
