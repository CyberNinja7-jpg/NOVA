from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.utils.logging import get_logger


logger = get_logger("NOVA")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="NOVA Autonomous AI Coding Agent"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def startup_event():

    logger.info("NOVA backend starting")

    logger.info(
        "Workspace: %s",
        settings.WORKSPACE_DIR
    )


@app.get("/")
async def root():

    return {
        "name": "NOVA",
        "status": "online",
        "version": settings.APP_VERSION,
        "description": "Autonomous AI Coding Agent"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "agent": "NOVA",
        "backend": "running"
    }
