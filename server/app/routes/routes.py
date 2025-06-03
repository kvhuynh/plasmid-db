from fastapi import APIRouter, Depends;
from sqlalchemy.orm import Session;
from app.schemas.schema_user import UserCreate, User
from app.controllers.controller_user import handle_create_user;
from app.db.database import get_db;
from app.models.model_user import User as UserModel;

router = APIRouter(prefix="/api/v1", tags=["Plasmids"]);


@router.post("/user/create", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return handle_create_user(user, db);

@router.post("/user/login", response_model=User)
def login_user():
    pass

# @router.post("/plasmid/create", response_model=Plasmid)
# def create_plasmid(plasmid: PlasmidCreate, db: Session = Depends(get_db)):
#     return crud.create_plasmid(db, plasmid, user_id=1)  # TODO: get real user
