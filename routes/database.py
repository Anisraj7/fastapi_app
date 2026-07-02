from fastapi import APIRouter
from sqlalchemy import text

from core.database import SessionLocal

router = APIRouter(
    prefix="/database",
    tags=["Database"],
)

@router.get("/test")
def test_database():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {
            "success": True,
            "message": "Database connected successfully",
        }
    finally:
        db.close()