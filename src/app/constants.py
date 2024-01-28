from enum import Enum, auto

class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    CANCELLED = auto()
    DONE = auto()
