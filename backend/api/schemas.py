from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

class QueryRequest(BaseModel):
    question: str

class ExecutionPlan(BaseModel):
    task: str
    question: str
    steps: list[str]

class QueryResponse(BaseModel):
    success: bool
    message: str
    user_query: str
    plan: ExecutionPlan
