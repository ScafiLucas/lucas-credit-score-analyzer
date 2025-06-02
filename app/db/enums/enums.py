import enum


class JobStatus(str, enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"
