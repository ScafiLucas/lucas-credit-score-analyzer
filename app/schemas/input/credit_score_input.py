from pydantic import BaseModel, Field
from uuid import UUID


class CreditScoreInputDTO(BaseModel):
    job_id: UUID
    income: float
    debt: float
    late_payments: int
    savings: float