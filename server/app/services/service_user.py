from sqlalchemy.orm import Session;
from app.schemas.schema_user import UserCreate;
from app.models.model_user import User as UserModel;
from app.utils.security import hash_password;

def create_user(user: UserCreate, db: Session):
    hashed_pw = hash_password(user.password);
    db_user = UserModel(name=user.name, role=user.role, hashed_password=hashed_pw);
    db.add(db_user);
    db.commit();
    db.refresh(db_user);
    return db_user;
