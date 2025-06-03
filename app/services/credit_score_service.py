import csv
import io
import uuid
from fastapi import UploadFile, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models.credit_score_db import CreditScoreJobDB, CreditScoreInputDB
from app.repositories.credit_score_repository import CreditScoreRepository
from app.schemas.input.credit_score_input import CreditScoreInputDTO
from app.schemas.responses.upload_response import UploadResponseDTO
from app.core.queue import publish_job
from app.interfaces.services.credit_score_service_interface import ICreditScoreService


class CreditScoreService(ICreditScoreService):
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.repo = CreditScoreRepository(self.db)

    async def upload_csv_and_dispatch_job(self, file: UploadFile) -> UploadResponseDTO:
        if file.content_type != "text/csv":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")

        contents = await file.read()
        decoded = contents.decode("utf-8")
        reader = csv.DictReader(io.StringIO(decoded))

        job_id = uuid.uuid4()
        job = CreditScoreJobDB(job_id=job_id)
        self.db.add(job)
        self.db.flush()

        inputs = []
        for row in reader:
            try:
                dto = CreditScoreInputDTO(
                    job_id=job_id,
                    income=float(row["income"]),
                    debt=float(row["debt"]),
                    late_payments=int(row["late_payments"]),
                    savings=float(row["savings"])
                )
                inputs.append(CreditScoreInputDB(**dto.model_dump()))
            except (KeyError, ValueError) as e:
                raise HTTPException(status_code=400, detail=f"Invalid row data: {row} :: {str(e)}")

        self.db.add_all(inputs)
        self.db.commit()

        await publish_job(str(job_id))
        return UploadResponseDTO(job_id=job_id)
