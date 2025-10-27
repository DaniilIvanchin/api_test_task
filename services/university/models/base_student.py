from pydantic import BaseModel, ConfigDict
from enum import StrEnum

class DegreeEnum(StrEnum):
    ASSOCIATE = "Associate"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"

class BaseStudent(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str
    last_name: str
    email: str
    degree: DegreeEnum
    phone: str
    group_id: int