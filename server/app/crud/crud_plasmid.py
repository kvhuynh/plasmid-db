from sqlalchemy.orm import Session;
from app.schemas.schema_plasmid import PlasmidCreate;
from app.models.model_plasmid import Plasmid;
from app.schemas.schema_user import UserCreate;
from app.models.model_user import User;

def create_user(db: Session, user: UserCreate, role: str):
    print("test")
    db_user = user(**user.dict(), role=role);
    db.add(db_user);
    db.commit();
    db.refresh(db_user);
    return db_user;

def create_plasmid(db: Session, plasmid: PlasmidCreate, user_id: int):
    db_plasmid = Plasmid(**plasmid.dict(), owner_id=user_id);

    db.add(db_plasmid);
    db.commit();
    db.refresh(db_plasmid);
    return db_plasmid;

