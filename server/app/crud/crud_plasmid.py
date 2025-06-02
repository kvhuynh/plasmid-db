from sqlalchemy.orm import Session
from app.schema.plasmid_db import Plasmid
from app.models.plasmid import PlasmidCreate

def create_plasmid(db: Session, plasmid: PlasmidCreate, user_id: int):
    db_plasmid = Plasmid(**plasmid.dict(), owner_id=user_id);

    db.add(db_plasmid);
    db.commit();
    db.refresh(db_plasmid);
    return db_plasmid;
