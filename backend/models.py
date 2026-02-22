from sqlalchemy import Column, Integer, String
from db import Base

class Fabric(Base):

    __tablename__ = "fabrics"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)

    sustainability_score = Column(Integer, nullable=False)