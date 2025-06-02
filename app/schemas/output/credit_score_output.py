from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class CreditScoreOutputDTO(BaseModel):
    job_id: UUID
    score: int
    category: str
    explanation: str | None = None
    created_at: datetime
