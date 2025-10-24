from pydantic import BaseModel, ConfigDict, Field
from services.university.models.grade_constants import MAX_GRADE, MIN_GRADE

class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int
    min: int | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE, description="Minimum grade")
    max: int | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE, description="Maximum grade")
    avg: float | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE, description="Average grade")