# plasmid-db

source .venv/Scripts/activate to launch shell (prob diff on mac)

uvicorn main:app --reload to run server

POST http://127.0.0.1:8000/api/v1/user/create for testing user creation endpoint

need to implement password hashing and field validation

pip install fastapi[all] uvicorn sqlalchemy passlib[bcrypt]
