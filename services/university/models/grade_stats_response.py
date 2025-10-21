from pydantic import BaseModel, ConfigDict
from typing import Optional

class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int
    min: Optional[int]
    max: Optional[int]
    avg: Optional[float]