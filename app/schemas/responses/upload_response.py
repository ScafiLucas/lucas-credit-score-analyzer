from pydantic import BaseModel
from uuid import UUID


class UploadResponseDTO(BaseModel):
    job_id: UUID
    message: str = "Upload received. Processing will begin shortly."
