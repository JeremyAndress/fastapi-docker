from fastapi import FastAPI
from api.routes import router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, 
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(
    router, prefix=settings.API_V1_STR
)