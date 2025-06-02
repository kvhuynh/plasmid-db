from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.plasmid import PlasmidCreate, Plasmid
from server.app.crud import crud_plasmid as crud
from app.db.database import get_db

router = APIRouter(prefix="/plasmids", tags=["Plasmids"])

@router.post("/", response_model=Plasmid)
def create(plasmid: PlasmidCreate, db: Session = Depends(get_db)):
    return crud.create_plasmid(db, plasmid, user_id=1)  # TODO: get real user
