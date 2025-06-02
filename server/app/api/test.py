from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(prefix="/test", tags=["Test"])

@router.get("/")
def test_db_connection(db: Session = Depends(get_db)):
    # Try a simple raw SQL query
    result = db.execute("SELECT 1")
    return {"success": True, "result": [row for row in result]}
