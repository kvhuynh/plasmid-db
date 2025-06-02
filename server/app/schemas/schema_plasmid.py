from pydantic import BaseModel

class PlasmidBase(BaseModel):
    name: str
    description: str
    sequence: str

class PlasmidCreate(PlasmidBase):
    pass

class Plasmid(PlasmidBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
