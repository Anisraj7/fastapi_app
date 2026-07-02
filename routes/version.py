from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    prefix="/version",
    tags=["Version"],
)


@router.get("")
def version():
    return {
        "application": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
    }