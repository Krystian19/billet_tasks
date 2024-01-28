from enum import Enum, auto

DATABASE_URL = 'postgresql://postgres:pass@billet.postgres/billet'

class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    CANCELLED = auto()
    DONE = auto()
