from pydantic import BaseModel, ConfigDict

class GradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int