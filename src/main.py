from fastapi import FastAPI

from src.services.database import init_pool
from src.routes.healthcheck import router as heathcheck_router
from src.routes.user import router as user_router


app = FastAPI(title="GitCollector", version="0.0.1")

app.include_router(router=heathcheck_router, prefix="/healthcheck", tags=["tools"])
app.include_router(router=user_router, prefix="/user", tags=["user"])


@app.on_event("startup")
async def setup_application():
    """
    Routine executed at the application's start.
    """
    try:
        await init_pool()
    except Exception as error:
        print(error)
