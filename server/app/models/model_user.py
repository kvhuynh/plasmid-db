from sqlalchemy import Column, Integer, String, ForeignKey, Text;
from sqlalchemy.orm import relationship;
from app.db.database import Base;

class User(Base):
    __tablename__ = "users";

    id = Column(Integer, primary_key=True, index=True);
    name = Column(String(255), index=True);
    role = Column(String(255));
    hashed_password = Column(String(255));
    plasmids = relationship("Plasmid", back_populates="owner")
    
