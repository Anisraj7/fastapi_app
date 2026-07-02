from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.exceptions import global_exception_handler

from routes.health import router as health_router
from routes.version import router as version_router
from routes.database import router as database_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(version_router)
app.include_router(database_router)


@app.get("/")
def root():
    return {"message": "Enterprise Collaboration Workflow API is running."}

