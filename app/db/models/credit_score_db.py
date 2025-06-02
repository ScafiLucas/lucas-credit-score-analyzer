from datetime import datetime
from uuid import UUID
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.db.enums import JobStatus


class CreditScoreJobDB(Base):
    __tablename__ = "credit_score_jobs"

    job_id = Column(PG_UUID(as_uuid=True), primary_key=True)
    status = Column(Enum(JobStatus, name="job_status"), nullable=False, default=JobStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

    inputs = relationship("CreditScoreInputDB", back_populates="job", cascade="all, delete-orphan")
    outputs = relationship("CreditScoreOutputDB", back_populates="job", cascade="all, delete-orphan")


class CreditScoreInputDB(Base):
    __tablename__ = "credit_score_inputs"

    id = Column(PG_UUID(as_uuid=True), primary_key=True)
    job_id = Column(PG_UUID(as_uuid=True), ForeignKey("credit_score_jobs.job_id", ondelete="CASCADE"))
    income = Column(Float, nullable=False)
    debt = Column(Float, nullable=False)
    late_payments = Column(Integer, nullable=False)
    savings = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    job = relationship("CreditScoreJobDB", back_populates="inputs")


class CreditScoreOutputDB(Base):
    __tablename__ = "credit_score_outputs"

    id = Column(PG_UUID(as_uuid=True), primary_key=True)
    job_id = Column(PG_UUID(as_uuid=True), ForeignKey("credit_score_jobs.job_id", ondelete="CASCADE"))
    score = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    explanation = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    job = relationship("CreditScoreJobDB", back_populates="outputs")
