from pydantic import BaseModel;

class Plasmid(BaseModel):
    id: int
    name: str
    
    pass;
