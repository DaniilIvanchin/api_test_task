from pydantic import BaseModel, ConfigDict, Field

class GradeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    teacher_id: int
    student_id: int
    grade: int = Field(ge=1, le=5, description="Grade must be between 1 and 5")