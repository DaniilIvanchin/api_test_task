from pydantic import BaseModel, ConfigDict, Field

class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int
    min: int | None = Field(default=None, ge=1, le=5, description="Minimum grade")
    max: int | None = Field(default=None, ge=1, le=5, description="Maximum grade")
    avg: float | None = Field(default=None, ge=1, le=5, description="Average grade")