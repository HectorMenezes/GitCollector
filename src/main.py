from http.client import ImproperConnectionState
from fastapi import FastAPI

from src.routes.healthcheck import router as heathcheck_router

app = FastAPI(title="GitCollector", version="0.0.1")

app.include_router(router=heathcheck_router, prefix="/healthcheck", tags=["tools"])
