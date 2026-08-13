from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="QPilot API",
    description="Backend API for the QPilot Agentic SQL Analytics Platform",
    version="1.0.0"
)

app.include_router(router)