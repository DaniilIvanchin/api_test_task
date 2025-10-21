from enum import Enum

class DegreeEnum(str, Enum):
    ASSOCIATE = "Associate"
    BACHELOR  = "Bachelor"
    MASTER    = "Master"
    DOCTORATE = "Doctorate"


class SubjectEnum(str, Enum):
    MATHEMATICS = "Mathematics"
    PHYSICS     = "Physics"
    HISTORY     = "History"
    BIOLOGY     = "Biology"
    GEOGRAPHY   = "Geography"