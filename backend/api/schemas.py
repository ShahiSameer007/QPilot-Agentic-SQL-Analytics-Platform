from pydantic import BaseModel
from typing import Literal

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
    sql: str | None = None
    sql_explanation: str | None = None
    results: list[dict] | None = None
    analysis: AnalyticsResponse | None = None

class SQLGenerationResult(BaseModel):
    sql: str
    explanation: str

class VisualizationSpec(BaseModel):
    recommended: bool
    chart_type: Literal[
        "bar",
        "line",
        "pie",
        "scatter",
        "histogram",
        "box"
    ] | None = None
    x_axis: str | None = None
    y_axis: str | None = None
    title: str | None = None
    reason: str


class AnalyticsResponse(BaseModel):
    summary: str
    insights: list[str]
    visualization: VisualizationSpec