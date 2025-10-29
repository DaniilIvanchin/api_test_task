from pydantic import ConfigDict
from services.university.models.base_student import BaseStudent

class StudentResponse(BaseStudent):
    model_config = ConfigDict(extra="forbid")
    id: int