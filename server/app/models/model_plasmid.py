from sqlalchemy import Column, Integer, String, ForeignKey, Text;
from sqlalchemy.orm import relationship;
from app.db.database import Base;

class Plasmid(Base):
    __tablename__ = "plasmids";

    id = Column(Integer, primary_key=True, index=True);
    name = Column(String(255), index=True);
    description = Column(Text);
    sequence = Column(Text);
    owner_id = Column(Integer, ForeignKey("users.id"));

    owner = relationship("User", back_populates="plasmids");
