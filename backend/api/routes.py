from fastapi import APIRouter
from services.query_service import get_health_status
from services.orchestrator import process_user_request
from api.schemas import HealthResponse,QueryRequest,QueryResponse

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Welcome to QPilot API"}


@router.get("/health", response_model=HealthResponse)
def health_check():
    return get_health_status()


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    return process_user_request(request.question)


