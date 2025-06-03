from abc import ABC, abstractmethod
from fastapi import UploadFile
from app.schemas.responses.upload_response import UploadResponseDTO

class ICreditScoreService(ABC):

    @abstractmethod
    async def upload_csv_and_dispatch_job(self, file: UploadFile) -> UploadResponseDTO:
        pass
