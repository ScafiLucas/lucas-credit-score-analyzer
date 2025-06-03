from fastapi import APIRouter
from app.api.v1.endpoints import credit_score

api_router = APIRouter()

api_router.include_router(
    credit_score.router,
    prefix="/credit_score",
    tags=["credit_score"]
)