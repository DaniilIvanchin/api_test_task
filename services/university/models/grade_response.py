from pydantic import BaseModel, ConfigDict, Field
from services.university.models.grade_constants import MIN_GRADE, MAX_GRADE

class GradeResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    teacher_id: int
    student_id: int
    grade: int = Field(
        ge=MIN_GRADE,
        le=MAX_GRADE,
        description=f"Grade must be between {MIN_GRADE} and {MAX_GRADE}",
    )