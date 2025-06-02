from fastapi import APIRouter, Depends;
from sqlalchemy.orm import Session;
# from app.models.model_user import User as UserModel;
# from app.schemas.schema_plasmid import PlasmidCreate, Plasmid;
# from app.schemas.schema_user import UserCreate
from app.models.model_user import User as UserModel
from app.schemas.schema_user import UserCreate, User as UserSchema


from app.crud import crud_plasmid as crud;
from app.db.database import get_db;

router = APIRouter(prefix="/api/v1", tags=["Plasmids"]);


@router.post("/user/create", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(
        name=user.name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# @router.post("/user/create", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(
#         name=user.name,
#         role=user.role
#     );

#     db.add(db_user);
#     db.commit();
#     db.refresh(db_user);
#     return db_user;

# @router.post("/plasmid/create", response_model=Plasmid)
# def create_plasmid(plasmid: PlasmidCreate, db: Session = Depends(get_db)):
#     return crud.create_plasmid(db, plasmid, user_id=1)  # TODO: get real user
