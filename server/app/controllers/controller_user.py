from sqlalchemy.orm import Session;
from app.schemas.schema_user import UserCreate;
from app.services.service_user import create_user;

def handle_create_user(user: UserCreate, db: Session):
    return create_user(user, db);
