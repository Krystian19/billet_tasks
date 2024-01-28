from enum import Enum, auto

class TaskStatus(str, Enum):
    PENDING = "PENDING" 
    IN_PROGRESS = "IN_PROGRESS" 
    CANCELLED = "CANCELLED" 
    DONE = "DONE" 
