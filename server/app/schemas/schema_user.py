from pydantic import BaseModel

class User_Base(BaseModel):
    name: str;
    role: str;


class User(User_Base):
    id: int;    
    
    class Config:
        orm_mode = True