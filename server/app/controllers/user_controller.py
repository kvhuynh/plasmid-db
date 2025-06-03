from sqlalchemy.orm import Session;
from app.db.database import get_db;
from app.schemas.schema_user import UserCreate, User as UserSchema
from app.services.user_service import create_user;

def handle_create_user(user: UserCreate, db: Session):
    return create_user(user, db);



    # db_user = UserModel(
    #     name=user.name,
    #     role=user.role
    # )
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user