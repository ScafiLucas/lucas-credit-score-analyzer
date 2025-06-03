from sqlalchemy.orm import Session
from typing import List
from app.db.models.credit_score_db import CreditScoreJobDB, CreditScoreInputDB

class CreditScoreRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_job(self, job: CreditScoreJobDB):
        self.db.add(job)
        self.db.flush()

    def add_inputs(self, inputs: List[CreditScoreInputDB]):
        self.db.add_all(inputs)
        self.db.commit()