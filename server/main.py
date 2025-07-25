from fastapi import FastAPI;
# from app.api import test;
from app.routes import routes;
# from app.models import User, Plasmid;
from app.models.model_user import User;
from app.models.model_plasmid import Plasmid;
from app.db.database import Base, engine;

app = FastAPI();

print("Resetting database schema...");
Base.metadata.drop_all(bind=engine);
Base.metadata.create_all(bind=engine);
print("Done resetting tables.");

print("Establishing routes");
app.include_router(routes.router);
