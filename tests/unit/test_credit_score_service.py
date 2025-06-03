import io
import pytest
from uuid import UUID
from unittest.mock import MagicMock, AsyncMock
from app.services.credit_score_service import CreditScoreService
from fastapi import UploadFile


@pytest.fixture
def csv_file():
    content = b"name,age,income,debt,late_payments,savings\nLucas,30,5000,1000,0,2000\nBianca,28,6000,1500,1,3000\n"
    file_like = io.BytesIO(content)

    upload = MagicMock(spec=UploadFile)
    upload.filename = "test.csv"
    upload.content_type = "text/csv"
    upload.read = AsyncMock(return_value=content)
    return upload


@pytest.fixture
def mock_db():
    mock = MagicMock()
    mock.add = MagicMock()
    mock.commit = MagicMock()
    return mock


@pytest.mark.asyncio
async def test_upload_csv_should_add_inputs_to_db(csv_file, mock_db):
    service = CreditScoreService(db=mock_db)

    result = await service.upload_csv_and_dispatch_job(csv_file)

    assert isinstance(result.job_id, UUID)
    assert result.message == "Upload received. Processing will begin shortly."
    mock_db.add.assert_called()
    mock_db.commit.assert_called()
