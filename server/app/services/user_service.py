# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = UserModel(
#         name=user.name,
#         role=user.role
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# app/services/user_service.py

from sqlalchemy.orm import Session
from app.models.model_user import User as UserModel
from app.schemas.schema_user import UserCreate

def create_user_service(user: UserCreate, db: Session):
    db_user = UserModel(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
