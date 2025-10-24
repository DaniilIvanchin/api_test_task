from pydantic import ConfigDict
from services.university.models.base_group import BaseGroup

class GroupResponse(BaseGroup):
    model_config = ConfigDict(extra="forbid")
    id: int