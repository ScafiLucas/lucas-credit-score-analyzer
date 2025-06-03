from fastapi import APIRouter, UploadFile, Depends
from app.services.credit_score_service import CreditScoreService
from app.schemas.responses.upload_response import UploadResponseDTO

router = APIRouter()

@router.post("/upload", response_model=UploadResponseDTO)
async def upload_credit_score_file(
    file: UploadFile,
    service: CreditScoreService = Depends()
):
    return await service.upload_csv_and_dispatch_job(file)
